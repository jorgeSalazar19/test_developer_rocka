#imports librarys or package (python or django)
import os

# third librays
import json
import redis
import pickle


#imports files of project
from domain.models import Actor
from domain.models import Genre
from domain.models import RatingMovie
from domain.models import Movie

class UploadMoviesService(object):
    """ service for upload data to databases
    """
    
    def __init__(self, *args, **kwargs):
        self.redis_client = redis.StrictRedis(host=os.environ['REDIS_SERVER'], port=os.environ['REDIS_PORT'], db=0)


    def _upload_actors(self, movie):
        actor_ids = []
        for actor in movie['actors']:
            actor_cache = self.redis_client.get(actor)
            if actor_cache == None:
                actor_object = Actor(name=actor)
                actor_object.save()
                actor_ids.append(actor_object)
                actor_object = pickle.dumps(actor_object)
                self.redis_client.set(actor, actor_object, 3600000)
            else:
                actor_ids.append(pickle.loads(actor_cache))
        del movie['actors'] 
        return actor_ids


    def _upload_genres(self, movie):
        genres_ids = []
        for genre in movie['genres']:
            genre_cache = self.redis_client.get(genre)
            if genre_cache == None:
                genre_object = Genre(name=genre)
                genre_object.save()
                genres_ids.append(genre_object)
                genre_object = pickle.dumps(genre_object)
                self.redis_client.set(genre, genre_object, 3600000)
                
            else:
                genres_ids.append(pickle.loads(genre_cache))
        del movie['genres']
        return genres_ids
    
    
    def _upload_ratings(self, movie):
        movie['averageRating'] = str(self._calculate_average_rating(movie['ratings']))
        rating_json = json.dumps(dict(ratings=movie['ratings']))
        rating = RatingMovie(ratings=rating_json)
        rating.save()
        del movie['ratings']
        return rating
    

    def _exist_movie(self, movie_title):
        return True if Movie.objects.filter(title=movie_title) else False


    def _upload_movie(self, movie, rating_id, genres_ids, actor_ids):
        if not self._exist_movie(movie['title']):
            movie = Movie(**movie)
            movie.ratings = rating_id
            movie.save()
            movie.genres.add(*genres_ids)
            movie.actors.add(*actor_ids)
        


    def _upload_movies(self, data):
        for movie in data:
            actors = self._upload_actors(movie)
            genres = self._upload_genres(movie)
            rating = self._upload_ratings(movie)
            del movie['poster']  # delete this field because not use in the movie model
            self._upload_movie(movie, rating, genres, actors)
    

    def uploadMoviesToDataBase(self, data):
        self._upload_movies(data['movies'])
    

    def _calculate_average_rating(self, ratings_list):
        average = 0
        for rating in ratings_list:
            average += int(rating)
        return int(average/len(ratings_list))
        