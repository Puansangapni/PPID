# signals.py
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import InformasiBerkala, InformasiPublik, InformationRequest, PengajuanKeberatan
from .models import BannerImage, Content
import os

def delete_file_if_exists(file_field):
    """
    Helper function to delete a file from the filesystem if it exists.
    """
    if file_field:
        if os.path.isfile(file_field.path):
            os.remove(file_field.path)

@receiver(post_delete, sender=Content)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem when corresponding `InformasiBerkala` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

@receiver(post_delete, sender=InformationRequest)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem when corresponding `InformasiBerkala` object is deleted.
    """
    if instance.Upload_KTP:
        if os.path.isfile(instance.Upload_KTP.path):
            os.remove(instance.Upload_KTP.path)

@receiver(post_delete, sender=PengajuanKeberatan)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem when corresponding `InformasiBerkala` object is deleted.
    """
    if instance.Upload_KTP:
        if os.path.isfile(instance.Upload_KTP.path):
            os.remove(instance.Upload_KTP.path)

@receiver(post_delete, sender=BannerImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem when corresponding `InformasiBerkala` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(post_delete, sender=InformasiPublik)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem when corresponding `InformasiBerkala` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

@receiver(post_delete, sender=InformasiBerkala)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem when corresponding `InformasiBerkala` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

