from django.shortcuts import render
from .models import Rant
# Create your views here.

def rants_list(request):
    rants = Rant.objects.all()
    context = {'rants': rants}
    #template = "base.html"
    return rants

def rant_detail(request, rant):
    print(rant.title)
    context = {'rant': rant}
    template = "rants/rant_detail.html"
    return render(request, template, context)
