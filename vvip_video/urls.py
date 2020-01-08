"""vvip_video URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    # url子路由
    path('admin/', admin.site.urls),
    path('help/', include('video_help.urls')),
    # 视图路由
    path('', views.index),
    path('get_channels', views.get_channels),
    # 静态文件路由
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': 'static'}),

]
