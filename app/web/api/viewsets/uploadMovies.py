from rest_framework.response import Response
from rest_framework import status
from rest_framework import views


from web.api.serializers import UploadMoviesSerializer
from web.api.services import UploadMoviesService


import json


class UploadMovies(views.APIView):
    """
	This endpoint is use for upload movies from json file     
	"""

    def __init__(self, *args, **kwargs):
        self.serializer_class = UploadMoviesSerializer
        

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                self.data = serializer.data
                UploadMoviesService().uploadMoviesToDataBase(self.data)
                return Response(data='Upload json correctly', status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response = dict(detail = str(e))
            return Response(response, status = status.HTTP_500_INTERNAL_SERVER_ERROR)