from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin

from .models import LandingData, Subscribers


class LandingDataAdminForm(forms.ModelForm):
    # добавляем ckeditor в нашу форму в админке
    h1_block1 = forms.CharField(label="Заголовок h1", widget=CKEditorWidget())
    text2_block2 = forms.CharField(label="Текст 2", widget=CKEditorWidget())
    h4_block3 = forms.CharField(label="Подзаголовок (h4)", widget=CKEditorWidget())
    text_block4 = forms.CharField(label="Текст на голубом фоне", widget=CKEditorWidget())
    text_block7 = forms.CharField(label="Текст в форме", widget=CKEditorWidget())

    class Meta:
        model = LandingData
        fields = '__all__'


class LandingDataAdmin(admin.ModelAdmin):
    form = LandingDataAdminForm


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('first_last_name', 'email', 'phone')
    readonly_fields = ('first_last_name', 'email', 'phone')


admin.site.register(LandingData, LandingDataAdmin)
admin.site.register(Subscribers, SubscriberAdmin)
