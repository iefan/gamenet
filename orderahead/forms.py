#coding:utf8
from django import forms
from models import OrderlistModel
from django.contrib.admin import widgets

class OrderForm(forms.ModelForm):
    sexchoices      = ( ('男','男'),('女','女'),)
    agechoices      = tuple([(`i`,`j`) for i,j in zip(range(16,30), range(16,30))])
    ppnumschoices   = tuple([(`i`,`j`) for i,j in zip(range(1,6), range(1,6))])

    startdate   = forms.DateField(widget=widgets.AdminDateWidget, label="日期")
    starttime   = forms.TimeField(widget=widgets.AdminTimeWidget, label="时间")
    sex         = forms.ChoiceField(choices=sexchoices, label='性别')#, widget=forms.RadioSelect
    age         = forms.ChoiceField(choices = agechoices, label='年龄')
    personnums  = forms.ChoiceField(choices = ppnumschoices, label='人数')

    class Meta:
        model=OrderlistModel
        exclude=('iscancel','isagree',)

    def clean(self):
        return self.cleaned_data
    #     self.instance.starttime=self.cleaned_data.get('starttime')

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit() or len(phone)<11 or len(phone) > 12:
            raise forms.ValidationError("请输入11或12位电话号码")
        return phone
