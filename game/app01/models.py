from django.db import models

# Create your models here.
class Player(models.Model):
    player = models.CharField(max_length=64,unique=True)
    makr = models.IntegerField(null=False)