from django.shortcuts import render
from rest_framework import generics,filters,permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Artist, Recipe, Favourite
from .serializers import ArtistSerializer, RecipeSerializer,FavouriteSerializer

# /api/artists/  (GET list, POST create)
class ArtistListCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

# /api/artists/<id>/  (GET single)
class ArtistDetailView(generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

# /api/recipes/  (GET list, POST create)
class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.select_related('artist').all().order_by('-created_at')
    serializer_class = RecipeSerializer

# /api/recipes/<id>/  (GET single)
class RecipeDetailView(generics.RetrieveAPIView):
    queryset = Recipe.objects.select_related('artist').all()
    serializer_class = RecipeSerializer

class FavouriteListCreateView(generics.ListCreateAPIView):
    serializer_class = FavouriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user).select_related('recipe', 'recipe__artist')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FavouriteDeleteView(generics.DestroyAPIView):
    serializer_class = FavouriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username', '').strip()
        password = request.data.get('password', '').strip()
        email = request.data.get('email', '').strip()

        if not username or not password:
            return Response({'message': 'Username or password is required'}, status=400)
        if User.objects.filter(username=username).exists():
            return Response({'message': 'Username already exists'}, status=400)
        user = User.objects.create_user(username=username, password=password, email=email or "")
        return Response({"id": user.id, "username": user.username}, status=201)

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        u = request.user
        return Response({"id":u.id, "username": u.username, "email": u.email})

