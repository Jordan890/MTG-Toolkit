from django.urls import include, path

# import routers
from rest_framework import routers
 
# import everything from views
from .views import *

# define the router
router = routers.DefaultRouter()
 
# define the router path and viewset to be used
 
# specify URL Path for rest_framework
urlpatterns = [
    path('api/cards/', get_scryfall_cards, name='get_scryfall'),
    path('api/get_card_by_id/<str:id>', get_card_by_id, name='get_card_by_id'),
    path('api/decks/', get_all_decks, name='get_all_decks'),
    path('api/add-deck/',create_deck, name="create_new_deck"),
    path('api/update-deck/<str:deckId>',edit_deck, name="edit_deck"),
    path('api/delete-deck/<str:deckId>',delete_deck, name="delete_deck"),
    path('api-auth/', include('rest_framework.urls'))
]