# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import patterns, url
from .views import EmbeddableGenerator


urlpatterns = patterns('',
    url(r'^generator/$', EmbeddableGenerator.as_view(), name='generator'),
)