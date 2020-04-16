from rest_framework import serializers

from referrals.models import Seeker
from api_auth.serializers import UserSerializer

class SeekerSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only = True)
  class Meta:
    model = Seeker
    fields = [
      'id',
      'summary',
      'offer_letter',
      'resume',
      'user'
    ]
  
