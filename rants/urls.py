from django.conf.urls import url
from .views import new_rant, rant_detail

urlpatterns = [
    url(r'new$', new_rant, name='rants_new_rant'),

    url(r'(?P<id>[^/]\d+)/(?P<rant_title>[^/]*)/$', rant_detail, name='rant_detail'),

]
