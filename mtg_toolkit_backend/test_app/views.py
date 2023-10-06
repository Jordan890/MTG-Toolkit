from django.shortcuts import render
from .serializers import CardSerializer, DeckSerializer
from .models import Card, Deck
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status
import requests
from django.views.decorators.cache import cache_page


# Create your views here.

@cache_page(60*15)
@api_view(['GET'])
def test_list(request):
    cards = Card.objects.all()
    serializer = CardSerializer(cards, many=True)
    return Response(serializer.data)

@cache_page(60*15)
@api_view(['GET'])
def get_all_decks(request):
    decks = Deck.objects.all()
    serializer = DeckSerializer(decks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def test_card_specifc(request, cardId):
    cards = Card.objects.get(id=cardId)
    serializer = CardSerializer(cards, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def test_post_card(request):
    serializer = CardSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def create_deck(request):
    deckSerializer = DeckSerializer(data=request.data)
    deckSerializer.is_valid(raise_exception=True)
    deck = deckSerializer.save()
    cardIds = request.data['cardsToAdd']
    for cardId in cardIds:
        card = Card.objects.get(id=cardId)
        deck.cards.add(card)
    return Response(deckSerializer.data)

@api_view(['PUT'])
def test_put_card(request,cardId):
    card = Card.objects.get(id=cardId)
    serializer = CardSerializer(card,request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def edit_deck(request,deckId):
    deck = Deck.objects.get(id=deckId)
    serializer = DeckSerializer(deck,request.data)
    serializer.is_valid(raise_exception=True)
    deck = serializer.save()
    cardIdsToAdd = request.data['cardsToAdd']
    cardIdsToDelete = request.data['cardsToDelete']
    for id in cardIdsToAdd:
        if(id not in deck.cards.all()):
            card = Card.objects.get(id=id)
            deck.cards.add(card)
    for id in cardIdsToDelete:
        card = Card.objects.get(id=id)
        deck.cards.remove(card)

    return Response(serializer.data)

@api_view(['DELETE'])
def test_delete_card(request,cardId):
    card = Card.objects.get(id=cardId)
    card.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_deck(request,deckId):
    deck = Deck.objects.get(id=deckId)
    deck.delete()
    return Response(status=status.HTTP_200_OK)

@cache_page(60*15)
@api_view(['GET'])
def get_scryfall_cards(request):
    url = "https://api.scryfall.com/bulk-data"
    response = requests.get(url)
    data = response.json()
    cardResponse = requests.get(data['data'][2]['download_uri'])
    cardData = cardResponse.json()
    return Response(cardData)

@cache_page(60*15)
@api_view(['GET'])
def get_card_by_id(request, id):
    url = "https://api.scryfall.com/cards/" + id
    response = requests.get(url)
    data = response.json()
    return Response(data)
