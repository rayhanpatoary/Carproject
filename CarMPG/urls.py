from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()



urlpatterns = [
   # path('prediction/',Views.Prediction),

    path('', views.Prediction),
    
    
]