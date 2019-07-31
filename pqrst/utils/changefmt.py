import pandas as pd
import numpy as np



def npy_to_csv(path,scaler_factor=None,make_abs=False):
    data = np.load(path,allow_pickle=True)


    df_array = []
    if scaler_factor != None:
        print("scaling...")
        data_ = 1000*data
        if make_abs == True:
            print("Absoluting...")
            for i in range(len(data_)):
                df = pd.DataFrame(data_[i], index=None, columns=None, dtype=None)
                min_ = np.amin(data_[i])
                df_ = [x[0] - min_ for x in df.values]
                df_array.append(df_)
        else:
            for i in range(len(data_)):
                df = pd.DataFrame(data_[i], index=None, columns=None, dtype=None)
                df_ = [x[0] for x in df.values]
                df_array.append(df_)

    else:
        if make_abs == True:
            for i in range(len(data)):
                df = pd.DataFrame(data[i], index=None, columns=None, dtype=None)
                min_ = np.amin(data[i])
                df_ = [x[0] - min_ for x in df.values]
                df_array.append(df_)
        else:
            for i in range(len(data)):
                df = pd.DataFrame(data[i], index=None, columns=None, dtype=None)
                df_ = [x[0] for x in df.values]
                df_array.append(df_)

    return df_array
