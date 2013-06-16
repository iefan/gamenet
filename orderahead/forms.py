#coding:utf8
# from django.forms import ModelForm
from django import forms
# from django.forms.extras import SelectDateWidget
from models import orderlist
from django.contrib.admin import widgets

class OrderForm(forms.ModelForm):
    # starttime   = forms.DateField(widget=widgets.AdminDateWidget)
    starttime   = forms.DateTimeField(widget=widgets.AdminSplitDateTime)
    endtime     = forms.DateTimeField(widget=widgets.AdminSplitDateTime)
    # endtime     = forms.SplitDateTimeField(input_time_formats=['%I:%M %p'])
    # starttime.widgets[0].attrs = {'class': 'vDateField'}
    # starttime.widgets[1].attrs = {'class': 'vTimeField'}
    class Meta:
        model=orderlist
        exclude=('starttime','endtime')
    def clean(self):
        self.instance.starttime=self.cleaned_data.get('starttime')
        self.instance.endtime=self.cleaned_data.get('endtime')


# class OrderForm2(forms.Form):
#     CHOICES = (('1', '男',), ('2', '女',))
#     name        = forms.CharField(widget=forms.TextInput)
#     sex         = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
#     age         = forms.CharField(widget = forms.TextInput)
#     address     = forms.CharField(widget = forms.TextInput)
#     phone       = forms.CharField(widget = forms.TextInput)
#     starttime   = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder':'--Please Input...', 'class':"vDateField"}))
#     endtime     = forms.DateTimeField()
#     desc        = forms.CharField(widget = forms.Textarea)
