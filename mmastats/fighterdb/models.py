from django.db import models

# Create your models here.

class Fighter(models.Model):
    id = models.IntegerField(primary_key=True)
    given_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    nick_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    weight = models.DecimalField()
    height = models.DecimalField()
    locality = models.CharField(max_length=300)
    country = models.CharField(max_length=100)
    weight_class = models.CharField(max_length=80)
    thumbnail = models.FileField()