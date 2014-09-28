# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.models.filemodels import File
from yaml import load as yaml_load
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class Embeddable(File):
    class Meta:
        app_label = 'filer_embeddable'
        verbose_name = _('embeddable')
        verbose_name_plural = _('embeddables')

    src = models.CharField(
        _('src'),
        max_length=250,
        blank=True,
        null=True,
        default=None)

    width = models.PositiveIntegerField(
        _('width'),
        blank=True,
        null=True,
        default=720)

    height = models.PositiveIntegerField(
        _('height'),
        blank=True,
        null=True,
        default=405)

    def save(self, *args, **kwargs):
        data = yaml_load(self.file)

        self.width = data.get('width', 720)
        self.height = data.get('height', 720)
        self.src = data.get('src')

        super(Embeddable, self).save(*args, **kwargs)

    @classmethod
    def matches_file_type(self, iname, ifile, request):
        filename_extensions = ['.embeddable']
        ext = os.path.splitext(iname)[1].lower()
        return ext in filename_extensions


class Youtube(Embeddable):
    class Meta:
        app_label = 'filer_embeddable'
        verbose_name = _('youtube embeddable')
        verbose_name_plural = _('youtube embeddables')

    @classmethod
    def matches_file_type(cls, iname, ifile, request):
        filename_extensions = ['.youtube']
        ext = os.path.splitext(iname)[1].lower()
        return ext in filename_extensions