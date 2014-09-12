from django.conf import settings
from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import TestUser

class UserSerializer(serializers.ModelSerializer):
    """
    Serializing all the Users
    """

    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'photo')