# StudyPlan - Asistensi 1 (Quiz 2 PBP: Django Auth + JavaScript)

> FILE INI = STATE BELAJAR. Dibaca oleh AI mana pun yang user pakai (AI tidak punya memory antar sesi).
> Raw link (AI: fetch ini, bukan halaman github.com biasa):
> https://raw.githubusercontent.com/zidan-do-pbp/Asistensi-Kuis-PBP/main/Asistensi-1/StudyPlan.md

---

## 0. AI PROTOCOL (WAJIB BACA PERTAMA)

1. Baca file ini sampai habis SEBELUM menjawab apa pun. Lalu balas maksimal 3 baris: (a) posisi terakhir belajar, (b) Next Action di Section 2, (c) tanya user siap lanjut atau mau ubah fokus.
2. Materi sumber = file notes transkrip (Section 1). Ikuti aturan LEGEND di file itu:
   - Percaya tag [EXT]. Tag [INF] dan [AMB] = belum terverifikasi, cek repo/slide user sebelum dijadikan kode.
   - Info tidak ada di notes -> bilang "not in notes". Jangan karang dari memori.
   - Teks spec kuis/tugas dari user mengalahkan notes.
3. Kalau AI tidak bisa buka link: minta user paste isi StudyPlan.md dan notes. Jangan pura-pura sudah baca.
4. Gaya mengajar: Bahasa Indonesia santai, ringkas. Active recall: tanya dulu, jelaskan SESUDAH user menjawab. Satu konsep per giliran. User harus menulis kode sendiri; jangan kasih jawaban penuh sebelum user mencoba. Koreksi dengan menunjuk node id notes (contoh `rule:post_csrf`).
5. Prioritas: kerjakan P1 dulu (yang dikonfirmasi dosen), lalu P2, lalu P3.
6. Aturan mengubah status (JANGAN longgar):
   - `[ ]` belum / `[~]` sedang / `[x]` lulus.
   - Paham = `[x]` hanya jika user menjelaskan ALASAN (bukan sekadar apa) dengan kata sendiri DAN menjawab 2 pertanyaan recall benar tanpa hint.
   - Latihan = `[x]` hanya jika user menulis kodenya dari kosong (tanpa melihat jawaban) dan user mem-paste kode ke chat untuk direview AI. Kesalahan sintaks kecil boleh.
   - "Saya sudah paham" dari user saja BUKAN bukti. Pakai `[~]`.
   - Setiap perubahan status wajib ada bukti 1 kalimat di kolom Catatan atau Session Log.
7. AI tidak bisa push ke GitHub dan tidak bisa melihat repo/laptop user kecuali user paste. Jangan klaim sudah memverifikasi.
8. Log (Section 6 dan 7) bersifat append-only. Jangan hapus entri lama.
9. HANDOFF: saat user bilang "handoff", "simpan", "limit", "ganti AI", atau setelah selesai sekitar 3-5 item, atau kalau percakapan sudah panjang, AI proaktif mengingatkan lalu mengeluarkan:
   (a) FULL isi StudyPlan.md terbaru dalam SATU code block (Section 2, 3, 6, 7 terupdate; Section 0, 1, 4, 5, 8 tidak diubah), dan
   (b) perintah PowerShell dari Section 8 yang sudah terisi.
10. Jangan ubah struktur/heading file ini supaya AI lain tetap bisa parse.

---

## 1. SUMBER & KONTEKS

- Repo: https://github.com/zidan-do-pbp/Asistensi-Kuis-PBP (folder `Asistensi-1`)
- Notes transkrip asistensi (knowledge map, tag [EXT]/[INF]/[AMB], node id, edges):
  https://raw.githubusercontent.com/zidan-do-pbp/Asistensi-Kuis-PBP/main/Asistensi-1/notes-asistensi-django-auth-js.md
- Rekaman: 2026-10-04, topik Django auth/authz + JS interaktif. Persiapan Quiz 2 (Tutorial 4 + 5).
- Tiga topik kuis yang dikonfirmasi dosen (via TA, notes `rule:quiz2_topics`):
  1. JavaScript.
  2. Login page termasuk CSRF token; buat form dan kirim data ke database.
  3. Batasi halaman hanya untuk user yang sudah login.
- Unit testing: tidak disebut dosen. Selenium: kemungkinan tidak keluar.
- Tanggal kuis: [ISI USER: belum diketahui pasti, notes menandai [AMB]]
- Task: A1-A4 = tugas Django. B1-B4 = tugas JS.

---

## 2. STATE SAAT INI (AI: update tiap handoff)

