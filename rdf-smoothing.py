import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from scipy.ndimage import gaussian_filter1d
import plotly.graph_objs as go
import plotly.offline as pyo
import argparse

def read_data(file_path):
    """
    Load two-column data from a whitespace-delimited .dat file.
    Columns: x (distance), y (RDF)
    """
    return pd.read_csv(file_path, sep=r'\s+', header=None)

def moving_average(y_series: pd.Series, window_size: int) -> np.ndarray:
    """Compute a centered moving average."""
    return y_series.rolling(window=window_size, center=True).mean().values

def spline_interpolation(x: np.ndarray,
                         y: np.ndarray,
                         smoothing_factor: float) -> np.ndarray:
    """
    Smooth data using UnivariateSpline.
    The smoothing_factor 's' controls the trade-off between closeness and smoothness.
    """
    spline = UnivariateSpline(x, y, s=smoothing_factor)
    return spline(x)

def gaussian_smoothing(y: np.ndarray, sigma: float) -> np.ndarray:
    """Apply a 1D Gaussian filter with the given standard deviation sigma."""
    return gaussian_filter1d(y, sigma)

def main():
    parser = argparse.ArgumentParser(
        description="Apply smoothing to RDF data and compare algorithms."
    )
    parser.add_argument("input_file", help="Path to the input .dat file")
    parser.add_argument("--window", type=int, default=50,
                        help="Moving average window size")
    parser.add_argument("--spline-s", type=float, default=110,
                        help="Spline smoothing factor")
    parser.add_argument("--gauss-sigma", type=float, default=9,
                        help="Gaussian filter sigma")
    args = parser.parse_args()

    # Load data
    df = read_data(args.input_file)
    x = df[0].values
    y = df[1].values

    # Compute smoothed curves
    sm_ma = moving_average(df[1], args.window)
    sm_sp = spline_interpolation(x, y, args.spline_s)
    sm_ga = gaussian_smoothing(y, args.gauss_sigma)

    # Interactive Plotly visualization
    traces = [
        go.Scatter(x=x, y=y, mode='lines', name='Original', opacity=0.5),
        go.Scatter(x=x, y=sm_ma, mode='lines', name='Moving Average'),
        go.Scatter(x=x, y=sm_sp, mode='lines', name='Spline'),
        go.Scatter(x=x, y=sm_ga, mode='lines', name='Gaussian'),
    ]
    layout = go.Layout(
        title='RDF Smoothing Comparison',
        xaxis=dict(title='r'),
        yaxis=dict(title='g(r)')
    )
    fig = go.Figure(data=traces, layout=layout)
    pyo.iplot(fig)

    # Save results
    base = args.input_file.rsplit('.', 1)[0]
    np.savetxt(f"{base}_smoothed_ma.dat", np.column_stack((x, sm_ma)), delimiter='\t')
    np.savetxt(f"{base}_smoothed_spline.dat", np.column_stack((x, sm_sp)), delimiter='\t')
    np.savetxt(f"{base}_smoothed_gaussian.dat", np.column_stack((x, sm_ga)), delimiter='\t')

    print(f"Smoothed data saved as {base}_smoothed_[ma|spline|gaussian].dat")

if __name__ == "__main__":
    main()
