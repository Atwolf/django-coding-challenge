from rest_framework import serializers
from django.db.models import Avg

from movies.models import Movie
from .review_serializer import ReviewSerializer

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "runtime",
            "release_date",
            "runtime_formatted",
            "reviews",
            "avg_rating",
        )
    runtime_formatted = serializers.SerializerMethodField()

    def get_runtime_formatted(self, obj):
        hours = obj.runtime // 60
        minutes = obj.runtime % 60
        return f'{hours}:{minutes:02}'
    
    def get_avg_rating(self, obj):
        average = obj.reviews.aggregate(Avg('rating')).get('rating__avg')
        return round(average, 2) if average is not None else None