from django.db import models


class Photo(models.Model):
    heightImage = models.IntegerField()
    widthImage = models.IntegerField()
    image = models.ImageField(upload_to='media/')
