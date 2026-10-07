- Implementasi Autentikasi, Session, dan Cookie

# **Soal 1 – AUTENTIKASI, SESSION, DAN COOKIE** ([https://github.com/Jaysenlestari/Asistensi-Kuis-PBP/tree/main/Asistensi-2](https://github.com/Jaysenlestari/Asistensi-Kuis-PBP/tree/main/Asistensi-2)) 

Campus Showcase membutuhkan akun pengguna. Struktur route dan template sudah tersedia, tetapi fungsi register, login, dan logout belum diimplementasikan.

**Tugas**

Lengkapi main/views.py dengan kontrak berikut:

1. register:

   - GET menampilkan UserCreationForm kosong pada main/register.html.

   - POST tidak valid menampilkan kembali form beserta error tanpa membuat User.

   - POST valid menyimpan User dan redirect ke named route main:login.

2. login_user:

   - GET menampilkan AuthenticationForm pada main/login.html.

   - POST tidak valid menampilkan kembali form beserta error.

   - POST valid memanggil login(), redirect ke main:home, dan memasang cookie last_login.

   - Nilai cookie memakai waktu saat login dalam format YYYY-MM-DD HH:MM:SS.

3. logout_user:

   - Hanya menerima POST. GET menghasilkan HTTP 405 Method Not Allowed.

   - Memanggil logout(), menghapus cookie last_login, lalu redirect ke main:home.

4. Jangan menyimpan password, username, atau data kredensial lain dalam cookie.

**Bonus**

Tambahkan max_age=3600, httponly=True, dan samesite="Lax" ketika memasang cookie last_login.

**Batas scope**

- Ubah hanya main/views.py.

- Jangan mengubah route, template, settings, atau memakai model User buatan sendiri.

- Gunakan sistem autentikasi bawaan Django.

# **Soal 2 – OTORISASI DAN FITUR STAR**

Campus Showcase dapat dibaca publik. Perubahan data mengikuti role pengguna yang disimpan menggunakan Django Group. Tidak ada pemeriksaan is_superuser dalam logika aplikasi.

**Peran dan hak akses**

- Pengunjung: membaca daftar; aksi akun diarahkan ke login.

- User tanpa role khusus: membaca dan toggle star.

- Editor: seluruh hak User serta edit.

- Owner: seluruh hak User serta create, edit, dan delete.

**Persiapan**

  python manage.py migrate

  python manage.py loaddata projects

Migrasi sudah membuat Group Editor dan Owner. Buat tiga akun biasa melalui Django shell, kemudian masukkan akun terkait ke Group:

from django.contrib.auth.models import Group, User

regular = User.objects.create_user("regular", password="aaaaa")

editor = User.objects.create_user("editor", password="aaaaa")

owner = User.objects.create_user("owner", password="aaaaa")

editor.groups.add(Group.objects.get(name="Editor"))

owner.groups.add(Group.objects.get(name="Owner"))

**Tugas**

Lengkapi main/views.py dan TODO pada templates/main/project_list.html:

1. create_project hanya mengizinkan anggota Group Owner. Pengguna login tanpa role tersebut mendapat PermissionDenied (HTTP 403). Proses ProjectForm untuk GET/POST dan redirect setelah sukses.

2. edit_project hanya mengizinkan anggota Group Editor atau Owner. Ambil objek dengan get_object_or_404, proses form instance, lalu redirect setelah sukses. User biasa mendapat 403.

3. delete_project hanya menerima POST dan hanya mengizinkan anggota Group Owner. Setelah menghapus, redirect ke daftar.

4. toggle_star hanya menerima POST dan membutuhkan login. Jika pengguna sudah ada di starred_by, hapus; jika belum, tambahkan.

5. Template menyembunyikan create hanya untuk Owner, edit untuk Editor/Owner, dan delete hanya untuk Owner. Pemeriksaan server-side tetap wajib.

**Bonus**

Optimalkan query daftar menggunakan prefetch_related("starred_by") tanpa mengubah perilaku halaman.

**Batas scope**

- Ubah hanya main/views.py dan templates/main/project_list.html.

- Jangan mengubah model, form, route, fixture, migrasi, atau settings.

- Dilarang memakai is_superuser untuk menentukan hak akses fitur.

- Semua aksi perubahan data memakai POST dan CSRF token.

