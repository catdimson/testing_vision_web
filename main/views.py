from django.shortcuts import render

from .forms import SubscribersForm
from .models import LandingData, Subscribers
from .handlers import custom_send_mail


def base_view(request):
    content = LandingData.objects.last()
    context = {
        'data': content,
    }

    if request.method == 'POST':
        form = SubscribersForm(request.POST)

        if form.is_valid():
            first_last_name = form.cleaned_data['first_last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            subscriber = Subscribers(first_last_name=first_last_name, email=email, phone=phone)
            subscriber.save()

            custom_send_mail(first_last_name, email, phone)

    return render(request, 'base.html', context=context)
