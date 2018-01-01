from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Rant
from .forms import RantForm, CommentForm

# Create your views here.

def rants_list(request):
    rants = Rant.objects.all()
    context = {'rants': rants}
    #template = "base.html"
    return rants

def rant_detail(request, rant_title):
    rant = get_object_or_404(Rant, title=rant_title)

    comments = rant.comments.filter(active=True)
    if request.method == 'POST':
        comment_form =CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.rant = rant
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {'rant': rant, 'comments': comments, 'comment_form': comment_form}
    template = "rants/rant_detail.html"
    return render(request, template, context)

#@login_required
def new_rant(request):
    if request.method == "POST":
        rant = Rant()
        if request.user.is_authenticated:
            rant.author=request.user
        form = RantForm(instance=rant, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts_user_home')
    else:
        form = RantForm()
        return render(request, "rants/new_rant.html", {'form': form})
