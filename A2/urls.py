from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # This makes the home view accessible at the root URL
    path('accounts/', include('accounts.urls')),
    path('banks/', include('banks.urls')),
]





