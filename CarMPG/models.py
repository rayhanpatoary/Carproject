from django.db import models



class Car(models.Model): # Creating Model for Car Database table
    car_name = models.CharField(max_length=50, null=False, blank=False)
    mpg = models.CharField(max_length=20, null=False, blank=False)
    cylinders = models.CharField(max_length=20, null=False, blank=False)
    displacement = models.CharField(max_length=20, null=False, blank=False)
    horsepower = models.CharField(max_length=20, null=False, blank=False)
    weight = models.CharField(max_length=20, null=False, blank=False)
    acceleration = models.CharField(max_length=20, null=False, blank=False)
    model_year = models.CharField(max_length=20, null=False, blank=False)
    origin = models.CharField(max_length=20, null=False, blank=False)
    
    def __str__(self):
        return self.car_name

