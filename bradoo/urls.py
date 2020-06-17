from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('bradoo.core.urls')),
    path('admin/', admin.site.urls),
]
