from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ppid.models import InformationRequest
from ppid.models import ContactSubmission
from ppid.models import PengajuanKeberatan
from django.contrib.auth.decorators import login_required
from django.db import models

# Create your views here.

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

@login_required
def dashboard(request):
    total_permohonan = InformationRequest.objects.count()
    total_pengajuan = PengajuanKeberatan.objects.count()
    # user_registrations = UserRegistrations.objects.count()
    # unique_visitors = UniqueVisitors.objects.count()

    context = {
        'total_permohonan': total_permohonan,
        'total_pengajuan': total_pengajuan,
        # 'user_registrations': user_registrations,
        # 'unique_visitors': unique_visitors,
    }
    return render(request, 'custom_admin/dashboard.html', context)

class CustomLoginView(LoginView):
    template_name = 'Login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        # Redirect to the custom dashboard after successful login
        return reverse_lazy('custom_admin:dashboard')

def total_permohonan(request):
    totals = InformationRequest.objects.all().order_by('-submitted_at')
    return render(request, 'custom_admin/total_permohonan.html', {'totals' : totals})

def data_contact(request):
    contacts =ContactSubmission.objects.all().order_by('-submitted_at')
    return render(request, 'custom_admin/contact.html', {'contacts' : contacts})

def update_status(request, id):
    total = get_object_or_404(InformationRequest, id=id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        total.status = new_status
        total.save()
    return redirect('custom_admin:total_permohonan')

# def update_status(request, id):
#     if request.method == 'POST':
#         permohonan = get_object_or_404(InformationRequest, id=id)
#         new_status = request.POST.get('status')
#         permohonan.status = new_status
#         permohonan.save()
#         return redirect('custom_admin:grouped_by_status')

def status_permohonan(request):
    diterima = InformationRequest.objects.filter(status='Diterima')
    dalam_proses = InformationRequest.objects.filter(status='Dalam Proses')
    disetujui = InformationRequest.objects.filter(status='Disetujui')
    ditolak = InformationRequest.objects.filter(status='Ditolak')

    context = {
        'diterima': diterima,
        'dalam_proses': dalam_proses,
        'disetujui': disetujui,
        'ditolak': ditolak,
    }
    
    return render(request, 'your_template.html', context)
    
def permohonan_diterima(request):
    return render(request, 'custom_admin/permohonan_diterima.html')

def permohonan_ditolak(request):
    return render(request, 'custom_admin/permohonan_ditolak.html')

def total_pengajuan(request):
    alls = PengajuanKeberatan.objects.all().order_by('-submitted_at')
    return render(request, 'custom_admin/total_pengajuan.html', {'alls' : alls})

def perbarui_status(request, id):
    total = get_object_or_404(PengajuanKeberatan, id=id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        total.status = new_status
        total.save()
    return redirect('custom_admin:total_permohonan')


def pengajuan_diterima(request):
    return render(request, 'custom_admin/pengajuan_diterima.html')

def pengajuan_ditolak(request):
    return render(request, 'custom_admin/pengajuan_ditolak.html')

def informasi_berkala(request):
    return render(request, 'custom_admin/informasi_berkala.html')

def permohonan_informasi(request):
    return render(request, 'custom_admin/permohonan_informasi.html')

def upload_banner(request):
    return render(request, 'custom_admin/upload_banner.html')

def login(request):
    return render(request, 'custom_admin/Login.html')











































