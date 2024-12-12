from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import validate_email
from .models import *

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password', 'confirm_password']

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})

        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        email = validated_data.get('email')

        # Generate the username by combining first name, last name, and email (customizable)
        username = f"{first_name.lower()} {last_name.lower()}"

        # Ensure the username is unique (optional, for example)
        if User.objects.filter(username=username).exists():
            username = f"{username}_{validated_data['email'].split('@')[0]}"

        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=validated_data['password']
        )
        return user
    def update(self, instance, validated_data):
        validated_data.pop('confirm_password', None)
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)
        instance.save()
        return instance



