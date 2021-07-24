# """CarProject URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from django.urls.conf import include
# from.import Views
# from django.urls import include, path
# from rest_framework import routers
# from Devportfolio import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)


# urlpatterns = [
    
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('admin/', admin.site.urls),
#     path('home/', Views.home ),
#     path('about/', Views.about),
#     path('contact/', Views.contact),
#     path('prediction/', Views.Prediction),
#     path('sample/', Views.sample),
    

#     path('devPortfolio/', include('Devportfolio.urls'))

# ]


from django import urls

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from CarProject import Views


urlpatterns = [
   # path('prediction/',Views.Prediction),
    path('',Views.home),
    path('admin/', admin.site.urls),
    # home
    path('api/', include('dev_portfolio.urls')),

    path('car/', include('CarMPG.urls')),
    
]



