from .models import *
from .serializers import *

"""
This method gets all of the decks that are stored in the database
"""
def get_all_decks():
    decks = Deck.objects.all()
    serializer = DeckSerializer(decks, many=True)
    return serializer.data

"""
This method allows the user to create a new deck in the database
"""
def create_new_deck(deckToSave):
    deckSerializer = DeckSerializer(data=deckToSave)
    deckSerializer.is_valid(raise_exception=True)
    deck = deckSerializer.save()
    cardsToSave = deckToSave['cardsToAdd']
    cardsInDatabase = Card.objects.all()
    cardsToDecks = CardToDeck.objects.all()
    for currCard in cardsToSave:
        cardId = add_card_to_database(currCard, cardsInDatabase)
        card = Card.objects.get(id=cardId)
        add_card_to_deck(card,deck,cardsToDecks, currCard['qty'])
    return deckSerializer.data


"""
This method allows the user to update the deck and that includes changing the cards in it
It will auto delete any cards that have 0 quantity from the deck
"""
def update_deck(deckToSave,deckId):
    currentDeck = Deck.objects.get(id=deckId)
    serializer = DeckSerializer(currentDeck,deckToSave)
    serializer.is_valid(raise_exception=True)
    deck = serializer.save()
    cardsToSave = deckToSave['cardsToAdd']
    cardsInDatabase = Card.objects.all()
    cardsToDecks = CardToDeck.objects.all()
    for currCard in cardsToSave:
        cardId = add_card_to_database(currCard, cardsInDatabase)
        card = Card.objects.get(id=cardId)
        add_card_to_deck(card,deck,cardsToDecks, currCard['qty'])
    
    cardsInDeck = cardsToDecks.filter(deck__id=deck.id)
    print(cardsInDeck)
    for cardToDelete in cardsInDeck:
        if cardToDelete.quantity <= 0:
            cardToDelete.delete()

    return serializer.data

"""
This method will delete the deck from the database
"""
def delete_deck_service(deckId):
    deck = Deck.objects.get(id=deckId)
    deck.delete()
    return

"""
This method handles adding a card to the database that we use as a foreign key for decks
"""
def add_card_to_database(card, cards):
    filteredCards = cards.filter(id=card['id'])
    if(len(filteredCards) == 0):
        cardSerializer = CardSerializer(data=card)
        cardSerializer.is_valid(raise_exception=True)
        card = cardSerializer.save()
        return card.id
    return filteredCards[0].id

"""
This method handles connecting the cards to the decks through an in between model called
CardToDeck
"""
def add_card_to_deck(card, deck, cardsToDecks, qty):
    filterdCardsToDecks = cardsToDecks.filter(deck__id=deck.id).filter(card__id=card.id)
    if(len(filterdCardsToDecks) == 0):
        cardToDeck = CardToDeck(quantity=qty, card=card, deck=deck)
        cardToDeck.save()
        return cardToDeck
    else:
        cardToDeck = filterdCardsToDecks[0]
        cardToDeckSerializer =  CardToDeckSerializer(cardToDeck, {"quantity":qty,"deck":deck, "card":card})
        cardToDeckSerializer.is_valid(raise_exception=True)
        cardToDeck = cardToDeckSerializer.save()
        return cardToDeck
