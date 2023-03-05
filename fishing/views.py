from django.shortcuts import render
from .models import *


def fishing(request):

    template = 'fishing/index.html'
    context = {
    }

    return render(request, template, context)
