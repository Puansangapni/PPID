from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# ------------------------------------------------------ content ------------------------------------------------------
# ------------------------------------------------------- views -------------------------------------------------------

class Content(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/')
    upload_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super().delete(*args, **kwargs)

# ------------------------------------------------------ contact ------------------------------------------------------
# ------------------------------------------------------- views -------------------------------------------------------

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    Email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/')  # Image upload directory

    def __str__(self):
        return self.name

# ------------------------------------------------ model information request ----------------------------------------------
# --------------------------------------------------------- models --------------------------------------------------------

import uuid
import random
import string
from django.core.mail import send_mail

class InformationRequest(models.Model):
    # jumlah_permohonan = models.IntegerField(default=0)

    STATUS_CHOICES = [
        ('Diterima', 'Diterima'),
        ('Dalam Proses', 'Dalam Proses'),
        ('Disetujui', 'Disetujui'),
        ('Ditolak', 'Ditolak'),
    ]

    mendapatkan_informasi_choices = [
        ('lihat/baca/dengar/catat', 'Melihat/membaca/mendengarkan/mencatat'),
        ('hardcopy/softcopy', 'Mendapatkan salinan (Hardcopy/Softcopy)**'),
    ]

    mendapatkan_salinan_choices = [
        ('pickup', 'Mengambil Langsung'),
        ('kurir', 'Kurir'),
        ('pos', 'Via Pos'),
        ('email', 'Email'),
        ('fax', 'Faksimili'),
    ]

    penyampaian_informasi_choices = [
        ('langsung', 'Langsung'),
        ('website', 'Website'),
        ('email', 'Email'),
        ('fax', 'Fax'),
        ('pos', 'Via Pos'),
    ]

    kode_permohonan = models.CharField(max_length=6, blank=True, null=True)

    Category = models.CharField(max_length=100, choices=[
        ('perorangan', 'Perorangan'),
        ('badan_hukum', 'Badan Hukum'),
    ])
    Cara_Penyampaian_Permohonan = models.CharField(max_length=50, choices=penyampaian_informasi_choices)
    Nama_Lengkap = models.CharField(max_length=100)
    NIK = models.CharField(max_length=16)
    Alamat_Rumah = models.TextField()
    Nomor_Telepon = models.CharField(max_length=15)
    Email = models.EmailField()
    Pekerjaan = models.CharField(max_length=100)
    Alamat_Kantor = models.TextField()
    Upload_KTP = models.FileField(upload_to='KTP_Permohonan/', blank=True, null=True)
    Rincian_Informasi = models.TextField()
    Tujuan_Penggunaan = models.TextField()
    Cara_Memperoleh_Informasi = models.CharField(max_length=50, choices=mendapatkan_informasi_choices)
    Cara_Mendapatkan_Salinan = models.CharField(max_length=50, choices=mendapatkan_salinan_choices)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Submitted')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.kode_permohonan:
            self.kode_permohonan = self.generate_unique_code()
            super().save(*args, **kwargs)  # Save first to generate ID
            self.send_confirmation_email()  # Send email after saving
        else:
            super().save(*args, **kwargs)

    def generate_unique_code(self):
        # Generate a 6-character alphanumeric code
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        # Ensure the code is unique
        while InformationRequest.objects.filter(kode_permohonan=code).exists():
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return code

    def send_confirmation_email(self):
        subject = 'Konfirmasi Permohonan Informasi Publik'
        message = f'Yth. {self.Nama_Lengkap},\n\n' \
                  f'Terima kasih telah mengajukan permohonan. Kode permohonan Anda adalah: {self.kode_permohonan}.\n\n' \
                  f'Silakan gunakan kode ini untuk mengecek status permohonan Anda.\n\n' \
                  f'Salam,\nPPID BPPW Sulawesi Utara'
        recipient_list = [self.Email]
        send_mail(subject, message, 'BPPW SULUT <puansangapni@gmail.com>', recipient_list)

    # def __str__(self):
    #     return self.Nama_Lengkap
    
    # def __str__(self):
    #     return self.kode_permohonan


    def delete(self, *args, **kwargs):
        if self.Upload_KTP:
            if os.path.isfile(self.Upload_KTP.path):
                os.remove(self.Upload_KTP.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Keberatan by {self.Nama_Lengkap} for {self.kode_permohonan}"

# ----------------------------------------------- model pengajuan keberatan ------------------------------------------------------
# --------------------------------------------------------- models ---------------------------------------------------------------

from multiselectfield import MultiSelectField 
from datetime import datetime

class PengajuanKeberatan(models.Model):
    # jumlah_pengajuan = models.IntegerField(default=0)

    STATUS_CHOICES = [
        ('Diterima', 'Diterima'),
        ('Dalam Proses', 'Dalam Proses'),
        ('Disetujui', 'Disetujui'),
        ('Ditolak', 'Ditolak'),
    ]

    alasan_choices = [
        ('alasan1', 'Permohonan informasi ditolak'),
        ('alasan2', 'Informasi berkala tidak disediakan'),
        ('alasan3', 'Permintaan informasi tidak ditanggapi'),
        ('alasan4', 'Permintaan informasi ditanggapi tidak sebagaimana yang diminta'),
        ('alasan5', 'Permintaan informasi tidak dipenuhi'),
        ('alasan6', 'Biaya yang dikenakan tidak wajar'),
        ('alasan7', 'Informasi disampaikan melampaui jangka waktu yang ditentukan'),
    ]

    kode_permohonan = models.ForeignKey(InformationRequest, on_delete=models.CASCADE)
    kode_keberatan = models.CharField(max_length=6, blank=True, null=True)
    Nama_Lengkap = models.CharField(max_length=16)
    NIK = models.CharField(max_length=16)
    Alamat_Rumah = models.CharField(max_length=100)
    Pekerjaan = models.CharField(max_length=100)
    Email = models.EmailField()
    Nomor_Telepon = models.CharField(max_length=13)
    No_Register_Permintaan = models.CharField(max_length=200)
    Tujuan_Penggunaan_Informasi = models.TextField()
    Alasan_Keberatan = MultiSelectField(max_length=100, choices=alasan_choices)
    Kasus_Posisi = models.TextField()
    Upload_KTP = models.FileField(upload_to='KTP_Keberatan/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Submitted')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.No_Register_Permintaan:
            tahun = datetime.now().year
            urutan = PengajuanKeberatan.objects.count() + 1
            Nomor_Register = f"{urutan}/reg.keberatan/{tahun}"
            self.fields['No_Register_Permintaan'].initial = Nomor_Register
        super().save(*args, **kwargs)
        
        if not self.kode_keberatan:
            self.kode_keberatan = self.generate_unique_code()
            super().save(*args, **kwargs)
            self.send_confirmation_email()

        else:
            super().save(*args, **kwargs)

    def generate_unique_code(self):
        # Generate a 6-character alphanumeric code
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        # Ensure the code is unique
        while PengajuanKeberatan.objects.filter(kode_keberatan=code).exists():
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return code

    def send_confirmation_email(self):
        subject = 'Konfirmasi Pengajuan Keberatan Informasi Publik'
        message = f'Yth. {self.Nama_Lengkap},\n\n' \
                  f'Terima kasih telah mengajukan pengajuan. Kode keberatan Anda adalah: {self.kode_keberatan}.\n\n' \
                  f'Silakan gunakan kode ini untuk mengecek status pengajuan Anda.\n\n' \
                  f'Salam,\nPPID BPPW Sulawesi Utara'
        recipient_list = [self.Email]
        send_mail(subject, message, 'BPPW SULUT <puansangapni@gmail.com>', recipient_list)

    # def __str__(self):
    #     return self.Nama_Lengkap

    def delete(self, *args, **kwargs):
        if self.Upload_KTP:
            if os.path.isfile(self.Upload_KTP.path):
                os.remove(self.Upload_KTP.path)
        super().delete(*args, **kwargs)

    # def __str__(self):
    #     return self.kode_permohonan
    
    def __str__(self):
        return f"Keberatan by {self.Nama_Lengkap} for {self.kode_permohonan}"
    
# ------------------------------------------------- model Banner Images ----------------------------------------------------------
# ----------------------------------------------------------model -----------------------------------------------------------------

class BannerImage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='banner_images/')
    is_active = models.BooleanField(default=True)  # To activate or deactivate the image

    def __str__(self):
        return self.title if self.title else "Untitled"

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)


# ----------------------------------------------- model informasi publik ----------------------------------------------------------
# ----------------------------------------------------------model -----------------------------------------------------------------

import os

class InformasiBerkala(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='file_informasi_berkala/')
    category = models.CharField(max_length=100)  # For grouping purposes, e.g., "Informasi Profil", "Ringkasan Program"
    
    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super().delete(*args, **kwargs)


class InformasiPublik(models.Model):
    title = models.CharField(max_length=200)
    kode = models.CharField(max_length=6, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='file_informasi_publik/')
    
    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super().delete(*args, **kwargs)