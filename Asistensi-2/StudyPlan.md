# StudyPlan SPEEDRUN: Kuis 2 PBP (Asistensi-2)

Terakhir diupdate: 2026-10-07 (sesi baru, fokus Asistensi-2). Repo: https://github.com/zidan-do-pbp/Asistensi-Kuis-PBP , branch `latihan`, folder `Asistensi-2`. Jangan kerja di `main`, jangan merge `latihan` ke `main`.

## 0. AI PROTOCOL (WAJIB BACA PERTAMA)

1. Baca file ini sampai habis, lalu `ProgressLog.md` (baris terakhir = posisi terakhir). Link raw GitHub bisa cache lama: kalau punya bash, `git clone --branch latihan` itu sumber yang benar. Tidak bisa buka? Minta user paste StudyPlan dan ProgressLog, jangan pura-pura sudah baca. Tidak ada memory antar sesi: file ini dan ProgressLog.md satu-satunya state.
2. Balasan pembuka maksimal 3 baris: posisi terakhir, NEXT ACTION, tanya siap lanjut. Lalu langsung jalankan NEXT ACTION.
3. Mode GUIDED-ATTEMPT, user pemula Django: jelaskan TUJUAN dulu, beri kode lengkap (jangan suruh menebak syntax, jangan tanya recall), user mengetik sendiri di editor, AI mereview.
4. Satu langkah per giliran. Mode SPEEDRUN: boleh gabung beberapa langkah kalau user minta.
5. AI memverifikasi sendiri: `git pull` ke clone, baca file user, jalankan dengan Django test client (database sementara). Jangan klaim "berhasil" kalau belum dijalankan atau belum ada bukti dari user (screenshot/log).
6. Tiap jawaban: AI append 1 baris ke `ProgressLog.md` dan push SEBELUM membalas (kalau punya bash dan akses). Kalau tidak punya akses, tutup jawaban dengan perintah PowerShell Section 8.
7. TOKEN: jangan pernah menulis token ke file apa pun. Token yang ditempel user di chat hanya untuk repo ini, sekali sesi; ingatkan revoke di akhir.
8. Bahasa Indonesia, ramah, tanpa kata kasar, tanpa bullet saat menolak sesuatu.
9. Pola salah user yang sering muncul (cek duluan saat review): typo nama (`exist`, `samsite`, `project_ud`), `request.method != POST` tanpa kutip, `!= request.POST`, nama parameter view beda dengan nama di `urls.py`, lupa `()`, lupa `instance=`, nama template salah (`project_form.html` vs `projects_form.html`), kurung dict vs set `{'k': v}`.
10. Konten kuis tiruan: `Asistensi-2/SOAL-KUIS2.md` (teks docx asli). Kontrak tiap soal ada di sana, rujuk file itu.

## 1. SUMBER

- Soal Django: `soal1` (auth), `soal2` (otorisasi), `soal3` (session+cookie). Soal 4 docx (dashboard `login_required`) dilatih di D4.
- Soal JS: `js-itemfinder` (asal: github.com/amelia-juliawati/asistensi-pbp). Soal 1 sampai 4 di `static/js/itemfinder.js`.
- Semua fungsi TODO sudah dikosongkan jadi kerangka. Versi lama yang berisi jawaban buatan orang lain (ada bug) ada di commit git `e744cb3`; jangan dibuka sebelum selesai menulis sendiri.
- Tidak ada tanggal kuis di sumber. Tanya user kalau perlu.

## 2. STATE SAAT INI

- Paham 0/20 | Latihan 0/20
- NEXT ACTION: D1.1 `register` di `soal1/main/views.py`.
- Akun tes soal2: `regular`, `editor`, `owner` (password `aaaaa`, dibuat dengan `seed_users.py`). Soal3 pakai `regular`/`aaaaa` (`seed_user.py`). Soal1: daftar lewat halaman register.
- Catatan: template soal2 memakai variabel konteks `is_owner` dan `is_editor` yang dikirim view `project_list`, BUKAN `user.is_owner`.

## 3. CHECKLIST (P1 = inti)

