# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import UserProfileForm
from .models import Content, BannerImage

def home(request):
    contents = Content.objects.all()
    banner_images = BannerImage.objects.filter(is_active=True)
    return render(request, 'ppid/home.html', {'contents': contents, 'banner_images': banner_images})

def base(request):
    contents = Content.objects.all()
    return render(request, 'admin/base_site.html', {'contents': contents})

# --------------------------------------------------- upload content --------------------------------------------------
# ------------------------------------------------------- views -------------------------------------------------------

@login_required
def upload_content(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        file = request.FILES['file']
        content = Content(title=title, description=description, file=file, uploaded_by=request.user)
        content.save()
        return redirect('base_site')
    return render(request, 'admin/upload.html')
 
# ------------------------------------------------------ contact ------------------------------------------------------
# ------------------------------------------------------- views -------------------------------------------------------

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect or render a success page
    else:
        form = ContactForm()
    
    return render(request, 'ppid/contact.html', {'form': form})

# ------------------------------------------------------ success ------------------------------------------------------
# ------------------------------------------------------- views -------------------------------------------------------

def success(request):
    return render(request, 'ppid/success.html')

def upload_profile_picture(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_success')
    else:
        form = UserProfileForm()
    return render(request, 'ppid/upload.html', {'form': form})


# ----------------------------------------------- pengajuan keberatan ------------------------------------------------------
# ------------------------------------------------------- views ------------------------------------------------------------

from .forms import PengajuanKeberatanForm
from django.utils import timezone

def pengajuan_keberatan(request):
    if request.method == 'POST':
        form = PengajuanKeberatanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Handle form processing here
            return redirect('success')  # Redirect or render a success page
    else:
        # Generate nomor register otomatis
        current_year = timezone.now().year
        nomor_urut = PengajuanKeberatan.objects.count() + 1
        initial_data = {
            'No_Register_Permintaan': f"{nomor_urut}/reg.keberatan/{current_year}"
        }
        form = PengajuanKeberatanForm(initial=initial_data)

    return render(request, 'ppid/pengajuan_keberatan.html', {'form': form})

# ----------------------------------------- form permohonan informasi ------------------------------------------------------------------
# ----------------------------------------------------- views --------------------------------------------------------------------------

from .forms import PermohonanInformasiForm

def permohonan_informasi(request):
    if request.method == 'POST':
        form = PermohonanInformasiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Handle form submission, save data, or send an email, etc.
            return redirect('success')  # Redirect or render a success page
    else:
        form = PermohonanInformasiForm()
    
    return render(request, 'ppid/permohonan_informasi.html', {'form': form})


# ----------------------------------------------------- statistics ------------------------------------------------------
# ------------------------------------------------------- views ---------------------------------------------------------

from .models import InformationRequest

def statistics(request):
    # Aggregate counts
    total_information = InformationRequest.objects.count()
    total_requests = InformationRequest.objects.filter(status='Terkirim').count()
    Approved_requests = InformationRequest.objects.filter(status='Disetujui').count()
    Objections_requests = InformationRequest.objects.filter(status='Ditolak').count()
    total_objections = PengajuanKeberatan.objects.count()
    Approved_objections = InformationRequest.objects.filter(status='Disetujui').count()
    Objections_objections = InformationRequest.objects.filter(status='Ditolak').count()


    context = {
        'total_information': total_information,
        'total_requests': total_requests,
        'Approved_requests': Approved_requests,
        'Objections_requests': Objections_requests,
        'total_objections': total_objections,
        'Approved_objections': Approved_objections,
        'Objections_objections': Objections_objections,
    }
    
    return render(request, 'ppid/statistics.html', context)

# ----------------------------------------- form cek informasi -----------------------------------------------------------------------------
# ----------------------------------------------- views ------------------------------------------------------------------------------------

from .forms import CekInformasiForm 

def cek_informasi(request):
    result = None
    error_message = None
    
    if request.method == 'POST':
        form = CekInformasiForm(request.POST)
        if form.is_valid():
            NIK = form.cleaned_data['NIK']
            kode_permohonan = form.cleaned_data['kode_permohonan']
            
            try:
                # Fetch the record that matches the NIK and kode_permohonan
                result = InformationRequest.objects.get(NIK=NIK, kode_permohonan=kode_permohonan)
            except InformationRequest.DoesNotExist:
                error_message = "Data tidak ditemukan. Periksa kembali NIK dan Kode permohonan Anda."

    else:
        form = CekInformasiForm()
    
    return render(request, 'ppid/cek_informasi.html', {
        'form': form,
        'result': result,
        'error_message': error_message
    })
# ----------------------------------------- form cek keberatan -----------------------------------------------------------------------------
# ------------------------------------------------views.py----------------------------------------------------------------------------------

from .forms import CekKeberatanForm
from .models import PengajuanKeberatan
# from django.core.mail import send_mail

def cek_keberatan_view(request):
    result = None
    error_message = None
    
    if request.method == 'POST':
        form = CekKeberatanForm(request.POST)
        if form.is_valid():
            NIK = form.cleaned_data['NIK']
            kode_keberatan = form.cleaned_data['kode_keberatan']
            
            try:
                # Fetch the record that matches the NIK and kode_keberatan
                result = PengajuanKeberatan.objects.get(NIK=NIK, kode_keberatan=kode_keberatan)
            except PengajuanKeberatan.DoesNotExist:
                error_message = "Data tidak ditemukan. Periksa kembali NIK dan Kode Keberatan Anda."

    else:
        form = CekKeberatanForm()
    
    return render(request, 'ppid/cek_keberatan.html', {
        'form': form,
        'result': result,
        'error_message': error_message
    })

# ------------------------------------------ informasi publik -----------------------------------------------------------------------------
# ------------------------------------------------ views ----------------------------------------------------------------------------------

from itertools import groupby
from operator import attrgetter
from .models import InformasiPublik
from .models import InformasiBerkala

def informasi_berkala(request):
    informations = InformasiBerkala.objects.all()
    # grouped = groupby(sorted(informations, key=attrgetter('category')), key=attrgetter('category'))
    # grouped = groupby(sorted, attrgetter('category'))
    return render(request, 'ppid/informasi_publik.html', {'informations': informations})


def informasi_publik(request):
    informations = InformasiPublik.objects.all()
    # grouped = groupby(sorted(informations, key=attrgetter('category')), key=attrgetter('category'))
    # grouped = groupby(sorted, attrgetter('category'))
    return render(request, 'ppid/file_permohonan.html', {'informations': informations})

