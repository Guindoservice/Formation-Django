# urls de l'aplication

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', include('Produits.urls'))

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))