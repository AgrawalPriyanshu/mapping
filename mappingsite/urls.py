"""mappingsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from mapping import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('mapping.urls')),
    url(r'^registrationurl/',views.RegistrationList.as_view()),
    url(r'^gameurl/$',views.GameList.as_view()),
    url(r'^athleteurl/$',views.AthleteList.as_view()),
    url(r'^gameurl/([0-9]+)/',views.GameDetail.as_view()),
    url(r'^athleteurl/([0-9]+)/',views.AthleteDetail.as_view()),
]
urlpatterns=format_suffix_patterns(urlpatterns)
