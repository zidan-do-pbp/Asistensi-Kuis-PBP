from django.urls import path

from .views import (
    add_report_ajax,
    reports_json,
    show_itemfinder,
)

app_name = "main"

urlpatterns = [
    path("", show_itemfinder, name="show_itemfinder"),
    path("reports/data/", reports_json, name="reports_json"),
    path("reports/add/", add_report_ajax, name="add_report_ajax"),
]