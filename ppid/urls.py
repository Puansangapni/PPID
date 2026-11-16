from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('custom-admin/', include('custom_admin.urls')),
    path('', views.home, name='home'),
    path('upload/', views.upload_content, name='upload_content'),
    path('contact/', views.contact, name='contact'),
    path('pengajuan-keberatan/', views.pengajuan_keberatan, name='pengajuan_keberatan'),
    path('permohonan-informasi/', views.permohonan_informasi, name='permohonan_informasi'),
    path('success/', views.success, name='success'),
    path('cek-informasi/', views.cek_informasi, name='cek_informasi'),
    path('cek-keberatan/', views.cek_keberatan_view, name='cek_keberatan'),
    path('statistics/', views.statistics, name='statistics'),
    path('informasi-berkala/', views.informasi_berkala, name='informasi_berkala'),
    path('informasi-publik/', views.informasi_publik, name='informasi_publik'),
]

LOGIN_URL = '/admin/login/'  # or wherever your login page is

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
