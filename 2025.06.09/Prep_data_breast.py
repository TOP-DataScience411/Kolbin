from pandas import read_csv,  DataFrame, Series
from matplotlib import pyplot as plt
from sklearn.datasets import load_breast_cancer

from sys import path
from pathlib import Path

path_dir = Path(path[0])
data_raw = load_breast_cancer()

data = DataFrame(data_raw['data'], columns=data_raw['feature_names'])
target = Series(data_raw['target'], name='target')

data_norm = (data - data.describe().loc['mean']) / data.describe().loc['std']

data_norm["target"] = target
data_norm.to_csv(path_dir / "breast_cancer_filter.csv", index=False)