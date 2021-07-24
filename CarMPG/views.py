from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from CarMPG import MLPrediction
from .models import Car
from .serializers import CarSerializer
import requests
# Create your views here.


# def Prediction(request):
#     prediction_result = MLPrediction.prediction_function(1, 2 , 3 , 4 , 5 , 6 , 7) # pass the User Input parameters here
#     context={'prediction_result':prediction_result}
#     return render(request,'CarMPG/predictionResult.html',context)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('car_name')
    serializer_class = CarSerializer

# def ShowDB(request):
#     r = requests.get('http://127.0.0.1:8000/car/car')
#     context={'db_all':r.json()}
#     return render(request,'CarMPG/ShowDB.html',context)




    
    
