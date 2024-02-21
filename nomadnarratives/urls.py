from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración
    path('', include('pages.urls')),   # URLs de la aplicación "pages"
    

]
