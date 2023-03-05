from django.shortcuts import render
from .models import *


def home(request):

    template = 'home/index.html'
    context = {
    }

    return render(request, template, context)
