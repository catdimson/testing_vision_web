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
    fieldsets = (
        ('Шапка', {
            'fields': ('logo', 'button_cabinet', 'link_button_cabinet',
                        ('menu_item1', 'menu_item2', 'menu_item3', 'menu_item4')),
            'classes': ('collapse', 'collapsed')
        }),
        ('Блок 1', {
            'fields': ('h1_block1', 'text_block1', 'button_1', 'link_button_1', 'button_2', 'link_button_2',
                       'img_block1'),
            'classes': ('collapse', 'collapsed')
        }),
        ('Блок 2', {
            'fields': ('h2_block2', 'text1_block2', 'text2_block2', 'img_block2',
                        ('speech_cloud1', 'speech_cloud2', 'speech_cloud3')),
            'classes': ('collapse', 'collapsed')
        }),
        ('Блок 3', {
            'fields': ('h2_block3', 'h4_block3', 'img_col1', 'text_col1', 'img_col2', 'text_col2', 'img_col3',
                       'text_col3', 'img_col4', 'text_col4'),
            'classes': ('collapse', 'collapsed')
        }),
        ('Блок 4', {
            'fields': ('text_block4', 'img_block4'),
            'classes': ('collapse', 'collapsed')
        }),
        ('Блок 5', {
            'fields': ('h3_block5', ('button_block5', 'link_button_block5')),
            'classes': ('collapse', 'collapsed')
        }),
        ('Блок 6', {
            'fields': ('h2_block6', ('digit_col1', 'desc_col1'), ('digit_col2', 'desc_col2'), ('digit_col3',
                                                                                                'desc_col3'),
                        ('digit_col4', 'desc_col4')),
            'classes': ('collapse', 'collapsed')
        }),
        ('Блок 7', {
            'fields': ('h2_block7', 'text_block7'),
            'classes': ('collapse', 'collapsed')
        })
    )


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('first_last_name', 'email', 'phone')
    readonly_fields = ('first_last_name', 'email', 'phone')


admin.site.register(LandingData, LandingDataAdmin)
admin.site.register(Subscribers, SubscriberAdmin)
