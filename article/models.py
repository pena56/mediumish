import math
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import cloudinary
from cloudinary.models import CloudinaryField

from topic.models import Topic
from account.models import CustomUser

# Create your models here.
class Article(models.Model):

    ARTICLE_STATUS = (
        ('draft', 'DRAFT'),
        ('published', 'PUBLISHED'),
    )

    title = models.CharField(max_length=300)
    slug = models.SlugField()
    body = models.TextField()
    author = models.ForeignKey(CustomUser, related_name='author', on_delete=models.CASCADE)
    article_img = CloudinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=ARTICLE_STATUS, default='draft', max_length=100)
    topic = models.ForeignKey(Topic, related_name='topic', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,
        }

        return reverse('article', kwargs=kwargs)

    def get_read_time(self):
        return math.floor(len(self.body.split())/200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

@receiver(pre_delete, sender=Article)
def article_img_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.article_img.public_id)
