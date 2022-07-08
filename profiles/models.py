from distutils.command.upload import upload
from email.policy import default
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Profile(models.Model):
    user =models.OneToOneField(
        User,
        on_delete= models.CASCADE
        )

    image = ImageField(upload_to = "profiles", default = True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created,**kwargs):
    """Create a new profile() object when a django user is created"""
    if created:
        Profile.objects.create(user= instance)