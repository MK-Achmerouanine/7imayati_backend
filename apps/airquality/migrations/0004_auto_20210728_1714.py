# Generated by Django 3.2.5 on 2021-07-28 15:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('airquality', '0003_alter_airquality_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airquality',
            name='latitude',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='airquality',
            name='slug',
            field=models.SlugField(default=uuid.UUID('c79e01f1-ee96-40c7-b38f-5c2c3192b120'), verbose_name='Slug'),
        ),
    ]
