# imports django
from django.contrib import admin


#imports files to project
from domain.models import Actor
from domain.models import Genre
from domain.models import Movie
from domain.models import RatingMovie




@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):

    list_display = ('pk', 'name', )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):

    list_display = ('pk', 'name', )


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = ('pk', 'title')




