#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from forms import OrderForm
from models import OrderlistModel
import datetime

def orderahead(request):
    today = datetime.date.today()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # form.clean()
            form.save()
            name    = request.POST['name']
            phone   = request.POST['phone']
            return selectorder(request, name, phone)
    else:
        form = OrderForm()

    jscal_min = int(today.isoformat().replace('-', ''))
    jscal_max = int((today + datetime.timedelta(30)).isoformat().replace('-', ''))
    return render_to_response('orderahead.html', {'form': form,  "jscal_min":jscal_min, "jscal_max":jscal_max})


def gamedisplay(request):
    return render_to_response('gamedisplay.html')


def selectorder(request, name="", phone=""):
    curppname = [u"姓名", u"场景", u"电话", u"人数", u"预订时间", u"是否通过申请"]
    curpp     = ["","","","","",""]

    if request.method == 'POST':
        if name == "" and phone == "":
            name = request.POST['name']
            phone = request.POST['phone']

        cur_re = OrderlistModel.objects.filter(name=name, phone=phone)
        if len(cur_re) != 0:
            cur_re = cur_re[0]
            tmpdatetime = cur_re.startdate.isoformat() + "--" + cur_re.starttime.isoformat()
            if cur_re.isagree:
                isagree = u"通过"
            else:
                isagree = u"未通过"
            curpp = [cur_re.name,  cur_re.gameclass, cur_re.phone, cur_re.personnums, tmpdatetime, isagree]
        else:
            curpp[0] = "没有登记"

    return render_to_response('selectorder.html', {'curpp': curpp, 'curppname':curppname})


def about(request):
    return render_to_response('about.html')

def contact(request):
    return render_to_response('contact.html')
