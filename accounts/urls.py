from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from .views import create_alias

urlpatterns = [
    url(r'new$', create_alias, name='accounts_new_alias'),
    url(r'login$', LoginView.as_view(template_name='accounts/login_form.html'), name='accounts_login'),
    url(r'logout$',LogoutView.as_view(), name='accounts_logout'),
]
