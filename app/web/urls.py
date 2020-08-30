from django.urls import path


#imports viewsets class for urls
from web.api.viewsets.uploadMovies import UploadMovies

urlpatterns = [
    path('upload/movies/', UploadMovies.as_view(), name='upload movies'),
]
