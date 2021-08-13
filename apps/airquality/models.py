from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

class AirQuality(models.Model):
    slug = models.SlugField(_("Slug"), default=uuid.uuid4())

    longitude = models.CharField(_("Longitude"), max_length=150, null=True, blank=True)
    latitude = models.CharField(_("Latitude"), max_length=150, null=True, blank=True)

    aq = models.CharField(_("Air Quality (%)"), max_length=50)
    co = models.CharField(_("Carbon monoxide (ppm)"), max_length=50)
    h = models.CharField(_("Hydrogene"), max_length=50)
    lpg = models.CharField(_("LPG (ppm)"), max_length=50)
    t = models.CharField(_("Temperature (°)"), max_length=50)
    smoke = models.CharField(_("Smoke (ppm)"), max_length=50)

    modified_at = models.DateTimeField(_("Modified at"), auto_now=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Air Quality")
        verbose_name_plural = _("Air Qualities")

    def __str__(self):
        return f'[{self.longitude},{self.latitude}] : {self.aq} %' 

