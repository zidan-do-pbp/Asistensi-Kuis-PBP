import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from .forms import ReportForm
from .models import Report


def get_report_data():
    return list(
        Report.objects.order_by("-id").values(
            "id",
            "title",
            "location",
            "status",
        )
    )


@require_GET
def show_itemfinder(request):
    return render(
        request,
        "itemfinder.html",
        {"initial_reports": get_report_data()},
    )


@require_GET
def reports_json(request):
    return JsonResponse(
        {"reports": get_report_data()}
    )


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