from django.db import models

# Create your models here.
class TodoItme(models.Model):
    content = models.TextField()
