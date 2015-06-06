import json
import fresh_tomatoes as ft
import p1


def render_movie_json(filestr):
    # Open and load json file.
    f = open(filestr)
    jsondecode = json.load(f)
    # Read each node and generate movie object.
    movies = []
    for item in jsondecode[u'movie']:
        movies.append(p1.Jsoncontainer(item))
    # Use the fresh tomatoes movie trailer to make the movie page.
    ft.open_movies_page(movies)
