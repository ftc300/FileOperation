from django.forms import forms

class FileUploadForm(forms.Form):
    upload_file = forms.FileField()