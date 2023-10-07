from rest_framework import serializers
from .models import *

class CardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Card
        fields = ['scryfallId','cardName']


class CardToDeckSerializer(serializers.ModelSerializer):

    class Meta:
        model = CardToDeck
        fields = ['quantity']


class DeckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deck
        fields = ['deckName', 'owner']
        depth = 1