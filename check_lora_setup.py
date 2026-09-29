"""Offline Pythia/LoRA smoke check; no dataset or pretrained downloads required.

Run in a separate process before training: python check_lora_setup.py
The temporary tiny model is only for dependency and training-path validation.
"""

import tempfile
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

import torch
from transformers import GPTNeoXConfig, GPTNeoXForCausalLM

from models import NewsClassifierModel


def main():
    for package in ("torch", "transformers", "peft", "torchao"):
        try:
            installed = version(package)
        except PackageNotFoundError:
            installed = "not installed"
        print(f"{package}: {installed}", flush=True)

    torch.set_num_threads(1)
    torch.manual_seed(42069)
    config = GPTNeoXConfig(
        vocab_size=32, hidden_size=16, intermediate_size=32,
        num_hidden_layers=1, num_attention_heads=2,
        max_position_embeddings=16, bos_token_id=0, eos_token_id=1,
    )
    with tempfile.TemporaryDirectory(prefix="augmp-pythia-check-") as directory:
        checkpoint = Path(directory) / "pythia-tiny"
        GPTNeoXForCausalLM(config).save_pretrained(checkpoint)

        def load_model():
            torch.manual_seed(42069)
            return NewsClassifierModel(
                model_name=str(checkpoint), num_labels=4, use_lora=True,
                lora_r=8, lora_alpha=16, lora_dropout=0.1,
            )

        model = load_model()
        repeat = load_model()
        assert torch.equal(model.get_flat_params(), repeat.get_flat_params()), \
            "Trainable initialization is not reproducible with the same seed"
        del repeat

        trainable = {n: p for n, p in model.named_parameters() if p.requires_grad}
        assert any("lora_A" in n for n in trainable), "LoRA was not attached"
        assert any("score" in n for n in trainable), "Classification head is frozen"
        assert all("lora_" in n or "score" in n for n in trainable), \
            "Unexpected trainable backbone parameters"
        before = {n: p.detach().clone() for n, p in model.named_parameters()}

        input_ids = torch.tensor([[2, 3, 4, 1], [5, 6, 7, 1]])
        attention_mask = torch.tensor([[1, 1, 1, 0], [1, 1, 1, 0]])
        labels = torch.tensor([0, 3])
        model.train()
        optimizer = torch.optim.Adam(trainable.values(), lr=5e-5)
        logits = model(input_ids, attention_mask)
        assert logits.shape == (2, 4)
        loss = torch.nn.functional.cross_entropy(logits, labels)
        assert torch.isfinite(loss), "Non-finite loss"
        loss.backward()
        assert all(p.grad is not None and torch.isfinite(p.grad).all()
                   for p in trainable.values()), "Missing or non-finite gradients"
        torch.nn.utils.clip_grad_norm_(trainable.values(), 1.0)
        optimizer.step()

        changed = {n for n, p in model.named_parameters()
                   if not torch.equal(before[n], p.detach())}
        assert any("lora_B" in n for n in changed), "LoRA weights did not update"
        assert any("score" in n for n in changed), "Classification head did not update"
        assert changed <= trainable.keys(), "Frozen backbone weights changed"
        flat = model.get_flat_params().clone()
        model.set_flat_params(flat)
        assert torch.equal(flat, model.get_flat_params()), "FL parameter round-trip failed"
        print(f"PASS: Pythia LoRA initialization, reproducibility, forward/backward, "
              f"optimizer step and FL parameter round-trip (loss={loss.item():.6f}).")


if __name__ == "__main__":
    main()
