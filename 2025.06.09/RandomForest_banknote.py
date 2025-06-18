from pandas import read_csv
from sklearn.metrics import fbeta_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sys import path
from pathlib import Path

path_dir = Path(path[0])
data = read_csv(path_dir / "banknote-auth.csv")

target = data["class"]
data = data.drop("class", axis=1)


x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=1)

model = RandomForestClassifier(
        n_estimators=25,
        max_depth=5,
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

# accuracy=99.6%
# specificity=99.4%
# precision=99.2%
# recall=100.0%
# f1=99.6%
# fbeta=99.3%