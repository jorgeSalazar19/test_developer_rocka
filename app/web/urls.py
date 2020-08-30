from django.urls import path


#imports viewsets class for urls
from web.api.viewsets.uploadMovies import UploadMovies
from web.api.viewsets import MoviesListView

urlpatterns = [
    path('upload/movies/', UploadMovies.as_view(), name='upload movies'),
    path('order/movies/', MoviesListView.as_view(), name='movies list'),
]
