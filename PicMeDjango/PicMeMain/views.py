from django.shortcuts import render

from django.http import HttpResponse, \
    HttpResponseNotFound, HttpResponseForbidden, \
    HttpResponseServerError, HttpResponseBadRequest, Http404

from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from PIL import Image, ImageFilter

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
    response = HttpResponse(content_type='image/jpeg')
    temp_filename = photo.image.name
    response['Content-Disposition'] = f'attachment; filename="{photo.image.name}"'
    return response


def convertPage(request, convert_id):
    # photo = Photo.objects.all()
    photo = Photo.objects.get(id=convert_id)
    imge = Image.open(photo.image)
    data = {
        'menu': menu,
        'footer': footer,
        'logo': logo,
        'url_image': photo.image.url,
        'name_image': photo.image.name[6:],
        'img_orig_width': imge.width,
        'img_orig_height': imge.height,
    }
    if request.method == 'POST':
        dat_ass = request.POST
        height_pic = dat_ass.get('height')
        width_pic = dat_ass.get('width')
        rotation = dat_ass.get('rotation')
        check_box = dat_ass.get('radio')

        imge_rotate = imge.rotate(angle=int(rotation))

        img_resized = imge_rotate.resize((int(width_pic), int(height_pic)))

        if check_box == "One":
            convert_img = img_resized.filter(ImageFilter.BLUR)
        elif check_box == "Two":
            convert_img = img_resized.convert('L')
        elif check_box == "Three":
            convert_img = img_resized.filter(ImageFilter.CONTOUR)
        elif check_box == "Four":
            convert_img = img_resized.filter(ImageFilter.SMOOTH)
        else:
            convert_img = img_resized.filter(ImageFilter.DETAIL)
        full_path = 'media/'+photo.image.name

        convert_img.save(full_path)

        data_new = {
            'menu': menu,
            'footer': footer,
            'logo': logo,
            'url_image': photo.image.url,
            'name_image': photo.image.name[6:],
        }

        return render(request, 'PicMeMain/convertedPhoto.html', context=data_new)
    return render(request, 'PicMeMain/selectedPhoto.html', context=data)


def pageBadRequest(request, exception):
    exc = {
        'menu': menu,
        'footer': footer,
        'logo': logo,
        'codeNumber': '400',
        'errorText': 'Ошибка',
        'descText': 'Ошибка отправленного запроса.',
    }

    return render(request, 'PicMeMain/exception.html', context=exc)
    # return HttpResponseBadRequest('<h1>Ошибка 400 - Ошибка запроса!</h1>')


def pageForbidden(request, exception):
    exc = {
        'menu': menu,
        'footer': footer,
        'logo': logo,
        'codeNumber': '403',
        'errorText': 'Ошибка',
        'descText': 'Доступ запрещён!',
    }

    return render(request, 'PicMeMain/exception.html', context=exc)
    # return HttpResponseForbidden('<h1>Ошибка 403 - Нету доступа!</h1>')


def pageNotFound(request, exception):
    exc = {
        'menu': menu,
        'footer': footer,
        'logo': logo,
        'codeNumber': '404',
        'errorText': 'Ошибка',
        'descText': 'Данная страница не была найдена.',
    }

    return render(request, 'PicMeMain/exception.html', context=exc)
    # return HttpResponseNotFound('<h1>Ошибка 404 - Не найдено!</h1>')


def pageServerError(exception):
    exc = {
        'menu': menu,
        'footer': footer,
        'logo': logo,
        'codeNumber': '500',
        'errorText': 'Ошибка',
        'descText': 'Ошибка на стороне сервера.'
    }

    return render('PicMeMain/exception.html', context=exc)
    # return HttpResponseServerError('<h1>Ошибка 500 - Ошибка сервера!</h1>')

