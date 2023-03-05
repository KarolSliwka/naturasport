from django.shortcuts import render
from .models import *


def reservation(request):

    template = 'reservation/index.html'
    context = {
    }

    return render(request, template, context)
