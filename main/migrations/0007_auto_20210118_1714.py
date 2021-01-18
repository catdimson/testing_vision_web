# Generated by Django 3.1.5 on 2021-01-18 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_auto_20210117_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingdata',
            name='desc_col2',
            field=models.TextField(default='уроков с заданиями в форме видеолекций и квестов', max_length=120, verbose_name='Текст под числом колонки 2'),
        ),
        migrations.AlterField(
            model_name='landingdata',
            name='desc_col3',
            field=models.TextField(default='минут среднее время прохождения урока', max_length=120, verbose_name='Текст под числом колонки 3'),
        ),
        migrations.AlterField(
            model_name='landingdata',
            name='desc_col4',
            field=models.TextField(default='онлайн-квеста в Zoom с кураторами и однокурсниками', max_length=120, verbose_name='Текст под числом колонки 4'),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
