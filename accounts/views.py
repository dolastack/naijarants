from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AliasForm
from rants.models import Rant
# Create your views here.

def create_alias(request):
    if request.method == 'POST':
        form = AliasForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('index')
    else:
        form = AliasForm()
        return render(request, 'accounts/alias_creation_form.html', {'form': form} )
#@login_required
def accounts_user_home(request):
    rants = Rant.objects.all()
    context = {'rants': rants }
    if request.user.is_authenticated:
        return render(request, 'accounts/user_home.html' , context )
    else:
        return redirect('index')
