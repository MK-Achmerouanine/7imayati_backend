from django.contrib import admin
from .models import Person, Picture
from django.utils.html import format_html


class PersonAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'slug','firstname', 'lastname', 'created_at',)
    search_fields = ('slug', 'firstname', 'lastname',)

    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.image.url))

    image_tag.short_description = 'Image'


admin.site.register(Person, PersonAdmin)


class PictureAdmin(admin.ModelAdmin):
    list_display = ('image', 'created_at',)

    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag']
    readonly_fields = ['image_tag']


admin.site.register(Picture, PictureAdmin)
