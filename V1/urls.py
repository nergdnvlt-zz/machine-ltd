from django.contrib import admin
from django.urls import path, include
from V1.views import SessionViews

urlpatterns = [
    path('devices/', include('V1.devices.urls')),
    path('users/', include('V1.users.urls')),
    path('locations/', include('V1.locations.urls')),
    path('sessions/', SessionViews.as_view({
        'post': 'create',
    })),
]
