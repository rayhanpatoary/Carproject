from django.urls import path, include
from rest_framework import routers
from . import views
from .views import CarViewSet, ShowDB


router = routers.DefaultRouter()
router.register('car', CarViewSet)


urlpatterns = [
   # path('prediction/',Views.Prediction),
     path('', include(router.urls)),
     path('mpg/', views.CarViewSet),
     path('prediction/' ,views.Prediction ),
     path('showdb/',views.ShowDB)
    
    
]