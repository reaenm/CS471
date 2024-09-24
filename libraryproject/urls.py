from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include("apps.bookmodule.urls")),  # Include bookmodule URLs
    path('users/', include("apps.usermodule.urls")),  # Include usermodule URLs
]
