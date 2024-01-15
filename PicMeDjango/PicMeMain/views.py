from django.shortcuts import render

from django.http import HttpResponse, \
    HttpResponseNotFound, HttpResponseForbidden, \
    HttpResponseServerError, HttpResponseBadRequest, Http404

from django.shortcuts import render, redirect, get_object_or_404
# from .models import Photo
from PIL import Image

def pageBadRequest(request, exception):
    # exc = {'titleError': 'Ошибка 400()', 'descError': 'Ошибка запроса.'}
    # return render(request, 'PicMeMain/exception.html', context=exc)
    return HttpResponseBadRequest('<h1>Ошибка 400 - Ошибка запроса!</h1>')

def pageForbidden(request, exception):
    # exc = {'titleError': 'Ошибка 403()', 'descError': 'Доступ запрещён!'}
    # return render(request, 'PicMeMain/exception.html', context=exc)
    return HttpResponseForbidden('<h1>Ошибка 403 - Нету доступа!</h1>')

def pageNotFound(request, exception):
    # exc = {'titleError': 'Ошибка 404()', 'descError': 'Страничка не найдена.'}
    # return render(request, 'PicMeMain/exception.html', context=exc)
    return HttpResponseNotFound('<h1>Ошибка 404 - Не найдено!</h1>')

def pageServerError(exception):
    # exc = {'titleError': 'Ошибка 500()', 'descError': 'Ошибка сервера.'}
    # return render('PicMeMain/exception.html', context=exc)
    return HttpResponseServerError('<h1>Ошибка 500 - Ошибка сервера!</h1>')

