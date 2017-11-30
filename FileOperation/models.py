from django.db import models


class FileSimpleModel(models.Model):
    """
    文件接收 Model
    upload_to：表示文件保存位置
    """
    file_field = models.FileField(upload_to="upload/")