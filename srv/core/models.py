from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserProfile(models.Model):
    mojo = models.IntegerField()
    user = models.ForeignKey(User)
    username = models.CharField(max_length=40, blank=True)


def create_user_profile(sender, instance, created, **kwargs):
    """Create the UserProfile when a new User is saved"""
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.mojo = 1
        profile.username = ""
        profile.save()

post_save.connect(create_user_profile, sender=User)
