from django.urls import path, include
from rest_framework import routers
from . import views
from .views import CarViewSet


router = routers.DefaultRouter()
router.register('list', CarViewSet) # Registering CarViewset in /list Url


urlpatterns = [
   
     path('', include(router.urls)),
     
     
     
    
    
]