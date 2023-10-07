import requests

"""
This method gets all of the cards in English from the scryfall database
"""
def get_all_cards():
    url = "https://api.scryfall.com/bulk-data"
    response = requests.get(url)
    data = response.json()
    cardResponse = requests.get(data['data'][2]['download_uri'])
    cardData = cardResponse.json()
    return cardData

"""
This method gets the card details based on the scryfall id
"""
def get_card_by_id(id):
    url = "https://api.scryfall.com/cards/" + id
    response = requests.get(url)
    data = response.json()
    return data