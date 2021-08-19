
from django.contrib import admin
from django.urls import path,include
from django.config.urls.static import static
from django.config import settings

from django.views.static import serve
from django.config.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resumesite.urls')),
    path('/submit', )
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

