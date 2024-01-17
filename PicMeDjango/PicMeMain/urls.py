from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_photo, name='mainPage'),
    path('gallery/', views.gallery, name='galleryPage'),
    path('convert/<int:convert_id>', views.convertPage, name='convertPage'),
    # path('convert/<int:convert_id>/converted', views.convertPageFinal, name='convertPageFinal'),
]