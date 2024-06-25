from rest_framework import serializers

from movies.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='reviewer_name')
    rating = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ('name', 'rating')