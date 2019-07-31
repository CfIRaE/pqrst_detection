import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pathlib
from pqrst.src.detect import Detectors
from pqrst.data_loaders.data_loader import load_nparray, load_csv
from pqrst.utils.changefmt import npy_to_csv
from pqrst.utils.savitzky_golay import savitzky_golay

from scipy.signal import savgol_filter

current_dir = pathlib.Path(__file__).resolve()

example_dir_npy = current_dir.parent/'data'/'image5_signal.npy'
example_dir_csv = current_dir.parent/'data'/'data.csv'

data = npy_to_csv(example_dir_npy)
data_ = load_csv(example_dir_csv)
# for i in range(len(data)):
#     print(data[i][0])
yhat = savitzky_golay(data[3], 511, 3)

fs = 6880//3

detectors = Detectors(fs)

r_peaks = detectors.two_average_detector(yhat)
print(r_peaks)


plt.figure()
plt.plot(yhat)
plt.plot(r_peaks, [yhat[i] for i in r_peaks], 'ro')
plt.title('Detected R-peaks')

plt.show()
