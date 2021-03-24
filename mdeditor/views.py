# -*- coding:utf-8 -*-
import uuid

from django.views import generic
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from mdeditor.configs import MDConfig


MDEDITOR_CONFIGS = MDConfig(getattr(settings, 'MDEDITOR_CONFIGS_TYPE', 'default'))


class UploadView(generic.View):
    """
    Upload image file view
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UploadView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        upload_image = request.FILES.get('editormd-image-file', None)

        # image none check
        if not upload_image:
            return JsonResponse({
                'success': 0,
                # Ошибка при загрузке изображения
                'message': 'ImageUploadError',
                'url': ''
            })

        # Check image format
        file_name_list = upload_image.name.split('.')
        file_extension = file_name_list.pop(-1)

        if file_extension.lower() not in MDEDITOR_CONFIGS['upload_image_formats']:
            return JsonResponse({
                'success': 0,
                'message': 'WrongImageFormat',
                'url': ''
            })

        # Check image folder
        file_path = settings.MEDIA_ROOT / MDEDITOR_CONFIGS['image_folder']
        if not file_path.exists():
            try:
                file_path.makedirs()
            except Exception:
                return JsonResponse({
                    'success': 0,
                    'message': 'UploadError',
                    'url': ''
                })

        # Save image
        file_full_name = f'{uuid.uuid4()!s}.{file_extension}'
        file_path.write_bytes((v for v in upload_image.chunks()))
        # with open(file_path / file_full_name, 'wb+') as file:
        #     for chunk in upload_image.chunks():
        #         file.write(chunk)

        return JsonResponse({
            'success': 1,
            'message': 'UploadSuccess',
            'url': settings.MEDIA_URL / MDEDITOR_CONFIGS['image_folder'] / file_full_name
        })
