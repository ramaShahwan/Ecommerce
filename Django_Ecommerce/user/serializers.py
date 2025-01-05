from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ('user', 'first_name', 'father_name', 'last_name', 'birth_date')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        customer = Customer.objects.create(user=user, **validated_data)
        return customer
    
    


class EditUserAfterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'email', 'gender', 'username','profile_image')
   
class CustomerProfileSerializer(serializers.ModelSerializer):
    user = EditUserAfterSerializer()

    class Meta:
        model = Customer
        fields = ('user', 'first_name', 'father_name', 'last_name', 'birth_date')

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user = instance.user
            user_serializer = EditUserAfterSerializer(instance=user, data=user_data)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()
        return super().update(instance, validated_data)
    
    




class PasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)     