from rest_framework import serializers

from domain.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    """ serializer model to view data movie order
    """
    actors = serializers.StringRelatedField(many=True)
    genres = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Movie
        fields = ('title', 'averageRating', 'actors', 'genres', 'imdbRating')