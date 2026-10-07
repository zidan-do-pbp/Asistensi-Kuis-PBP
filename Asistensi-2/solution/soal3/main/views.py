from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST


@login_required
def dashboard(request):
    visit_count = request.session.get("visit_count", 0) + 1
    request.session["visit_count"] = visit_count
    theme = request.session.get("theme", "light")
    announcement_dismissed = request.COOKIES.get("announcement_dismissed") == "1"
    return render(
        request,
        "main/dashboard.html",
        {
            "visit_count": visit_count,
            "theme": theme,
            "announcement_dismissed": announcement_dismissed,
        },
    )


@login_required
@require_POST
def set_theme(request):
    theme = request.POST.get("theme")
    if theme not in ("light", "dark"):
        return HttpResponseBadRequest("Tema tidak valid")
    request.session["theme"] = theme
    return redirect("main:dashboard")


@login_required
@require_POST
def dismiss_announcement(request):
    response = redirect("main:dashboard")
    response.set_cookie(
        "announcement_dismissed",
        "1",
        max_age=604800,
        httponly=True,
        samesite="Lax",
    )
    return response


@login_required
@require_POST
def reset_preferences(request):
    request.session.pop("theme", None)
    request.session.pop("visit_count", None)
    response = redirect("main:dashboard")
    response.delete_cookie("announcement_dismissed")
    return response
