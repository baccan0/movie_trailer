import json
import fresh_tomatoes as ft
import p1

def render_movie_json(filestr):
  #open and load json file
  f=open(filestr)
  jsondecode=json.load(f)
  #jsondecode=json.load(file(f))
  #read each node and generate movie object
  movies=[]
  for item in jsondecode[u'movie']:
    movies.append(p1.Jsoncontainer(item))
  #use the fresh tomatoes movie trailer to make the movie page
  ft.open_movies_page(movies)
