from datetime import datetime


def FooterContext(request):

    currentYear = datetime.now().year

    context = {
        'currentYear': currentYear,
    }

    return context
