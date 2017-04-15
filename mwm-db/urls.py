"""mwm-db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.flatpages import views

urlpatterns = [
    # url(r'^admin/', include('smuggler.urls')),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'', include('apps.database.urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),

    # Flatpages
    url(r'^contributor-guidelines-1/$', views.flatpage,
        {'url': '/contributor-guidelines-1/'}, name='guidelines-1'),
    url(r'^contributor-guidelines-2/$', views.flatpage,
        {'url': '/contributor-guidelines-2/'}, name='guidelines-2'),
    url(r'^contributor-guidelines-3/$', views.flatpage,
        {'url': '/contributor-guidelines-3/'}, name='guidelines-3'),
    url(r'^contributor-guidelines-4/$', views.flatpage,
        {'url': '/contributor-guidelines-4/'}, name='guidelines-4'),
]
