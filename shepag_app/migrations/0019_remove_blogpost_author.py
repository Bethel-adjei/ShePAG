# Generated by Django 5.1.5 on 2025-01-23 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shepag_app', '0018_blogpost_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='author',
        ),
    ]
