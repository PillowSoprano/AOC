import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameter Settings
np.random.seed(42)
n_models = 100  # Simulate 100 models
I2 = np.random.uniform(10, 40, n_models)  # Random Heterogeneity

# Simulated AUC and Correlation (with Noise)
true_auc = np.random.uniform(0.7, 0.95, n_models)
true_corr = np.random.uniform(0.4, 0.9, n_models)

# Plus noise (±0.05)
noise_auc = true_auc + np.random.normal(0, 0.03, n_models)
noise_corr = true_corr + np.random.normal(0, 0.03, n_models)

# Restricted range [0,1]
auc = np.clip(noise_auc, 0, 1)
corr = np.clip(noise_corr, 0, 1)

# Calculate AOC
aoc = (auc * corr) / (1 + I2 / 100)

# Save data
df = pd.DataFrame({
    "AUC": auc,
    "Corr": corr,
    "I²": I2,
    "AOC": aoc
})
df.to_csv("simulation/robustness_results.csv", index=False)
print("^_^ Data saved to simulation/robustness_results.csv")

# Scatter Plot: AOC vs AUC / Correlation
plt.figure(figsize=(7,5))
plt.scatter(auc, aoc, alpha=0.7, label='AUC vs AOC')
plt.scatter(corr, aoc, alpha=0.7, label='Corr vs AOC', marker='x')
plt.xlabel("AUC / Corr")
plt.ylabel("AOC")
plt.title("AOC relation to AUC and Corr under random noise")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("simulation/AOC_scatter_robustness.png", dpi=300)
plt.show()

# Box Plot: Comparison of Indicator Fluctuations
plt.figure(figsize=(6,5))
plt.boxplot([auc, corr, aoc], labels=["AUC", "Corr", "AOC"])
plt.ylabel("Metric Value")
plt.title("Robustness comparison under noisy conditions")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("simulation/AOC_boxplot_robustness.png", dpi=300)
plt.show()

print("\(≧▽≦)/ Figures saved: AOC_scatter_robustness.png and AOC_boxplot_robustness.png")
