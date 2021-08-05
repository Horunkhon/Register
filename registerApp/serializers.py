from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    
    password1 = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])

    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password2': "password field dont match !"})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password1'])

        user.save()

        return user