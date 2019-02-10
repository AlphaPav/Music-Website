"""MusicWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from web import views
from web import my_init
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^explore/$', views.explore, name='explore'),
    url(r'^search/$', views.search, name='search'),
    url(r'^help/$', views.help, name='help'),

    url(r'^domain/(.+)/$', views.domain, name='domain'),
    url(r'^play/(.+)/$', views.play, name='play'),
    url(r'^dealsearch/$', views.dealsearch, name='dealsearch'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

my_init.setup()