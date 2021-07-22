from django.db import models

# Create your models here
class Developer(models.Model):
    first_name = models.CharField(max_length=20, blank= False, null= False),
    last_name = models.CharField(max_length=20, blank= False, null= False),
    email = models.EmailField(max_length=20, blank= False, null= False, unique= True),
    phone_number = models.CharField(max_length=20, blank= False, null= False, unique= True),


    def __str__(self):
        return self.first_name






