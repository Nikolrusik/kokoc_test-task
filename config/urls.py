from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls', namespace='authapp')),
    path('mainapp/', include('mainapp.urls', namespace='mainapp')),
    path('shop/', include('shopapp.urls', namespace='shop'))
]
