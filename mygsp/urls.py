from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mygsp'

urlpatterns = [
    path('', views.offer_list, name='offer_list'),
    path('<slug:category_slug>/', views.offer_list, name='offer_list_by_category'),
    path('<int:id>/<slug:slug>/', views.offer_detail, name='offer_detail'),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
