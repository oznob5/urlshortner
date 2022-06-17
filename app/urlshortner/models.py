from tabnanny import verbose
from django.db import models

class Url(models.Model):
    link = models.CharField(max_length=330, verbose_name='Full url address')
    uuid = models.CharField(max_length=10, verbose_name='Short url address')
