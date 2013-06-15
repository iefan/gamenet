#coding:utf8
from django import forms

class OrderForm(forms.Form):
    CHOICES = (('1', '男',), ('2', '女',))
    name        = forms.CharField(widget=forms.TextInput)
    sex         = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    age         = forms.CharField(widget = forms.TextInput)
    address     = forms.CharField(widget = forms.TextInput)
    phone       = forms.CharField(widget = forms.TextInput)
    starttime   = forms.DateTimeField()
    endtime     = forms.DateTimeField()
    desc        = forms.CharField(widget = forms.Textarea)
