from django.db import models

# Create your models here.
class industry(models.Model):
    actor_name = models.CharField(max_length=30)
    first_movie = models.CharField(max_length=30)
    second_movie = models.CharField(max_length=30)
    release_date = models.DateField()