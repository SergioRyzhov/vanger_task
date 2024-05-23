from django.db import models
from filer.fields.image import FilerImageField


class Image(models.Model):
    image = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(null=True, max_length=255)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        app_label = 'homepage'
        ordering = ['order']

    def __str__(self):
        return self.name
