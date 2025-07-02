from keras import Sequential
from keras.layers import Input, Dense, Dropout
from keras.activations import relu, softmax, sigmoid
from keras.optimizers import Adam
from keras.losses import CategoricalCrossentropy
from keras.metrics import F1Score
from numpy import array
from pandas import read_csv, DataFrame
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

from functools import partial
from pathlib import Path
from sys import path


script_dir = Path(path[0])

data = read_csv(
    script_dir / 'sonar.csv',
    names=[f'attr{i}' for i in range(1, 61)] + ['target']
)
data.loc[data['target'] == 'R', 'target'] = 0
data.loc[data['target'] == 'M', 'target'] = 1
data['target'] = data['target'].astype(dtype=int)

x_train, x_test, y_train, y_test = train_test_split(
    data.loc[:, :'attr60'],
    data['target'],
    test_size=0.2,
    random_state=1
)

y_train_cat = to_categorical(y_train, num_classes=2)
y_test_cat = to_categorical(y_test, num_classes=2)

input_shape = x_train.shape[1]
epochs=150


model = Sequential(name="2_layers")
model.add(Input(shape=(input_shape,)))
model.add(Dense(60, activation=partial(relu, threshold=0.0)))
model.add(Dropout(0.3))
model.add(Dense(10, activation=partial(relu, threshold=0.0)))
model.add(Dropout(0.2))
model.add(Dense(2, activation=softmax, name="output"))

model.summary()

model.compile(
        optimizer=Adam(learning_rate=0.001, weight_decay=0.01),
        loss=CategoricalCrossentropy,
        metrics=["acc", F1Score(name="f1")]
        )        
        

model.fit(
        x_train.values, 
        y_train_cat,
        epochs=epochs,
        verbose=2,
        validation_split=0.15
        )

print('\nТЕСТИРОВАНИЕ\n')

scores = model.evaluate(
    x_test.values,
    y_test_cat,
    return_dict=True,
    verbose=2
)
print(
    f'\nloss = {scores["loss"]:.3f}',
    f'\naccuracy = {scores["acc"]:.1%}\n',
)

# С Dropout слоями
# Epoch 150/150
# 5/5 - 0s - 6ms/step - acc: 0.9433 - f1: 0.9426 - loss: 0.1818 - val_acc: 0.8800 - val_f1: 0.8768 - val_loss: 0.2034
# loss = 0.570
# accuracy = 71.4%

# Без Dropout
# Epoch 150/150
# 5/5 - 0s - 6ms/step - acc: 1.0000 - f1: 1.0000 - loss: 0.0550 - val_acc: 0.8800 - val_f1: 0.8768 - val_loss: 0.3486
# loss = 0.645
# accuracy = 71.4%

"""На модели с друмя скрытыми слоями Dropout значительно ограничивает рост метрик и снижение значения функции потерь на тренировочных данных. При этом значение функции потерь на тестировочных данных реально уменьшилось. Это говорит о снижении тенденции к переобучению модели."""