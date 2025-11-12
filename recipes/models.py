from django.db import models
from django.conf import settings

class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    theme_color = models.CharField(max_length=7,blank=True, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('med', 'Medium'),
        ('hard', 'Hard'),
]
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='recipes')

    era = models.CharField(max_length=120, blank=True, null=True)

    ingredients = models.TextField()
    instructions = models.TextField()

    difficulty = models.CharField(max_length=5, choices=DIFFICULTY_CHOICES, default='easy')
    prep_minutes = models.PositiveIntegerField(blank=True, null=True)
    cook_minutes = models.PositiveIntegerField(blank=True, null=True)
    servings = models.PositiveIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.artist.name})"


class Favourite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favourites')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favourites')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f"{self.user.username} ({self.recipe.title})"