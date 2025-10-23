import numpy as np

def calculate_aoc(auc, corr, i2=0):
    """
    Calculate Algorithm-to-Outcome Concordance
    
    Parameters:
    -----------
    auc : float
        Area under ROC curve (0.5-1.0)
    corr : float
        Correlation between predicted score and outcome (-1 to 1)
    i2 : float
        Heterogeneity statistic (0-100, default=0 for single cohort)
    
    Returns:
    --------
    aoc : float
        AOC score (0-1)
    interpretation : str
    """
    if not (0.5 <= auc <= 1.0):
        raise ValueError("AUC must be between 0.5 and 1.0")
    if not (-1 <= corr <= 1):
        raise ValueError("Corr must be between -1 and 1")
    if not (0 <= i2 <= 100):
        raise ValueError("I² must be between 0 and 100")
    
    aoc = (auc * max(0, corr)) / (1 + i2/100)
    
    if aoc < 0.4:
        interp = "Poor translational fidelity"
    elif aoc < 0.7:
        interp = "Moderate fidelity"
    else:
        interp = "High fidelity"
    
    return aoc, interp

# Example usage
if __name__ == "__main__":
    # KEYNOTE-942 example
    aoc, interp = calculate_aoc(auc=0.85, corr=0.70, i2=0)
    print(f"AOC: {aoc:.3f} - {interp}")
