import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataDir = '../data/ml-az/1_data_preprocessing/'

dataset = pd.read_csv(dataDir + 'Data.csv')

X = dataset.iloc[:, :-1].values
print(X)
