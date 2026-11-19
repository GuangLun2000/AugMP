# AugMP Model Manipulation on FedLLMs

[![arXiv](https://img.shields.io/badge/arXiv-2605.07961-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.07961) &nbsp; [![GitHub](https://img.shields.io/badge/GitHub-Code-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/GuangLun2000/AugMP)

- Graph Representation Learning Augmented Model Manipulation on Federated Fine-Tuning of LLMs.
- [**Hanlin Cai**](https://caihanlin.com/), Kai Li, Houtianfu Wang, Haofan Dong, Yichen Li, Falko Dressler, Ozgur B. Akan
- University of Cambridge; University of Luxembourg; TU Berlin; Koc University

## Overview

![AugMP framework: federated setup, VGAE, iterative manipulation, and qualitative effect on the global LLM](Figure/AugMP.png)

---

## File Structure

```text
.
├── main.py                            # Entry point: experiment config + federated training loop
├── client.py                          # BenignClient and AttackerClient (AugMP: VGAE + constrained manipulation)
├── server.py                          # FedAvg aggregation, evaluation, round orchestration
├── models.py                          # NewsClassifierModel (HF backbone + optional LoRA), VGAE
├── data_loader.py                     # Dataset loading (AG News, Yahoo Answers, IMDB, DBpedia)
├── attack_baseline_alie.py            # ALIE baseline (NeurIPS ’19)
├── attack_baseline_gaussian.py        # Gaussian baseline (USENIX Security ’20)
├── attack_baseline_sign_flipping.py   # Sign-flipping baseline (ICML ’18)
├── attack_baseline_gap.py             # GAP baseline (Gradient Assembly Poisoning)
├── shadow_defense.py                  # Optional: Krum / Trimmed Mean / Median detection stats (not applied)
├── visualization.py                   # Experiment figures / plots
├── fed_checkpoint.py                  # Save global model + metadata after FL
├── decoder_adapters.py                # SeqCLS backbone → CausalLM transfer (Qwen2.5, Pythia)
├── run_downstream_generation.py       # Task 2 CLI: checkpoint + probes → JSONL
├── observe/                           # Optional experiments, run through main.py (usage in each file header)
│   ├── observe_config.py              # Config of the limited-observability experiment
│   ├── observability.py               # Which benign updates the attackers observe
│   ├── run_observability_sweep.py     # Multi-run sweep driver
│   ├── plot_observability.py          # Sweep figures + CSV summary
│   ├── overhead.py                    # Per-round runtime / GPU-memory profiling (config 'profile_overhead')
│   └── run_m_sweep.py                 # Runtime vs. number of selected parameters M
├── data/                              # Training and testing datasets
│   ├── AG News Datasets/              # train.csv, test.csv, Task 2 probe files (*.json)
│   └── Yahoo! Answers Datasets/       # Source link (downloaded automatically)
├── demo/                              # Example Task 2 outputs (Qwen2.5-0.5B)
├── Figure/                            # Framework figure
├── AugMP_Colab.ipynb                  # Colab notebook
├── requirements.txt                   # Python dependencies
└── LICENSE
```

## Supported Models

- Encoder-only (BERT-style): `distilbert-base-uncased`, `bert-base-uncased`, `roberta-base`, `microsoft/deberta-v3-base`
- Decoder-only (GPT-style): `gpt2`, `EleutherAI/pythia-160m`, `EleutherAI/pythia-1b`, `facebook/opt-125m`, `Qwen/Qwen2.5-0.5B`
- Configure in `main.py` via `model_name`.

## Supported Datasets

- **AG News**: `dataset='ag_news'`, `num_labels=4`, `max_length=128` (default)
- **Yahoo Answers** (yassiracharki/Yahoo_Answers_10_categories_for_NLP): `dataset='yahoo_answers'`, `num_labels=10`, `max_length=128` (10 topic classes, 1.4M train / 60K test)
- **IMDB** (stanfordnlp/imdb): `dataset='imdb'`, `num_labels=2`, `max_length=512` (or 256 for lower memory)
- **DBpedia 14** (fancyzhx/dbpedia_14): `dataset='dbpedia'`, `num_labels=14`, `max_length=512` (14 topic classes, 560K train / 70K test)
- Configure in `main.py` via `dataset`, `num_labels`, and `max_length`. AG News is included in `data/`; the other datasets are downloaded from Hugging Face on first use.

## Supported Attacks

- Proposed: `attack_method='AugMP'`
- Baselines: `'ALIE'`, `'Gaussian'`, `'SignFlipping'`, `'GAP'`
- No attack (benign setting): `num_attackers=0`
- Configure in `main.py` via `attack_method` and `num_attackers`.

<br>

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Code

### Local Execution

```bash
python main.py
```

Results (JSON log, CSV tables and figures, named after `experiment_name`) are saved to `results/`.

### Google Colab Execution (or other Cloud AI platforms)

**Option 1: Simple Version (Recommended for quick runs)**

```python
# Cell 1: Install dependencies
!git clone https://github.com/GuangLun2000/AugMP.git
!pip uninstall -y torchao  # optional preinstalled package that can stop PEFT from attaching LoRA
!pip install -r ./AugMP/requirements.txt

# Cell 2: Run experiment
!cd ./AugMP && python main.py
```

**Option 2: Interactive Notebook (Recommended for configuration changes)**

1. Open `AugMP_Colab.ipynb` in Google Colab
2. Enable GPU: Runtime → Change runtime type → GPU
3. Run all cells: Runtime → Run all

<br>

---

### Task 2: Downstream Generation (optional)

Task 2 checks how the federated global model behaves in a downstream generation task: the saved classification head labels each probe article, the backbone is copied into `AutoModelForCausalLM` (no extra fine-tuning), and the causal LM explains the label.

1. In `main.py`, set `save_global_checkpoint=True` and train a Qwen2.5 or Pythia model on AG News. The checkpoint is saved to `results/global_checkpoint/`.
2. Generate explanations (or set `run_downstream_after_fl=True` to run this automatically after training):

```bash
python run_downstream_generation.py \
  --checkpoint results/global_checkpoint \
  --probes "data/AG News Datasets/ag_news_business_30.json" \
  --output results/downstream_gen.jsonl \
  --stable
```

Each JSONL line holds the predicted label, the dataset label and the generated explanation. `--stable` uses greedy decoding with a repetition penalty; `--help` lists all options. Probe sets in `data/AG News Datasets/`: `ag_news_business_30.json` (30 Business articles, default) and `ag_news_curated_10.json` (10 articles from all four classes). Example outputs are in [`demo/`](demo/).

To support another decoder family, implement a `DecoderAdapter` and add it to `ADAPTER_REGISTRY` in [`decoder_adapters.py`](decoder_adapters.py).
