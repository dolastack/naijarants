from django.conf.urls import url
from . import views
urlpatterns = [
    url('', views.articles_list, name='index' )
]
