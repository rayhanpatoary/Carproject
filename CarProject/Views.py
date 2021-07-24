
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'HomePage/home.html')

def about(request):
    message = "This is our about page message"
    return HttpResponse(message)

def contact(request):
    message = "This is our Contact page message"
    return HttpResponse(message)


def sample(request):
    
    return HttpResponse("This is sample")



    