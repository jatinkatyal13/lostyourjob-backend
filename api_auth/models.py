from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = (
  ('referrer', 'referrer'),
  ('seeker', 'seeker')
)

class User(AbstractUser):
  photo = models.CharField(max_length = 1024, blank = True)
  role = models.CharField(max_length = 32, choices = ROLES)
