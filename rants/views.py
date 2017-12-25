from django.shortcuts import render
from .models import Rant
from .forms import RantForm
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

def new_rant(request):
    if request.method == "POST":
        pass
    else:
        form = RantForm()
    return render(request, "rants/new_rant.html", {'form': form})
