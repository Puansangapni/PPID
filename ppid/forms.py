from django import forms

# --------------------------------------------------------------------- form contact -----------------------------------------------------
# ----------------------------------------------------------------------- komen ------------------------------------------------

from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'Email', 'message'] 
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Masukan Nama Lengkap Anda', 
                'class': 'form-control'
            }),
            'Email': forms.EmailInput(attrs={
                'label' : 'Email',
                'placeholder': 'Masukan Alamat Email Anda', 
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Masukan Pesan Anda', 
                'class': 'form-control'
            }),
        }    

from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'profile_picture']


# --------------------------------------------------- form pengajuan keberatan ------------------------------------------------------------------
# ------------------------------------------------------------- form ----------------------------------------------------------------------------

from .models import PengajuanKeberatan
from datetime import datetime

class PengajuanKeberatanForm(forms.ModelForm):
    class Meta:
        model = PengajuanKeberatan
        fields = ['Nama_Lengkap',
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
                  ] 
        widgets = {
            'Nama_Lengkap': forms.TextInput(attrs={
                'label' : 'Nama Lengkap',
                'placeholder': 'Masukan Nama Lengkap Anda', 
                'class': 'form-control'
            }),
            'kode_permohonan': forms.Select(attrs={'class': 'form-control'}),
            'NIK': forms.TextInput(attrs={
                'label' : 'NIK',
                'placeholder': 'Masukan NIK/No. Identitas Pribadi', 
                'class': 'form-control'
            }),
            'Alamat_Rumah': forms.TextInput(attrs={
                'label' : 'Alamat Rumah',
                'placeholder': 'Masukan Alamat Anda', 
                'class': 'form-control'
            }),
            'Pekerjaan': forms.TextInput(attrs={
                'label' : 'Pekerjaan',
                'placeholder': 'Masukan Pekerjaan Anda', 
                'class': 'form-control'
            }),
            'Email': forms.EmailInput(attrs={
                'label' : 'Email',
                'placeholder': 'Masukan Email Anda', 
                'class': 'form-control'
            }),
            'Nomor_Telepon': forms.TextInput(attrs={
                'label' : 'Nomor Telepon',
                'placeholder': 'Masukan Nomor Telepon Anda', 
                'class': 'form-control'
            }),
            'No_Register_Permintaan': forms.TextInput(attrs={
                'readonly' : 'readonly', 
                'class': 'form-control'
            }),
            'Tujuan_Penggunaan_Informasi': forms.Textarea(attrs={
                'placeholder': 'Masukan Tujuan Penggunaan Informasi', 
                'class': 'form-control'
            }),
            'Alasan_Keberatan': forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-list'}, choices=[
                ('alasan1', 'Permohonan informasi ditolak'),
                ('alasan2', 'Informasi berkala tidak disediakan'),
                ('alasan3', 'Permintaan informasi tidak ditanggapi'),
                ('alasan4', 'Permintaan informasi ditanggapi tidak sebagaimana yang diminta'),
                ('alasan5', 'Permintaan informasi tidak dipenuhi'),
                ('alasan6', 'Biasa yang dikenakan tidak wajar'),
                ('alasan7', 'Informasi disampaikan melampaui jangka waktu yang ditentukan'),
            ]),
            'Kasus_Posisi': forms.Textarea(attrs={
                'placeholder': 'Masukan Kasus Posisi', 
                'class': 'form-control',
                'rows' : 3
            }),
            'Upload_KTP': forms.ClearableFileInput(attrs={
                'label' : 'Upload KTP',
                'class': 'form-control'
            }),
        }    

    def __init__(self, *args, **kwargs):
        super(PengajuanKeberatanForm, self).__init__(*args, **kwargs)
        # Menyesuaikan queryset untuk hanya menampilkan permohonan berstatus 'Ditolak' atau 'Disetujui'
        self.fields['kode_permohonan'].queryset = InformationRequest.objects.filter(
            status__in=['Ditolak', 'Disetujui']  # Memilih status yang relevan
        )

    #  def __init__(self, *args, **kwargs):
    #     super(PengajuanKeberatanForm, self).__init__(*args, **kwargs)
        
    #     # Generate nomor urut dan tahun untuk No_Register_Permintaan
    #     if not self.instance.pk:  # Jika form untuk instance baru
    #         tahun = datetime.now().year
    #         urutan = PengajuanKeberatan.objects.count() + 1  # Menghitung nomor urut
    #         nomor_register = f"{urutan}/reg.keberatan/{tahun}"
    #         self.fields['No_Register_Permintaan'].initial = nomor_register  # Set nomor register ke initial value

