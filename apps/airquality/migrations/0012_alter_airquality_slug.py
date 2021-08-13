# Generated by Django 3.2.5 on 2021-08-12 15:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('airquality', '0011_alter_airquality_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airquality',
            name='slug',
            field=models.SlugField(default=uuid.UUID('b79209bd-bb78-4804-82fc-82c16c879451'), verbose_name='Slug'),
        ),
    ]
