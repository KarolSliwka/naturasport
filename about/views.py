from django.shortcuts import render
from .models import *


def about(request):

    template = 'about/index.html'
    context = {
    }

    return render(request, template, context)
