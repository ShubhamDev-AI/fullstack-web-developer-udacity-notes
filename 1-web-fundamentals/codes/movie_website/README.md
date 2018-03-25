# Nanodegree: Movie trailer Website

## Installation

#### **Requires**:
* Python 3.5

## Deploy

Run this command: ```python entertainment_center.py```

## Modification guide:

#### **Create new movie**
```
new_movie = Movie(
    "Movie name",
    "Movie storyline",
    "Movie poster image url",
    "Movie trailer youtube url"
)
```

#### **Store movies in a list to render to web page**
```
movies = [..., new_movie]
```

#### **Render to web page**
```
from movie_website.fresh_tomatoes import open_movies_page
open_movies_page(movies)
```

## TODO
- [ ] Alter html/css/js to improve the look of the page
- [ ] Use API to supply movie data