# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms


class EmbeddableGeneratorForm(forms.Form):

    class Meta:
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'})}

    title = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    src = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    width = forms.IntegerField(
        initial=720,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    height = forms.IntegerField(
        initial=405,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