- Terakhir diupdate: 2026-10-06 oleh Claude (setup awal dari notes transkrip)
- Total sesi belajar: 0
- Progres Paham: 0/32 | Progres Latihan: 0/29
- Fokus sekarang: belum mulai
- NEXT ACTION: Mulai P1 dari A4.1 (login_required, paling cepat dan sering keluar), lanjut A2.0, lalu A1.1 dan A1.2.
- Jalur belajar P1 yang disarankan: A4.1 -> A2.0 -> A1.1 -> A1.2 -> A2.2 -> A2.3 -> A2.4 -> A2.6 -> B1.1 -> B1.2 -> B2.1 -> B2.4 -> B2.5 -> B3.1 -> B3.2 -> B4.1 -> B4.2 -> B4.3
- Catatan kondisi user (AI isi kalau relevan): -

---

## 3. CHECKLIST

Kolom: P = prioritas (P1 dikonfirmasi dosen/inti, P2 penting, P3 bonus). Node = id di notes (grep di Section 3 notes untuk edges). Tgl = terakhir disentuh.

### Django (A1-A4)

| ID | P | Topik (node id) | Paham | Latihan | Tgl | Catatan |
|----|---|-----------------|-------|---------|-----|---------|
| A1.1 | P1 | register: UserCreationForm, save, redirect login (`fn:register`) | [ ] | [ ] | - | |
| A1.2 | P1 | login: AuthenticationForm, login(), set_cookie (`fn:login_user`) | [ ] | [ ] | - | |
| A1.3 | P2 | logout: POST only 405, logout(), delete_cookie (`fn:logout_user`) | [ ] | [ ] | - | |
| A1.4 | P2 | cookie last_login, flags max_age/httponly/samesite, no secrets (`concept:cookie_flags`, `rule:no_secrets_in_cookie`) | [ ] | [ ] | - | |
| A2.0 | P1 | Django shell: buat user + assign Group (`tip:lab_prep_a2`, `concept:role_group`) | [ ] | [ ] | - | |
| A2.1 | P1 | Role = Group, tanpa superuser (`concept:role_group`, `rule:no_superuser`) | [ ] | - | - | |
| A2.2 | P1 | create_project: Owner only, else 403 (`fn:create_project`) | [ ] | [ ] | - | |
| A2.3 | P1 | edit_project: cek permission DULU, lalu get_object_or_404 (`fn:edit_project`) | [ ] | [ ] | - | |
| A2.4 | P1 | delete_project: POST only + Owner only (`fn:delete_project`) | [ ] | [ ] | - | |
| A2.5 | P2 | toggle_star: POST + login, add/remove starred_by (`fn:toggle_star`) | [ ] | [ ] | - | |
| A2.6 | P1 | template project_list: tombol per role + csrf_token + server-side check (`tmpl:project_list`, `rule:server_side_check`, `rule:post_csrf`) | [ ] | [ ] | - | |
| A2.7 | P3 | bonus prefetch_related('starred_by') (`fn:project_list_bonus`) | [ ] | [ ] | - | |
| A3.1 | P3 | A3 tidak dijelaskan di asistensi, kerjakan dari deskripsi + kode di GitHub tutorial | [ ] | [ ] | - | |
| A4.1 | P1 | login_required + login_url di dashboard, tampilkan username (`fn:dashboard_protected`) | [ ] | [ ] | - | |

### JavaScript (B1-B4)

| ID | P | Topik (node id) | Paham | Latihan | Tgl | Catatan |
|----|---|-----------------|-------|---------|-----|---------|
| B1.1 | P1 | renderReports: clear innerHTML, createElement, badge, append (`fn:renderReports`) | [ ] | [ ] | - | |
| B1.2 | P1 | textContent vs innerHTML (XSS) (`why:textContent_not_innerHTML`) | [ ] | - | - | |
| B1.3 | P3 | bonus: ringkasan hitung hilang/ditemukan + empty message | [ ] | [ ] | - | |
| B2.1 | P1 | applyFilters: query + status, filter AND, return array (`fn:applyFilters`) | [ ] | [ ] | - | |
| B2.2 | P2 | `===` vs `==` vs `=` (`trap:eq_vs_strict`) | [ ] | - | - | |
| B2.3 | P2 | openModal (bersihkan state lama) / closeModal (`fn:openModal`, `fn:closeModal`) | [ ] | [ ] | - | |
| B2.4 | P1 | init wiring: addEventListener, renderReports(applyFilters()) (`concept:init_wiring`) | [ ] | [ ] | - | |
| B2.5 | P1 | jebakan kurung: handler tanpa `()` (`trap:parentheses_on_handler`) | [ ] | - | - | |
| B3.1 | P1 | loadReports: fetch GET, isLoading guard, try/catch/finally (`fn:loadReports`, `concept:busy_flag`) | [ ] | [ ] | - | |
| B3.2 | P1 | async/await dan kenapa finally (`concept:async_await`, `why:finally`) | [ ] | - | - | |
| B3.3 | P3 | bonus: validasi Array.isArray sebelum replace state | [ ] | [ ] | - | |
| B4.1 | P1 | submitReport: event 'submit' (bukan click), preventDefault, guard, validasi (`fn:submitReport`) | [ ] | [ ] | - | |
| B4.2 | P1 | POST fetch + CSRF header + parsing error JSON (`rule:post_csrf`) | [ ] | [ ] | - | |
| B4.3 | P1 | urutan isSubmitting=false SEBELUM closeModal (`trap:close_modal_order`) | [ ] | [ ] | - | |
| B4.4 | P2 | let vs const (`concept:let_vs_const`) | [ ] | - | - | |

