from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

api_patterns = [
    path('products/', include('products.urls')),
    path('users/', include('account.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(api_patterns))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

