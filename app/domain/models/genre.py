from django.db import models


class Genre(models.Model):
    name = models.CharField(verbose_name="Genre name", max_length=30)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'