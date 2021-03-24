# -*- coding:utf-8 -*-
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


DEFAULT_CONFIG = {
    'width': '100%',
    'height': 500,
    'toolbar': [
        'undo', 'redo', '|',
        'bold', 'del', 'italic', 'quote', 'ucwords', 'uppercase', 'lowercase', '|',
        'h1', 'h2', 'h3', 'h5', 'h6', '|',
        'list-ul', 'list-ol', 'hr', '|',
        'link', 'reference-link', 'image', 'code', 'preformatted-text', 'code-block', 'table', 'datetime',
        'emoji', 'html-entities', 'pagebreak', 'goto-line', '|',
        'help', 'info',
        '||', 'preview', 'watch', 'fullscreen'
    ],
    'upload_image_formats': [
        'jpg', 'jpeg', 'gif', 'png', 'webp', 'bmp',
    ],
    'image_folder': 'editor',

    # Available themes:
    # * Dark
    # * Default
    'theme': 'default',
    'preview_theme': 'default',
    # pastel-on-dark
    'editor_theme': 'default',

    'toolbar_autofixed': True,
    'search_replace': True,
    'emoji': True,
    'tex': True,
    'task_list': False,
    'flow_chart': True,
    'sequence': True,
    'language': 'zh',  # zh / en
    'watch': True,  # Live preview
    'lineWrapping': False,  # lineWrapping
    'lineNumbers': False  # lineNumbers
}


class MDConfig(dict):

    def __init__(self, config_name='default'):
        self.update(DEFAULT_CONFIG)
        self.set_configs(config_name)
        super().__init__()

    def set_configs(self, config_name=None):
        """
        Args:
            config_name (str)
        """
        # Try to get valid config from settings.
        configs = getattr(settings, 'MDEDITOR_CONFIGS', None)
        config_name = config_name if config_name else 'default'

        if not isinstance(configs, dict):
            raise ImproperlyConfigured(
                'MDEDITOR_CONFIGS setting must be a dict-type.'
            )

        if not config_name in configs:
            raise ImproperlyConfigured(
                f'No configuration named "{config_name}" found in your CKEDITOR_CONFIGS setting'
            )

        config = configs[config_name]
        if not isinstance(config, dict):
            raise ImproperlyConfigured(
                f'MDEDITOR_CONFIGS["{config_name}"] is not a dict-type'
            )

        self.update(config)
