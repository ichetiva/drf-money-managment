from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.serializers import UserSerializer, UserCreateSerializer


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        serializer.data["password"] = make_password(serializer.data["password"])
        serializer.save()


class GetUserAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        serializer = UserSerializer(self.request.user)
        return Response(serializer.data)
