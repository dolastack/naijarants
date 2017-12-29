from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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
@login_required
def new_rant(request):
    if request.method == "POST":
        rant = Rant()

        rant.author=request.user

        form = RantForm(instance=rant, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts_user_home')
    else:
        form = RantForm()
        return render(request, "rants/new_rant.html", {'form': form})
