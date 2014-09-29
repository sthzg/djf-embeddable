# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django.views.generic import FormView
from .forms import EmbeddableGeneratorForm


class EmbeddableGenerator(FormView):
    """
    Returns a JSON-encoded file object for an embeddable.

    Displays a form that lets user enter parameters of the embeddable.
    After submitting the form a json encoded text file is generated.

    This file is not stored on the server's file system.

    .. note::

        Rather than using this view directly it is supposed to be extended
        from applications that need its functionality. By overriding the
        ``FormView`` attributes the theming can be  completely customized.

    """
    # TODO(sthzg) Implement plugin system to easily enable different providers.

    template_name = 'filer_embeddable/embeddable_generator.html'
    success_url = reverse_lazy('filer_embeddable:generator')
    form_class = EmbeddableGeneratorForm

    def form_valid(self, form):
        file_content = json.dumps(form.cleaned_data)
        file_name = slugify(form.cleaned_data.get('title').lower())
        # TODO(sthzg) Make configurable.
        file_ext = 'youtube'

        res = HttpResponse(file_content)
        res['Content-Disposition'] = 'attachment; filename={}.{}'.format(
            file_name, file_ext)

        return res