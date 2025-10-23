### AOC Simulation Framework

### Overview
This folder contains the simulation modules used to demonstrate and validate the Algorithm-to-Outcome Concordance (AOC) metric proposed in the accompanying manuscript.
The tools here allow researchers to explore how model performance (AUC), model-outcome correlation (Corr), and study heterogeneity (I²) jointly influence the AOC score — a quantitative measure of AI-to-clinical translation fidelity.
### File Structure
File	Description
cross_validation_AOC.py	Simulates 100 pseudo-models and performs cross-validation to examine how AOC responds to changes in AUC, Corr, and I². Generates scatter plots and CSV outputs.
aoc_streamlit_app.py	An interactive Streamlit dashboard for real-time AOC visualization. Users can manipulate parameters and observe AOC trends dynamically.

### Installation
Ensure you have Python ≥3.10 and the following dependencies installed:

```bash
pip install streamlit numpy pandas matplotlib
```

Alternatively, you can install all dependencies from the root folder:
```bash
pip install -r requirements.txt
```
### Running the Simulator

### 1. Interactive Streamlit App
Run the interactive simulator to visualize AOC behavior in your browser:
```bash
streamlit run simulation/aoc_streamlit_app.py
```
or (if streamlit isn’t in PATH):
```bash
python3 -m streamlit run simulation/aoc_streamlit_app.py
```
### Features
Adjustable sliders for AUC, Corr, and I²
Real-time AOC computation and interpretive feedback:
\(≧▽≦)/ High translational concordance
( ･᷄ὢ･᷅ ) Moderate concordance
┻━┻︵╰(‵□′)╯︵┻━┻ Low concordance
Comparative chart showing AUC, Corr, and AOC vs. I²
One-click export of results to aoc_output.csv

### 2. Cross-Validation Simulation
To generate pseudo-data and compare AOC vs. AUC stability:
```bash
python simulation/cross_validation_AOC.py
```
This will output:
AOC_sensitivity_plot.png — scatter plot of AOC trends
simulation_results.csv — generated dataset
cv_results.csv — correlation table from cross-validation
🧩 Interpretation
AOC is computed as:
# AOC Formula
AOC = (AUC × Corr) / (1 + I<sup>2</sup> / 100)

AUC → model discriminative ability
Corr → alignment between model predictions and clinical outcomes
I² → between-study heterogeneity penalty

The simulation and app demonstrate that AOC:
Increases with stronger AUC and Corr
Decreases smoothly with higher heterogeneity
Provides a more interpretable, translationally meaningful measure than AUC alone
### Citation
If you use this simulator or the AOC metric in your research, please cite:
[Your Name], et al. “A Proposed Framework for Quantifying AI-to-Clinical Translation:
The Algorithm-to-Outcome Concordance (AOC) Metric.” (2025)
### Author Notes
Developed by Xiyao Yu (@PillowSoprano)
School of Chemistry, Nanyang Technological University, Singapore
For research in computational oncology and AI-driven clinical translation.
