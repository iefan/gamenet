#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from forms import OrderForm
from forms import Order2StepForm, Order3StepForm
from models import OrderlistModel
import datetime

def order1step(request):
    request.session['gameclass'] = ""
    return render_to_response('order1step.html')

def order2step(request):
    request.session['startdate'] = ""
    request.session['starttime'] = ""
    today   = datetime.date.today()
    weekday = today.weekday()
    tablehead = [u"日期", u"星期", u"钟点"]
    tabletime = [today.isoformat(), weekday, '0900']

    jscal_min = int(today.isoformat().replace('-', ''))
    jscal_max = int((today + datetime.timedelta(30)).isoformat().replace('-', ''))

    scene = ""
    if request.method == "POST":
        if "optionscene" in request.POST:
            scene = request.POST['optionscene']
            request.session['gameclass'] = scene

    scene = request.session['gameclass']
    form = Order2StepForm()
    return render_to_response('order2step.html', {"tablehead":tablehead, "tabletime":tabletime, "form":form,"jscal_min":jscal_min, "jscal_max":jscal_max, "scene":scene})

def order3step(request):
    if request.method == "POST":
        if 'startdate' in request.POST:
            startdate = request.POST['startdate']
            starttime = request.POST['starttime']
            request.session['startdate'] = startdate
            request.session['starttime'] = starttime
        else:
            form = Order3StepForm(request.POST)
            if form.is_valid():
                request.session['name']         = request.POST['name']
                request.session['phone']        = request.POST['phone']
                request.session['personnums']   = request.POST['personnums']
                return HttpResponseRedirect('/ordersubmit/') # Redirect

    form = Order3StepForm()
    return render_to_response('order3step.html', {"form":form})

def ordersubmit(request):
    name            = request.session['name']
    phone           = request.session['phone']
    personnums      = request.session['personnums']
    gameclass       = request.session['gameclass']
    startdate       = request.session['startdate']
    starttime       = request.session['starttime']

    submitinfo = OrderlistModel(name=name, phone=phone, personnums=personnums, gameclass=gameclass, startdate=startdate, starttime=starttime)
    print submitinfo

    tablehead = ['姓名', '电话', '人数', '预订场景', '预订日期', '预订时间']
    tableinfo = [name, phone, personnums, gameclass, startdate, starttime]
    return render_to_response('ordersubmit.html', {"tablehead":tablehead, "tableinfo":tableinfo})

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
