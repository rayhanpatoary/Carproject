from CarProject.Views import sample
from django.urls import path, include
from rest_framework import routers
from . import views
from .views import DeveloperViewSet

router = routers.DefaultRouter()

router.register('developer', DeveloperViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('developer/', views.DeveloperViewSet),
    path('sample/', views.sample)
]
