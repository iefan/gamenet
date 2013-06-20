#coding:utf8
from django import forms
from models import OrderlistModel
from django.contrib.admin import widgets
import datetime

class OrderForm(forms.ModelForm):
    # sexchoices      = ( ('男','男'),('女','女'),)
    # agechoices      = tuple([(`i`,`j`) for i,j in zip(range(16,30), range(16,30))])
    ppnumschoices   = tuple([(`i`,`j`) for i,j in zip(range(4,8), range(4,8))])
    today = datetime.date.today()
    datechoices     = tuple([((today+datetime.timedelta(i)).isoformat(), (today+datetime.timedelta(i)).isoformat()) for i in range(1,10)])
    timechoices     = []
    for i in range(9,18):
        tmptime1 = datetime.time(i,0)
        tmptime2 = datetime.time(i,30)
        timechoices.append((tmptime1, tmptime1))
        timechoices.append((tmptime2, tmptime2))
    timechoices     = tuple(timechoices)
    gameclasschoices= (("场景1", "场景1"), ("场景2", "场景2"))

    # startdate   = forms.ChoiceField(choices = datechoices, label='日期')
    startdate   = forms.CharField(label='日期', widget= forms.TextInput(attrs={'id': "calendar-inputField"}))
    starttime   = forms.ChoiceField(choices = timechoices, label='时间')
    # sex         = forms.ChoiceField(choices=sexchoices, label='性别')   #widget=forms.RadioSelect
    # age         = forms.ChoiceField(choices = agechoices, label='年龄')
    personnums  = forms.ChoiceField(choices = ppnumschoices, label='人数')
    gameclass  = forms.ChoiceField(choices = gameclasschoices, label='场景')

    class Meta:
        model=OrderlistModel
        exclude=('isagree',)

    def clean(self):
        return self.cleaned_data
    #     self.instance.starttime=self.cleaned_data.get('starttime')

    def clean_starttime(self):
        startdate   = self.cleaned_data['startdate']
        starttime   = self.cleaned_data['starttime']
        curpp = OrderlistModel.objects.filter(startdate=startdate, starttime=starttime) #, isagree=False
        if len(curpp) != 0:
            raise forms.ValidationError("当前时间段已经有人预订，请另选时间！")
        else:
            pass

        return starttime

    def clean_phone(self):
        name   = self.cleaned_data['name']
        phone  = self.cleaned_data['phone']

        if not phone.isdigit() or len(phone)<11 or len(phone) > 12:
            raise forms.ValidationError("请输入11或12位电话号码")


        curpp = OrderlistModel.objects.filter(name=name, phone=phone, isagree=False)
        if len(curpp) != 0:
            raise forms.ValidationError("该电话及姓名在当前系统您已经预订！")
        else:
            pass

        return phone
