from django.shortcuts import render

def base_view(request):
    context = {
        'name': 'Дмитрий',
        'info': 'Hello world!'
    }
    return render(request, 'index.html', context=context)