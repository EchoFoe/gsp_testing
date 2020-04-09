from django.contrib import admin
import mptt.admin
from .models import Category, Offer


admin.site.register(Category, mptt.admin.DraggableMPTTAdmin,
                    list_display=('tree_actions', 'indented_title', 'name', 'parent',),
                    list_display_links=('indented_title',),
                    list_filter=(('parent', mptt.admin.TreeRelatedFieldListFilter),),
                    prepopulated_fields={'slug': ('name', )}
                    )


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    save_as = True
    filter_horizontal = ['category']
    fields = ['category', ('name', 'slug'), ('last_name', 'first_name', 'middle_name'), ('email', 'phone'), 'description', 'price', 'image', 'available', ('start_time', 'end_time'), ('created', 'updated')]
    list_display = ['name', 'Категории', 'start_time', 'end_time', 'available']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}

