
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('foodadmin/', admin.site.urls),
    
    path('', include('foodie.urls')),
    path('shopcart/', include('shopcart.urls')),
    path('userprofile', include('userprofile.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)