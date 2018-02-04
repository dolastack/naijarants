from django.conf.urls import url
from .views import new_rant, rant_detail
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    url(r'new$', new_rant, name='rants_new_rant'),

    url(r'(?P<id>\d+)/(?P<rant_title>[^/]*)/$', rant_detail, name='rant_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_URL)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
