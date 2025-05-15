# app/characters/views.py
from django.http import JsonResponse
from django.views import View

# Sample CharacterList class-based view
class CharacterList(View):
    def get(self, request):
        # Sample data - replace this with actual character data from your models
        characters = [
            {"id": 1, "name": "Character 1"},
            {"id": 2, "name": "Character 2"},
            {"id": 3, "name": "Character 3"},
        ]
        return JsonResponse(characters, safe=False)