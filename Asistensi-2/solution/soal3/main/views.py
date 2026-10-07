from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST


# ALUR SOAL 3: ubah main/views.py (urutan 1 sampai 4) lalu templates/main/dashboard.html (urutan 5)
# Urutan kerja views: dashboard -> set_theme -> dismiss_announcement -> reset_preferences
# Session = data di server (visit_count, theme). Cookie = data di browser (announcement_dismissed)


# TODO: (urutan 1) dashboard. login_required sudah ada. Soal 4 ikut selesai di sini (decorator + sapaan di template)
@login_required
def dashboard(request):
    # TODO: (urutan 1a) visit_count dari session default 0, tambah 1, SIMPAN kembali ke session
    visit_count = request.session.get("visit_count", 0) + 1
    request.session["visit_count"] = visit_count
    # TODO: (urutan 1b) theme dari session default "light"
    theme = request.session.get("theme", "light")
    # TODO: (urutan 1c) True hanya jika cookie bernilai persis "1"
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


# TODO: (urutan 2) set_theme. POST saja, hanya "light" atau "dark", selain itu HTTP 400 tanpa mengubah session
@login_required
@require_POST
def set_theme(request):
    theme = request.POST.get("theme")
    if theme not in ("light", "dark"):
        return HttpResponseBadRequest("Tema tidak valid")
    # TODO: (urutan 2a) simpan ke session key "theme" lalu redirect ke dashboard
    request.session["theme"] = theme
    return redirect("main:dashboard")


# TODO: (urutan 3) dismiss_announcement. Buat response redirect DULU, baru set_cookie
@login_required
@require_POST
def dismiss_announcement(request):
    response = redirect("main:dashboard")
    # TODO: (urutan 3a) nilai "1", max_age=604800 (7 hari), httponly=True, samesite="Lax"
    response.set_cookie(
        "announcement_dismissed",
        "1",
        max_age=604800,
        httponly=True,
        samesite="Lax",
    )
    return response


# TODO: (urutan 4) reset_preferences. DILARANG session.flush() karena user harus tetap login
@login_required
@require_POST
def reset_preferences(request):
    # TODO: (urutan 4a) pop hanya theme dan visit_count, lalu hapus cookie di response redirect
    request.session.pop("theme", None)
    request.session.pop("visit_count", None)
    response = redirect("main:dashboard")
    response.delete_cookie("announcement_dismissed")
    return response
