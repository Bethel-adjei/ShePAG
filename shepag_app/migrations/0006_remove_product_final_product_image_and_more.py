# Generated by Django 5.1.1 on 2024-09-28 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shepag_app', '0005_product_final_product_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='final_product_image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='processing_stage_image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='raw_material_image',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
