from django.urls import path, include
from rest_framework import routers
from . import views
from .views import CarViewSet


router = routers.DefaultRouter()
router.register('', CarViewSet)

urlpatterns = [
   # path('prediction/',Views.Prediction),
     path('', include(router.urls)),
     path('mpg/', views.CarViewSet),
     path('prediction/' ,views.Prediction )
    
    
]