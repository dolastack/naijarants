from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .models import Rant
from .forms import RantForm, CommentForm
from django.views.generic import ListView, DetailView, FormView,TemplateView
from django.utils import timezone
from rssfeed.models import Article

# Create your views here.
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def rants_by_category(request, category):
    rants = Rant.objects.rant_by_category(category)
    template = "index.html"
    context = {'rants': rants}
    return render(request, template, context)

def rants_list(request):
    rants = Rant.objects.all()
    return rants
"""
class IndexView(TemplateView):
    template_name = 'index.html'
"""

class RantsListView(ListView):
    model = Rant
    paginate_by = 200
    template_name = 'index.html'
    context_object_name = 'rants_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['news_article_list'] = Article.objects.articles_after(days=2)
        return context

"""      
class RantDetailView(DetailView):
    model = Rant
    template_name = 'rant_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
"""

def rant_detail(request, id,rant_title):
    rant = get_object_or_404(Rant, title=rant_title , pk=id)

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

def new_rant(request):
    if request.method == "POST":
        form = RantForm( request.POST, request.FILES)

        if form.is_valid():
            rant = form.save(commit=False)
            if request.user.is_authenticated:
                rant.author=request.user
                
            rant.files = form.cleaned_data['files']
            rant.save()
        return redirect('accounts_user_home')
    else:
        form = RantForm()
    #return render(request, "index.html", {'form': form})
    return render(request, "rants/new_rant.html", {'form': form})

"""
class NewRantView(FormView):
    template_name = 'new_rant.html'
    form_class = RantForm

    def form_valid(self, form):
"""