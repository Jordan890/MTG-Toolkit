from rest_framework import serializers
from .models import Card, Deck

class CardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Card
        fields = ['cardName', 'text', 'type','colors']


class DeckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deck
        fields = ['deckName', 'owner']