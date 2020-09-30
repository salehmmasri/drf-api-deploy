from django.urls import path

from .views import GameDetails, GamesList

urlpatterns = [
    path('', GamesList.as_view(), name='games'), # localhost:8000/api/v1/posts
    path('/<int:pk>', GameDetails.as_view(), name='game_details') # localhost:8000/api/v1/posts/1
]