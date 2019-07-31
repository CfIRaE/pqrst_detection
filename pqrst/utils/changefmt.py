import pandas as pd
import numpy as np



def npy_to_csv(path):
    data = np.load(path,allow_pickle=True)


    df_array = []

    for i in range(len(data)):
        df = pd.DataFrame(data[i], index=None, columns=None, dtype=None)
        df_ = [x[0] for x in df.values]
        df_array.append(df_)

    return df_array
