from rest_framework import serializers
from .models import Artist, Recipe,Favourite

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'description', 'image_url', 'theme_color']


class RecipeSerializer(serializers.ModelSerializer):
    # Show full artist info when reading
    artist = ArtistSerializer(read_only=True)

    # Allow setting artist by ID when creating
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist',
        write_only=True
    )

    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'artist',
            'artist_id',
            'era',
            'ingredients',
            'instructions',
            'difficulty',
            'prep_minutes',
            'cook_minutes',
            'servings',
            'created_at',
        ]

class FavouriteSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True)
    recipe_id = serializers.PrimaryKeyRelatedField(
        queryset=Recipe.objects.all(),
        source='recipe',
        write_only=True
    )

    class Meta:
        model = Favourite
        fields = ['id','user','recipe','recipe_id','created_at']