# **Soal 3 – PREFERENSI PENGGUNA DENGAN SESSION DAN COOKIE**

Campus Showcase memiliki dashboard khusus pengguna. Pengguna dapat memilih tema selama session berlangsung dan menutup pengumuman selama tujuh hari pada browser yang sama.

**Tugas**

Lengkapi main/views.py dan satu TODO pada templates/main/dashboard.html:

1. dashboard:

   - Hanya dapat diakses setelah login karena decorator yang sudah tersedia.

   - Ambil visit_count dari session dengan default 0, tambah satu, lalu simpan kembali.

   - Ambil theme dari session dengan default "light".

   - announcement_dismissed bernilai True hanya jika cookie tersebut bernilai "1".

   - Kirim ketiga nilai itu ke template dengan key yang sama.

2. set_theme:

   - Hanya menerima POST.

   - Hanya menerima nilai "light" atau "dark" dari request.POST["theme"].

   - Nilai lain menghasilkan HTTP 400 tanpa mengubah session.

   - Simpan nilai valid pada session key theme lalu redirect ke dashboard.

3. dismiss_announcement:

   - Hanya menerima POST.

   - Buat response redirect terlebih dahulu, lalu set cookie announcement_dismissed="1".

   - Cookie berlaku tujuh hari (max_age=604800), HttpOnly, dan SameSite=Lax.

4. reset_preferences:

   - Hanya menerima POST.

   - Hapus hanya key theme dan visit_count dari session menggunakan pop(..., None).

   - Jangan memakai session.flush() karena pengguna harus tetap login.

   - Hapus cookie announcement_dismissed pada response redirect.

5. Template hanya menampilkan section #announcement ketika pengumuman belum ditutup.

**Batas scope**

- Ubah hanya main/views.py dan templates/main/dashboard.html.

- Jangan membuat model atau menyimpan preferensi pada database.

- Jangan menghapus session autentikasi ketika reset preferensi.

- Seluruh endpoint perubahan state tetap memakai POST dan CSRF token.

# **Soal 4 – Membatasi Akses Dashboard**

Campus Showcase memiliki dashboard khusus pengguna. Pengguna dapat memilih tema selama session berlangsung dan menutup pengumuman selama tujuh hari pada browser yang sama.

**Tugas:**

- Lengkapi halaman dashboard agar hanya dapat dibuka setelah login

- Tampilkan sapaan** Halo, [username]!** dari request.user.username

- Buktikan bahwa pembatasan tetap berlaku saat URL dashboard diketik langsung

		Batas Scope

- Ubah hanya bagian TODO pada main/views.py dan templates/main/dashboard.html.

- Gunakan decorator login_required dari sistem autentikasi bawaan Django.

- Login, logout, route, dan konfigurasi proyek sudah disediakan; jangan mengubah bagian-bagian tersebut.

- Tidak perlu membuat model, form, halaman, atau fitur baru.

- Pembatasan wajib dilakukan pada view di server. Menyembunyikan tombol atau isi halaman melalui template saja tidak cukup.

- Tidak ada pembatasan peran: semua akun yang sudah login boleh mengakses dashboard, termasuk akun biasa.

- Web Interactivity with JavaScript

# **Soal **1** - **Fetching** ****&**** Rendering Data**

