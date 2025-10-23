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

# --- Result Interpretation (Dynamic Feedback) ---
if aoc > 0.6:
    st.success("High translational concordance \(≧▽≦)/")
elif aoc > 0.3:
    st.warning("Moderate concordance ( ･᷄ὢ･᷅ )")
else:
    st.error("Low concordance ┻━┻︵╰(‵□′)╯︵┻━┻ – model may not translate clinically.")

st.caption("Formula: AOC = (AUC × Corr) / (1 + I² / 100)")

# --- Visualisation Section ---
st.markdown("### ˊ_>ˋComparative Stability: AUC, Corr, and AOC vs I²")

i2_values = np.linspace(0, 100, 200)
aoc_values = (auc * corr) / (1 + i2_values / 100)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(i2_values, np.repeat(auc, len(i2_values)), 'k--', label='AUC (constant)')
ax.plot(i2_values, np.repeat(corr, len(i2_values)), 'g--', label='Corr (constant)')
ax.plot(i2_values, aoc_values, 'r-', label='AOC')
ax.axvline(i2, color="gray", linestyle=":", alpha=0.5)
ax.set_xlabel("I² (%)")
ax.set_ylabel("Metric Value")
ax.set_title("AOC shows smoother decay with increasing heterogeneity")
ax.legend()
ax.grid(alpha=0.3)

st.pyplot(fig)

# --- Save Results ---
if st.button(":D Export simulation result"):
    import pandas as pd
    df = pd.DataFrame([[auc, corr, i2, aoc]], columns=["AUC", "Corr", "I²", "AOC"])
    df.to_csv("aoc_output.csv", index=False)
    st.success("Saved! Check aoc_output.csv in your workspace.")

st.markdown("---")
st.caption("Built with ( ´ ▽ ` )ﾉ❤️ by Xiyao Yu | Inspired by Algorithm-to-Outcome Concordance Framework")
