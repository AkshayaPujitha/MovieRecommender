import json
import pickle
import requests
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    

    #plot=data['plot']
    #actor=data['actors']
    #release=data['release']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    #print(full_path)
    return full_path

def get_genre(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    genres = [genre['name'] for genre in data['genres']]
    return genres

def get_release_year(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    release_date=data["release_date"]
    release_year = release_date.split("-")[0]
    return release_year




def recommend_movie(movie,__title,__model,__id):
    recommended_movie_names = []
    recommended_movie_posters = []
    movie_index=0
    try:
        movie_index=__title.index(movie)
        print(movie_index)
    except:
        print("Sorry!!!Cant recommend")
        return
    similar_list=__model[movie_index]
    movie_list=sorted(list(enumerate(similar_list)),reverse=True,key=lambda x:x[1])[1:7]
    for i in movie_list:
        movie_id = __id[i[0]]
        #print(movie_id)
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(__title[i[0]])
        

    return recommended_movie_names,recommended_movie_posters


def load(__model=None,__title=None,__id=None):
    with open("movies.pickle",'rb') as f:
       __model=pickle.load(f)
    with open("movies_list.json",'r') as f:
        __title=json.load(f)['title']
    with open("movies_list.json",'r') as f:
        __id=json.load(f)['id']
    #print(__id)
    return __model,__title,__id

if __name__=="__main__":
    __model,__title,__id=load()
    print(get_genre(__id[0]))
    #recommend_movie("Independence Day")