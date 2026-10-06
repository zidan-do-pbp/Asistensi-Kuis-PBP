# StudyPlan - Asistensi 1 (Quiz 2 PBP: Django Auth + JavaScript)

> FILE INI = STATE BELAJAR. Dibaca oleh AI mana pun yang user pakai (AI tidak punya memory antar sesi).
> Raw link (AI: fetch ini, bukan halaman github.com biasa): <https://raw.githubusercontent.com/zidan-do-pbp/Asistensi-Kuis-PBP/main/Asistensi-1/StudyPlan.md>

---

## 0. AI PROTOCOL (WAJIB BACA PERTAMA)

1. Baca file ini sampai habis SEBELUM menjawab apa pun. Lalu balas maksimal 3 baris: (a) posisi terakhir belajar, (b) Next Action di Section 2, (c) tanya user siap lanjut atau mau ubah fokus.
2. Materi sumber = file notes transkrip (Section 1). Ikuti aturan LEGEND di file itu:
  - Percaya tag [EXT]. Tag [INF] dan [AMB] = belum terverifikasi, cek repo/slide user sebelum dijadikan kode.
  - Info tidak ada di notes -> bilang "not in notes". Jangan karang dari memori.
  - Teks spec kuis/tugas dari user mengalahkan notes.
3. Kalau AI tidak bisa buka link: minta user paste isi StudyPlan.md dan notes. Jangan pura-pura sudah baca.
4. Gaya mengajar dan format output: IKUTI Section 0B (style caveman-lite + format Open/Read/Explain/Before-After/Run/Push + loop GUIDED-ATTEMPT). Section 0B wajib.
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
(a) FULL isi StudyPlan.md terbaru dalam SATU code block (Section 2, 3, 6, 7 terupdate; Section 0, 0B, 1, 4, 5, 8 tidak diubah), dan
(b) perintah PowerShell dari Section 8 yang sudah terisi.
10. Jangan ubah struktur/heading file ini supaya AI lain tetap bisa parse.

---

## 0B. STYLE + OUTPUT FORMAT (MANDATORY, overrides default chat habits)

Why: other AIs do not have Zydan's personal style skill, so the rules are embedded here.
Zydan = Fasilkom UI student. Cannot validate Django/JS code alone. Often forgets how to run venv, migrations, manage.py. So the AI guides step by step and spells out every command with its directory.

### Style (gaya-zydan + caveman-lite)

1. Chat language = Indonesian. Technical terms stay English. Gloss a new term once per session.
2. Caveman-lite: no greeting, no praise, no closing recap. Fragments ok. `->` for flow/cause. Code, commands, paths, identifiers stay exact.
3. No em-dash. Use period, comma, colon, parentheses.
4. Start with the answer. End with delta: what changed, what is still open, what starts next.
5. Every factual claim needs a source: notes node id, Zydan's repo file, or official docs actually opened. Unknown -> say "not in notes" or "belum tahu, cek: ". Never invent APIs, numbers, or file contents.
6. Do not ask Zydan to approve technical choices. Decide, state the assumption in one line, go. Ask only about intent.
7. One question per turn, max 30 words.
8. Zydan correct -> say correct + one reinforcing detail. Wrong -> say wrong, supportive tone, point to node id. No cheerleading.
9. "Done / works / safe" only after a check. Say what was checked (command run, output pasted).
10. Active recall: never put the answer next to the question. Grade honestly. Diagnose the weak concept, log it in Section 6.
11. Avoid: delve, leverage, robust, seamless, comprehensive, crucial, utilize, streamline.

### Mode: GUIDED-ATTEMPT (default)

Per TODO, loop in this order. One step per turn. Wait for Zydan's "ok"/output before the next step.

1. OPEN file (F1).
2. READ the TODO (F2).
3. EXPLAIN inside F2. Concept + node id. Do NOT reveal the solution.
4. Zydan attempts the code himself. AI waits.
5. Zydan pastes his attempt. AI reviews.
6. CHANGE (F3): Before = Zydan's code, After = corrected. Only the changed region.
7. RUN (F4): command to test.
8. Verify expected result with Zydan (pasted output or browser behavior).
9. PUSH (F5).
10. Update checklist status in-session using Section 0 rule 6. Then next TODO.

