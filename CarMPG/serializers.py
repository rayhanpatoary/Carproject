from rest_framework import serializers
from .models import Car


#Serializer is responsible for converting objects into data types understandable by javascript and front-end frameworks.

class CarSerializer(serializers.ModelSerializer):# Car Serializer
    class Meta:
        model = Car
        fields = ('car_name' , 'mpg' , 'cylinders', 'displacement','horsepower', 'weight' , 'acceleration', 'model_year', 'origin' )
     
