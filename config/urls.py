from django.contrib import admin
from django.urls import path, include
from trade.views import contact
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('trade.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +\
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
