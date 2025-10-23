import streamlit as st
from aoc_calculator import calculate_aoc

st.title("Algorithm-to-Outcome Concordance (AOC) Calculator")
st.write("Compute AOC for AI-to-Clinical Translation Studies")

auc = st.number_input("AUC (0.5-1.0)", 0.5, 1.0, 0.85)
corr = st.number_input("Correlation (-1 to 1)", -1.0, 1.0, 0.7)
i2 = st.number_input("Heterogeneity (I², 0-100)", 0, 100, 0)

aoc, interp = calculate_aoc(auc, corr, i2)
st.metric("AOC Value", f"{aoc:.3f}")
st.info(interp)
