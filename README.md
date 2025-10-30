# RT Analysis (Reaction Time) — Synthetic Demo

A tiny, clean pipeline for reaction-time (RT) data:
- generate a synthetic dataset,
- compute per-subject means for each condition,
- save a simple histogram figure.

## Files
- `src/generate_synthetic_rt.py` – creates `data/rt_demo.csv`
- `src/analyze_rt.py` – prints stats and saves `figs/rt_hist.png`
- `requirements.txt` – dependencies (`pandas`, `numpy`, `matplotlib`)

## How to run (locally)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt

# (Re)create data
python src/generate_synthetic_rt.py

# Analyze + make figure
python src/analyze_rt.py
