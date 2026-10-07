# Catatan Transkrip Asistensi 2 (Kuis 2 PBP)

Sumber: transkrip Zoom 2026-10-04 (Jaysen untuk Django A1 dan A2, Neal untuk A4 dan info kuis, Angelo dan Amelia untuk JS). Format ini melengkapi `PANDUAN-URUTAN.md`.

## 1. Intel kuis (dikonfirmasi dosen lewat TA)
Tepat tiga poin:
1. JavaScript.
2. Membuat halaman login termasuk CSRF token, membuat form, dan mengirim data ke database.
3. Membatasi halaman agar hanya bisa diakses user yang sudah login.

Catatan tambahan:
- Membatasi fitur atau endpoint berdasarkan user adalah inti materi autentikasi. Jaysen: "pasti keluar di kuis".
- JS di kuis akan berbeda dari tutorial. Kuasai potongan konsepnya, bukan hafal solusinya.
- Unit testing tidak disebut dosen. Selenium kemungkinan besar tidak keluar.
- Template kuis diberikan, sama seperti kuis 1. Hambatan kuis 1 adalah mengunduh dependensi setelah aktivasi venv di lab.
- Tempat duduk tidak tetap. Cek setup lab (jaringan, keyboard, monitor, akun) 1 sampai 2 hari sebelumnya.
- Tanggal kuis tidak disebut jelas di transkrip.

## 2. Tips lab
- Jaringan lab membatasi situs luar. Favicon dan Google Fonts bisa error dan tampil kotak rusak.
- Jika baris `<link>` eksternal (font atau favicon) menyebabkan error dan tidak terkait `settings.py`, `urls.py`, atau `views.py`, hapus baris itu di HTML.
- Persiapan soal 2: jalankan `migrate` dan `loaddata projects` dulu, lalu buat akun lewat shell:

```
python manage.py shell
from django.contrib.auth.models import Group, User
u = User.objects.create_user("editor", password="aaaaa")
u.groups.add(Group.objects.get(name="Editor"))
exit()
```
- Pintasan soal 4: tidak perlu membangun register atau login, cukup buat akun hardcoded lewat shell dengan `create_user`.

## 3. Open items di transkrip, sudah diverifikasi ke repo
| Item | Hasil |
|---|---|
| Format timestamp cookie `last_login` | `%Y-%m-%d %H:%M:%S` (spesifikasi soal 1) |
| `login_url` untuk soal 4 | `LOGIN_URL = 'main:login'` sudah ada di `settings.py` soal3, jadi `@login_required` cukup tanpa argumen |
| `user.is_owner` dan `user.is_editor` | Tidak ada di model. Pakai variabel konteks `is_owner` dan `is_editor` dari view `project_list` |
| ID DOM soal 1 | `result-count` dan `empty-message` |
| Header CSRF dan encoding body soal 4 | Header `X-CSRFToken`, body `JSON.stringify(...)` dengan `Content-Type: application/json` |
| Kunci payload list soal 3 | `data.reports` |
| Tanggal kuis | Tidak diketahui dari sumber |

## 4. Tabel respons HTTP
| Situasi | Respons |
|---|---|
| Method salah (logout, delete butuh POST) | 405 `HttpResponseNotAllowed` |
| Sudah login tapi tidak punya role | 403 `PermissionDenied` |
| Objek tidak ditemukan | 404 `get_object_or_404` |
| Nilai tema tidak valid (soal 3) | 400 `HttpResponseBadRequest` |
| POST form tidak valid | render ulang form dengan error, tanpa menulis data |
| POST form valid | simpan lalu redirect |

## 5. Pola dan jebakan JS
| Situasi | Pola |
|---|---|
| Menampilkan teks user ke DOM | `textContent`, bukan `innerHTML` (cegah XSS) |
| Cegah fetch ganda | flag sibuk (`isLoading`, `isSubmitting`) dan `return` dini |
| Selalu membersihkan state | `finally` |
| Refresh daftar sambil menjaga filter | `renderReports(applyFilters())` |
| Submit form lewat JS | event `submit` (bukan `click`) dan `preventDefault()` |
| Meneruskan handler | tanpa kurung: `addEventListener("click", openModal)` |
| Perbandingan | `===`, bukan `==` atau `=` |
| `let` dan `const` | `let` untuk nilai yang berubah, `const` untuk yang tetap |
| `await` | hanya di dalam `async function` |

Jebakan urutan di soal 4: `closeModal()` langsung keluar jika `isSubmitting` masih true, jadi set `isSubmitting = false` dulu sebelum memanggil `closeModal()`.

## 6. Prinsip yang berulang
- Pengecekan wajib di server. Menyembunyikan tombol di template hanya kosmetik.
- Semua aksi yang mengubah data memakai POST dan CSRF token.
- `logout_user` dan `delete_project` bentuknya sama: hanya POST, selain itu 405 atau 403.
- Jangan simpan password, username, atau kredensial di cookie.
