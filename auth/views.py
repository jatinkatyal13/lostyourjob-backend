from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

import json

from auth.utils import linkedin as linkedinUtils

# Create your views here.
class LinkedIn(View):
  def post(self, request):
    body = json.loads(request.body)
    accessToken = linkedinUtils.exchangeGrantCode(body['code'])
    user = linkedinUtils.getUserFromAccessToken(accessToken)
    user = json.loads(user.content)

    return JsonResponse(user)
