from matplotlib import pyplot as plt
from pandas import DataFrame, read_csv, merge
from scipy.io.arff import loadarff
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix, 
    ConfusionMatrixDisplay,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import load_iris

from pathlib import Path
from sys import path


script_dir = Path(path[0])
data_raw = load_iris(as_frame=True)
data = DataFrame(data_raw['data'], columns=data_raw['feature_names'])
data = merge(data, data_raw["target"], left_index=True, right_index=True)
data = data[data["target"] != 2]
print(data)

x_train, x_test, y_train, y_test = train_test_split(
    data.loc[:, ['sepal length (cm)', 'sepal width (cm)',  'petal length (cm)',  'petal width (cm)']],
    data['target'],
    test_size=0.1,
    random_state=3
)
model = DecisionTreeClassifier(
    max_depth=5,
    min_samples_leaf=1
)
model.fit(x_train, y_train)

y_predict = model.predict(x_test)
conf = confusion_matrix(y_test, y_predict)
print(conf)

ConfusionMatrixDisplay(conf).plot(cmap='inferno').figure_.show()
print(
    f'\naccuracy = {accuracy_score(y_test, y_predict):.2f}'
    f'\nrecall = {recall_score(y_test, y_predict):.2f}\n'
)

'''
    Дополнительно был взят датасет из библиотеки sklearn. Результаты обучения дают 100% точности модели, 
    что свидетельствует о ее вырождении. Вероятно из-за недостаточного объема данных.
'''