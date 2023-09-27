from django.shortcuts import render
from .serializers import CardSerializer
from .models import Card
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
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def test_card_specifc(request, requestedCardName):
    cards = Card.objects.get(cardName=requestedCardName)
    serializer = CardSerializer(cards, many=False)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def test_post_card(request):
    print(request.method)
    serializer = CardSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def test_put_card(request,requestedCardName):
    card = Card.objects.get(cardName=requestedCardName)
    serializer = CardSerializer(card,request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def test_delete_card(request,requestedCardName):
    card = Card.objects.get(cardName=requestedCardName)
    card.delete()
    return Response(status=status.HTTP_200_OK)