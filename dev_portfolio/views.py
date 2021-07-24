from rest_framework import viewsets
from .models import Developer
from .serializers import DeveloperSerializer
from django.shortcuts import render

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all().order_by('first_name')
    serializer_class = DeveloperSerializer

def sample(request):
    return render(request,'dev_portfolio/profile.html')
