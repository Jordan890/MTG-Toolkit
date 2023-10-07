from django.shortcuts import render
from .serializers import DeckSerializer
from .models import *
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.cache import cache_page
from .scryfall_card_service import *
from .deck_service import *


# Create your views here.

@cache_page(60*15)
@api_view(['GET'])
def get_all_decks(request):
    return Response(get_all_decks())

@api_view(['POST'])
def create_deck(request):
    return Response(create_new_deck(request.data))

@api_view(['PUT'])
def edit_deck(request,deckId):
    return Response(update_deck(request.data, deckId))

@api_view(['DELETE'])
def delete_deck(request,deckId):
    delete_deck_service(deckId)
    return Response(status=status.HTTP_200_OK)

@cache_page(60*15)
@api_view(['GET'])
def get_scryfall_cards(request):
    return Response(get_all_cards())

@cache_page(60*15)
@api_view(['GET'])
def get_card_by_id(request, id):
    return Response(get_card_by_id(id))
