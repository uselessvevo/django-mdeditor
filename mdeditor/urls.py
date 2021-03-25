# -*- coding:utf-8 -*-
from mdeditor.views import UploadView
from django.conf.urls import url


urlpatterns = [
    url(r'^media/$', UploadView.as_view(), name='media'),
]
