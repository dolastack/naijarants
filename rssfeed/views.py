from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import  Article, Feed
from .forms import FeedForm
#from background_task import background
from django.utils import timezone
import feedparser, datetime
from .tasks import  save_article

from django.core.cache.backends.base import DEFAULT_TIMEOUT

from django.views.decorators.cache import cache_page
from django.conf import settings

from rants.views import rants_list

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@cache_page(CACHE_TTL)
def articles_list(request):

    display_list = Article.objects.articles_after(days=2)

    rowsd = [display_list[x:x+1] for x in range(0, len(display_list), 1)]

    paginator = Paginator(rowsd, 20)
    page = request.GET.get('page')


    try:
        rows = paginator.page(page)

    except PageNotAnInteger:
        rows = paginator.page(1)


    except EmptyPage:
        rows = paginator.page(paginator.num_pages)

    rants = rants_list(request)
   
    context = {'rows' : rows, 'rants': rants}
    return render (request, 'rssfeed/articles_list.html' , context)

@cache_page(CACHE_TTL)
def feeds_list(request):
    feeds = Feed.objects.all()
    return render(request, 'news/feeds_list.html', {'feeds': feeds})
