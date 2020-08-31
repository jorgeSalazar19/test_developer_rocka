"""Tests for service upload data from json to database"""

# import django
from django.test import TestCase


# imports python lybrarys
import requests
import json

# import files to project
from web.api.services import UploadMoviesService
from domain.models import Movie


class UploadServideTestCase(TestCase):
    """" class test to verify if funtionality is ok for service upload data
    """

    # methos for upload data to test
    def setUp(self):
        self.service_upload = UploadMoviesService()
        self.movie = dict( 
            title="Logan: The Wolverine",
            year="2017",
            genres=[
                "Action",
                "Drama",
                "Sci-Fi"
            ],
            ratings=[
                10,
                9,
            ],
            poster="MV5BMjI1MjkzMjczMV5BMl5BanBnXkFtZTgwNDk4NjYyMTI@._V1_SY500_CR0,0,338,500_AL_.jpg",
            contentRating=15,
            duration="PT137M",
            releaseDate="2017-03-01",
            averageRating=0,
            originalTitle="Logan",
            storyline="In the near future, a weary Logan cares for an ailing Professor X in a hide out on the Mexican border.",
            actors=[
                "Hugh Jackman",
                "Patrick Stewart",
                "Dafne Keen"
            ],
            imdbRating=9.5,
            posterurl=""
        )
        self.ratings = [5, 2, 3, 5, 8]
        with open('web/api/tests/movies.json') as f:
            self.data = json.load(f)
        self.data = dict(movies=self.data)
    

    # methos for delete keys of redis for cache test
    def delete_keys_redis(self):
        for key in self.service_upload.redis_client.keys():
            self.service_upload.redis_client.delete(key)



    # test case for upload genres, should retorno list
    def test_service_upload_genres_return(self):
        reponse_service = self.service_upload._upload_genres(self.movie)
        self.delete_keys_redis()
        self.assertIsNotNone(reponse_service)
    

    # test case for upload genres, should retorno list
    def test_service_upload_genres_instance(self):
        reponse_service = self.service_upload._upload_genres(self.movie)
        self.delete_keys_redis()
        self.assertIsInstance(reponse_service, list)
    

    # test for average rating
    def test_average_rating(self):
        average = self.service_upload._calculate_average_rating(self.ratings)
        self.assertIsInstance(average, int)
    

    # test for validate that not insert more register that the lñen of json
    def test_json_upload(self):
        self.service_upload.uploadMoviesToDataBase(self.data)
        count_movies = Movie.objects.all().count()
        self.delete_keys_redis()
        self.assertEqual(count_movies, 33)
        
