from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from CarMPG import MLPrediction
from .models import Car
from .serializers import CarSerializer
import requests


def Prediction(request): # By connectiong this view the prediction result can be generated
    prediction_result = MLPrediction.prediction_function(1, 2 , 3 , 4 , 5 , 6 , 7) # pass the User Input parameters here
    context={'prediction_result':prediction_result}
    return render(request,'CarMPG/predictionResult.html',context)


class CarViewSet(viewsets.ModelViewSet): # return the full car Database table in Backend
    queryset = Car.objects.all().order_by('car_name')
    serializer_class = CarSerializer






    
    
