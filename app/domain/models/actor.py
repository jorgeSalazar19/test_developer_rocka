from django.db import models


class Actor(models.Model):
    """ model for the actor object
    """
    name = models.CharField(verbose_name="Actor Name", max_length=60)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'