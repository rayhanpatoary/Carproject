from django.urls import path, include
from rest_framework import routers
from . import views
from .views import DeveloperViewSet

router = routers.DefaultRouter()

router.register('list', DeveloperViewSet) # Register Developer database to /list url

urlpatterns = [
    path('', include(router.urls)),
    #path('developer/', views.DeveloperViewSet),
]
