# Generated by Django 5.1.1 on 2024-11-12 13:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shepag_app', '0015_remove_newsletter_message_newsletter_content'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='subject',
        ),
        migrations.AddField(
            model_name='newsletter',
            name='recipients',
            field=models.ManyToManyField(related_name='newsletters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='title',
            field=models.CharField(default='No Title', max_length=200),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='content',
            field=models.TextField(),
        ),
    ]