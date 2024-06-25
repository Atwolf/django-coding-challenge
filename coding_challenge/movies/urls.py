from django.urls import path

from movies.views import MovieListView
from .views import MovieDetailView

urlpatterns = [
    path("", MovieListView.as_view(), name="MovieListView"),
    path('<int:id>', MovieDetailView.as_view(), name='MovieDetailView'),
]
