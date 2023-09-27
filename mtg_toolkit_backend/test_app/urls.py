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
    path('api/card-detail/<str:requestedCardName>', test_card_specifc, name='view_card_details'),
    path('api-auth/', include('rest_framework.urls'))
]