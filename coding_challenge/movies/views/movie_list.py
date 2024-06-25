from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListView(APIView):
    def get(self, request, format=None):
        queryset = Movie.objects.all()
        min_runtime = request.query_params.get('min_runtime')
        max_runtime = request.query_params.get('max_runtime')

        if min_runtime is not None:
            queryset = queryset.filter(runtime__gte=min_runtime)

        if max_runtime is not None:
            queryset = queryset.filter(runtime__lte=max_runtime)

        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)
