from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'new$', views.new_rant, name='rants_new_rant'),
    url(r'([^/]*)', views.rant_detail, name='rant_detail'),

]
