from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    topic_img = CloudinaryField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,
        }

        return reverse('topic', kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

@receiver(pre_delete, sender=Topic)
def topic_img_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.topic_img.public_id)
