from django.db import models

class LitWork(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500)
    docLocation = models.CharField(max_length=500, blank=True)
    audioLocation = models.CharField(max_length=500, blank=True)
    picLocation = models.CharField(max_length=500, blank=True)
    vedioLocation = models.CharField(max_length=500, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
# Create your models here.
