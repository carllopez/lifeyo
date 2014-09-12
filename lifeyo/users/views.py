from django.shortcuts import render
from rest_framework import generics

from django.contrib.auth import get_user_model

from .serializers import UserSerializer

class UsersListView(generics.ListCreateAPIView):
    """
    Returns a list of all users
    """
    model = get_user_model()
    serializer_class = UserSerializer


class UserInstanceView(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns a single user
    Also allows updating and deleting
    """
    model = get_user_model()
    serializer_class = UserSerializer