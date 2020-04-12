from django.db import models

class Company(models.Model):
  name = models.CharField(max_length = 256)
  website = models.URLField()
