# Generated by Django 5.1.1 on 2024-10-04 13:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shepag_app', '0011_blogpost_image_blogpost_reading_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='sent_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
