import json
import mimetypes
from wsgiref.util import FileWrapper

from django.http import HttpResponse, JsonResponse
from FileOperation.forms import FileUploadForm
from django.shortcuts import render
from FileOperation.models import FileSimpleModel
from FileOperation.models import Book
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOWNLOAD_DIR = os.path.join(BASE_DIR, "static/download")


def handle_upload_file(f):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(BASE_DIR, 'upload', f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# def upload(request):
#     if request.method == 'POST':
#         my_form = FileUploadForm(request.POST, request.FILES)
#         if my_form.is_valid():
#             f = my_form.cleaned_data['my_file']
#             handle_upload_file(f)
#         return HttpResponse('Upload Success')
#     else:
#         my_form = FileUploadForm()
#     return render(request, 'upload.html', {'form': my_form})


def index(request):
    return render(request, 'index.html', "")


def jsontest(request):
    json_data = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
    return HttpResponse(json_data, content_type="application/json")


def upload(request):
    """
    文件接收 view
    :param request: 请求
    :return:
    """
    if request.method == 'POST':
        my_form = FileUploadForm(request.POST, request.FILES)
        if my_form.is_valid():
            # f = my_form.cleaned_data['my_file']
            # handle_uploaded_file(f)
            file_model = FileSimpleModel()
            file_model.file_field = my_form.cleaned_data['upload_file']
            file_model.save()
        return HttpResponse('Upload Success')
    else:
        my_form = FileUploadForm()
    return render(request, 'upload.html', {'form': my_form})


def download(request):
    context = {}
    context['download'] = '文件列表'
    ln = os.listdir(DOWNLOAD_DIR)
    l = []
    for i in ln:
        l.append(dictName(i, request.path + i))
    context['dict'] = l
    return render(request, 'download.html', context)


class dictName:
    name = ""
    href = ""

    def __init__(self, name, href):
        self.name = name
        self.href = href


def downloadFile(request, filename):
    filepath = os.path.join(DOWNLOAD_DIR, filename)
    print(filepath)
    wrapper = FileWrapper(open(filepath, 'rb'))
    response = HttpResponse(wrapper, content_type="text/file")
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as Arg:
        response['msg'] = "error"
        response['error_num'] = 1
    return JsonResponse(response)

def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        from django.core import serializers
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception:
        response['msg'] = "Error"
        response['error_num'] = 1
    return JsonResponse(response)