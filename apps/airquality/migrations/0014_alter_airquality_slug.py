# Generated by Django 3.2.5 on 2021-08-12 15:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('airquality', '0013_alter_airquality_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airquality',
            name='slug',
            field=models.SlugField(default=uuid.UUID('a02fb5fb-9241-4578-9e75-33b03286440f'), verbose_name='Slug'),
        ),
    ]