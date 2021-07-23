
from rest_framework import serializers
from .models import Developer


# Developer Serializer
class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number')
