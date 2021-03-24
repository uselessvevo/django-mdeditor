from django import forms
from django.db import models

from .widgets import MDEditorWidget


class MDTextFormField(forms.fields.CharField):
    """
    Custom text form field
    """

    def __init__(self, config_name=None, *args, **kwargs):
        config_name = config_name if config_name else 'default'
        kwargs.update({
            'widget': MDEditorWidget(config_name=config_name)
        })
        super(MDTextFormField, self).__init__(*args, **kwargs)


class MDTextField(models.TextField):
    """
    Custom text field
    """

    def __init__(self, *args, **kwargs):
        self.config_name = kwargs.pop("config_name", "default")
        super(MDTextField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': MDTextFormField,
            'config_name': self.config_name
        }
        defaults.update(kwargs)
        return super(MDTextField, self).formfield(**defaults)
