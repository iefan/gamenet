#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from forms import OrderForm
from models import OrderlistModel
import datetime

def orderahead(request):
    orderdate = []
    today = datetime.date.today()
    lstchinesenum = ["一", "二", "三", "四", "五", "六", "七"]
    for i in range(0, 7):
        tmpday = (today+datetime.timedelta(i))
        tmpweekday = "周" + lstchinesenum[tmpday.weekday()]
        orderdate.append((tmpday.isoformat(), tmpweekday, '0800-1200,0800-1200'))
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.clean()
            name    = form['name']
            phone   = form['phone']
            form.save()
            return selectorder(request, name, phone)
    else:
        form = OrderForm()
    return render_to_response('orderahead.html', {'form': form, 'orderdate':orderdate})


def gamedisplay(request):
    return render_to_response('gamedisplay.html')


def selectorder(request, name="", phone=""):
    curppname = [u"姓名", u"性别", u"年龄", u"场景", u"电话", u"人数", u"预订时间", u"是否通过申请"]
    curpp     = ["","","","","","","",""]
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        try:
            curpp = OrderlistModel.objects.get(name=name, phone=phone)
            tmpdatetime = curpp.startdate.isoformat() + "--" + curpp.starttime.isoformat()
            if curpp.isagree:
                isagree = u"通过"
            else:
                isagree = u"未通过"
            curpp = [curpp.name, curpp.sex, curpp.age, curpp.gameclass, curpp.phone, curpp.personnums, tmpdatetime, isagree]
        except OrderlistModel.DoesNotExist:
            curpp[0] = "没有登记"
    return render_to_response('selectorder.html', {'curpp': curpp, 'curppname':curppname})


def about(request):
    return render_to_response('about.html')

def contact(request):
    return render_to_response('contact.html')
