from django.shortcuts import render
from .models import *


def offer(request):

    template = 'offer/index.html'
    context = {
    }

    return render(request, template, context)
