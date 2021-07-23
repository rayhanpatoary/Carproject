from rest_framework import viewsets
from .models import Developer
from .serializers import DeveloperSerializer


class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all().order_by('first_name')
    serializer_class = DeveloperSerializer
