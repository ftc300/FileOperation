"""FileOperation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views as v

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^upload/$', v.upload),
    url(r'^download/$', v.download),
    url(r'^api/jsontest/$', v.jsontest),
    url(r'^api/add_book$', v.add_book),
    url(r'^api/show_books$', v.show_books),
    url(r'^$', v.index),
    url('^download/(?P<filename>.{1,100})/$', v.downloadFile)
]
