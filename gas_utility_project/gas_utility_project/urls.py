from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gas_utility/', include('gas_utility_app.urls')),  # Include the app's URLs
]
