from django.contrib import admin
from .models import ContactSubmission
from .models import InformationRequest
# from .models import Content
from .models import PengajuanKeberatan

# Register your models here.

# admin.site.register(Content)

@admin.register(ContactSubmission)
class InformationRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'Email', 'message','submitted_at')
    search_fields = ('name', 'Email')


@admin.register(InformationRequest)
class InformationRequestAdmin(admin.ModelAdmin):
    list_display = ('kode_permohonan', 
                    'Category', 
                    'Cara_Penyampaian_Permohonan',
                    'Nama_Lengkap',
                    'NIK', 
                    'Alamat_Rumah', 
                    'Nomor_Telepon', 
                    'Email', 
                    'Pekerjaan',
                    'Alamat_Kantor',
                    'Upload_KTP', 
                    'Rincian_Informasi',
                    'Tujuan_Penggunaan', 
                    'Cara_Memperoleh_Informasi', 
                    'Cara_Mendapatkan_Salinan', 
                    'status', 
                    'submitted_at'
                    )
    list_filter = ('status', 'submitted_at')
    search_fields = ('Nama_Lengkap', 'NIK', 'Email', 'kode_permohonan')
    ordering = ('-submitted_at',)
    list_editable = ('status',)  # Make the status field editable in the list view

# admin.site.register(InformationRequest, InformationRequestAdmin)

@admin.register(PengajuanKeberatan)
class PengajuanKeberatanAdmin(admin.ModelAdmin):
    list_display = ('kode_keberatan',
                    'Nama_Lengkap', 
                    'kode_permohonan', 
                    'NIK', 
                    'Alamat_Rumah',
                    'Pekerjaan',
                    'Email',
                    'Nomor_Telepon',
                    'No_Register_Permintaan',  
                    'Tujuan_Penggunaan_Informasi', 
                    'Alasan_Keberatan', 
                    'Kasus_Posisi',  
                    'Upload_KTP',
                    'status', 
                    'submitted_at')
    list_filter = ('status', 'submitted_at')
    search_fields = ('Nama_Lengkap','NIK', 'Email', 
                     'No_Register_Permintaan', 'kode_keberatan', 'kode_permohonan')
    ordering = ('-submitted_at',)
    list_editable = ('status',)

from .models import BannerImage

@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'image')
    list_filter = ('is_active',)

from .models import InformasiBerkala

class InformasiBerkalaAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'file')
    search_fields = ('title', 'category')

admin.site.register(InformasiBerkala, InformasiBerkalaAdmin)

from .models import InformasiPublik

class InformasiPublikAdmin(admin.ModelAdmin):
    list_display = ('title', 'kode', 'file')
    search_fields = ('title', 'kode')

admin.site.register(InformasiPublik, InformasiPublikAdmin)