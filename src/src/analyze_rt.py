from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA = Path("data/rt_demo.csv")
FIGS = Path("figs")

if __name__ == "__main__":
    if not DATA.exists():
        raise SystemExit("Run first:  python src/generate_synthetic_rt.py")
    FIGS.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA)
    table = df.groupby(["subject","condition"])["rt_ms"].mean().unstack()
    diff = table["control"] - table["treatment"]

    print("Per-subject mean RT (ms) [first 5]:")
    print(table.head())
    print("\nMean diff (control - treatment):", round(diff.mean(),2), "ms")

    plt.figure()
    df["rt_ms"].hist(bins=50)
    plt.title("RT distribution (ms)"); plt.xlabel("rt_ms"); plt.ylabel("count")
    out = FIGS/"rt_hist.png"; plt.savefig(out, dpi=150, bbox_inches="tight")
    print(f"[OK] Saved figure to {out}")
