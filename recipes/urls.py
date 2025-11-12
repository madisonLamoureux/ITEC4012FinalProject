from django.urls import path
from .views import (
    ArtistListCreateView,
    ArtistDetailView,
    RecipeListCreateView,
    RecipeDetailView,
    FavouriteListCreateView,
    FavouriteDeleteView
)

urlpatterns = [
    path('artists/', ArtistListCreateView.as_view(), name='artist-list-create'),
    path('artists/<int:pk>/', ArtistDetailView.as_view(), name='artist-detail'),

    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),

    path('favourites/', FavouriteListCreateView.as_view(), name='favourite-list-create'),
    path('favourites/<int:pk>/', FavouriteDeleteView.as_view(), name='favourite-delete'),
]
