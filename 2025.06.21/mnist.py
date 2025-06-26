from keras import Sequential
from keras.activations import (
    relu, 
    leaky_relu, 
    sigmoid,
    softmax,
)
from keras.layers import Dense, Input
from keras.losses import CategoricalCrossentropy
from keras.metrics import (
    CategoricalAccuracy,
    CategoricalCrossentropy as CategoricalCrossentropyMetric,
    F1Score
)
from keras.optimizers import Adam

from matplotlib import pyplot as plt
from numpy import (
    array, 
    load as load_npz, 
)
from numpy.random import default_rng
from PIL import Image
from sklearn.metrics import accuracy_score

from functools import partial
from pathlib import Path
from sys import path


def one_hot_encoder(x):
    return (0,) * x + (1,) + (0,) * (9 - x)



script_dir = Path(path[0])
data_path = script_dir / 'mnist.npz'

with open(data_path, 'rb') as fileout:
    x_test, x_train, y_train, y_test = load_npz(fileout).values()


input_vector_len = x_train.shape[1] * x_train.shape[2]

# изменение размерности
x_train = x_train.reshape((x_train.shape[0], input_vector_len))
x_test = x_test.reshape((x_test.shape[0], input_vector_len))
# масштабирование — приведение к диапазону [0; 1]
x_train = x_train / 255
x_test = x_test / 255
# перекодирование
y_train = array([one_hot_encoder(y) for y in y_train])
y_test = array([one_hot_encoder(y) for y in y_test])


model = Sequential(name='MNIST_digits_reckognition')

model.add(Input(shape=(input_vector_len,), dtype='float64'))
model.add(Dense(200, activation=partial(relu, threshold=0.4)), )
model.add(Dense(100, activation=partial(relu, threshold=0.4)), )
model.add(Dense(10, activation=softmax, name='output'))

model.summary()


model.compile(
    loss=CategoricalCrossentropy(),
    optimizer=Adam(learning_rate=0.0001),
    metrics=[
        CategoricalAccuracy(name='acc'),
    ]
)

print('\nОБУЧЕНИЕ\n')
epochs = 15
training_results = model.fit(
    x_train,
    y_train,
    epochs=epochs,
    validation_split=0.25,
    verbose=2
)

print('\nТЕСТИРОВАНИЕ\n')
scores = model.evaluate(
    x_test,
    y_test,
    return_dict=True,
    verbose=0
)


fig = plt.figure(figsize=(11, 5))
axs = fig.subplots(1, 2)

axs[0].plot(range(1, epochs+1), training_results.history['loss'], label='loss')
axs[0].plot(range(1, epochs+1), training_results.history['val_loss'], label='val_loss')
axs[0].scatter(epochs+1, scores['loss'], s=30, c='#c80608', label='test_loss')
axs[0].set_xticks(range(1, epochs+2))
axs[0].legend()

axs[1].plot(range(1, epochs+1), training_results.history['acc'], label='accuracy')
axs[1].plot(range(1, epochs+1), training_results.history['val_acc'], label='val_accuracy')
axs[1].scatter(epochs+1, scores['acc'], s=30, c='#c80608', label='test_accuracy')
axs[1].set_xticks(range(1, epochs+2))
axs[1].legend()

plt.show()


test_images_dir = script_dir / 'mnist_test/28'

test_images = array([
    array(Image.open(img_path).convert('L'))
    for img_path in test_images_dir.iterdir()
    if img_path.is_file()
])
test_images = test_images.reshape(
    test_images.shape[0], 
    test_images.shape[1] * test_images.shape[2]
)
test_images = test_images / 255


predictions = model.predict(test_images, verbose=1)

test_true = array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 4, 8])
print(
    f"\n{predictions.round(2)=}\n",
    f"{test_true=}\n",
    f"loss = {scores["loss"]:.3f}\n",
    f"accuracy = {scores["acc"]:.1%}\n",
    f"test_accuracy = {accuracy_score(test_true, predictions.argmax(axis=1)):.2f}"
    )



# Эксперимент № 1
# При 3 слоях (200 (ReLU), 100 (sigmoid) и 10 (softmax) параметров), 15 эпохах, validation_split=0.25, learning_rate=0.01

