from django.contrib import admin
from .models import AirQuality

class AirQualityAdmin(admin.ModelAdmin):
    list_display = ('longitude', 'latitude', 'aq', 'co','h', 'lpg','t','smoke', )
admin.site.register(AirQuality, AirQualityAdmin)
