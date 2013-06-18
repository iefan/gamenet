#-*- coding:utf-8 -*-

from django.db import models

# Create your models here.
class OrderlistModel(models.Model):
    name        = models.CharField(max_length=30, verbose_name="姓名")
    sex         = models.CharField(max_length=2, verbose_name="性别")
    age         = models.IntegerField(verbose_name="年龄")
    address     = models.CharField(max_length=100, null=True,blank=True, verbose_name="地址")
    phone       = models.CharField(max_length=12, verbose_name="电话")
    personnums  = models.IntegerField(verbose_name="人数")
    starttime   = models.DateTimeField(verbose_name="预订")
    descinfo    = models.TextField(null=True, blank=True, verbose_name="说明")

    def __unicode__(self):
        return "%s %s %s %s %s" % (self.name, self.sex, self.age, self.phone, self.personnums)
