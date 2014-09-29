# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms
from django.contrib import admin
from filer.admin.fileadmin import FileAdmin
from .models import Embeddable, Youtube


#                                                                          _____
#                                                                EmbeddableAdmin
class EmbeddableAdminForm(forms.ModelForm):
    class Meta:
        model = Embeddable


class EmbeddableAdmin(FileAdmin):
    form = EmbeddableAdminForm


#                                                                          _____
#                                                                   YoutubeAdmin
class YoutubeAdminForm(forms.ModelForm):
    class Meta:
        model = Youtube


class YoutubeAdmin(EmbeddableAdmin):
    form = YoutubeAdminForm


#                                                                          _____
#                                                                      Fieldsets
EmbeddableAdmin.fieldsets = EmbeddableAdmin.build_fieldsets(
    extra_main_fields=('src', 'width', 'height',))


#                                                                          _____
#                                                                   Registration
admin.site.register(Embeddable, EmbeddableAdmin)
admin.site.register(Youtube, YoutubeAdmin)
