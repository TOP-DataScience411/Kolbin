from matplotlib import pyplot as plt
from pandas import DataFrame
from scipy.io.arff import loadarff
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix, 
    ConfusionMatrixDisplay,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

from pathlib import Path
from sys import path


script_dir = Path(path[0])
with open(script_dir / 'blood.arff', encoding='utf-8') as filein:
    data_raw = loadarff(filein)

blood = DataFrame(data_raw[0])

blood.columns = ['recency', 'frequency', 'monetary', 'time', 'donated']

blood.loc[blood['donated'] == b'1', 'donated'] = 0
blood.loc[blood['donated'] == b'2', 'donated'] = 1

blood = blood.astype(dtype=int)

# blood.info()


corr_table = blood.corr().round(2)

fig = plt.figure(figsize=(15, 15))
axs = fig.subplots(*corr_table.shape)

for i, var_i in enumerate(corr_table.index):
    for j, var_j in enumerate(corr_table.columns):
        axs[i][j].scatter(blood[var_i], blood[var_j])
        axs[i][j].set_title(
            f'{var_i.upper()}—{var_j.upper()}\n'
            f'corr = {corr_table.loc[var_i, var_j]}'
        )
        axs[i][j].xaxis.set_visible(False)
        axs[i][j].yaxis.set_visible(False)

# fig.savefig(script_dir / 'blood_corr.png', dpi=150)
# по результатам графического анализа — monetary не включать (за бесполезностью)


x_train, x_test, y_train, y_test = train_test_split(
    blood.loc[:, ['recency', 'frequency', 'time']],
    blood['donated'],
    test_size=0.2,
    random_state=1
)
model = DecisionTreeClassifier(
    max_depth=5,
    min_samples_leaf=5
)
model.fit(x_train, y_train)

y_predict = model.predict(x_test)
conf = confusion_matrix(y_test, y_predict)
print(conf)
# >>> conf
# array([[94, 15],
#        [20, 21]])
ConfusionMatrixDisplay(conf).plot(cmap='inferno').figure_.show()
print(
    f'\naccuracy = {accuracy_score(y_test, y_predict):.2f}'
    f'\nrecall = {recall_score(y_test, y_predict):.2f}\n'
)
# accuracy = 0.77
# recall = 0.51

fig = plt.figure(figsize=(15, 12))
axs = fig.subplots()

plot_tree(model, ax=axs)

# fig.savefig(script_dir / 'blood_tree.png', dpi=600)

'''
    Перебор параметров модели не дает улучшений работы самой модели, а напротив, только ухудшает ее. 
    Если взять за ошибку первого рода принятие человека за донора, а он окажется не донором, то в нашей модели вероятность ошибки первого рода примерно 23%. А вот ошибка второго рода составляет примерно 50%. 
    Также наблюдается большой разброс оценки эффективности при изменении разбивки на тестовую и обучающую выборки, 
    что указывает на недостаточную обработку данных или на плохо выбранную модель.
'''