# --------------------------------------------- form permohonan informasi -------------------------------------------------------------------------
# ----------------------------------------------------forms.py----------------------------------------------------------------------

from .models import InformationRequest

class PermohonanInformasiForm(forms.ModelForm):
    class Meta:
        model = InformationRequest
        fields = ['Category', 
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
                  'Cara_Mendapatkan_Salinan'
                  ] 
        labels = {
            'Cara_Penyampaian_Permohonan': 'Cara Penyampaian Permohonan *'}
        widgets = {
            'Category': forms.Select(attrs={'class': 'form-control'}),
            'Cara_Penyampaian_Permohonan': forms.Select(attrs={
                'label' : 'Cara Penyampaian Permohonan*',
                'class': 'form-control'}),
            'Nama_Lengkap': forms.TextInput(attrs={
                'label' : 'Nama Lengkap',
                'placeholder': 'Masukan Nama Lengkap Anda', 
                'class': 'form-control'
            }),
            'NIK': forms.TextInput(attrs={
                'label' : 'NIK',
                'placeholder': 'Masukan NIK/No. Identitas Pribadi', 
                'class': 'form-control'
            }),
            'Alamat_Rumah': forms.Textarea(attrs={
                'label' : 'Alamat Rumah',
                'placeholder': 'Masukan Alamat Rmah Anda', 
                'class': 'form-control',
                'rows': 3
            }),
            'Nomor_Telepon': forms.TextInput(attrs={
                'placeholder': 'Masukan Nomor Telepon Anda', 
                'class': 'form-control'
            }),
            'Email': forms.EmailInput(attrs={
                'placeholder': 'Masukan Email Anda', 
                'class': 'form-control'
            }),
            'Pekerjaan': forms.TextInput(attrs={
                'placeholder': 'Masukan Pekerjaan Anda', 
                'class': 'form-control'
            }),
            'Alamat_Kantor': forms.Textarea(attrs={
                'placeholder': 'Masukan Alamat Kantor Anda', 
                'class': 'form-control',
                'rows': 3
            }),
            'Upload_KTP': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'Rincian_Informasi': forms.Textarea(attrs={
                'placeholder': 'Masukan Rincian Informasi', 
                'class': 'form-control'
            }),
            'Tujuan_Penggunaan': forms.Textarea(attrs={
                'placeholder': 'Masukan Tujuan Penggunaan Informasi', 
                'class': 'form-control'
            }),
            'Cara_Memperoleh_Informasi': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('lihat/baca/dengar/catat', 'Melihat/membaca/mendengarkan/mencatat'),
                ('hardcopy/softcopy', 'Mendapatkan salinan (Hardcopy/Softcopy)**'),
            ]),
            'Cara_Mendapatkan_Salinan': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('pickup', 'Mengambil Langsung'),
                ('kurir', 'Kurir'),
                ('pos', 'Via Pos'),
                ('Email', 'Email'),
                ('fax', 'Faksimili'),
            ]),
        }    

# --------------------------------------------------- cek informasi ------------------------------------------------------
# ------------------------------------------------------- forms -------------------------------------------------------

class CekInformasiForm(forms.Form):
    NIK = forms.CharField(
        label='NIK/No. Identitas Pribadi',
        max_length=16,
        widget=forms.TextInput(attrs={
            'placeholder': 'Masukan NIK/No. Identitas Pribadi',
            'class': 'form-control'
        })
    )
    kode_permohonan = forms.CharField(
        label='Kode Permohonan',
        max_length=30,
         widget=forms.TextInput(attrs={
            'placeholder': 'Masukan Kode Permohonan',
            'class': 'form-control'
        })
    )

# --------------------------------------------------- cek keberatan ------------------------------------------------------
# ------------------------------------------------------- forms -------------------------------------------------------

class CekKeberatanForm(forms.Form):
    NIK = forms.CharField(
        label='NIK/No. Identitas Pribadi',
        max_length=16,
        widget=forms.TextInput(attrs={
            'placeholder': 'Masukan NIK/No. Identitas Pribadi',
            'class': 'form-control'
        })
    )

    kode_keberatan = forms.CharField(
        label='Kode Keberatan',
        max_length=30,
         widget=forms.TextInput(attrs={
            'placeholder': 'Masukan Kode Keberatan',
            'class': 'form-control'
        })
    )