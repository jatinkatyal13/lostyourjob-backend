from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from api_auth.models import User

class Seeker(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'profile')
  summary = models.TextField(blank = True)
  offer_letter = models.URLField(blank = True)
  resume = models.URLField(blank = True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Seeker.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.profile.save()
