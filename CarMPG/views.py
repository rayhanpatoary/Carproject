from django.shortcuts import render
from django.http import HttpResponse
from CarMPG import MLPrediction


# Create your views here.
def Prediction(request):
    predict_result = MLPrediction.prediction_function(1, 2 , 3 , 4 , 5 , 6 , 7) # pass the User Input parameters here
    return HttpResponse(predict_result)