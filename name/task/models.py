from django.db import models

# Create your models here.

class NameModel(models.Model):
    data = models.JSONField()

