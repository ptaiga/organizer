from django.db import models
from django.conf import settings

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    num_rand_tasks = models.IntegerField(default=1)
