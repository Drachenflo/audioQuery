"""Skriptsprachen_Semesterprojekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
import os
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from accounts.views import login_view, logout_view ,register_view, view_xi, simple_upload, model_form_upload, view_home, getAudio, getButtons, getPad,getPadData,editPad,editButton,delButton
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^register/', register_view, name='register'),
    url(r'^xi/', view_xi, name='xi'),
    #url(r'^u/', simple_upload),
    url(r'^o/', model_form_upload,name='upload'),
    url(r'^home/', view_home, name='home'),
    url(r'^list_audio/', getAudio, name='list_audio'),
    url(r'^list_button/', getButtons, name='list_but'),
    url(r'^list_pad/', getPad, name='list_pad'),
    url(r'^list_paddata/',  getPadData, name='data'),
    url(r'^add_Audio/', getPad, name='list_pad'),
    url(r'^edit_pad/', editPad, name='edit_pad'),
    url(r'^edit_button/(?P<pk>.*)/doclist/(?P<user>.*)/doclist/$', editButton, name='edit_button'),
    url(r'^delete_button/(?P<pk>.*)/doclist/(?P<user>.*)/doclist/$', delButton, name='delete_button'),
]
#os.path.join((BASE_DIR), "static_cdn"
if settings.DEBUG:
    urlpatterns += static('/user_audio/', document_root=os.path.join((settings.BASE_DIR), "user_audio"))
