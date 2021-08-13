from django.contrib import admin
from .models import User    
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_filter = ('is_staff', 'is_superuser')
    
#admin.site.unregister(User) 
admin.site.register(User, UserAdmin)