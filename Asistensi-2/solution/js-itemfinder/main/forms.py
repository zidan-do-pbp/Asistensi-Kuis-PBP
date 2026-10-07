from django import forms

from .models import Report


# DOKUMENTASI (jangan diubah). Validasi di server untuk add_report_ajax: field wajib, max 80 karakter, status harus salah satu pilihan.
# Kalau tidak valid, view membalas 400 {"errors": {...}} (dibaca JS untuk bonus soal 4). Validasi di JS saja tidak cukup.
class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["title", "location", "status"]