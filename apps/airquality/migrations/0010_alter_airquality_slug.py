# Generated by Django 3.2.5 on 2021-08-12 15:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('airquality', '0009_alter_airquality_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airquality',
            name='slug',
            field=models.SlugField(default=uuid.UUID('bfb2499a-ceae-4f1a-b1a2-e21265709094'), verbose_name='Slug'),
        ),
    ]
