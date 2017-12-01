import os

from django.db import models


class FileSimpleModel(models.Model):
    """
    文件接收 Model
    upload_to：表示文件保存位置
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DOWNLOAD_DIR = os.path.join(BASE_DIR, "static/download")
    file_field = models.FileField(upload_to=DOWNLOAD_DIR)

# class DownloadModel(models.Model):