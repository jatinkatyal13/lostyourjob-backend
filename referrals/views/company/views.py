from rest_framework import generics

from referrals.models import Company
from . import serializer

class ListCompany(generics.ListAPIView):
  queryset = Company.objects.all()
  serializer_class = serializer.CompanySerializer
