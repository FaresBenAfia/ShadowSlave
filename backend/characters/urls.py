# app/characters/urls.py
from django.urls import path
from .views import CharacterList

urlpatterns = [
    path('', CharacterList.as_view(), name='character-list'),  # Adjust this to your actual view
]
