from django.shortcuts import render
from .models import LandingData

def base_view(request):
    content = LandingData.objects.last()
    context = {
        'data': content,
    }
    return render(request, 'base.html', context=context)