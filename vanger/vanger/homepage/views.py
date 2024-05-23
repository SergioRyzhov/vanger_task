from django.shortcuts import render
from .models import Image


def home(request):
    images = Image.objects.all()
    return render(request, 'homepage/index.html', {'images': images})
