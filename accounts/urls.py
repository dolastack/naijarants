from django.conf.urls import url
from .views import create_alias

urlpatterns = [
    url(r'new$', create_alias, name='accounts_new_alias'),
]
