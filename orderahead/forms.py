#coding:utf8
from django import forms
from models import OrderlistModel
from django.contrib.admin import widgets
import datetime

class Order2StepForm(forms.Form):
    today = datetime.date.today()
    datechoices     = tuple([((today+datetime.timedelta(i)).isoformat(), (today+datetime.timedelta(i)).isoformat()) for i in range(1,10)])
    timechoices     = []
    for i in range(9,18):
        tmptime1 = datetime.time(i,0)
        tmptime2 = datetime.time(i,30)
        timechoices.append((tmptime1, tmptime1))
        timechoices.append((tmptime2, tmptime2))
    timechoices     = tuple(timechoices)
    tomorrow = (today + datetime.timedelta(1)).isoformat()
    startdate   = forms.CharField(error_messages={'required':u'日期不能为空'}, label='日期', widget= forms.TextInput()) #initial=tomorrow
    starttime   = forms.ChoiceField(choices = timechoices, label='时间')

    def clean(self):
        return self.cleaned_data

class Order3StepForm(forms.Form):
    ppnumschoices   = tuple([(`i`,`j`) for i,j in zip(range(4,8), range(4,8))])
    name        = forms.CharField(error_messages={'required':u'姓名不能为空'}, label='姓名', widget= forms.TextInput())
    personnums  = forms.ChoiceField(choices = ppnumschoices, label='人数')
    phone       = forms.CharField(error_messages={'required':u'电话不能为空'}, label='电话', widget= forms.TextInput(), initial='15915533701')
    # class Meta:
    #     fields = ('name', 'phone', 'personnums',)

    def clean(self):
        return self.cleaned_data

    def clean_phone(self):
        phone  = self.cleaned_data['phone']

        if not phone.isdigit() or len(phone)<11 or len(phone) > 12:
            raise forms.ValidationError("请输入11或12位电话号码")

        curpp = OrderlistModel.objects.filter(phone=phone, isagree=False)
        if len(curpp) != 0:
            raise forms.ValidationError("该电话在当前系统您已经预订！")
        else:
            pass

        return phone

class OrderForm(forms.ModelForm):
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


    startdate   = forms.CharField(error_messages={'required':u'日期不能为空'}, label='日期', widget= forms.TextInput())
    starttime   = forms.ChoiceField(choices = timechoices, label='时间')
    personnums  = forms.ChoiceField(choices = ppnumschoices, label='人数')
    gameclass  = forms.ChoiceField(choices = gameclasschoices, label='场景')

    class Meta:
        model=OrderlistModel
        fields = ('name', 'phone', 'personnums', 'startdate', 'starttime', 'gameclass')
        exclude=('isagree',)

    def clean(self):
        return self.cleaned_data

    def clean_name(self):
        name   = self.cleaned_data['name']
        curpp = OrderlistModel.objects.filter(name=name, isagree=False)
        if len(curpp) != 0:
            raise forms.ValidationError("该姓名在当前系统您已经预订！")
        else:
            pass
        return name

    def clean_phone(self):
        phone  = self.cleaned_data['phone']

        if not phone.isdigit() or len(phone)<11 or len(phone) > 12:
            raise forms.ValidationError("请输入11或12位电话号码")

        curpp = OrderlistModel.objects.filter(phone=phone, isagree=False)
        if len(curpp) != 0:
            raise forms.ValidationError("该电话在当前系统您已经预订！")
        else:
            pass

        return phone

    def clean_gameclass(self):
        if 'startdate' not in self.cleaned_data.keys():
            raise forms.ValidationError("请先输入日期！") #
        if 'starttime' not in self.cleaned_data.keys():
            raise forms.ValidationError("请先输入合适的时间！") #
        gameclass = self.cleaned_data['gameclass']
        startdate = self.cleaned_data['startdate']
        starttime = self.cleaned_data['starttime']
        curpp = OrderlistModel.objects.filter(startdate=startdate, starttime=starttime, gameclass=gameclass, isagree=False)
        if len(curpp) != 0:
            raise forms.ValidationError("该场景在该时段已经有人预订，请重新选择！")
        else:
            pass

        return gameclass
