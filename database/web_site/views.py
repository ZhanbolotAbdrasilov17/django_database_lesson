from django.shortcuts import render
from .models import *

def home(request):
    up_gallery = UpImages.objects.all()
    context = {'up_gallery': up_gallery}
    return render(request, 'index.html', context)