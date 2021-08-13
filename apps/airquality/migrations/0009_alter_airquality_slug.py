# Generated by Django 3.2.5 on 2021-08-12 15:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('airquality', '0008_alter_airquality_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airquality',
            name='slug',
            field=models.SlugField(default=uuid.UUID('7a1b0de6-6bcb-4c43-8437-ceab98ec1e6b'), verbose_name='Slug'),
        ),
    ]
