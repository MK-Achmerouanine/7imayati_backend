# Generated by Django 3.2.5 on 2021-08-12 15:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('airquality', '0005_alter_airquality_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airquality',
            name='slug',
            field=models.SlugField(default=uuid.UUID('68c39269-8542-4e10-a063-a76978a8687e'), verbose_name='Slug'),
        ),
    ]