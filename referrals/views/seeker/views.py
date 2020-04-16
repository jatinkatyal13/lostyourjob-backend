from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from referrals.models import Seeker
from api_auth.models import User
from api_auth.serializers import UserSerializer
from . import serializer

class ListSeekerView(generics.ListAPIView):
  queryset = Seeker.objects.filter(user__role = 'seeker')
  permission_classes = [IsAuthenticated]
  serializer_class = serializer.SeekerSerializer

class RetrieveProfile(APIView):
  serializer_class = serializer.SeekerSerializer
  permission_classes = [IsAuthenticated]

  def get(self, request):
    seeker = get_object_or_404(Seeker, user = self.request.user)
    serializer = self.serializer_class(seeker)

    return Response(serializer.data)

  def post(self, request):
    seeker = get_object_or_404(Seeker, user = self.request.user)
    serializer = self.serializer_class(seeker, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)
