"""
URL configuration for PicMeDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from PicMeDjango import settings
from PicMeMain.views import pageBadRequest, pageForbidden,\
    pageNotFound, pageServerError


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PicMeMain.urls')),
]

handler400 = pageBadRequest
handler403 = pageForbidden
handler404 = pageNotFound
handler500 = pageServerError

admin.site.site_header = "Pic me, Django!"
admin.site.index_title = "Страница администратора сервиса Pic me, Django."

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)