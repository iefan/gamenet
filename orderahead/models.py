from django.db import models

# Create your models here.
class orderlist(models.Model):
    name        = models.CharField(max_length=30)
    sex         = models.CharField(max_length=2)
    age         = models.IntegerField()
    address     = models.CharField(max_length=100, null=True)
    phone       = models.IntegerField()
    starttime   = models.DateTimeField()
    endtime     = models.DateTimeField()
    desc        = models.TextField(null=True)
