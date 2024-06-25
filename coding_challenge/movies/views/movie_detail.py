from rest_framework import status, serializers
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from movies.models import Movie
from movies.serializers import MovieSerializer

class DynamicFieldsMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)
        if fields:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class MovieDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer

    def get_serializer(self, *args, **kwargs):
        fields = self.request.query_params.get('fields', None)
        if fields:
            fields = fields.split(',')
            kwargs['context'] = self.get_serializer_context()
            kwargs['fields'] = fields
            return DynamicFieldsMovieSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)

    def get(self, request, id):
        movie = get_object_or_404(Movie, id=id)
        serializer = self.get_serializer(movie)
        return Response(serializer.data)

    def put(self, request, id):
        movie = get_object_or_404(Movie, id=id)
        serializer = self.get_serializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        movie = get_object_or_404(Movie, id=id)
        serializer = self.get_serializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        movie = get_object_or_404(Movie, id=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
