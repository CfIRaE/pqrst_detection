import sys
sys.path.append("..")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pathlib
from ..pqrst.src.detect import Detectors

current_dir = pathlib.Path(__file__).resolve()

example_dir = current_dir.parent/'data'/'ECG.tsv'
example_dir_np = current_dir.parent/'data'/'dummy.npy'
example_dir_csv = current_dir.parent/'data'/'data.csv'



unfiltered_ecg_dat = np.loadtxt(example_dir)
data__ = np.load(example_dir_np,allow_pickle = True)

def csv_loader(path):
    #load csv data
    df = pd.read_csv(path)
    return df.values

csv_data = csv_loader(example_dir_csv)

print("------------------------------------------------------------------------------------")
print(len(data__))
print("------------------------------------------------------------------------------------")
# unfiltered_ecg = unfiltered_ecg_dat[:,0]
unfiltered_ecg = data__
# print(unfiltered_ecg)


fs = 6880//3

detectors = Detectors(fs)

r_peaks = detectors.two_average_detector(csv_data)
print(r_peaks)
#r_peaks = detectors.matched_filter_detector(unfiltered_ecg)
#r_peaks = detectors.swt_detector(unfiltered_ecg)
#r_peaks = detectors.engzee_detector(unfiltered_ecg)
#r_peaks = detectors.christov_detector(unfiltered_ecg)
#r_peaks = detectors.hamilton_detector(unfiltered_ecg)
#r_peaks = detectors.pan_tompkins_detector(unfiltered_ecg)


plt.figure()
plt.plot(csv_data)
plt.plot(r_peaks, csv_data[r_peaks], 'ro')
plt.title('Detected R-peaks')

plt.show()
