from django.db import models

from account.models import CustomUser
from article.models import Article

# Create your models here.
class Response(models.Model):
    response = models.TextField()
    fan = models.ForeignKey(CustomUser, related_name='fan', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='article', on_delete=models.CASCADE)
    replied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.fan} commented on {self.article}'

