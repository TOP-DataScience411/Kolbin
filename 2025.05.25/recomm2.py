from pandas import read_csv
from scipy.sparse import csc_matrix, csr_matrix
from sklearn.neighbors import NearestNeighbors

from pathlib import Path
from sys import path


script_dir = Path(path[0])
movies = read_csv(script_dir / 'movies_ref.csv', index_col='movie_id')
genres = read_csv(script_dir / 'genres_ref.csv')
ratings = read_csv(script_dir / 'ratings_ref.csv')
genres.drop("Unnamed: 0", axis=1, inplace=True)

# Формирование матрицы предпочтений
movies_ratings = ratings.pivot_table(values='rating', index='user_id', columns='movie_id')

# Подсчет количества значений (не NaN) в столбцах и строках
user_votes = ratings.groupby('user_id')['rating'].agg('count')
movies_votes = ratings.groupby('movie_id')['rating'].agg('count')

# Создание масок для удаления
user_mask = user_votes.loc[user_votes > 50].index
movies_mask = movies_votes.loc[movies_votes > 10].index

# Удаление строк и столбцов, в которых содержится мало значений
movies_ratings = movies_ratings.loc[user_mask, movies_mask]
# Замена всех NaN на 0
movies_ratings = movies_ratings.fillna(0)

# Сжатие матрицы в csc (csr) формат
movies_ratings_csc = csc_matrix(movies_ratings.values)


model = NearestNeighbors(
    n_neighbors=20,
    metric='cosine',
    algorithm='brute',
    n_jobs=-1,
)
model.fit(movies_ratings_csc.transpose())


recommendations = 7
movie_title = 'How to Train Your Dragon'

search_mask = movies['title'].str.contains(movie_title)
search_results = movies[search_mask]
# print(search_results.loc)

try:
    movie_id = search_results.iloc[0].name

except IndexError:
    print(f'отсутствует фильм с названием {movie_title!r}')

else:
    # Из-за изменения индексации при сжатии матрицы, находим позиционный индекс, соответствующий movie_id
    movie_id_pos = movies_ratings.columns.get_loc(movie_id)
    movie_vector = movies_ratings_csc[:, movie_id_pos]
    
    # kneighbors возвращает кортежи: расстояния до ближайших точек, позиционные индексы фильмов
    closest_movies_dist, closest_movies_ind = model.kneighbors(movie_vector.transpose())
    
    distances_indexes = sorted(zip(
        closest_movies_dist.flatten(),
        closest_movies_ind.flatten(),
    ))[1:]
    
    recommendations_ind = []
    for _, movie_id_pos in distances_indexes:
        movie_id = movies_ratings.columns[movie_id_pos]
        recommendations_ind.append(movie_id)
    
    print("\n\tВыбранный фильм:\n", search_results.iloc[[0]], end="\n\n\n")
    print("\tДо фильтрации по жанрам:\n", movies.loc[recommendations_ind], end="\n\n\n")
    
    # Список жанров выбранного фильма
    movie_genres = list(genres.loc[genres["movie_id"] == search_results.iloc[0].name]["genre"])
    # Словарь с жанрами каждого рекомендованного фильма
    genres_rec_movies = {}
    for rec in recommendations_ind:
        genres_rec_movies[rec] = list(genres.loc[genres["movie_id"] == rec]["genre"])
    
    
    out_rec = []
    # Должна совпадать хотя бы половина жанров
    min_matching_genres = round(len(movie_genres) / 2)
    
    for movie, genres in genres_rec_movies.items():
            cnt_match = 0
            for g in genres:
                if g in movie_genres: cnt_match += 1
                if cnt_match == min_matching_genres: 
                    out_rec.append(movie)
                    break
                
    print("\tПосле фильтрации по жанрам:\n", movies.loc[out_rec], end="\n\n\n")
    

