# Generated by Django 3.2.5 on 2021-08-12 15:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('airquality', '0007_alter_airquality_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airquality',
            name='slug',
            field=models.SlugField(default=uuid.UUID('1cab8cea-858a-4a79-8c38-ec444db49f6c'), verbose_name='Slug'),
        ),
    ]
