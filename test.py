from pqrst.utils.changefmt import npy_to_csv
import pathlib


current_dir = pathlib.Path(__file__).resolve()
example_dir_npy = current_dir.parent/'data'/'image5_signal.npy'

data = npy_to_csv(example_dir_npy)

print(data[0])
