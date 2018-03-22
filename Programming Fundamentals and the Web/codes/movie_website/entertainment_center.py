from movie_website.media import Movie
from movie_website.fresh_tomatoes import open_movies_page

# Create Movie's instances
toy_story = Movie(
    "Toy story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=4KPTXpQehio"
)

avatar = Movie(
    "Avatar",
    "A marine on a aline planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
)

la_la_land = Movie(
    "La La Land",
    "A love story of Mia and Seb",
    "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
    "https://www.youtube.com/watch?v=0pdqf4P9MB8"
)

game_of_throne = Movie(
    "Game Of Thrones",
    "A series TV made by HBO",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
)

stranger_thing = Movie(
    "Stranger Thing",
    "A story of a stranger thing in an small village",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
)

black_mirror = Movie(
    "Black Mirror",
    "A black side of internet or technology",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
)

# Store movies in a list to render to a web page
movies = [toy_story, la_la_land, avatar, game_of_throne, stranger_thing,
          black_mirror]

# Render movies to web page
open_movies_page(movies)
