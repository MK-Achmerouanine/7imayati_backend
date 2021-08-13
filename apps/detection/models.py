from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver


def upload_avatar_path(instance, filename):
    import os
    name, extension = os.path.splitext(filename)
    return "detection/{f}{fn}".format(f=instance.slug, fn=extension)


class Person(models.Model):
    slug = models.SlugField(_("Slug"), default=uuid.uuid4())
    firstname = models.CharField(_("Firstname"), max_length=150)
    lastname = models.CharField(_("Lastname"), max_length=150)
    image = models.ImageField(
        _("Image"), upload_to=upload_avatar_path, max_length=150,  null=True, blank=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    user = models.ForeignKey("accounts.User", verbose_name=_(
        "User"), on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")

    def __str__(self):
        return f'{self.slug} : {self.firstname} {self.lastname}'


@receiver(post_save, sender=Person)
def push_img_to_firebase(sender, instance, created, **kwargs):
    if created:
        slug = instance.slug
        img = instance.image

        print(img)

        import pyrebase, os
        config = {

            "apiKey": "AIzaSyAlQHZXApzwLxNXSpudYY0907hfcgEznPk",
            "authDomain": "smartcity-d01f1.firebaseapp.com",
            "databaseURL": "gs://smartcity-d01f1.appspot.com",
            " projectId": "smartcity-d01f1",
            "storageBucket": "smartcity-d01f1.appspot.com",
            "messagingSenderId": "956757560056",
            "appId": "1:956757560056:web:32b28ba601bcf8ea6b890d",
            "measurementId": "G-GLZ0H5GKBM",

        }
        firebasestorage = pyrebase.initialize_app(config)
        storage = firebasestorage.storage()
        from django.conf import settings
        storage.child(os.path.basename(img.url)).put(f'{settings.MEDIA_ROOT}\\detection\\{os.path.basename(img.url)}')


def nameFile(instance, filename):
    return '/'.join(['data', str(instance), filename])


class Picture(models.Model):
    slug = models.SlugField(_("Slug"), default=uuid.uuid4())

    image = models.ImageField(_("Image"), upload_to="data")

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified at"), auto_now=True)

    class Meta:
        verbose_name = _("Picture")
        verbose_name_plural = _("Pictures")

    def __str__(self):
        return self.image.url
