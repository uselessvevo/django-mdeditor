# -*- coding:utf-8 -*-
from mdeditor.views import UploadView
from django.conf.urls import url


urlpatterns = [
    url(r'^uploads/$', UploadView.as_view(), name='uploads'),
]
