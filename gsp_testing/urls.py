from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account_master/', include('account_master.urls')),
    # path('ad/', include('ad.urls', namespace='ad')),
    path('promotions/', include('reclame.urls', namespace='promotions')),
    path('', include('job.urls', namespace='job')),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
