from django.contrib import admin
from .models import Category, Offer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    save_as = True
    fields = ['category', ('name', 'slug'), ('last_name', 'first_name', 'middle_name'), ('email', 'phone'), 'description', 'price', 'image', 'available', ('start_time', 'end_time'), ('created', 'updated')]
    list_display = ['name', 'category', 'start_time', 'end_time', 'available']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}

