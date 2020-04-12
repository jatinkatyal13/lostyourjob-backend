from decouple import config

from minio import Minio
from minio.error import ResponseError

minioClient = Minio(
  config('S3_ENDPOINT'),
  access_key=config('S3_ACCESS_KEY'),
  secret_key=config('S3_SECRET_KEY'),
  secure=config('S3_SSL', cast = bool)
)
