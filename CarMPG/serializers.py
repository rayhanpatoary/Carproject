from rest_framework import serializers
from .models import Car

# Developer Serializer
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('car_name' , 'mpg' , 'cylinders', 'displacement','horsepower', 'weight' , 'acceleration', 'model_year', 'origin' )
     
