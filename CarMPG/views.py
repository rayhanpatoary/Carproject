from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from CarMPG import MLPrediction
from .models import Car
from .serializers import CarSerializer

# Create your views here.
def Prediction(request):
    predict_result = MLPrediction.prediction_function(1, 2 , 3 , 4 , 5 , 6 , 7) # pass the User Input parameters here
    return HttpResponse(predict_result)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('car_name')
    serializer_class = CarSerializer
