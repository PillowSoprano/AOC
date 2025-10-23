import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit Page Settings
st.set_page_config(page_title="AOC Interactive Simulator", page_icon="^_^", layout="centered")

st.title("^_^Algorithm-to-Outcome Concordance (AOC) Simulator")
st.markdown("""
Use the sliders below to explore how **AUC**, **Correlation (Corr)**, and **Heterogeneity (I²)** 
interact to determine the **AOC** metric.
""")

# --- Parameter Input ---
auc = st.slider("Model AUC (0-1)", 0.5, 1.0, 0.85, 0.01)
corr = st.slider("Correlation between model and clinical outcome (-1 to 1)", -1.0, 1.0, 0.7, 0.01)
i2 = st.slider("Study Heterogeneity I² (0-100%)", 0.0, 100.0, 30.0, 1.0)

# --- AOC Computing ---
aoc = (auc * corr) / (1 + i2 / 100)

# --- Display results ---
st.metric(label="Calculated AOC", value=f"{aoc:.3f}")
st.caption("Formula: AOC = (AUC × Corr) / (1 + I² / 100)")

# --- Visualisation Section ---
st.markdown("### 📈 Sensitivity of AOC to I²")

i2_values = np.linspace(0, 100, 200)
aoc_values = (auc * corr) / (1 + i2_values / 100)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(i2_values, aoc_values, label="AOC vs I²", linewidth=2)
ax.axvline(i2, color="red", linestyle="--", alpha=0.6)
ax.set_xlabel("I² (%)")
ax.set_ylabel("AOC Value")
ax.set_title("AOC Decreases with Increasing Heterogeneity")
ax.legend()
ax.grid(alpha=0.3)

st.pyplot(fig)

# --- Save Results ---
if st.button(" Save current simulation"):
    np.savetxt("aoc_simulation_snapshot.csv", [[auc, corr, i2, aoc]], 
               delimiter=",", header="AUC,Corr,I2,AOC", comments="")
    st.success("Saved to aoc_simulation_snapshot.csv!")

st.markdown("---")
st.caption("Built with ( ´ ▽ ` )ﾉ❤️ by Xiyao Yu | Inspired by Algorithm-to-Outcome Concordance Framework")
