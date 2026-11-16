from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView

app_name = 'custom_admin'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('total-permohonan/', views.total_permohonan, name='total_permohonan'),
    path('permohonan-diterima/', views.permohonan_diterima, name='permohonan_diterima'),
    path('permohonan-ditolak/', views.permohonan_ditolak, name='permohonan_ditolak'),
    path('update-status/<int:id>/', views.update_status, name='update_status'),
    path('total-pengajuan/', views.total_pengajuan, name='total_pengajuan'),
    path('pengajuan-diterima/', views.pengajuan_diterima, name='pengajuan_diterima'),
    path('pengajuan-ditolak/', views.pengajuan_ditolak, name='pengajuan_ditolak'),
    path('perbarui-status/<int:id>/', views.perbarui_status, name='perbarui_status'),
    path('upload-informasi-berkala/', views.informasi_berkala, name='informasi_berkala'),
    path('upload-permohonan-informasi/', views.permohonan_informasi, name='permohonan_informasi'),
    path('upload-banner/', views.upload_banner, name='upload_banner'),
    path('contact/', views.data_contact, name='data_contact'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]

# LOGIN_URL = '/admin/login/'  # or wherever your login page is

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
