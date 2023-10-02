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
    path('api/cards/', test_list),
    path('api/decks/', get_all_decks, name='get_all_decks'),
    path('api/card-detail/<str:cardId>', test_card_specifc, name='view_card_details'),
    path('api/add-card/',test_post_card, name="add_card_details"),
    path('api/add-deck/',create_deck, name="create_new_deck"),
    path('api/update-card/<str:cardId>',test_put_card, name="edit_card_details"),
    path('api/update-deck/<str:deckId>',edit_deck, name="edit_deck"),
    path('api/delete-card/<str:cardId>',test_delete_card, name="delete_card_details"),
    path('api/delete-deck/<str:deckId>',delete_deck, name="delete_deck"),
    path('api-auth/', include('rest_framework.urls'))
]