from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

"""<----------for manually token generation----start-->"""


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


"""<----------for manually token generation----end-->"""

"""<----------API View Decorator , Model Serializer-----APIVIew Serializer-------start---->"""
class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        exclude=['image']

    def validate(self, data):
        if data['price'] < 5:
            raise serializers.ValidationError({'errors': "price can not be less than 5"})

        return data

"""<----------API View Decorator , Model Serializer-----APIVIew Serializer-----end------>"""
