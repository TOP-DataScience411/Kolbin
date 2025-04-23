from matplotlib import pyplot as plt, rcParams, colormaps
from numpy import array
from numpy.random import default_rng
from pandas import read_csv, DataFrame, Series
from sklearn.metrics import silhouette_score

from itertools import combinations, pairwise
from pathlib import Path
from sys import path
from time import sleep


def euclid_line(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 - x2)**2 + (y1 - y2)**2)**.5


dir_path = Path(path[0])

rcParams['axes.labelcolor'] = '#eee'
rcParams['axes.labelsize'] = 8

# colors = colormaps['tab10'].colors
# Размеры изображения с графиками
row = 3
col = 5
# Кол-во кластеров для проверки от 2 до clusters_cnt
clusters_cnt = 8


fig = plt.figure(figsize=(17, 8), facecolor='#455A64')
fig.suptitle("Суммы внутрикластерных расстояний (WCSS)\nРазности значений WCSS.\n")
axs = fig.subplots(row, col)

data = read_csv(dir_path / 'test_clusters.csv', names=['x1', 'x2'])
all_scores = []

# Прогон алгоритма для определения подходящего числа кластеров.
for i in range(row):
    for j in range(col):
        wcss = []
        # проверка различного количества кластеров 
        for n in range(2, clusters_cnt):
            # выбор случайных точек для начального положения центроид
            centroids = default_rng().choice(data, n, replace=False)
            
            for _ in range(10):
                cluster = []
                for point_i in data.values:
                    lines = []
                    for centr_k in centroids:
                        # вычисление расстояния от каждой точки до каждой центроиды
                        lines.append(euclid_line(point_i, centr_k))
                    # выбор минимального из вычисленных расстояний
                    cluster.append(array(lines).argmin())
                
                centroids = []
                for k in range(n):
                    x1_k = data.loc[array(cluster) == k]['x1']
                    x2_k = data.loc[array(cluster) == k]['x2']
                    centroids.append((x1_k.mean(), x2_k.mean()))
                centroids = array(centroids)
            
            total = 0
            for k in range(n):
                data_k = data.loc[array(cluster) == k]
                for p1, p2 in combinations(data_k.values, 2):
                    total += euclid_line(p1, p2)
            wcss.append(total)
            
            wcss_diff = array([
                n1 - n2
                for n1, n2 in pairwise(wcss)
            ])
            wcss_diff_x = range(2, 2+len(wcss_diff))
            
            # Сохранение кол-ва кластеров и значений метрики silhouette_score
            all_scores.append([n, silhouette_score(data.values, cluster)])

        wcss_x = range(2, 2+len(wcss))
        if not j:
            axs[i][j].set( 
                ylabel='Разность WCSS, WCSS'
            )
        if i == row-1:
            axs[i][j].set(
                xlabel='количество кластеров'
            )
        axs[i][j].set_xticks(wcss_x)
        axs[i][j].plot(wcss_x, wcss, '.-r', lw=2, ms=10)
        axs[i][j].plot(wcss_diff_x, wcss_diff, 's-c', lw=2, ms=5)
plt.savefig(dir_path / "all WCSS.jpg", dpi=150)

    
data_scores = DataFrame(all_scores, columns=["clusters", "score"])
mean_clusters_score = {}
# Вычисление средних значений silhouette_score для каждого кол-ва кластеров
for i in range(2, clusters_cnt):
    mean_clusters_score[i] = data_scores.loc[data_scores["clusters"]==i, "score"].mean().round(3)
print(mean_clusters_score)


# {2: np.float64(0.491), 3: np.float64(0.59), 4: np.float64(0.53), 5: np.float64(0.459), 6: np.float64(0.45), 7: np.float64(0.428)}