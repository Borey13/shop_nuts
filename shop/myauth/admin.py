from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'mobile', 'city', 'created']
    list_filter = ['city']


admin.site.register(Profile, ProfileAdmin)
