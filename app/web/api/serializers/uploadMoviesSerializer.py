from rest_framework import serializers


class UploadMoviesSerializer(serializers.Serializer):
    movies = serializers.JSONField()

