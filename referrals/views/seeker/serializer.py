from rest_framework import serializers

from referrals.models import Seeker

class SeekerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Seeker
    fields = [
      'summary',
      'offer_letter',
      'resume'
    ]
  
