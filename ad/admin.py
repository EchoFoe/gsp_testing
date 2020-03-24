from django.contrib import admin
from .models import Category, SubCategory, Promotion


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ['name', 'slug', 'is_active']
    list_editable = ['is_active']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ['name', 'category', 'is_active']
    list_filter = ['category', 'is_active']
    list_editable = ['is_active']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    save_as = True
    filter_horizontal = ['category']
    fields = ['category', 'subcategory', ('name', 'slug'), ('email', 'phone'), ('country', 'region', 'town'), 'address', 'site', 'description', 'logotype', 'photo', 'is_active', 'paid', ('schedule_start', 'schedule_end'), ('created', 'updated')]
    list_display = ['name', 'Категории', 'subcategory', 'is_active', 'paid']
    list_filter = ['is_active', 'paid', 'category', 'subcategory', 'created', 'updated']
    list_editable = ['is_active', 'paid']
    prepopulated_fields = {'slug': ('name',)}


