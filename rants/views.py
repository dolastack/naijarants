from django.shortcuts import render, redirect, get_object_or_404
from .models import Rant
from .forms import RantForm
# Create your views here.

def rants_list(request):
    rants = Rant.objects.all()
    context = {'rants': rants}
    #template = "base.html"
    return rants



def rant_detail(request, rant_title):
    rant = get_object_or_404(Rant, title=rant_title)
    context = {'rant': rant}
    template = "rants/rant_detail.html"
    return render(request, template, context)

def new_rant(request):
    if request.method == "POST":
        rant = Rant(created_by=request.user)
        form = RantForm(instance=rant, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RantForm()
        return render(request, "rants/new_rant.html", {'form': form})
