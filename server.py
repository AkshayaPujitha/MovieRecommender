import util
import pandas as pd
#import requests
from flask import Flask,render_template,request
app=Flask(__name__)

__model=None
__title=None
__id=None

@app.route("/")
def home():
   return render_template("home.html")


#For Recommendation Page   
@app.route("/recommendation.html",methods=['GET','POST'])
def recommendation():
   global __model
   global __title
   global __id
   __model,__title,__id=util.load()
   title=__title.copy()
   title.sort()
   genere_list=[]
   poster=[]
   genere_movies=[]
   ind=0
   genre="Action" #By default
   try:
      genre=request.form['genres']
      #print(genre)
   except:
      genre="Action"
   while len(genere_list)!=6:
      generes_id=util.get_genre(__id[ind])
      if genre in generes_id:
         #print(generes_id)
         genere_list.append(__id[ind])
         genere_movies.append(__title[ind])
      ind+=1
   for id in genere_list:
      poster.append(util.fetch_poster(id))
   
   ind=0
   year_list=[]
   year_posters=[]
   year_movies=[]
   try:
      year=request.form['years']
      #print(genre)
   except:
      year="2012"
   while len(year_movies)!=6:
      year_id=util.get_release_year(__id[ind])
      #print(year_id)
      if year==year_id:
         year_list.append(__id[ind])
         year_movies.append(__title[ind])
      ind+=1
   for id in year_list:
      year_posters.append(util.fetch_poster(id))
   return render_template("recommendation.html",movie_names=title,poster=poster,genere_movies=genere_movies,genre=genre,year_posters=year_posters,year_movies=year_movies,year=year)


#For movie-recommendation
@app.route('/movie/<movie_name>')
def movie_recommendation(movie_name):
   global __model
   global __title
   global __id
   __model,__title,__id=util.load()
   movie=movie_name
   print(movie)
   recommended_movie_names,recommended_movie_posters=util.recommend_movie(movie,__title,__model,__id)
   title=__title.copy()
   title.sort()

   return render_template("movie_recommendation.html",recommended_movie_names=recommended_movie_names,recommended_movie_posters=recommended_movie_posters,movie_names=title)


      

if __name__=="__main__":
   app.run(debug=True)

    
            