Hint ladder when Zydan says "hint", "stuck", "kasih":

- H1: concept pointer + node id only.
- H2: skeleton with blanks.
- H3: full After. After H3, Latihan for that item stays `[~]` at most.

Zydan can say "mode cepat" to skip the attempt step (AI shows After directly). Latihan stays `[~]` at most.

### Output formats (use exactly, labels in English, content in Indonesian caveman-lite)

F1 OPEN. At the start of every step that touches a file:

|      |                   |
| ---- | ----------------- |
| Open | `views.py`        |
| Path | `./main/views.py` |

F2 READ. When Zydan asks to read a TODO:

|         |                                                         |
| ------- | ------------------------------------------------------- |
| Read    | `// TODO: <exact text from the file>`                   |
| Explain | <1-3 short lines: what it asks, which concept, node id> |

F3 CHANGE. When modifying a file. One-line code goes inside the cell. Multi-line code: keep the Before/After rows as labels and put the code in fenced blocks right under each label. Show only the changed region plus 1-2 context lines, anchored by function name.

|        |          |
| ------ | -------- |
| Before | `<code>` |
| After  | `<code>` |

F4 RUN. When Zydan must run something. Always state the directory, because Zydan forgets. Never assume the venv is active, say when it is needed.

`PS: <current directory>`

```
<command>
```

Why: <one line, what this command does>
Expect: <one line, what success looks like + the most common error and its meaning>

F5 PUSH. After a verified step. List exact files, no blind `git add .`. Commit message starts with the checklist id.

```
git status --short
git add <file1> <file2>
git commit -m "<ID>: <what changed>"
git push origin HEAD
```

### Session start (once per new AI session)

1. Do Section 0 rule 1 (3-line summary).
2. Ask Zydan to paste the output of this, so paths are never guessed:

`PS: <repo folder>`

```
git ls-files
```

3. To find all TODOs:

```
Select-String -Path (git ls-files '*.py','*.html','*.js') -Pattern 'TODO'
```

### Run cheatsheet (standard Python/Django commands, verify against the repo README/requirements)

Run `manage.py` commands from the folder that contains `manage.py`. Check: `Test-Path .\manage.py`.

| Need | Command | Note |
| --- | --- | --- |
| create venv | `python -m venv <venv>` | once per clone |
| activate venv | `.\<venv>\Scripts\Activate.ps1` | prompt shows `(<venv>)`. If blocked: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first |
| install deps | `pip install -r requirements.txt` | venv must be active. Lab bottleneck, see notes `tip:quiz_env` |
| apply DB schema | `python manage.py migrate` | run after clone or after new migration files |
| make migration | `python manage.py makemigrations` | only after editing models.py |
| run server | `python manage.py runserver` | open <http://127.0.0.1:8000/> , stop with Ctrl+C |
| Django shell | `python manage.py shell` | leave with `exit()`. Used for creating users/groups, see A2.0 |
| run tests | `python manage.py test` | only if the task has tests |

---

## 1. SUMBER & KONTEKS

- Repo: <https://github.com/zidan-do-pbp/Asistensi-Kuis-PBP> (folder `Asistensi-1`)
- Notes transkrip asistensi (knowledge map, tag [EXT]/[INF]/[AMB], node id, edges):
<https://raw.githubusercontent.com/zidan-do-pbp/Asistensi-Kuis-PBP/main/Asistensi-1/notes-asistensi-django-auth-js.md>
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

