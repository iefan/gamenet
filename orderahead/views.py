#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from forms import OrderForm
from models import OrderlistModel
import datetime

def orderahead(request):
    # OrderlistModel.objects.only('name','phone',)
    # orderpersondata = OrderlistModel.objects.all()
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
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = OrderForm()
    return render_to_response('orderahead.html', {'form': form, 'orderdate':orderdate})


# form = OrderForm()
# return render_to_response('orderahead.html', {'form':form})

def gamedisplay(request):
    return render_to_response('gamedisplay.html')

def selectorder(request):
    # strinfo = u"姓名：%s <br/>"
    # strinfo += u"性别：%s <br/>"
    # strinfo += u"年龄：%s <br/>"
    curpp = []
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        curpp = OrderlistModel.objects.get(name=name, phone=phone)
        curpp = [curpp.name, curpp.sex, curpp.age, curpp.phone]
        # strinfo = strinfo % (curpp.name, curpp.sex, curpp.age)
        # print curpp
        # print strinfo

    # orderpersondata = OrderlistModel.objects.all()
    return render_to_response('selectorder.html', {'curpp': curpp})
