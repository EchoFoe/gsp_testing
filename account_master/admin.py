from django.contrib import admin
from .models import Master


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ['user', 'date_of_birth', 'photo']
    prepopulated_fields = {'slug': ('user',)}
    list_filter = ['available', 'created', 'updated']
