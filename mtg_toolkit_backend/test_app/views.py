from django.shortcuts import render
from .serializers import CardSerializer, DeckSerializer
from .models import Card, Deck
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

@api_view(['GET'])
def test_list(request):
    cards = Card.objects.all()
    serializer = CardSerializer(cards, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_decks(request):
    decks = Deck.objects.all()
    for deck in decks:
        for card in deck.card_set.all():
            print(card)
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
        card.decks.add(deck)
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
    return Response(serializer.data)

@api_view(['DELETE'])
def test_delete_card(request,cardId):
    card = Card.objects.get(id=cardId)
    card.delete()
    return Response(status=status.HTTP_200_OK)