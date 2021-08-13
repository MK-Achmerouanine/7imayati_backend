# Generated by Django 3.2.5 on 2021-08-12 15:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('airquality', '0006_alter_airquality_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airquality',
            name='slug',
            field=models.SlugField(default=uuid.UUID('2c3ef9a3-cd0d-447e-b5ed-227bb47efde5'), verbose_name='Slug'),
        ),
    ]
