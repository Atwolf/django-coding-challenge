from django.db import models
from movies.models import Movie  # Assuming 'Movie' is your existing model

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating out of 5 stars

    def __str__(self):
        return f'{self.reviewer_name}\'s review for {self.movie.title}'
