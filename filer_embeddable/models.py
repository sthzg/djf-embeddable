# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.models.filemodels import File


class Embeddable(File):
    """
    Base model for more specific embeddable instances.
    """
    class Meta:
        app_label = 'filer_embeddable'
        verbose_name = _('embeddable')
        verbose_name_plural = _('embeddables')

    #: Src url for embed code. Usually used in <iframe /> tag.
    src = models.CharField(
        _('src'),
        max_length=250,
        blank=True,
        null=True,
        default=None)

    #: Width value for embedding. (often times this is altered through
    #: responsive embedding techniques directly from within the templates.
    width = models.PositiveIntegerField(
        _('width'),
        blank=True,
        null=True,
        default=720)

    #: Height value for embedding. (often times this is altered through
    #: responsive embedding techniques directly from within the templates.
    height = models.PositiveIntegerField(
        _('height'),
        blank=True,
        null=True,
        default=405)

    def save(self, *args, **kwargs):
        """
        Extracts json data from file object to mode fields and updates file
        object if data is altered in admin.

        Filename extension: *.embeddable
        File format JSON.
        """
        data = json.loads(self.file.file.read())

        if not self.pk:
            # On upload initially read all data form the json file.
            self.width = data.get('width', 720)
            self.height = data.get('height', 405)
            self.src = data.get('src')

        else:
            # On change, write changed data to the json file on disk.
            data['width'] = self.width
            data['height'] = self.height
            data['src'] = self.src

            with open(self.file.path, 'w') as f:
                f.write(json.dumps(data))

        super(Embeddable, self).save(*args, **kwargs)

    @classmethod
    def matches_file_type(cls, iname, ifile, request):
        filename_extensions = ['.embeddable']
        ext = os.path.splitext(iname)[1].lower()
        return ext in filename_extensions


class Youtube(Embeddable):
    """
    Embeddable model for Youtube video embeds.

    Filename extension: .youtube
    File format JSON.
    """
    class Meta:
        app_label = 'filer_embeddable'
        verbose_name = _('youtube embeddable')
        verbose_name_plural = _('youtube embeddables')

    @classmethod
    def matches_file_type(cls, iname, ifile, request):
        filename_extensions = ['.youtube']
        ext = os.path.splitext(iname)[1].lower()
        return ext in filename_extensions
