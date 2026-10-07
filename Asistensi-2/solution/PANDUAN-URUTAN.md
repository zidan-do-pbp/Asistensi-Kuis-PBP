# Panduan Urutan Pengerjaan Kuis 2 PBP (Asistensi-2)

Cari penanda `TODO: (urutan N)` di tiap file. Angka N = urutan kerja, huruf (1a, 1b) = langkah kecil di dalamnya.
Python memakai `# TODO`, template memakai `{# TODO #}`, JavaScript memakai `//TODO`.

## Django Soal 1: Autentikasi, Session, Cookie (soal1)
Ubah hanya `main/views.py`.
1. `register`: GET form kosong, POST invalid render ulang, POST valid save lalu redirect `main:login`
2. `login_user`: `AuthenticationForm(request, data=...)`, `login()`, redirect `main:home`, cookie `last_login`
3. `logout_user`: selain POST 405, `logout()`, `delete_cookie`, redirect `main:home`

## Django Soal 2: Otorisasi dan Star (soal2)
Ubah `main/views.py` lalu `templates/main/project_list.html`.
1. `create_project` (Owner, 403)
2. `edit_project` (Editor/Owner, `get_object_or_404`, `instance=`)
3. `delete_project` (POST + Owner)
4. `toggle_star` (POST + login, tambah/hapus `starred_by`)
5. Template: 5A tombol create (Owner), 5B edit (Editor/Owner) dan delete (Owner)

## Django Soal 3 dan 4: Session, Cookie, login_required (soal3)
Ubah `main/views.py` lalu `templates/main/dashboard.html`.
1. `dashboard` (session `visit_count`, `theme`, cookie `announcement_dismissed`)
2. `set_theme` (light/dark, selain itu 400)
3. `dismiss_announcement` (cookie `"1"`, 604800, httponly, Lax)
4. `reset_preferences` (`pop`, bukan `flush`, hapus cookie)
5. Template: `#announcement` hanya jika belum ditutup
6. Soal 4: `login_required` (sudah terpasang) dan sapaan `Halo, [username]!`. Bukti: logout, ketik URL dashboard langsung, hasilnya redirect ke `/login/?next=/`

## JavaScript (js-itemfinder)
Ubah hanya `static/js/itemfinder.js`.
1. `renderReports` (kosongkan list, card, badge, bonus hitung status)
2. `applyFilters`, `openModal`, `closeModal`, listener di `init()`
3. `loadReports` (fetch GET, guard, try/catch/finally), listener Muat ulang, panggil sekali di `init()`
4. `submitReport` (preventDefault, validasi, fetch POST JSON + `X-CSRFToken`, finally), listener submit di `init()`

## Pola salah yang sering muncul
typo nama (`exist`, `samsite`), `request.method != POST` tanpa kutip, nama parameter view beda dengan `urls.py`, lupa `()`, lupa `instance=`, kurung dict vs set `{'k': v}`, `user.is_owner` padahal variabelnya `is_owner`.
