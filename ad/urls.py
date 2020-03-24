from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ad'

urlpatterns = [
    path('', views.promotion_list, name='promotion_list'),
    path('<slug:category_slug>/', views.promotion_list, name='promotion_list_by_category'),
    path('<slug:subcategory_slug>/', views.promotion_list, name='promotion_list_by_subcategory'),
    path('<int:id>/<slug:slug>/', views.promotion_detail, name='promotion_detail'),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
