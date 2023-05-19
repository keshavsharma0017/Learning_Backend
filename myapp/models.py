from django.db import models

# Create your models here.
class Cards(models.Model):
    name= models.CharField(max_length=50)
    logo= models.CharField(max_length=500)
    infoo= models.CharField(max_length=500, null = True)