| ID | Soal | File | Isi | Paham | Latihan |
|----|------|------|-----|-------|---------|
| D1.1 | Django 1 | soal1/main/views.py | register: UserCreationForm GET/POST, redirect main:login | [ ] | [ ] |
| D1.2 | Django 1 | idem | login_user: login(), redirect main:home, cookie last_login `%Y-%m-%d %H:%M:%S`; bonus max_age=3600 httponly samesite=Lax | [ ] | [ ] |
| D1.3 | Django 1 | idem | logout_user: POST only (405), logout(), delete_cookie, redirect | [ ] | [ ] |
| D2.1 | Django 2 | soal2/main/views.py | create_project: Owner only, PermissionDenied (403) | [ ] | [ ] |
| D2.2 | Django 2 | idem | edit_project: Owner/Editor, get_object_or_404, instance | [ ] | [ ] |
| D2.3 | Django 2 | idem | delete_project: POST only + Owner | [ ] | [ ] |
| D2.4 | Django 2 | idem | toggle_star: POST + login, tambah/hapus starred_by | [ ] | [ ] |
| D2.5 | Django 2 | soal2/templates/main/project_list.html | tombol create (Owner), edit (Editor/Owner), delete (Owner) | [ ] | [ ] |
| D3.1 | Django 3 | soal3/main/views.py | dashboard: visit_count session, theme, announcement_dismissed | [ ] | [ ] |
| D3.2 | Django 3 | idem | set_theme: POST, light/dark, selain itu 400 | [ ] | [ ] |
| D3.3 | Django 3 | idem | dismiss_announcement: cookie "1", 604800, httponly, Lax | [ ] | [ ] |
| D3.4 | Django 3 | idem | reset_preferences: pop theme dan visit_count, bukan flush, delete_cookie | [ ] | [ ] |
| D3.5 | Django 3 | soal3/templates/main/dashboard.html | section #announcement hanya jika belum ditutup | [ ] | [ ] |
| D4 | Django 4 | soal3 views + dashboard.html | `login_required` + sapaan `Halo, [username]!`, bukti URL diketik langsung redirect login | [ ] | [ ] |
| J1 | JS 1 | js-itemfinder/static/js/itemfinder.js | renderReports (+bonus hitung status) | [ ] | [ ] |
| J2.1 | JS 2 | idem | applyFilters (trim, huruf kecil, AND) | [ ] | [ ] |
| J2.2 | JS 2 | idem | openModal, closeModal | [ ] | [ ] |
| J2.3 | JS 2 | idem | listener di init (input, change, open, close) | [ ] | [ ] |
| J3 | JS 3 | idem | loadReports (fetch GET, isLoading, try/catch/finally) | [ ] | [ ] |
| J4 | JS 4 | idem | submitReport (preventDefault, validasi, fetch POST JSON + X-CSRFToken, finally) | [ ] | [ ] |

Urutan speedrun: D1.1 → D1.2 → D1.3 → D2.1 → D2.2 → D2.3 → D2.4 → D2.5 → D3.1 → D3.2 → D3.3 → D3.4 → D3.5 → D4 → J1 → J2.x → J3 → J4.

Kriteria: Paham = bisa jelaskan alasan. Latihan = tulis sendiri, di-review AI (terbukti jalan). `[~]` = dibantu.

## 4. RUN COMMAND (PowerShell)

Setup sekali (venv bersama di `Asistensi-2\env`, folder `env` di-ignore git):
```powershell
cd <folder-clone>\Asistensi-2
python -m venv env
.\env\Scripts\Activate.ps1
pip install django~=5.2
```
Soal Django (ganti `soal1` dengan soal2/soal3/js-itemfinder):
```powershell
cd <folder-clone>\Asistensi-2\soal1
python manage.py migrate
python manage.py runserver
```
Khusus soal2: sebelum runserver jalankan `python manage.py loaddata projects` lalu `python manage.py shell -c "exec(open('seed_users.py').read())"`. Khusus soal3: `python manage.py shell -c "exec(open('seed_user.py').read())"` lalu buka `/` (login di `/login/`). JS: `cd js-itemfinder`, `python manage.py migrate`, `python manage.py runserver`, buka `/`.

## 5. CATATAN KELEMAHAN (append-only)

- 2026-10-07 (sesi lama, Asistensi-1): typo nama, string vs object di perbandingan method, nama parameter view tidak sama dengan nama di urls.py. Lihat Section 0 poin 9.

## 6. HANDOFF (simpan progres, dari folder clone)

```powershell
cd <folder-clone>
Add-Content Asistensi-2\ProgressLog.md 'YYYY-MM-DD HH:MM | Claude | ID | STATUS | next: ...'
git add Asistensi-2/ProgressLog.md
git commit -m "log: ..."
git pull --rebase --autostash origin latihan
git push origin HEAD
```
STATUS: READ, EXPLAIN, ATTEMPT, REVIEW, RUN-OK, RUN-FAIL. Kalau `git commit` bilang "nothing to commit", filenya belum tersimpan. Kalau muncul `index.lock`, tutup VS Code Source Control/proses git, lalu ulang.
