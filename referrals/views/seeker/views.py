from rest_framework import generics

from . import serializer

class UpdateProfile(generics.UpdateAPIView):
  serializer_class = serializer.SeekerSerializer
