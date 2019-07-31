import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pathlib
from pqrst.src.detect import Detectors
from pqrst.data_loaders.data_loader import load_nparray, load_csv
from pqrst.utils.changefmt import npy_to_csv
from pqrst.utils.savitzky_golay import savitzky_golay
from pqrst.utils.plotter import plot_signal


from scipy.signal import savgol_filter

current_dir = pathlib.Path(__file__).resolve()

example_dir_npy = current_dir.parent/'data'/'image5_signal.npy'
example_dir_csv = current_dir.parent/'data'/'data.csv'

data = npy_to_csv(example_dir_npy, scaler_factor = 1, make_abs = True)
data_ = load_csv(example_dir_csv)
for i in range(len(data)):
    print(data[i][5])



# print(yhat)

fs = len(data[0])//3

detectors = Detectors(fs)

# r_peaks = detectors.two_average_detector(data[3])
# print(r_peaks)

r_peaks_list = []
for i in range(15):
    r_peaks = detectors.two_average_detector(data[i])
    r_peaks_list.append(r_peaks)

plot_signal(data,r_peaks_list)


#first applying smoothening filter

smooth_data = []
smooth_peaks = []
for i in range(15):
    yhat = savitzky_golay(data[i], 211, 3)
    peaks = detectors.two_average_detector(yhat)
    smooth_data.append(yhat)
    smooth_peaks.append(peaks)


plot_signal(smooth_data,smooth_peaks)
