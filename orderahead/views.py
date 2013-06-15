from django.shortcuts import render_to_response
from forms import OrderForm

def orderahead(request):
    form = OrderForm()
    return render_to_response('orderahead.html', {'form':form})
