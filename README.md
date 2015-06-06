# movie_trailer
udacity nanodegree project 1

data.json is the file to keep all the movie information which is writen in json format

p1.py is the class definition of Jsoncontainer which is to keep the movie infomation in python

test.py read the json file and then read the data into the Jsoncontainer objects and render the infomation into the fresh tomatoes framwork
   this one is tested under python3.4.2 and no error happen. if you use other version and it has error, please try to comment "f=open(filestr)" and
  "jsondecode=json.load(f)", then uncomment "jsondecode=json.load(file(f))". if it still doesn't work, please email me.

fresh_tomatoes.py is the frame work from the course of "Programming Foundations with Python" and I made a few modification.
   - movie shows year, rating and abstract
   - the abstract only show in one line. if it is more than one line, the abstract can pop over when the mouse is on the abstract

fresh_tomatoes.html is an example
 
how to use:
1 put all the file in the same folder,
2 open test.py with python
3 run render_movie_json("data.json") //if the data.json is not in the same folder, then you need to write the path of it