Github: [https://github.com/amelia-juliawati/asistensi-pbp.git](https://github.com/amelia-juliawati/asistensi-pbp.git)

Item Finder perlu menampilkan laporan barang hilang dan ditemukan. Data laporan sudah tersedia dalam array reports, tetapi belum ditampilkan pada halaman.

Tugas

- Kosongkan isi #report-list sebelum setiap render agar kartu tidak terduplikasi.

- Untuk setiap laporan dalam data:

- Buat elemen <article> dan berikan class card.

- Tentukan class dan teks badge.

- Isi card untuk menampilkan badge status, judul laporan, dan lokasi laporan.

- Tambahkan card ke dalam #report-list.

Bonus

- Tambahkan rincian jumlah setiap status, misalnya 3 laporan (2 hilang, 1 ditemukan).

Batas scope

- Ubah hanya renderReports(data).

- Belum perlu menggunakan fetch() atau melakukan request ke server.

# **Soal **2** - Event Handler, Filter, dan Modal**

Pengguna perlu mencari laporan barang hilang berdasarkan judul dan status. Pengguna juga harus dapat membuka dan menutup form laporan melalui modal tanpa reload halaman.

Tugas

- Implementasikan applyFilters() untuk mengembalikan laporan yang sesuai dengan kata pencarian dan status yang dipilih.

- Pencarian judul tidak membedakan huruf besar/kecil dan mengabaikan spasi di awal maupun akhir input.

- Status all menampilkan seluruh laporan, sedangkan status lainnya hanya menampilkan laporan dengan status yang sama.

- Gabungkan pencarian judul dan filter status dengan logika AND.

- Render ulang hasil filter ketika nilai pencarian atau filter status berubah.

- Implementasikan openModal() untuk membuka modal dan membersihkan pesan form sebelumnya.

- Implementasikan closeModal() untuk menutup modal selama proses submit tidak sedang berlangsung.

- Pasang event listener yang diperlukan untuk pencarian, filter status, tombol Buat laporan, dan tombol Tutup.

Bonus

- Arahkan fokus ke input judul ketika modal dibuka.

Batas scope

- Ubah hanya applyFilters(), openModal(), closeModal(), dan listener terkait dalam init().

- Jangan melakukan filter melalui backend.

# Soal 3 - Mengambil data dengan AJAX
Data laporan barang hilang terbaru harus dapat diambil dari server tanpa memuat ulang halaman. Lengkapi loadReports().

Tugas

- Ambil data laporan dari app.dataset.listUrl menggunakan fetch() dan async/await.

- Cegah request baru jika proses loading atau submit sedang berlangsung.

- Selama request berjalan, tampilkan kondisi loading dan nonaktifkan tombol yang dapat memicu request lain.

- Periksa apakah response berhasil sebelum membaca data JSON.

- Jika request berhasil, perbarui reports dengan data terbaru dari server dan render menggunakan filter yang sedang aktif.

- Jika request gagal, tampilkan pesan error dan pertahankan data lama.

- Pastikan state loading dan tombol dikembalikan ke kondisi semula setelah request selesai.

- Pasang event listener pada tombol Muat ulang data dan ambil data sekali ketika aplikasi pertama kali diinisialisasi.

Bonus

- Validasi bahwa data.reports merupakan array sebelum mengganti data lama.

Batas scope

- Ubah hanya loadReports() dan listener/pemanggilan terkait dalam init().

- Jangan memakai location.reload() atau melakukan navigasi.

- Respons endpoint berbentuk {"reports": [...]}.

# Soal 4 - Mengirim Data dengan AJAX
Pengguna perlu membuat laporan baru melalui form pada modal tanpa memuat ulang halaman.

Tugas

- Cegah perilaku default submit form agar halaman tidak reload.

- Cegah submit baru jika proses submit atau loading sedang berlangsung.

- Validasi input sebelum mengirim request. Judul dan lokasi tidak boleh kosong setelah spasi di awal dan akhir dihapus, dan status harus hilang atau ditemukan. Jika tidak valid, tampilkan pesan error pada form tanpa mengirim request.

- Kirim data dengan fetch() dan async/await menggunakan method POST, header Content-Type: application/json, dan body JSON.stringify(...). Sertakan CSRF token pada header X-CSRFToken.

- Selama request berjalan, aktifkan state submit, nonaktifkan tombol submit, dan ubah teksnya menjadi "Mengirim...".

- Periksa apakah response berhasil sebelum membaca data JSON.

- Jika request berhasil, kosongkan form, tutup modal, lalu perbarui daftar laporan menggunakan filter yang sedang aktif.

- Jika request gagal, tampilkan pesan error, biarkan modal tetap terbuka, dan pertahankan isi form agar pengguna tidak perlu mengetik ulang.

- Pastikan state submit dan tombol dikembalikan ke kondisi semula setelah request selesai, baik berhasil maupun gagal.

- Pasang event listener submit pada form di init().

Bonus

- Jika server mengembalikan HTTP 400, tampilkan pesan error dari errors di bawah form, bukan hanya pesan umum.

Batas scope

- Ubah hanya submitReport() dan listener terkait dalam init().

- Jangan memakai location.reload(), melakukan navigasi, atau mengirim form dengan cara tradisional (form.submit()).

- Jangan mengubah loadReports(), applyFilters(), openModal(), atau closeModal().

- Data dikirim sebagai JSON, bukan FormData