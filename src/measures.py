"""
Meixner and Semicircle Distributions

This module implements the core probability measures:
- Meixner measure η_c^r (Meixner-type measure)
- Semicircle Law ν_SC (limiting measure)
"""

import numpy as np
from scipy.special import comb


class MeixnerMeasure:
    """
    Represents the Meixner-type measure η_c^r.
    
    The density is given by:
    f_c^r(x) = (1 / 2π) * sqrt(4 - x^2) / (1 + (e^c - 1)(1 + rx^2))
    
    Parameters:
    -----------
    c : float
        The parameter c in the Meixner measure.
    r : float
        The parameter r > 0.
    """
    
    def __init__(self, c, r):
        self.c = c
        self.r = r
    
    def density(self, x):
        """Evaluate the density f_c^r(x) at x."""
        numerator = np.sqrt(np.maximum(4 - x**2, 0))
        denominator = 1 + (np.exp(self.c) - 1) * (1 + self.r * x**2)
        return (1 / (2 * np.pi)) * numerator / denominator
    
    def moment(self, n):
        """
        Compute the n-th moment using the formula:
        ∫ P_n dη_c^r = e^(-cn) * E[e^(-rS_n^2)]
        
        where S_n^2 is a chi-squared random variable.
        """
        # Placeholder implementation
        return np.exp(-self.c * n)


class SemicircleLaw:
    """
    Represents the Semicircle Law ν_SC.
    
    The density is given by:
    ν_SC(x) = (1 / 2π) * sqrt(4 - x^2)   for |x| ≤ 2
    """
    
    def density(self, x):
        """Evaluate the density at x."""
        return np.where(np.abs(x) <= 2, (1 / (2 * np.pi)) * np.sqrt(4 - x**2), 0)
    
    def moment(self, n):
        """Compute the n-th moment of the Semicircle Law."""
        if n % 2 == 1:
            return 0
        else:
            # The 2k-th moment of the Semicircle Law is C_k (Catalan number)
            k = n // 2
            return comb(2*k, k) / (k + 1)
