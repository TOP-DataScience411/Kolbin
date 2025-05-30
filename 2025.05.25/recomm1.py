from pandas import read_csv, DataFrame

from pathlib import Path
from re import compile
from sys import path


script_dir = Path(path[0])


movies = read_csv(script_dir / 'movies.csv', index_col='movie_id')
ratings = read_csv(script_dir / 'ratings.csv')


title_pat = compile(
    r'(?P<title>.+?) ?'
    r'(\((?P<loc_title>[^()]+)\) )?'
    r'(\((?P<year>\d{4})\))?'
)

genres = DataFrame(columns=['movie_id', 'genre'])

for i in movies.index:
    # обработка заголовка
    title = movies.loc[i, 'title'].rstrip()
    mo = title_pat.fullmatch(title)
    movies.loc[i, 'title'] = mo['title']
    movies.loc[i, 'loc_title'] = mo['loc_title'].strip(' ()') if type(mo['loc_title']) is str else None
    movies.loc[i, 'year'] = int(mo['year']) if type(mo['year']) is str else None
    # обработка жанров
    for g, genre in enumerate(movies.loc[i, 'genres'].rstrip().split('|'), 1):
        genres.loc[f'{i},{g}'] = i, genre

genres.drop(genres[genres["genre"] == "IMAX"].index, inplace=True)
genres.drop(genres[genres["genre"] == "(no genres listed)"].index, inplace=True)
genres.reset_index(drop=True, inplace=True)

movies.drop(columns='genres', inplace=True)
movies = movies.convert_dtypes()

ratings.drop(columns='timestamp', inplace=True)


movies.to_csv(script_dir / 'movies_ref.csv')
genres.to_csv(script_dir / 'genres_ref.csv')
ratings.to_csv(script_dir / 'ratings_ref.csv')

print(
    '',
    movies,
    genres,
    ratings,
    sep='\n\n'
)

