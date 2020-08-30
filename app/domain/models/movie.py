# imports django
from django.db import models


# imports for files project
from domain.models import Actor
from domain.models import Genre
from domain.models import RatingMovie


class Movie(models.Model):
    """ model for the movie object
    """

    title = models.CharField(verbose_name="Title", max_length=50)
    year = models.CharField(verbose_name="Year", max_length=4)
    genres = models.ManyToManyField(Genre)
    ratings = models.ForeignKey(RatingMovie, on_delete=models.CASCADE)
    contentRating = models.CharField(verbose_name="Content Rating", max_length=10)
    duration = models.CharField(verbose_name="Duration", max_length=10)
    releaseDate = models.DateField(verbose_name="Relase Date")
    averageRating = models.CharField(verbose_name="Average Rating", max_length=10)
    originalTitle = models.CharField(verbose_name="Original title", max_length=50)
    storyline = models.CharField(verbose_name="Story line", max_length=1000)
    actors = models.ManyToManyField(Actor)
    imdbRating = models.CharField(verbose_name="imdb Rating", max_length=10)
    posterurl = models.CharField(verbose_name="Poster Url", max_length=300)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