- Terakhir diupdate: 2026-10-07 oleh Claude (orientasi repo + cek hasil push, belum ada item belajar disentuh)
- Total sesi belajar: 0
- Progres Paham: 0/32 | Progres Latihan: 0/23 (dihitung ulang dari tabel Section 3, sebelumnya tertulis 29)
- Fokus sekarang: orientasi repo. Isi repo (soal1-3) tidak cocok dengan checklist A/B. File notes sudah ada di lokal (hasil git pull, 488 baris), belum dibaca.
- NEXT ACTION: (1) Verifikasi jumlah baris StudyPlan.md vs origin/main (selisih -66 baris di commit eaf6054 belum dijelaskan). (2) Cari di notes: peta soal1-3 ke checklist (grep 'soal'). (3) Tunggu jawaban user: branch `latihan` sengaja atau harus ke `main`. Setelah peta jelas, mulai P1 dari A4.1 (kalau kode auth/JS ada) atau ikuti spec user.
- Jalur belajar P1 yang disarankan: A4.1 -> A2.0 -> A1.1 -> A1.2 -> A2.2 -> A2.3 -> A2.4 -> A2.6 -> B1.1 -> B1.2 -> B2.1 -> B2.4 -> B2.5 -> B3.1 -> B3.2 -> B4.1 -> B4.2 -> B4.3
- Catatan kondisi user (AI isi kalau relevan): ATURAN USER: setiap jawaban AI WAJIB ditutup command simpan progress (handoff PowerShell), karena session bisa habis kapan saja. Isi repo lokal (git ls-files + TODO-INDEX.md): soal1 (models Book), soal2 (MVT urls/views/template), soal3 (unit test). Tidak ada kode auth/CSRF/login_required/JS di repo ini. Lokasi kode A1-B4: not in notes. BRANCH: lokal = `latihan`, push masuk ke origin/latihan (commit eaf6054), BUKAN main. Raw link di Section 0/1/8 menunjuk main, jadi AI baru fetch versi lama sampai di-merge ke main.

---

## 3. CHECKLIST

Kolom: P = prioritas (P1 dikonfirmasi dosen/inti, P2 penting, P3 bonus). Node = id di notes (grep di Section 3 notes untuk edges). Tgl = terakhir disentuh.

### Django (A1-A4)

| ID | P | Topik (node id) | Paham | Latihan | Tgl | Catatan |
| --- | --- | --- | --- | --- | --- | --- |
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
| --- | --- | --- | --- | --- | --- | --- |
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
| --- | --- | --- | --- | --- | --- | --- |
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
| --- | ---- | ------------------------------- | ------------------- |
| -   | -    | (belum ada)                     | -                   |

---

## 7. SESSION LOG (append-only, entri terbaru di bawah)

Format: `YYYY-MM-DD | AI (nama/model) | aktivitas | item disentuh + perubahan status | next`

- 2026-10-06 | Claude | setup file dari notes transkrip | tidak ada | mulai A4.1
- 2026-10-06 | Claude | tambah Section 0B (style + format output + cheatsheet run) | tidak ada | mulai A4.1
- 2026-10-07 | Claude | orientasi repo: baca git ls-files + TODO-INDEX.md. Repo = soal1 (models Book), soal2 (MVT), soal3 (unit test). Tidak ada kode auth/CSRF/login_required/JS, jadi A1-B4 tidak cocok dengan repo. Claude sempat salah asumsi lokasi kode = "tutorial", dikoreksi user. Hitung ulang Latihan 29 -> 23. User minta tiap jawaban AI ditutup command simpan | tidak ada | tentukan peta soal1-3 vs A/B
- 2026-10-07 | Claude | push pertama sukses: commit eaf6054 ke origin/latihan (branch lokal = latihan, bukan main). git pull membawa notes-asistensi-django-auth-js.md (488 baris) ke lokal. Stat commit 68 insertions/134 deletions, selisih belum diverifikasi | tidak ada | cek jumlah baris vs origin/main, grep 'soal' di notes, konfirmasi soal branch

---

## 8. CARA SIMPAN PROGRESS KE GITHUB (HANDOFF)

AI mengeluarkan full isi file terbaru, user menjalankan di `...\asistensi-kuis-pbp\Asistensi-1` (isi `<<...>>` oleh AI). Pola here-string: penutup harus ada di awal baris tanpa spasi.

```
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
```

(Catatan: di atas, baris `@'` dan `'@` harus ditulis tanpa indentasi saat dijalankan.)

Prompt untuk AI baru (user tinggal paste):
"Baca <https://raw.githubusercontent.com/zidan-do-pbp/Asistensi-Kuis-PBP/main/Asistensi-1/StudyPlan.md> lalu ikuti AI PROTOCOL di dalamnya. Notes sumber ada di link Section 1. Lanjutkan dari NEXT ACTION."