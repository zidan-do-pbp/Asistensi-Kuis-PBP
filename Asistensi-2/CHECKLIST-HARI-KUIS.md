# Checklist Hari Kuis 2 PBP (Asistensi-2)

Isi bagian 1 sampai 4 berasal dari spesifikasi soal (SOAL-KUIS2.md) dan transkrip asistensi. Bagian 5 adalah tebakan variasi dari AI, BUKAN dari sumber. Kalau bertentangan, teks soal kuis yang menang.

## 1. Sebelum kuis (1 sampai 2 hari)
- Cek lab: jaringan, keyboard, monitor, akun. Hambatan kuis 1 adalah download dependensi setelah aktivasi venv.
- Latihan tanpa melihat jawaban: urutan di `PANDUAN-URUTAN.md` (D1.1 sampai J4). Cara mengosongkan lagi: `git show 98f943e:Asistensi-2/<path-file>` menampilkan kerangka kosong asli.
- Tanggal kuis tidak ada di sumber. Tanya TA/dosen.

## 2. Saat kuis, urutan kerja
1. Baca soal sampai habis, cari bagian "Batas scope" (file apa yang boleh diubah).
2. Aktifkan venv, `pip install -r requirements.txt`, `python manage.py migrate`.
3. Soal yang butuh role atau akun: buat lewat `python manage.py shell` (snippet ada di `solution/CATATAN-TRANSKRIP.md` dan `SHELL-COPYPASTE.txt`).
4. Kalau `<link>` font atau favicon eksternal bikin error di lab dan tidak terkait settings/urls/views: hapus baris itu saja.
5. Kerjakan per fungsi, jalankan `runserver`, uji di browser setelah tiap fungsi.

## 3. Cek cepat sebelum kumpul (Django)
| Cek | Yang dicari |
|---|---|
| Nama parameter view | sama persis dengan `<int:project_id>` di urls.py |
| Method | `request.method == "POST"` pakai kutip; logout dan delete: selain POST 405 |
| Permission | dicek di view (server), bukan hanya template. Dilarang `is_superuser` |
| Status | 405 method salah, 403 tanpa role, 404 objek tidak ada, 400 nilai tema salah |
| Form | `instance=project` saat edit, render ulang form kalau POST tidak valid |
| Cookie | dipasang di response yang di-return (redirect dulu, baru `set_cookie`) |
| Reset | `pop` key, bukan `session.flush()` |
| Template | `{% csrf_token %}` di setiap form POST, variabel konteks `is_owner` (bukan `user.is_owner`) |
| Soal 4 | `@login_required` + `Halo, {{ user.username }}!`; bukti: logout, ketik URL langsung, redirect ke `/login/?next=/` |

## 4. Cek cepat sebelum kumpul (JS)
| Cek | Yang dicari |
|---|---|
| Teks dari user | `textContent`, bukan `innerHTML` |
| Listener | tanpa kurung: `addEventListener("click", openModal)` |
| Perbandingan | `===` |
| Fetch | `await`, cek `response.ok` SEBELUM `response.json()`, `try/catch/finally` |
| Guard | `isLoading` / `isSubmitting` dengan `return` dini |
| Submit | event `submit` (bukan `click`) + `event.preventDefault()` |
| POST | `Content-Type: application/json`, `X-CSRFToken`, `JSON.stringify(...)` |
| Urutan | `isSubmitting = false` SEBELUM `closeModal()` |
| Setelah sukses | `renderReports(applyFilters())` agar filter aktif tetap berlaku |
| Dilarang | `location.reload()`, `form.submit()`, navigasi |

## 5. Tebakan variasi (bukan dari sumber, latihan tambahan)
Transkrip bilang JS kuis akan berbeda dari tutorial. Latih pola yang sama pada bentuk lain:
- Django: ganti `@login_required` dengan `user_passes_test` atau `permission_required`; `login_url` eksplisit; role lain (misalnya Moderator) pada create/edit/delete; cookie lain (nama, `max_age`, `samesite`) di login.
- Django: view lain yang POST-only + login, mengubah data M2M seperti `starred_by`; konteks tambahan di dashboard (misalnya `last_login` dari cookie).
- JS: filter tambahan (lokasi), tombol hapus laporan lewat fetch, urutan data, pesan error per field dari `errors`, memuat ulang setelah submit lewat `loadReports()` atau menambah `data.report` di depan array.
