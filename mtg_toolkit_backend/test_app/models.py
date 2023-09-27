from django.db import models

# Create your models here.

class Deck(models.Model):
    deckName = models.CharField(default="New Deck", max_length=50)
    owner = models.CharField(default="", max_length=200)
    def __str__(self):
        return self.deckName


class Card(models.Model):
    cardName = models.CharField(default='', max_length=200)
    text = models.TextField(default='')
    type = models.CharField(default='', max_length=50)
    colors = models.CharField(default='',max_length=10)
    decks = models.ManyToManyField(Deck)
    def __str__(self):
        return self.cardName