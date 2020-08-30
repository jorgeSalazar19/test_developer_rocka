from django.contrib.postgres.fields import JSONField
from django.db import models


class RatingMovie(models.Model):
    ratings = JSONField(verbose_name="Ratings")

    def __str__(self):
        return "Ratings: {}".format(self.ratings)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'