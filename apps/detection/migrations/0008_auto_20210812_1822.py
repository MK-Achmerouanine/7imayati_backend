# Generated by Django 3.2.5 on 2021-08-12 16:22

import apps.detection.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0007_auto_20210812_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, max_length=150, null=True, upload_to=apps.detection.models.upload_avatar_path, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(default=uuid.UUID('9bf45b32-960f-473c-80c5-90f3e8471828'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='slug',
            field=models.SlugField(default=uuid.UUID('de32558c-033d-4ab9-9374-62c2f03d93ca'), verbose_name='Slug'),
        ),
    ]