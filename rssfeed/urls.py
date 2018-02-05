from django.conf.urls import url
from .views import articles_list
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    url('', articles_list, name='index' )
]
