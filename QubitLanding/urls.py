from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from QubitLanding import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('app.urls')),
    path('api/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




