from django.shortcuts import render
from .models import *


def kayaking(request):

    template = 'kayaking/index.html'
    context = {
    }

    return render(request, template, context)
