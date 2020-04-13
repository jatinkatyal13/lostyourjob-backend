from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import requires_csrf_token

from decouple import config
import time

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
  file = request.FILES['file']

  timestamp = int(time.time())
  fileName = f'{request.user.id}-{timestamp}-{file.name}'
  url = f'http{"s" if config("S3_SSL", cast = bool) else ""}://{config("S3_ENDPOINT")}/{config("S3_BUCKET")}/{fileName}'

  resp = minioClient.put_object(
    bucket_name = config('S3_BUCKET'), 
    object_name= fileName, 
    data = file.file,
    length = file.size,
    content_type = file.content_type
  )
  return Response({
    'url': url
  })
