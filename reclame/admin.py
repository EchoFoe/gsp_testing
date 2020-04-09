from django.contrib import admin
import mptt.admin
from reclame.models import Category, Promotion, PromotionDetails


class PromotionDetailsInline(admin.TabularInline):
    model = PromotionDetails
    extra = 0


admin.site.register(Category, mptt.admin.DraggableMPTTAdmin,
                    list_display=('tree_actions', 'indented_title', 'name', 'parent',),
                    list_display_links=('indented_title',),
                    list_filter=(('parent', mptt.admin.TreeRelatedFieldListFilter),),
                    prepopulated_fields={'slug': ('name', )}
                    )


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    save_as = True
    filter_horizontal = ['category']
    fields = ['category', ('name', 'slug'), 'email', ('country', 'region', 'town'), 'site', 'description', 'logotype', 'photo', 'is_active', 'paid', ('created', 'updated')]
    list_display = ['name', 'is_active']
    inlines = [PromotionDetailsInline]
    list_filter = ['category', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(PromotionDetails)
class PromotionDetailsAdmin(admin.ModelAdmin):
    save_as = True
    fields = ['promotion', ('is_main', 'is_not_main', 'is_active'), 'address', 'phone', ('schedule_start', 'schedule_end'), ('weekend_start', 'weekend_end'), ('weekend2_start', 'weekend2_end'), ('dinner_time_start', 'dinner_time_end'), ('created', 'updated')]
    list_display = ['promotion', 'is_main', 'is_not_main', 'is_active']
    list_filter = ['promotion', 'is_main', 'is_not_main', 'is_active']
    list_editable = ['is_main', 'is_not_main', 'is_active']
