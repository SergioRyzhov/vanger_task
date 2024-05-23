from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')

    class Meta:
        app_label = 'homepage'
