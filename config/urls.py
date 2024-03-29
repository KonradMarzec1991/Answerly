from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('qanda.urls', namespace='qanda')),
    path('user/', include('user.urls', namespace='user')),
]
