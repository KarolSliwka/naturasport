from django.shortcuts import render
from .models import *


def contact(request):

    template = 'contact/index.html'
    context = {
    }

    return render(request, template, context)
