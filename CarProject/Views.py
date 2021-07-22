
from django.http import HttpResponse
from.import MLPrediction
import joblib

def home(request):
    message = "This is home page message"
    return HttpResponse(message)

def about(request):
    message = "This is our about page message"
    return HttpResponse(message)

def contact(request):
    message = "This is our Contact page message"
    return HttpResponse(message)

def Prediction(request):
    predict_result = MLPrediction.prediction_function(1, 2 , 3 , 4 , 5 , 6 , 7) # pass the User Input parameters here
    return HttpResponse(predict_result)


def sample(request):
    
    return HttpResponse("This is sample")