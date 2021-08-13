# Generated by Django 3.2.5 on 2021-07-28 12:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('airquality', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='airquality',
            options={'verbose_name': 'Air Quality', 'verbose_name_plural': 'Air Qualities'},
        ),
        migrations.AlterField(
            model_name='airquality',
            name='slug',
            field=models.SlugField(default=uuid.UUID('64b56ecf-bc37-4f67-85fd-8e181c99f4cd'), verbose_name='Slug'),
        ),
    ]
