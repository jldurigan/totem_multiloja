from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('totem_cliente.urls')),
    path('cliente/', include('totem_cliente.urls')),
    path('restaurante/', include('totem_restaurante.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
