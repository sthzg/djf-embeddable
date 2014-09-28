# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from filer.admin.fileadmin import FileAdmin
from .models import Embeddable, Youtube

admin.site.register(Embeddable, FileAdmin)
admin.site.register(Youtube, FileAdmin)
