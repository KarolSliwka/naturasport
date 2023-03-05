from django.shortcuts import render
from .models import *


def equipment(request):

    template = 'equipment/index.html'
    context = {
    }

    return render(request, template, context)