### Logistik kuis

| ID | P | Topik (node id) | Paham | Latihan | Tgl | Catatan |
|----|---|-----------------|-------|---------|-----|---------|
| Q.1 | P2 | cek setup lab 1-2 hari sebelum (jaringan, venv, dependency) (`tip:quiz_env`) | [ ] | - | - | |
| Q.2 | P2 | lab jaringan terbatas: hapus link eksternal (favicon/font) yang bikin error (`tip:lab_restricted_network`) | [ ] | - | - | |
| Q.3 | P3 | tahu unit testing dan Selenium itu apa (kemungkinan tidak keluar) | [ ] | - | - | |

### Self-test bank (dari notes Section 1, tandai kalau user jawab benar tanpa hint)

- [ ] Status HTTP apa untuk: method salah, tidak punya izin, objek tidak ada? (405, 403, 404)
- [ ] Kenapa `textContent` bukan `innerHTML`? Kenapa event `submit` bukan `click`? Kenapa `finally`?
- [ ] Apa yang harus terjadi sebelum `closeModal()` di B4 dan kenapa?
- [ ] Cara tercepat melindungi satu view dari user anonim di lab?
- [ ] Apa yang rusak di lab saat internet dibatasi dan cara memperbaikinya?
- [ ] Kenapa menyembunyikan tombol di template BUKAN keamanan?
- [ ] Kenapa semua aksi ubah data harus POST + CSRF token?

---

## 4. KRITERIA LULUS (ringkas, detail ada di Section 0 poin 6)

- Paham = bisa jelaskan alasan + 2 recall benar tanpa hint.
- Latihan = tulis kode dari nol tanpa contek, dan di-review AI.
- Kuis nyata kemungkinan beda dari tutorial: yang dihafal adalah potongan konsep, bukan satu jawaban persis.

---

## 5. OPEN VERIFICATION (cek ke repo/slide user sebelum percaya; dari notes Section 5)

- [ ] V1 format string timestamp cookie `last_login` (A1)
- [ ] V2 bentuk nilai `login_url` (path atau nama route) (A4)
- [ ] V3 definisi `user.is_owner` / `user.is_editor` di models (A2)
- [ ] V4 DOM id pasti: `result-count`, id empty message (B1)
- [ ] V5 nama header CSRF + encoding body di B4 (kemungkinan `X-CSRFToken` + `JSON.stringify`)
- [ ] V6 key JSON list laporan di B3 (`data.reports` atau array langsung)
- [ ] V7 tanggal kuis pasti

---

## 6. KELEMAHAN / MISKONSEPSI (append-only)

| Tgl | Item | Kesalahan atau miskonsepsi user | Status (open/fixed) |
|-----|------|----------------------------------|---------------------|
| - | - | (belum ada) | - |

---

## 7. SESSION LOG (append-only, entri terbaru di bawah)

Format: `YYYY-MM-DD | AI (nama/model) | aktivitas | item disentuh + perubahan status | next`

- 2026-10-06 | Claude | setup file dari notes transkrip | tidak ada | mulai A4.1

---

## 8. CARA SIMPAN PROGRESS KE GITHUB (HANDOFF)

AI mengeluarkan full isi file terbaru, user menjalankan di `...\asistensi-kuis-pbp\Asistensi-1` (isi `<<...>>` oleh AI). Pola here-string: penutup harus ada di awal baris tanpa spasi.

    $ErrorActionPreference = 'Stop'
    $f = Join-Path (Get-Location).Path 'StudyPlan.md'
    $c = @'
    <<FULL ISI StudyPlan.md TERBARU DI SINI>>
    '@
    [System.IO.File]::WriteAllText($f, $c, [System.Text.UTF8Encoding]::new($false))
    git pull --rebase origin main
    git add StudyPlan.md
    git commit -m "progress: <<ringkasan singkat, contoh: A4.1 paham, A2.0 sedang>>"
    git push origin HEAD

(Catatan: di atas, baris `@'` dan `'@` harus ditulis tanpa indentasi saat dijalankan.)

Prompt untuk AI baru (user tinggal paste):
"Baca https://raw.githubusercontent.com/zidan-do-pbp/Asistensi-Kuis-PBP/main/Asistensi-1/StudyPlan.md lalu ikuti AI PROTOCOL di dalamnya. Notes sumber ada di link Section 1. Lanjutkan dari NEXT ACTION."