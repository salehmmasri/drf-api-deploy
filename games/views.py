from django.shortcuts import render
from rest_framework import generics

from .models import Game
from .serializer import GameSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework import permissions # In case you want to use IsAdmin permission

class GamesList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer