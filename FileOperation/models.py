import os
from django.contrib import admin
from django.db import models


class FileSimpleModel(models.Model):
    """
    文件接收 Model
    upload_to：表示文件保存位置
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DOWNLOAD_DIR = os.path.join(BASE_DIR, "static/download")
    file_field = models.FileField(upload_to=DOWNLOAD_DIR)

    def __str__(self):
        return self.file_field


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name


# class TagInline(admin.TabularInline):
#     model = Book
#
#
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('book_name', 'add_time')
#     search_fields = ('book_name',)
#     inlines = [TagInline]
#     fieldsets = (['Main', {'fields': ('book_name', 'add_time')}],)
#

admin.site.register(Book)
admin.site.register(FileSimpleModel)
