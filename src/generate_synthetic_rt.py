from pathlib import Path
import numpy as np, pandas as pd

def make_data(n_subj=25, trials_per_cond=80, seed=42):
    rng = np.random.default_rng(seed)
    rows = []
    for s in range(1, n_subj+1):
        for cond in ["control","treatment"]:
            base = 620 if cond=="control" else 590
            rts = rng.normal(loc=base, scale=85, size=trials_per_cond).clip(250,2000)
            correct = rng.binomial(1, 0.94 if cond=="control" else 0.92, size=trials_per_cond)
            for t, rt, c in zip(range(1,trials_per_cond+1), rts, correct):
                rows.append((s, cond, t, round(float(rt),2), int(c)))
    return pd.DataFrame(rows, columns=["subject","condition","trial","rt_ms","correct"])

if __name__ == "__main__":
    out = Path("data"); out.mkdir(parents=True, exist_ok=True)
    df = make_data(); csv = out/"rt_demo.csv"; df.to_csv(csv, index=False)
    print(f"[OK] Wrote {csv} (rows={len(df)})")
