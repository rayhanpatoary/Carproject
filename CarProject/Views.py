
from django.http import HttpResponse
from django.shortcuts import render
import requests


def home(request):
    return render(request,'home.html')


def managedb(request):
    r = requests.get('http://127.0.0.1:8000/api/car/list')
    context={'db_all':r.json()}
    return render(request,'manageDB.html',context)
       

def mpgprediction(request):
    return render(request,'mpg_prediction.html')



def aboutproject(request):
    return render(request,'about_project.html')

    