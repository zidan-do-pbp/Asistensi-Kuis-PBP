import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from .forms import ReportForm
from .models import Report


# FILE INI SUDAH JADI (tidak diubah saat kuis). Dibaca untuk tahu format data yang dikirim ke / diterima dari itemfinder.js
# Format satu laporan: {"id": 1, "title": "...", "location": "...", "status": "hilang" | "ditemukan"}
def get_report_data():
    return list(
        Report.objects.order_by("-id").values(
            "id",
            "title",
            "location",
            "status",
        )
    )


# HUBUNGAN: urls.py name="show_itemfinder". initial_reports -> template -> json_script id "initial-reports" -> JSON.parse di itemfinder.js
@require_GET
def show_itemfinder(request):
    return render(
        request,
        "itemfinder.html",
        {"initial_reports": get_report_data()},
    )


# HUBUNGAN: urls.py name="reports_json" -> data-list-url -> loadReports() (SOAL 3). Key "reports" harus sama dengan data.reports di JS. require_GET: method lain = 405
@require_GET
def reports_json(request):
    return JsonResponse(
        {"reports": get_report_data()}
    )


# HUBUNGAN: urls.py name="add_report_ajax" -> data-create-url -> submitReport() (SOAL 4). require_POST: GET = 405.
# Alur: baca JSON body -> ReportForm validasi (main/forms.py) -> simpan -> 201. Salah -> 400 {"errors": {field: [pesan]}} yang ditampilkan di #form-message oleh JS
# CSRF: header X-CSRFToken dari JS wajib, kalau tidak Django balas 403
@require_POST
def add_report_ajax(request):
    try:
        payload = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        payload = None

    if not isinstance(payload, dict):
        return JsonResponse(
            {"errors": {"__all__": ["Format data tidak valid."]}},
            status=400,
        )

    form = ReportForm(payload)

    if not form.is_valid():
        return JsonResponse(
            {"errors": dict(form.errors)},
            status=400,
        )

    report = form.save()

    return JsonResponse(
        {
            "report": {
                "id": report.id,
                "title": report.title,
                "location": report.location,
                "status": report.status,
            }
        },
        status=201,
    )