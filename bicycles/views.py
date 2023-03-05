from django.shortcuts import render
from .models import *


def bicycles(request):

    template = 'bicycles/index.html'
    context = {
    }

    return render(request, template, context)
