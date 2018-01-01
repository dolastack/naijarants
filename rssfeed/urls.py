from django.conf.urls import url
from .views import articles_list
urlpatterns = [
    url('', articles_list, name='index' )
]
