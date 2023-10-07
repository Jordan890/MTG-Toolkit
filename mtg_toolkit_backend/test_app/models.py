from django.db import models

# Create your models here.


class Card(models.Model):
    cardName = models.CharField(default='', max_length=200)
    scryfallId = models.CharField(default='', max_length=200)
    def __str__(self):
        return self.cardName
    

class Deck(models.Model):
    deckName = models.CharField(default="New Deck", max_length=50)
    owner = models.CharField(default="", max_length=200)
    def __str__(self):
        return self.deckName
    
class CardToDeck(models.Model):
    quantity = models.IntegerField(default=0)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, default=None)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.deck.deckName + " : " + self.card.cardName + " : " + str(self.quantity)