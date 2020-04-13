from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token

from decouple import config

from minio import Minio
from minio.error import ResponseError

minioClient = Minio(
  config('S3_ENDPOINT'),
  access_key=config('S3_ACCESS_KEY'),
  secret_key=config('S3_SECRET_KEY'),
  secure=config('S3_SSL', cast = bool)
)

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload(request):
  print(request.FILES)
  return HttpResponse('something')
