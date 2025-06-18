from pandas import read_csv
from sklearn.metrics import fbeta_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sys import path
from pathlib import Path

path_dir = Path(path[0])
data = read_csv(path_dir / "breast_cancer_filter.csv")

target = data["target"]
data = data.drop("target", axis=1)


x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=1)

model = RandomForestClassifier(
        n_estimators=6,
        max_depth=4,
        bootstrap=True,
        n_jobs=-1, 
        random_state=1
)

model.fit(x_train, y_train)
pred = model.predict(x_test)

conf_matr = confusion_matrix(y_test, pred)
(TN, FP), (FN, TP) = conf_matr

accuracy = (TN + TP) / (TN + FP + FN + TP)

specificity = TN / (TN + FP)
precision = TP / (FP + TP)
recall = TP / (FN + TP)

f1 = 2 * precision * recall / (precision + recall)
fbeta = fbeta_score(y_test, pred, beta=0.5)

print(
    f'{accuracy=:.1%}',
    f'{specificity=:.1%}',
    f'{precision=:.1%}',
    f'{recall=:.1%}',
    f'{f1=:.1%}',
    f'{fbeta=:.1%}',
    sep='\n'
)


# accuracy=96.5%
# specificity=90.5%
# precision=94.7%
# recall=100.0%
# f1=97.3%
# fbeta=95.7%