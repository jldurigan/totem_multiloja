from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente', include('totem_cliente.urls')),
    path('restaurante/', include('totem_restaurante.urls'))
]
