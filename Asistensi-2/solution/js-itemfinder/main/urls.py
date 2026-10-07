from django.urls import path

from .views import (
    add_report_ajax,
    reports_json,
    show_itemfinder,
)

# FILE INI TIDAK DIUBAH SAAT KUIS (sudah jadi). Dibaca supaya tahu nama yang harus dipakai di views.py dan template.
# Cara baca: path("alamat/", fungsi_view, name="nama_url")
#   - "alamat/"   : URL yang diketik di browser / dipakai action form
#   - fungsi_view : fungsi di main/views.py yang dijalankan (harus sama persis dengan nama fungsi dan di-import di atas)
#   - name        : dipakai redirect("main:name") dan {% url 'main:name' %} di template. "main" = app_name di bawah
# # Di soal JS, name dipakai template (templates/itemfinder.html) untuk mengisi data-list-url dan data-create-url, lalu dibaca itemfinder.js lewat app.dataset

app_name = "main"

urlpatterns = [
    # GET / -> show_itemfinder(): render itemfinder.html + data awal {{ initial_reports|json_script:"initial-reports" }} (dibaca JS: let reports = JSON.parse(...))
    path("", show_itemfinder, name="show_itemfinder"),
    # GET /reports/data/ -> reports_json(): balas JSON {"reports": [...]}. Dipanggil loadReports() (SOAL 3) lewat fetch(app.dataset.listUrl). Template: data-list-url="{% url 'main:reports_json' %}"
    path("reports/data/", reports_json, name="reports_json"),
    # POST /reports/add/ -> add_report_ajax(): terima body JSON {title, location, status}, 201 sukses / 400 {"errors": {...}}. Dipanggil submitReport() (SOAL 4) lewat fetch(app.dataset.createUrl). Template: data-create-url="{% url 'main:add_report_ajax' %}"
    path("reports/add/", add_report_ajax, name="add_report_ajax"),
]