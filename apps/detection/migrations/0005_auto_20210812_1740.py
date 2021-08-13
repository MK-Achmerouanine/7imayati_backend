# Generated by Django 3.2.5 on 2021-08-12 15:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0004_auto_20210812_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(default=uuid.UUID('bbad94ea-2a51-44b6-9626-6ce5bb12ce1a'), verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='slug',
            field=models.SlugField(default=uuid.UUID('a1fbabf6-4a8b-4532-bb4f-813b657903b7'), verbose_name='Slug'),
        ),
    ]
