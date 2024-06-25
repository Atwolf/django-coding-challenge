# Script used to add random reviews to the database, ran from Django shell

from faker import Faker
import random
from movies.models import Movie, Review

faker = Faker()
for movie in Movie.objects.all():
    for _ in range(5):  # Assuming you want 5 reviews per movie
        Review.objects.create(
            movie=movie,
            reviewer_name=faker.name(),
            rating=random.randint(1, 5)
        )
