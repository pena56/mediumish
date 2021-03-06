from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import cloudinary
from cloudinary.models import CloudinaryField
from django.urls import reverse

# from article.models import Article

# Create your models here.
class CustomUser(AbstractUser):
    profile_pic = CloudinaryField()
    bio = models.TextField()
    facebook_profile = models.URLField(null=True, blank=True)
    twitter_profile = models.URLField(null=True, blank=True)

    def get_absolute_url(self):
        kwargs = {
            'username': self.username,
            'pk': self.id,
        }
        return reverse('profile', kwargs=kwargs)

@receiver(pre_delete, sender=CustomUser)
def profile_pic_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.profile_pic.public_id)
