from django.shortcuts import render

from django.http import HttpResponse, \
    HttpResponseNotFound, HttpResponseForbidden, \
    HttpResponseServerError, HttpResponseBadRequest, Http404

from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from PIL import Image

logo = [
    {'logo': 'mainPage'}
]

menu = [
    {'menuTitle': 'Главная', 'menuUrl': 'mainPage'},
    {'menuTitle': 'Галерея изображений', 'menuUrl': 'galleryPage'},
]
footer = [
    {'footerTitle': 'Главная', 'footerUrl': 'mainPage'},
    {'footerTitle': 'Галерея', 'footerUrl': 'galleryPage'},
]


# def index(request):
#     data = {
#         'menu': menu,
#         'footer': footer,
#         'logo': logo,
#     }
#     return render(request, 'PicMeMain/index.html', context=data)


def gallery(request):
    photo = Photo.objects.all()

    data = {
        'menu': menu,
        'footer': footer,
        'logo': logo,
        'photo': photo,
    }
    return render(request, 'PicMeMain/gallery.html', context=data)


def upload_photo(request):
    data = {
        'menu': menu,
        'footer': footer,
        'logo': logo,
    }
    if request.method == 'POST':
        photo = request.FILES['photo']
        new_photo = Photo.objects.create(image=photo)
        new_photo.save()
        download_photo(request, int(new_photo.id))
        photo = Photo.objects.get(id=new_photo.id)
        print(photo.image.url)
        print(photo.image.name)
        data_image = {
            # 'url_image': photo.image.url,
            # 'name_image': photo.image.name[6:],
            'menu': menu,
            'footer': footer,
            'logo': logo,
            'information': 'Фотография успешно загружена!',
        }
        # return render(request, 'PicMeMain/selectedPhoto.html', context=data_image)
        return render(request, 'PicMeMain/index.html', context=data_image)
    return render(request, 'PicMeMain/index.html', context=data)


def download_photo(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    image = Image.open(photo.image)
    # black_white_image = image.convert('L')
    response = HttpResponse(content_type='image/jpeg')
    temp_filename = photo.image.name
    # black_white_image.save(temp_filename)
    response['Content-Disposition'] = f'attachment; filename="{photo.image.name}"'
    return response


def convertPage(request, convert_id):
    photo = Photo.objects.all()
    data = {
        'menu': menu,
        'footer': footer,
        'logo': logo,
    }
    return render(request, 'PicMeMain/selectedPhoto.html', context=data)


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

