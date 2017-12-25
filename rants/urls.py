from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'([^/]*)', views.rant_detail, name='rant_detail'),
    url(r'new$', views.new_rant, name='rant_new_rant'),
]
