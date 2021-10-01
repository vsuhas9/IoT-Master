"""
URLS for OM2M-APP
"""
from django.conf.urls import url
from .views import om2m, dummy

urlpatterns = []

urlpatterns += [
    url(
        'runserver/om2m$',
        om2m
    ),
    url(
        'test/om2m$',
        dummy
    ),
]
