
from django.http import HttpResponse

def home(request):
    message = "This is home page message"
    return HttpResponse(message)

def about(request):
    message = "This is our about page message"
    return HttpResponse(message)

def contact(request):
    message = "This is our Contact page message"
    return HttpResponse(message)

