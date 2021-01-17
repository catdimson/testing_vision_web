# from django.forms import ModelForm
#
# from .models import Subscribers
#
#
# class SubscribersForm(ModelForm):
#     class Meta:
#         model = Subscribers
#         fields = '__all__'
from django import forms

class SubscribersForm(forms.Form):
    first_last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.CharField(max_length=13)
