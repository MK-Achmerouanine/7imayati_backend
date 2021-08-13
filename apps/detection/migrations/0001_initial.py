# Generated by Django 3.2.5 on 2021-08-12 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.UUID('9aee5f25-3033-4ee2-ab41-d21203d67a41'), verbose_name='Slug')),
                ('image', models.ImageField(upload_to='data', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
            ],
            options={
                'verbose_name': 'Picture',
                'verbose_name_plural': 'Pictures',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.UUID('a124b5f2-5bcf-4a33-bcf1-ec23408094ad'), verbose_name='Slug')),
                ('cin', models.CharField(max_length=50, verbose_name='CIN')),
                ('firstname', models.CharField(max_length=150, verbose_name='Firstname')),
                ('lastname', models.CharField(max_length=150, verbose_name='Lastname')),
                ('image', models.ImageField(blank=True, max_length=150, null=True, upload_to='detection', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
    ]