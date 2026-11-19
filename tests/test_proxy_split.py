# tests/test_proxy_split.py -- CPU-only checks of the attacker proxy set (config 'attacker_proxy_independent').
# Run from the repo root:  python -m pytest tests/test_proxy_split.py -q
# Offline: a stub tokenizer replaces AutoTokenizer (nothing is tokenised) and AG News is read from data/.
import sys
from functools import lru_cache
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import numpy as np
import pytest
import torch

import data_loader
from data_loader import DataManager

AG_NEWS = ROOT / 'data' / 'AG News Datasets'
needs_ag_news = pytest.mark.skipif(not (AG_NEWS / 'train.csv').is_file() or not (AG_NEWS / 'test.csv').is_file(),
                                   reason='AG News CSVs not found under data/AG News Datasets/')


class _StubTokenizer:  # DataManager only reads pad_token at construction
    pad_token = '[PAD]'


class _StubAutoTokenizer:
    @staticmethod
    def from_pretrained(*args, **kwargs):
        return _StubTokenizer()


def _build(dataset='ag_news', independent=True, limit=20000, seed=42, size=512):
    with mock.patch.object(data_loader, 'AutoTokenizer', _StubAutoTokenizer):
        return DataManager(num_clients=7, num_attackers=2, test_seed=seed, dataset_size_limit=limit,
                           batch_size=128, test_batch_size=512, dataset=dataset,
                           proxy_independent=independent, proxy_sample_size=size)


_ag_news = lru_cache(maxsize=None)(_build)  # AG News managers are not mutated by the checks -> build each once


def _proxy_texts(dm, size):
    return list(dm.get_proxy_eval_loader(sample_size=size).dataset.texts)


@needs_ag_news
@pytest.mark.parametrize('seed,size', [(42, 512), (42069, 200)])
def test_independent_proxy_is_disjoint_and_keeps_client_and_eval_data(seed, size):
    legacy, indep = _ag_news(independent=False, seed=seed, size=size), _ag_news(independent=True, seed=seed, size=size)
    # client data and evaluation set are exactly those of the original setting -> benign / baseline runs unchanged
    assert indep.train_texts == legacy.train_texts and indep.train_labels == legacy.train_labels
    assert indep.test_texts == legacy.test_texts and indep.test_labels == legacy.test_labels
    proxy = _proxy_texts(indep, size)
    assert len(proxy) == len(set(proxy)) == size
    assert not set(proxy) & set(indep.test_texts)
    assert not set(proxy) & set(indep.train_texts)
    assert _proxy_texts(indep, size) == proxy  # every attacker gets the same set
    assert set(_proxy_texts(legacy, size)) <= set(legacy.test_texts)  # original setting: subset of the evaluation set


@needs_ag_news
def test_full_dataset_holds_out_proxy_rows():
    legacy, indep = _ag_news(independent=False, limit=None), _ag_news(independent=True, limit=None)
    assert indep.test_texts == legacy.test_texts
    assert len(indep.train_texts) <= len(legacy.train_texts) - 512
    assert set(indep.train_texts) <= set(legacy.train_texts)
    proxy = _proxy_texts(indep, 512)
    assert len(proxy) == 512 and not set(proxy) & (set(indep.test_texts) | set(indep.train_texts))


@needs_ag_news
def test_global_rng_streams_untouched():
    np.random.seed(123); torch.manual_seed(123)
    expected = (np.random.rand(3), torch.rand(3))
    np.random.seed(123); torch.manual_seed(123)
    _build(independent=True)  # fresh build (not cached) so the draw really happens here
    assert np.array_equal(np.random.rand(3), expected[0]) and torch.equal(torch.rand(3), expected[1])


@pytest.mark.parametrize('limit', [600, None])
def test_list_loader_excludes_cross_split_duplicates(monkeypatch, limit):
    datasets = pytest.importorskip('datasets')
    train = [f'train review {i}' for i in range(2000)]
    test = [f'test review {i}' for i in range(1000)]
    train[:30] = test[:30]  # 30 evaluation texts also appear in the training split
    fake = {'train': {'text': train, 'label': [i % 2 for i in range(2000)]},
            'test': {'text': test, 'label': [i % 2 for i in range(1000)]}}
    monkeypatch.setattr(datasets, 'load_dataset', lambda *a, **k: fake)
    legacy, indep = _build('imdb', independent=False, limit=limit, size=50), _build('imdb', independent=True, limit=limit, size=50)
    assert indep.test_texts == legacy.test_texts
    if limit is not None:
        assert indep.train_texts == legacy.train_texts
    proxy = _proxy_texts(indep, 50)
    assert len(proxy) == 50 and not set(proxy) & (set(indep.test_texts) | set(indep.train_texts))
