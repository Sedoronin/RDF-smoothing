# RDFsmooth — RDF Smoothing and Visualization Tool

This Python script allows you to smooth and visualize radial distribution function (RDF) data using several techniques: **Moving Average**, **Univariate Spline Interpolation**, and **Gaussian Filtering**. It also generates an interactive Plotly chart for comparison and saves the smoothed data to disk.

---

## Features

- Read `.dat` files with two columns: distance `r` and `g(r)`
- Apply:
  - Centered moving average
  - Spline smoothing via `UnivariateSpline`
  - Gaussian filter smoothing
- Interactive Plotly visualization
- Export results in `.dat` format

---

## Requirements

- Python 3.7+
- Required libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `scipy`
  - `plotly`

Install dependencies via pip:

```bash
pip install numpy pandas matplotlib scipy plotly



###Usage

python smooth_rdf.py path/to/input_file.dat [--window WINDOW_SIZE] [--spline-s SMOOTHING] [--gauss-sigma SIGMA]


## Arguments

input_file (required): Path to a whitespace-delimited .dat file with two columns: r, g(r)

--window: Window size for moving average (default: 50)

--spline-s: Smoothing factor for UnivariateSpline (default: 110)

--gauss-sigma: Sigma value for Gaussian smoothing (default: 9)

## Example

python smooth_rdf.py rdf_data.dat --window 40 --spline-s 100 --gauss-sigma 8


## Output

Three smoothed datasets will be saved in the same directory:

rdf_data_smoothed_ma.dat

rdf_data_smoothed_spline.dat

rdf_data_smoothed_gaussian.dat

An interactive Plotly chart will also open in your default web browser.

## License

This project is licensed under the MIT License.
See the LICENSE file for details.

Author

Sergey V. Doronin (sedoronin@gmail.com)

















