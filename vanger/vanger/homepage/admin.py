from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.utils.html import format_html
from .models import Image


class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'preview_image', 'file_name')

    def file_name(self, obj):
        if obj.image:
            return obj.name
        return "No Image"

    file_name.short_description = 'File Name'

    def preview_image(self, obj):
        if obj.image:
            image_url = obj.image.url
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', image_url)
        else:
            return "No Image"

    preview_image.short_description = 'Image Preview'


admin.site.register(Image, ImageAdmin)

