from django.shortcuts import render, redirect
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

def accounts_user_home(request):
    rants = Rant.objects.all()
    user = request.user
    context = {'rants': rants, 'user': user }

    return render(request, 'accounts/user_home.html' , context )
"""
def home(request):
    if is_authenticated:
        redirect(accounts_user_home)
    else
"""
