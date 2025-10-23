"""
demo_example.py
----------------
Demonstration script for the Algorithm-to-Outcome Concordance (AOC) metric.

Author: Xiyao Yu (NTU Chemistry)
Paper: "A Proposed Framework for Quantifying AI-to-Clinical Translation: The Algorithm-to-Outcome Concordance (AOC) Metric", 2025
Repository: https://github.com/PillowSoprano/my_first_project

This script:
1. Loads example_data.csv
2. Computes AUC and correlation
3. Calculates the AOC score using aoc_calculator.py
4. Prints and interprets the result
"""

import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score
from scipy.stats import pearsonr

from aoc_calculator import calculate_aoc  # make sure aoc_calculator.py is in same folder

# Step 1. Load example data
print("Loading example dataset...")
df = pd.read_csv("example_data.csv")

# Optional: preview the data
print("\nData preview:")
print(df.head())

# Step 2. Compute AUC and correlation
print("\n Computing AUC and correlation...")
auc = roc_auc_score(df["actual_outcome"], df["predicted_score"])
corr, _ = pearsonr(df["predicted_score"], df["actual_outcome"])

# Step 3. Calculate AOC
print("\n🔹 Calculating Algorithm-to-Outcome Concordance (AOC)...")
aoc, interp = calculate_aoc(auc=auc, corr=corr, i2=0)

# Step 4. Display results
print("\n==============================")
print(f"AUC: {auc:.3f}")
print(f"Corr: {corr:.3f}")
print(f"AOC: {aoc:.3f} → {interp}")
print("==============================")

# Step 5. (Optional) Interpret in context
if aoc >= 0.7:
    print("^_^ High translational fidelity — model predictions align strongly with clinical outcomes.")
elif aoc >= 0.4:
    print("( ･᷄ὢ･᷅ ) Moderate fidelity — partial consistency between AI and real-world outcomes.")
else:
    print("(╥﹏╥) Poor fidelity — weak link between AI predictions and observed clinical results.")

print("\nDone. You can modify example_data.csv or replace it with your own dataset to test other scenarios.")
