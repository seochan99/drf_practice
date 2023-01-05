from django.contrib import admin
from django.urls import path, include

# 미디어를 위한 import
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
