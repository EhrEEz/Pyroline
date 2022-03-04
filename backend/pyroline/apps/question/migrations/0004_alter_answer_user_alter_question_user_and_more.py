# Generated by Django 4.0.1 on 2022-02-06 13:38

import apps.question.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0003_remove_historicalquestion_chapter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=models.SET(apps.question.models.GET_DELETED_USER), to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(on_delete=models.SET(apps.question.models.GET_DELETED_USER), to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='questionpaper',
            name='user',
            field=models.ForeignKey(on_delete=models.SET(apps.question.models.GET_DELETED_USER), to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='questionsetter',
            name='user',
            field=models.ForeignKey(on_delete=models.SET(apps.question.models.GET_DELETED_USER), to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
