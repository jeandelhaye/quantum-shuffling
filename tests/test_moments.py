"""
Unit Tests for Moment Calculations

Verify the correctness of moment formulas and density functions.
"""

import numpy as np
import unittest
from src.measures import MeixnerMeasure, SemicircleLaw


class TestMeasures(unittest.TestCase):
    """Test suite for probability measures."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.meixner = MeixnerMeasure(c=0.5, r=1.0)
        self.semicircle = SemicircleLaw()
    
    def test_meixner_density_bounded(self):
        """Test that Meixner density is bounded and non-negative."""
        x = np.linspace(-2, 2, 100)
        density = self.meixner.density(x)
        
        self.assertTrue(np.all(density >= 0))
        self.assertTrue(np.all(density <= 1))
    
    def test_semicircle_moments(self):
        """Test known moments of the Semicircle Law."""
        # Even moments should be positive; odd moments should be zero
        self.assertEqual(self.semicircle.moment(1), 0)
        self.assertEqual(self.semicircle.moment(3), 0)
        self.assertGreater(self.semicircle.moment(2), 0)
        self.assertGreater(self.semicircle.moment(4), 0)
    
    def test_density_integration(self):
        """Test that density integrates to approximately 1."""
        x = np.linspace(-2.1, 2.1, 1000)
        dx = x[1] - x[0]
        
        integral = np.sum(self.semicircle.density(x)) * dx
        self.assertAlmostEqual(integral, 1.0, places=2)


if __name__ == '__main__':
    unittest.main()
