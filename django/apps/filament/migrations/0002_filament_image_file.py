# Generated by Django 2.2 on 2019-11-16 17:16

from django.db import migrations, models
import filament.models


class Migration(migrations.Migration):

    dependencies = [
        ('filament', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filament',
            name='image_file',
            field=models.ImageField(null=True, upload_to=filament.models.get_filament_image_upload_path),
        ),
    ]
