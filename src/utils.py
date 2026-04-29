"""
Utility Functions for Visualization and LaTeX Rendering

Helper functions to create high-quality plots and render mathematical expressions.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import rcParams


def latex_render():
    """Configure matplotlib for LaTeX rendering."""
    rcParams['text.usetex'] = True
    rcParams['font.family'] = 'serif'
    rcParams['font.serif'] = ['Computer Modern']


def plot_measure(x, density, label="", title="", filename=None):
    """
    Plot a probability density function.
    
    Parameters:
    -----------
    x : np.ndarray
        The x-axis values.
    density : np.ndarray
        The density values.
    label : str
        Label for the curve.
    title : str
        Title of the plot.
    filename : str, optional
        If provided, save the plot to this file.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x, density, linewidth=2.5, label=label)
    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'Density', fontsize=14)
    plt.title(title, fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(alpha=0.3)
    
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()


def plot_tv_distance(times, tv_distances, parameters, filename=None):
    """
    Plot the total variation distance over time.
    
    Parameters:
    -----------
    times : np.ndarray
        Time steps.
    tv_distances : np.ndarray
        TV distances at each time.
    parameters : dict
        Dictionary with parameters (c, r, etc.).
    filename : str, optional
        If provided, save the plot to this file.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(times, tv_distances, linewidth=2.5, marker='o')
    plt.xlabel(r'Time $t$', fontsize=14)
    plt.ylabel(r'$d_{TV}$', fontsize=14)
    plt.title(f"Total Variation Distance (c={parameters.get('c')}, r={parameters.get('r')})", fontsize=16)
    plt.grid(alpha=0.3)
    
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()
