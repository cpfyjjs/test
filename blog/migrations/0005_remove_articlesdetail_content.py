# Generated by Django 2.1.1 on 2018-12-04 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181204_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlesdetail',
            name='content',
        ),
    ]
