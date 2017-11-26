from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(rant)/', views.rant_detail, name='rant_detail')
]
