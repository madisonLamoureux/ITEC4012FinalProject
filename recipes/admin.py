from django.contrib import admin
from .models import Artist,Recipe,Favourite

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id','name','theme_color')
    search_fields = ('name',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id','title','artist','difficulty','created_at')
    list_filter = ('difficulty','artist')
    search_fields = ('title','era','ingredients')


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('id','user','recipe','created_at')
    list_filter = ('user','recipe')
