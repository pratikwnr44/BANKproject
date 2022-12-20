from django.db import models

# Create your models here.
class Students(models.Model):
    rn = models.IntegerField()
    name = models.CharField(max_length=60)
    age = models.IntegerField()

