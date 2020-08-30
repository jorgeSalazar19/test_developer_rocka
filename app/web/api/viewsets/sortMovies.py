from rest_framework.generics import ListAPIView


from domain.models import Movie
from web.api.serializers import MovieSerializer
from web.api.mixins import MovieMixin


class MoviesListView(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        """
        retorn lisst of movies order
        """
        ordering_method = self.request.GET.get('ordering_method')
        if ordering_method == "average":
            return Movie.objects.all().order_by('-averageRating')
        elif ordering_method == "same_movie":
            return Movie.objects.all().order_by('-genres__name', '-imdbRating', '-actors__name')
        else:
            return Movie.objects.all().order_by('-actors__name')

