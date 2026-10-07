from django.db import models


# DOKUMENTASI (jangan diubah). Satu Report = satu laporan barang. status hanya boleh "hilang" atau "ditemukan" (STATUS_CHOICES).
# Field title/location/status adalah key JSON yang dibaca itemfinder.js dan dikirim submitReport().
class Report(models.Model):
    STATUS_CHOICES = [
        ("hilang", "Hilang"),
        ("ditemukan", "Ditemukan"),
    ]

    title = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
    )