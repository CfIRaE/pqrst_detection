import os
import pandas as pd
import numpy as np



def load_nparray(path):
    array_ = np.load(path, allow_pickle=True)

    return array_

def load_txt(path):

    """
        File should contain single lead data

        for example:
        0.12312
        0.12312
        0.42323
        -0.34644
        .
        .
        .
    """
    with open(path,'r') as infile:
        lines = infile.readlines()

    array_ = []
    for line in lines:
        array_.append(float(line))

    return array_

def load_csv(path):
    """
        File should contain single lead data

        for example:
        0.12312
        0.12312
        0.42323
        -0.34644
        .
        .
        .
    """
    df = pd.read_csv(path)
    df_ = [x[0] for x in df.values]

    return df.values
