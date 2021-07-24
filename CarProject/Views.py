
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')


def managedb(request):
    return render(request,'manageDB.html')


def mpgprediction(request):
    return render(request,'mpg_prediction.html')

def aboutproject(request):
    return render(request,'about_project.html')

    