# loss = 0.188
# accuracy = 95.2%
# test_accuracy = 0.92

# loss = 0.146
# accuracy = 96.0%
# test_accuracy = 0.69

# -------------------------------------------------------------------------------------------------

# Эксперимент № 2
# При 3 слоях (200 (ReLU), 100 (ReLU) и 10 (softmax) параметров), 10 эпохах, validation_split=0.25, learning_rate=0.01
# Графики val_loss и val_acc стали более пологими.

# loss = 0.157
# accuracy = 96.4%
# test_accuracy = 0.85

# loss = 0.195
# accuracy = 96.2%
# test_accuracy = 0.69

# -------------------------------------------------------------------------------------------------

# Эксперимент № 3
# При 3 слоях (200 (ReLU), 100 (ReLU) и 10 (softmax) параметров), 10 эпохах, validation_split=0.25, learning_rate=0.001
# Графики val_loss и val_acc стали более пологими, без резких скачков.

# loss = 0.102
# accuracy = 97.7%
# test_accuracy = 0.85

# loss = 0.088
# accuracy = 97.9%
# test_accuracy = 0.85

# -------------------------------------------------------------------------------------------------

# Эксперимент № 4
# При 3 слоях (200 (leaky_relu), 100 (leaky_relu) и 10 (softmax) параметров), 10 эпохах, validation_split=0.25, learning_rate=0.001

# loss = 0.112
# accuracy = 97.4%
# test_accuracy = 0.69

#  loss = 0.131
#  accuracy = 96.8%
#  test_accuracy = 0.69

# -------------------------------------------------------------------------------------------------

# Эксперимент № 5
# При 3 слоях (200 (relu), 100 (relu) и 10 (softmax) параметров), 10 эпохах, validation_split=0.2, learning_rate=0.001
# Увеличение тренировочной выборки значимого результата не дало. (пробовал validation_split до 0.15)

# loss = 0.089
# accuracy = 97.6%
# test_accuracy = 0.85

# loss = 0.100
# accuracy = 97.7%
# test_accuracy = 0.85

# -------------------------------------------------------------------------------------------------

# Эксперимент № 6
# При 3 слоях (100 (relu), 50 (relu) и 10 (softmax) параметров), 10 эпохах, validation_split=0.25, learning_rate=0.001
# Точность немного ухудшилась по сравнению с экспериментом № 3.

# loss = 0.096
# accuracy = 97.4%
# test_accuracy = 0.77

# loss = 0.094
# accuracy = 97.4%
# test_accuracy = 0.77

# -------------------------------------------------------------------------------------------------

# Эксперимент № 7
# При 3 слоях (400 (relu), 200 (relu) и 10 (softmax) параметров), 10 эпохах, validation_split=0.25, learning_rate=0.001
# Увеличение количества параметров в слоях положительного результата не дало

# loss = 0.098
# accuracy = 97.8%
# test_accuracy = 0.69

# loss = 0.106
# accuracy = 97.5%
# test_accuracy = 0.85

# -------------------------------------------------------------------------------------------------

# Эксперимент № 8
# При 4 слоях (200 (relu), 100 (relu), 50 (relu) и 10 (softmax) параметров), 10 эпохах, validation_split=0.25, learning_rate=0.001
# Добавление еще одного слоя положительного результата не дало

# loss = 0.100
# accuracy = 97.7%
# test_accuracy = 0.69

# loss = 0.090
# accuracy = 97.7%
# test_accuracy = 0.77

# -------------------------------------------------------------------------------------------------

# Эксперимент № 9   Наилучшая полученная конфигурация гиперпараметров.
# При 3 слоях (200 (relu), 100 (relu) и 10 (softmax) параметров), 15 эпохах, validation_split=0.25, learning_rate=0.0001
# Графики без скачков. Возможно достаточно 10 эпох обучения. Наименьшее значение функции потерь.

# loss = 0.077
# accuracy = 97.7%
# test_accuracy = 0.77

# loss = 0.076
# accuracy = 97.6%
# test_accuracy = 0.62