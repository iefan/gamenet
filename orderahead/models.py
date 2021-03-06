#-*- coding:utf-8 -*-

from django.db import models

# Create your models here.
class OrderlistModel(models.Model):
    name        = models.CharField(max_length=30, verbose_name="姓名")
    # sex         = models.CharField(max_length=2, verbose_name="性别")
    # age         = models.IntegerField(verbose_name="年龄")
    gameclass   = models.CharField(max_length=100, verbose_name="场景")
    phone       = models.CharField(max_length=12, verbose_name="电话")
    personnums  = models.IntegerField(verbose_name="人数")
    startdate   = models.DateField(verbose_name="日期")
    starttime   = models.TimeField(verbose_name="时间")
    # descinfo    = models.TextField(null=True, blank=True, verbose_name="说明")
    # iscancel    = models.BooleanField(blank=True,verbose_name="是否取消")
    isagree     = models.BooleanField(verbose_name="申核同意")
    selfdel     = models.BooleanField(verbose_name="自己删除")

    def __unicode__(self):
        if self.isagree:
            isagree = u"通过"
        else:
            isagree = u"未通过"
        return u"%s　%s　%s　%s　%s--%s　 %s" % (self.name, self.phone, self.personnums, self.gameclass, self.startdate, self.starttime, isagree)
