# Generated by Django 4.2.11 on 2024-06-25 00:44

from django.db import migrations, models
import django.db.models.deletion
import random
from faker import Faker

def add_reviews(apps, schema_editor):
    Movie = apps.get_model("movies", "Movie")
    Review = apps.get_model("movies", "Review")
    db_alias = schema_editor.connection.alias

    # Add reviews to each existing movie
    faker = Faker()
    for movie in Movie.objects.using(db_alias).all():
        reviews = [
            Review(
                movie=movie,
                reviewer_name=faker.name(),
                rating=random.randint(1, 5)
            )
            for _ in range(5)  # Assuming you want 5 reviews per movie
        ]
        Review.objects.using(db_alias).bulk_create(reviews)

class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_seed_db"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reviewer_name", models.CharField(max_length=100)),
                (
                    "rating",
                    models.IntegerField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
                    ),
                ),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="movies.movie",
                    ),
                ),
            ],
        ),
        # migrations.RunPython(add_reviews),
    ]
