"""naijarants URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from .views import about
from rants.views import rants_by_category, RantsListView

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^about$', about, name='about_page'),
    url(r'^rant/', include('rants.urls')),
    url(r'^account/', include('accounts.urls')),
    #url(r'(?P<category>[^/]*)', rants_by_category , name='rants_by_catogory'),
    url(r'^$', RantsListView.as_view(), name='rants-list' ),
]
