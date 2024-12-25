from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.urls import path
from .views import qr_code_view

urlpatterns = [
    path('', qr_code_view, name='qr_code_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)