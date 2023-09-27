from django.shortcuts import render
from .serializers import CardSerializer
from .models import Card
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser


# Create your views here.

@api_view(['GET'])
def test_list(request):
    cards = Card.objects.all()
    serializer = CardSerializer(cards, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def test_card_specifc(request, requestedCardName):
    cards = Card.objects.get(cardName=requestedCardName)
    serializer = CardSerializer(cards, many=False)
    return JsonResponse(serializer.data, safe=False)