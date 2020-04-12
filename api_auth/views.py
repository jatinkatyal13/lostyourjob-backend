from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import login

import json

from api_auth.utils import linkedin as linkedinUtils
from api_auth.serializers import UserSerializer

# Create your views here.
class LinkedIn(APIView):
  def post(self, request):
    body = json.loads(request.body)
    accessToken = linkedinUtils.exchangeGrantCode(body['code'])
    user = linkedinUtils.getUserFromAccessToken(accessToken)

    # login the user
    login(request, user)
    serializer = UserSerializer(user)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
  user = request.user
  serializer = UserSerializer(user)
  return Response(serializer.data)