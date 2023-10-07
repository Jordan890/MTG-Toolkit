from django.contrib import admin
from .models import *
# Register your models here.

class CardAdmin(admin.ModelAdmin):
    model = Card
    readonly_fields = ('id',)
    fieldsets = [
        (None,               {'fields': ['cardName']}),
        (None,               {'fields': ['scryfallId']}),
    ]
    list_display = ('id','scryfallId','cardName')

class DeckAdmin(admin.ModelAdmin):
    model = Deck
    readonly_fields = ('id',)
    fieldsets = [
        (None,                {'fields': ['deckName']}),
        (None,                {'fields': ['owner']})
    ]
    list_display = ('id','deckName', 'owner')

class CartToDeckAdmin(admin.ModelAdmin):
    model = CardToDeck
    readonly_fields = ('id',)
    fieldsets = [
        (None,                {'fields': ['quantity']}),
    ]
    list_display = ('id', 'quantity')

admin.site.register(Card, CardAdmin)
admin.site.register(Deck, DeckAdmin)
admin.site.register(CardToDeck,CartToDeckAdmin)