from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import ProfileUsersApp

User = get_user_model()

@receiver(post_save, sender=User)
def create_profile_user(sender, instance, created, **kwargs):
    if created:
        ProfileUsersApp.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile_user(sender, instance, **kwargs):
    instance.profile.save()