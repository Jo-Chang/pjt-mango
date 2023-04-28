from django.db import models

from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class User(AbstractUser):
    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    

class Profile(models.Model):
    image = ProcessedImageField(upload_to='stores', blank=True,
                                    processors=[ResizeToFill(100,100)],
                                    format='jpg',
                                    options={'quality': 80})