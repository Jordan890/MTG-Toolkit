from django.contrib import admin
from .models import Card, Deck
# Register your models here.

class CardInline(admin.TabularInline):
    model = Card.decks.through

class CardAdmin(admin.ModelAdmin):
    model = Card
    fieldsets = [
        (None,               {'fields': ['cardName']}),
        (None,               {'fields': ['text']}),
        (None,               {'fields': ['type']}),
        (None,               {'fields': ['colors']})
    ]
    list_display = ('cardName', 'text', 'type', 'colors')

class DeckAdmin(admin.ModelAdmin):
    model = Deck
    fieldsets = [
        (None,                {'fields': ['deckName']}),
        (None,                {'fields': ['owner']})
    ]
    list_display = ('deckName', 'owner')
    inlines = [CardInline,]

admin.site.register(Card, CardAdmin)
admin.site.register(Deck, DeckAdmin)