# StudyPlan - Asistensi 1 (Quiz 2 PBP: Django Auth + JavaScript)

> FILE INI = STATE BELAJAR. Dibaca oleh AI mana pun yang user pakai (AI tidak punya memory antar sesi).
> Raw link (AI: fetch ini, bukan halaman github.com biasa):
> https://raw.githubusercontent.com/zidan-do-pbp/Asistensi-Kuis-PBP/latihan/Asistensi-1/StudyPlan.md
> Progress log (append-only, dibaca bersama file ini): https://raw.githubusercontent.com/zidan-do-pbp/Asistensi-Kuis-PBP/latihan/Asistensi-1/ProgressLog.md
> Index TODO (cari TODO di sini, jangan scan repo): https://raw.githubusercontent.com/zidan-do-pbp/Asistensi-Kuis-PBP/main/Asistensi-1/TODO-INDEX.md

---

## 0. AI PROTOCOL (WAJIB BACA PERTAMA)

1. Baca file ini sampai habis SEBELUM menjawab apa pun, lalu fetch ProgressLog.md (link di header; 404 = belum ada log, lanjut). Kalau ProgressLog punya entri SETELAH baris `HANDOFF-MERGED` terakhir, entri itu lebih baru dari Section 2 dan 3: percaya log. Lalu balas maksimal 3 baris: (a) posisi terakhir belajar, (b) Next Action, (c) tanya user siap lanjut atau mau ubah fokus.
2. Materi sumber = file notes transkrip (Section 1). Ikuti aturan LEGEND di file itu:
   - Percaya tag [EXT]. Tag [INF] dan [AMB] = belum terverifikasi, cek repo/slide user sebelum dijadikan kode.
   - Info tidak ada di notes -> bilang "not in notes". Jangan karang dari memori.
   - Teks spec kuis/tugas dari user mengalahkan notes.
3. Kalau AI tidak bisa buka link: minta user paste isi StudyPlan.md dan notes. Jangan pura-pura sudah baca.
4. Gaya mengajar dan format output: IKUTI Section 0B (style caveman-lite + format Open/Read/Explain/Before-After/Run/Push/Log + loop GUIDED-ATTEMPT). Section 0B wajib.
5. Prioritas: kerjakan P1 dulu (yang dikonfirmasi dosen), lalu P2, lalu P3.
6. Aturan mengubah status (JANGAN longgar):
   - `[ ]` belum / `[~]` sedang / `[x]` lulus.
   - Paham = `[x]` hanya jika user menjelaskan ALASAN (bukan sekadar apa) dengan kata sendiri DAN menjawab 2 pertanyaan recall benar tanpa hint.
   - Latihan = `[x]` hanya jika user menulis kodenya dari kosong (tanpa melihat jawaban) dan user mem-paste kode ke chat untuk direview AI. Kesalahan sintaks kecil boleh.
   - "Saya sudah paham" dari user saja BUKAN bukti. Pakai `[~]`.
   - Setiap perubahan status wajib ada bukti 1 kalimat di kolom Catatan atau Session Log.
7. AI tidak bisa melihat laptop user kecuali user paste atau screenshot. Jangan klaim sudah memverifikasi. Pengecualian: kalau user memberi izin dan token dan sesi punya akses bash, AI boleh clone branch `latihan` dan menjalankan F6 (log) sendiri. Kode user tetap user yang commit (lihat rule 13).
8. Log (Section 6 dan 7) bersifat append-only. Jangan hapus entri lama.
9. HANDOFF (merge berkala, bukan satu-satunya penyimpanan): saat user bilang "handoff", "simpan", "limit", "ganti AI", atau setelah selesai sekitar 3-5 item, atau kalau percakapan sudah panjang, AI proaktif mengingatkan lalu mengeluarkan:
   (a) FULL isi StudyPlan.md terbaru dalam SATU code block (Section 2, 3, 6, 7 diupdate dari ProgressLog; Section 0, 0B, 1, 4, 5, 8 tidak diubah), dan
   (b) perintah PowerShell dari Section 8 yang sudah terisi (termasuk baris `HANDOFF-MERGED` ke ProgressLog).
10. Jangan ubah struktur/heading file ini supaya AI lain tetap bisa parse.
11. READ SCOPE (hemat token, WAJIB): ikuti 0B "Read scope". Jangan fetch zip, folder, atau seluruh repo. Cari TODO di TODO-INDEX.md, fetch HANYA file yang berisi TODO yang diminta user.
12. COMMIT LOG (WAJIB): SETIAP balasan AI diakhiri blok F6 (0B). Tujuan: kalau AI kena limit mendadak, progress sudah ada di GitHub. Tidak ada balasan tanpa F6, termasuk balasan penjelasan saja.
13. ATURAN USER (koreksi sesi 2026-10-07, WAJIB, mengalahkan kebiasaan default AI):
    a. Cek ProgressLog.md dan state di Section 2 SEBELUM menyuruh apa pun. Jangan menyuruh ulang setup (env, venv, folder) yang sudah tercatat jalan. Jangan kirim perintah berisi placeholder seperti `<venv>`. Pakai path nyata.
    b. Zydan pemula total soal syntax Django. DILARANG menyuruh menebak syntax yang belum diajarkan. Urutan: jelaskan tujuan, tunjukkan kode lengkap (Before/After), jelaskan per baris, baru user mengetik sendiri.
    c. DILARANG pertanyaan recall/kuis/tebakan. Status Paham tetap `[~]` tanpa recall, dicatat jujur. Alasan konsep hanya ditanyakan kalau user sendiri yang mulai.
    d. SEMUA file kode Django (models, views, urls, forms, template) ditulis user sendiri di editor, AI hanya memandu lewat F1/F3. DILARANG menulis file kode lewat perintah PowerShell. Terminal hanya untuk menjalankan (migrate, runserver, shell, git).
    e. Label folder di tiap perintah harus sama dengan folder aktual user (baca dari prompt yang ia paste). Satu label salah = path salah.
    f. Log (F6) dijalankan AI sendiri dan di-push SEBELUM membalas, supaya `git pull --rebase` user sudah mencakup. Kode user: user yang commit, AI kirim terminal (git add path spesifik, commit, `git pull --rebase --autostash origin latihan`, `git push origin HEAD`).
    g. Raw link GitHub bisa stale (cache). Kalau bash dan token ada, clone branch `latihan` dan baca dari clone.

---

## 0B. STYLE + OUTPUT FORMAT (MANDATORY, overrides default chat habits)

Why: other AIs do not have Zydan's personal style skill, so the rules are embedded here.
Zydan = Fasilkom UI student. Cannot validate Django/JS code alone. Often forgets how to run venv, migrations, manage.py. So the AI guides step by step and spells out every command with its directory.

### Style (gaya-zydan + caveman-lite)

1. Chat language = Indonesian. Technical terms stay English. Gloss a new term once per session.
2. Caveman-lite: no greeting, no praise, no closing recap. Fragments ok. `->` for flow/cause. Code, commands, paths, identifiers stay exact.
3. No em-dash. Use period, comma, colon, parentheses.
4. Start with the answer. End with delta: what changed, what is still open, what starts next.
5. Every factual claim needs a source: notes node id, Zydan's repo file, or official docs actually opened. Unknown -> say "not in notes" or "belum tahu, cek: <how>". Never invent APIs, numbers, or file contents.
6. Do not ask Zydan to approve technical choices. Decide, state the assumption in one line, go. Ask only about intent.
7. One question per turn, max 30 words.
8. Zydan correct -> say correct + one reinforcing detail. Wrong -> say wrong, supportive tone, point to node id. No cheerleading.
9. "Done / works / safe" only after a check. Say what was checked (command run, output pasted).
10. Active recall: never put the answer next to the question. Grade honestly. Diagnose the weak concept, log it in Section 6.
11. Avoid: delve, leverage, robust, seamless, comprehensive, crucial, utilize, streamline.
12. Mulai jawaban dengan satu kalimat TUJUAN (kenapa langkah ini ada), baru kode. Jangan langsung perintah.
13. Tidak ada pertanyaan tebakan atau recall (Section 0 rule 13c). Kalau perlu cek paham, ajarkan lalu minta user menjalankan dan paste hasilnya.
14. User menulis semua kode Django sendiri di editor. AI tidak menulis file lewat terminal (rule 13d).
15. Nama di Django case-sensitive dan harus persis: `ProjectForm` bukan `Projectform`, `.exists()` bukan `.exist()`. `redirect('main:x')` merujuk `name=` di urls.py, BUKAN nama function.

### Mode: GUIDED-ATTEMPT (default)

Override sesi 2026-10-07: untuk syntax yang belum pernah diajarkan, AI mengajarkan kode lengkap dulu (tujuan, kode, penjelasan per baris), user mengetik dan menjalankan. Item yang diajarkan langsung = Latihan `[~]` paling tinggi. Tebakan baru diminta untuk pola yang sudah pernah dilihat user.

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

| | |
|---|---|
| Open | `views.py` |
| Path | `./main/views.py` |

F2 READ. When Zydan asks to read a TODO:

| | |
|---|---|
| Read | `// TODO: <exact text from the file>` |
| Explain | <1-3 short lines: what it asks, which concept, node id> |

F3 CHANGE. When modifying a file. One-line code goes inside the cell. Multi-line code: keep the Before/After rows as labels and put the code in fenced blocks right under each label. Show only the changed region plus 1-2 context lines, anchored by function name.

| | |
|---|---|
| Before | `<code>` |
| After | `<code>` |

F4 RUN. When Zydan must run something. Always state the directory, because Zydan forgets. Never assume the venv is active, say when it is needed.

`PS: <current directory>`
```powershell
<command>
```
Why: <one line, what this command does>
Expect: <one line, what success looks like + the most common error and its meaning>

F5 PUSH. After a verified step. List exact files, no blind `git add .`. Commit message starts with the checklist id.

```powershell
git status --short
git add <file1> <file2>
git commit -m "<ID>: <what changed>"
git push origin HEAD
```

Kalau step terverifikasi DAN ada file kode, jangan kirim F5 terpisah: tambahkan file itu ke `git add` di F6 (satu commit).

F6 LOG. WAJIB di akhir SETIAP balasan. Satu baris log + commit + push. Jalankan dari folder `Asistensi-1`, branch `latihan` (cek: `git branch --show-current`). Isi `<...>` oleh AI. Teks log tidak boleh mengandung `"`, `$`, atau backtick.

`PS: ...\asistensi-kuis-pbp\Asistensi-1`
```powershell
$l = "$(Get-Date -Format 'yyyy-MM-dd HH:mm') | <AI> | <ID> | <event> | next: <next>"
[IO.File]::AppendAllText("$PWD\ProgressLog.md", "$l`n", [Text.UTF8Encoding]::new($false))
git add ProgressLog.md <file kode terverifikasi, kalau ada>
git commit -m "log: <ID> <event>"
git push origin HEAD
```
Why: simpan posisi belajar ke GitHub tiap balasan. Contoh nyata di Section 7B.
Expect: baris `[latihan xxxxxxx] log: ...` lalu `branch 'latihan' -> ...`. Kalau push ditolak: `git pull --rebase origin latihan` lalu ulangi `git push origin HEAD`.

Nilai `<event>` (pilih satu): `READ`, `EXPLAIN`, `ATTEMPT`, `REVIEW`, `H1`, `H2`, `H3`, `RUN-OK`, `RUN-FAIL`, `PASS-paham`, `PASS-latihan`, `WEAK:<konsep>`, `HANDOFF-MERGED`. Perubahan status checklist (Section 0 rule 6) WAJIB tercatat di sini dengan bukti 1 kalimat di `<next>` atau event.

### Session start (once per new AI session)

1. Do Section 0 rule 1 (3-line summary), termasuk fetch ProgressLog.md.
2. Fetch TODO-INDEX.md (link di header). Jangan minta user paste `git ls-files`, jangan fetch zip atau folder.
3. Kalau TODO-INDEX.md perlu dibuat ulang, user jalankan dari `Asistensi-1`:

`PS: ...\asistensi-kuis-pbp\Asistensi-1`
```powershell
Get-ChildItem -Recurse -File -Include *.py,*.html,*.js | Where-Object { $_.FullName -notmatch '\\(venv|env|\.venv|__pycache__)\\' } | Select-String -Pattern 'TODO|BONUS'
```

### Read scope (hemat token, WAJIB)

Why: AI kena limit kalau membaca terlalu banyak. Baca sekecil mungkin.

1. Sumber state hanya 3 file kecil: StudyPlan.md, ProgressLog.md, TODO-INDEX.md.
2. User minta "TODO 3 soal2" -> cari baris di TODO-INDEX.md -> fetch raw HANYA file itu (branch `latihan`):
   `https://raw.githubusercontent.com/zidan-do-pbp/Asistensi-Kuis-PBP/latihan/Asistensi-1/<path dari index>`
3. Jangan fetch file lain, folder lain, atau soal lain. Jangan baca file yang tidak mengandung TODO yang diminta.
4. Notes (Section 1) hanya di-fetch saat butuh penjelasan node tertentu, sekali per sesi.
5. Jawaban/solusi ada di branch `solution`. Fetch HANYA kalau user minta H3 atau review, dan HANYA file yang sama:
   `https://raw.githubusercontent.com/zidan-do-pbp/Asistensi-Kuis-PBP/solution/Asistensi-1/<path>`
   Jangan preload, jangan tampilkan sebelum user mencoba (aturan GUIDED-ATTEMPT).
6. Link tidak bisa dibuka -> minta user paste potongan file TODO itu saja. Jangan pura-pura sudah baca.

### Branch layout

| Branch | Isi | Dipakai untuk |
| ------ | --- | ------------- |
| `main` | template bersih (TODO saja) + StudyPlan | sumber reset, jangan dikerjakan langsung |
| `latihan` | kerja user + ProgressLog.md + StudyPlan terupdate | semua latihan dan log F6 |
| `solution` | jawaban lengkap | rujukan H3 dan review |

Reset satu soal ke template: `git checkout main -- soal2` (dari `Asistensi-1`, di branch `latihan`).

### Run cheatsheet (standard Python/Django commands, verify against the repo README/requirements)

Run `manage.py` commands from the folder that contains `manage.py`. Check: `Test-Path .\manage.py`.

| Need | Command | Note |
|------|---------|------|
| create venv | `python -m venv <venv>` | once per clone |
| activate venv | `.\<venv>\Scripts\Activate.ps1` | prompt shows `(<venv>)`. If blocked: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first |
| install deps | `pip install -r requirements.txt` | venv must be active. Lab bottleneck, see notes `tip:quiz_env` |
| apply DB schema | `python manage.py migrate` | run after clone or after new migration files |
| make migration | `python manage.py makemigrations` | only after editing models.py |
| run server | `python manage.py runserver` | open http://127.0.0.1:8000/ , stop with Ctrl+C |
| Django shell | `python manage.py shell` | leave with `exit()`. Used for creating users/groups, see A2.0 |
| run tests | `python manage.py test` | only if the task has tests |

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
- Soal latihan di repo (folder `soal1`, `soal2`, `soal3`, tema model/MVT/test Book): checklist S1-S3 di Section 3. Lokasi tepatnya ada di TODO-INDEX.md.
- Project latihan Zydan sendiri (A1-A4/B1-B4, di luar repo soal1-3): dibuat dari nol di `Asistensi-1\quiz2-latihan\` (venv `env`, project config `quiz2_demo`, app `main`). File ini TIDAK dicommit ke repo soal1-3 secara campur, `.gitignore` sudah pasang `env/`, `db.sqlite3`, `__pycache__/`, `*.pyc`.

---

## 2. STATE SAAT INI (AI: update tiap handoff)

- Terakhir diupdate: 2026-10-07 oleh Claude (sesi 2: A2.0-A2.2 jalan terverifikasi, kode A2.3 sudah diajarkan)
- Total sesi belajar: 2
- Progres Paham: 3/46 | Progres Latihan: 1/37 (A2.0-A2.2 belum dihitung `[x]`: kode diajarkan langsung, Paham tanpa recall)
- Fokus sekarang: A2.3 `edit_project` (views.py + urls.py). Berhenti di sini dulu atas permintaan user.
- NEXT ACTION: user menulis `edit_project` di `main/views.py` (import `get_object_or_404`) dan path `projects/<int:project_id>/edit/` bernama `edit_project` di `main/urls.py`, lalu AI kirim perintah commit. Sesudahnya: tombol Edit di `projects.html`, tes owner1 dan editor1 (boleh) dan akun tanpa role (403), lalu A2.4 `delete_project` (POST only, Owner only), A2.6 tombol per role + csrf_token.
- Jalur belajar P1 sisa: A2.3 -> A2.4 -> A2.6 -> B1.1 -> B1.2 -> B2.1 -> B2.4 -> B2.5 -> B3.1 -> B3.2 -> B4.1 -> B4.2 -> B4.3 -> A4.1
- Fakta project (jangan tanya ulang): project Django ada di `Asistensi-1\quiz2-latihan\` (`manage.py`, venv `env\` di folder yang sama, project `quiz2_demo`, app `main`). Aktifkan: `.\env\Scripts\Activate.ps1` dari `quiz2-latihan`, prompt `(env)`. Akun tes (sudah dibuat lewat shell): `owner1`/`owner12345` (Group Owner), `editor1`/`editor12345` (Group Editor). Template: `projects.html`, `projects_form.html`. Route name: `login`, `register`, `logout`, `project_list`, `create_project`, `edit_project` (belum). Login diubah redirect ke `main:create_project`. Model `Project`: name, description, starred_by (M2M User). Cek role pakai `request.user.groups.filter(name=...).exists()`.
- Catatan kondisi user: pemula total soal Django, butuh penjelasan tujuan dulu dan kode lengkap, BUKAN tebakan (user marah kalau disuruh menebak syntax, 2026-10-07). Menolak pertanyaan recall. Sering ketuker `{'key': val}` (dict) vs `{'key', val}` (set). Sering salah nama (case, huruf s, nama route vs function). Aturan lengkap di Section 0 rule 13.

---

## 3. CHECKLIST

Kolom: P = prioritas (P1 dikonfirmasi dosen/inti, P2 penting, P3 bonus). Node = id di notes (grep di Section 3 notes untuk edges). Tgl = terakhir disentuh.

### Django (A1-A4)

| ID | P | Topik (node id) | Paham | Latihan | Tgl | Catatan |
|----|---|-----------------|-------|---------|-----|---------|
| A1.1 | P1 | register: UserCreationForm, save, redirect login (`fn:register`) | [x] | [~] | 2026-10-07 | Paham: jelasin alasan is_valid sebelum save (cegah data invalid masuk DB) + 2 recall benar. Latihan: dikasih H3 setelah stuck lama di if-statement, bukan murni dari nol. Verified browser: form render benar, submit sukses (302). |
| A1.2 | P1 | login: AuthenticationForm, login(), set_cookie (`fn:login_user`) | [x] | [~] | 2026-10-07 | Paham: jelasin alasan data= keyword + get_user ambil bukan query baru, 2 recall benar. Latihan: H3, 2 bug attempt (login_user manggil dirinya sendiri bukan Django login, dict vs set). Verified browser: POST login sukses (302). |
| A1.3 | P2 | logout: POST only 405, logout(), delete_cookie (`fn:logout_user`) | [x] | [x] | 2026-10-07 | Latihan: ditulis dari kosong, 1 bug logic (lupa panggil logout()) dikoreksi sendiri setelah ditunjuk. Paham: jelasin alasan GET berbahaya (trigger pasif) pakai kata sendiri. Verified browser: GET /logout/ -> 405 (manual test, screenshot). |
| A1.4 | P2 | cookie last_login, flags max_age/httponly/samesite, no secrets (`concept:cookie_flags`, `rule:no_secrets_in_cookie`) | [ ] | [ ] | - | Belum disentuh. Cookie value masih placeholder string, bukan timestamp asli (format `[AMB]` di notes, perlu diisi + 3 flag bonus). |
| A2.0 | P1 | Django shell: buat user + assign Group (`tip:lab_prep_a2`, `concept:role_group`) | [~] | [~] | 2026-10-07 | Kode diajarkan langsung (H3, user belum pernah lihat syntax). Verified di shell: owner1 di Group Owner, editor1 di Group Editor (`user.groups.all()`). Alasan no_superuser dijawab separuh, tanpa recall. |
| A2.1 | P1 | Role = Group, tanpa superuser (`concept:role_group`, `rule:no_superuser`) | [~] | - | 2026-10-07 | Dijelaskan AI. Jawaban user: superuser = admin yang bisa bikin user (separuh benar). Belum lewat syarat recall. |
| A2.2 | P1 | create_project: Owner only, else 403 (`fn:create_project`) | [~] | [~] | 2026-10-07 | Kode diajarkan langsung. User menulis ulang di editor dan memperbaiki 5 bug nama. Verified browser: owner1 simpan form (data tampil), non-Owner kena 403 (screenshot). Model Project, ProjectForm, projects.html, projects_form.html dibuat sebagai scaffold. Commit 41bce26 dan 3647f72. |
| A2.3 | P1 | edit_project: cek permission DULU, lalu get_object_or_404 (`fn:edit_project`) | [ ] | [ ] | - | Kode dan penjelasan sudah diberikan (name__in Owner/Editor, get_object_or_404 pk=project_id, instance=project). User belum menulis/menjalankan. NEXT ACTION. |
| A2.4 | P1 | delete_project: POST only + Owner only (`fn:delete_project`) | [ ] | [ ] | - | |
| A2.5 | P2 | toggle_star: POST + login, add/remove starred_by (`fn:toggle_star`) | [ ] | [ ] | - | |
| A2.6 | P1 | template project_list: tombol per role + csrf_token + server-side check (`tmpl:project_list`, `rule:server_side_check`, `rule:post_csrf`) | [ ] | [ ] | - | |
| A2.7 | P3 | bonus prefetch_related('starred_by') (`fn:project_list_bonus`) | [ ] | [ ] | - | |
| A3.1 | P3 | A3 tidak dijelaskan di asistensi, kerjakan dari deskripsi + kode di GitHub tutorial | [ ] | [ ] | - | |
| A4.1 | P1 | login_required + login_url di dashboard, tampilkan username (`fn:dashboard_protected`) | [ ] | [ ] | - | Ditunda, dikerjakan setelah A2 selesai (bisa reuse app `main` yang sama). |

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
| B2.5 | P1 | jebakan kurung: handler tanpa `()` (`trap:parentheses_on_handler`) | [ ] | [ ] | - | |
| B3.1 | P1 | loadReports: fetch GET, isLoading guard, try/catch/finally (`fn:loadReports`, `concept:busy_flag`) | [ ] | [ ] | - | |
| B3.2 | P1 | async/await dan kenapa finally (`concept:async_await`, `why:finally`) | [ ] | - | - | |
| B3.3 | P3 | bonus: validasi Array.isArray sebelum replace state | [ ] | [ ] | - | |
| B4.1 | P1 | submitReport: event 'submit' (bukan click), preventDefault, guard, validasi (`fn:submitReport`) | [ ] | [ ] | - | |
| B4.2 | P1 | POST fetch + CSRF header + parsing error JSON (`rule:post_csrf`) | [ ] | [ ] | - | |
| B4.3 | P1 | urutan isSubmitting=false SEBELUM closeModal (`trap:close_modal_order`) | [ ] | [ ] | - | |
| B4.4 | P2 | let vs const (`concept:let_vs_const`) | [ ] | - | - | |

### Soal latihan repo (S1-S3, lokasi file: lihat TODO-INDEX.md)

| ID   | P  | Topik (file, TODO)                                                  | Paham | Latihan | Tgl | Catatan |
| ---- | --- | ------------------------------------------------------------------ | ----- | ------- | --- | ------- |
| S1.1 | P1 | soal1 models.py TODO 1: field title, author, stock                  | [ ]   | [ ]     | -   |         |
| S1.2 | P1 | soal1 models.py TODO 2: `__str__` kembalikan judul                  | [ ]   | [ ]     | -   |         |
| S1.3 | P1 | soal1 models.py TODO 3: `is_available` (stock > 0)                  | [ ]   | [ ]     | -   |         |
| S1.4 | P3 | soal1 models.py BONUS: `is_low_stock` (1 sampai 3)                  | [ ]   | [ ]     | -   |         |
| S2.1 | P1 | soal2 quiz_mvt/urls.py TODO 1: include main.urls                    | [ ]   | [ ]     | -   |         |
| S2.2 | P1 | soal2 main/views.py TODO 2: ambil Book, kirim key "books"           | [ ]   | [ ]     | -   |         |
| S2.3 | P1 | soal2 main/urls.py TODO 3: path "books/" nama "book_list"           | [ ]   | [ ]     | -   |         |
| S2.4 | P1 | soal2 templates book_list.html TODO 4: loop, Tersedia/Stok habis/empty | [ ]   | [ ]     | -   |         |
| S3.1 | P1 | soal3 main/tests.py TODO 1: setUp buat Book                         | [ ]   | [ ]     | -   |         |
| S3.2 | P1 | soal3 main/tests.py TODO 2: test is_available                       | [ ]   | [ ]     | -   |         |
| S3.3 | P1 | soal3 main/tests.py TODO 3: test status 200 + template               | [ ]   | [ ]     | -   |         |
| S3.4 | P1 | soal3 main/tests.py TODO 4: test judul, penulis, Tersedia di response | [ ]   | [ ]     | -   |         |
| S3.5 | P1 | soal3 main/tests.py TODO 5: test daftar kosong                      | [ ]   | [ ]     | -   |         |
| S3.6 | P3 | soal3 main/tests.py BONUS: hapus @skip, test stok 0                 | [ ]   | [ ]     | -   |         |

### Logistik kuis

| ID | P | Topik (node id) | Paham | Latihan | Tgl | Catatan |
|----|---|-----------------|-------|---------|-----|---------|
| Q.1 | P2 | cek setup lab 1-2 hari sebelum (jaringan, venv, dependency) (`tip:quiz_env`) | [ ] | - | - | |
| Q.2 | P2 | lab jaringan terbatas: hapus link eksternal (favicon/font) yang bikin error (`tip:lab_restricted_network`) | [ ] | - | - | |
| Q.3 | P3 | tahu unit testing dan Selenium itu apa (kemungkinan tidak keluar) | [ ] | - | - | |

### Self-test bank (dari notes Section 1, tandai kalau user jawab benar tanpa hint)

- [x] Kenapa semua aksi ubah data harus POST + CSRF token? (jawab via konteks logout: GET bisa ke-trigger pasif tanpa niat user)
- [ ] Status HTTP apa untuk: method salah, tidak punya izin, objek tidak ada? (405, 403, 404)
- [ ] Kenapa `textContent` bukan `innerHTML`? Kenapa event `submit` bukan `click`? Kenapa `finally`?
- [ ] Apa yang harus terjadi sebelum `closeModal()` di B4 dan kenapa?
- [ ] Cara tercepat melindungi satu view dari user anonim di lab?
- [ ] Apa yang rusak di lab saat internet dibatasi dan cara memperbaikinya?
- [ ] Kenapa menyembunyikan tombol di template BUKAN keamanan?

---

## 4. KRITERIA LULUS (ringkas, detail ada di Section 0 poin 6)

- Paham = bisa jelaskan alasan + 2 recall benar tanpa hint.
- Latihan = tulis kode dari nol tanpa contek, dan di-review AI.
- Kuis nyata kemungkinan beda dari tutorial: yang dihafal adalah potongan konsep, bukan satu jawaban persis.

---

## 5. OPEN VERIFICATION (cek ke repo/slide user sebelum percaya; dari notes Section 5)

- [ ] V1 format string timestamp cookie `last_login` (A1) — saat ini masih placeholder string `'placeholder'` di kode Zydan, bukan timestamp asli.
- [ ] V2 bentuk nilai `login_url` (path atau nama route) (A4)
- [ ] V3 definisi `user.is_owner` / `user.is_editor` di models (A2)
- [ ] V4 DOM id pasti: `result-count`, id empty message (B1)
- [ ] V5 nama header CSRF + encoding body di B4 (kemungkinan `X-CSRFToken` + `JSON.stringify`)
- [ ] V6 key JSON list laporan di B3 (`data.reports` atau array langsung)
- [ ] V7 tanggal kuis pasti
- [ ] V8 tujuan redirect setelah login/logout sukses, saat ini placeholder `redirect('main:login')` dipakai di dua-duanya (login balik ke login, logout juga ke login), perlu diganti ke `home`/`dashboard` begitu halaman itu ada.

---

## 6. KELEMAHAN / MISKONSEPSI (append-only)

| Tgl | Item | Kesalahan atau miskonsepsi user | Status (open/fixed) |
|-----|------|----------------------------------|---------------------|
| 2026-10-07 | A1.1 | `if form.is_valid:` tanpa kurung (truthy selalu True), ketemu lagi di A1.2 | fixed (dikoreksi sendiri setelah ditunjuk, 2x kejadian) |
| 2026-10-07 | A1.1/A1.2 | `{'form', form}` (set) vs `{'form': form}` (dict) di context render, terjadi 2x (A1.1 lewat drill, A1.2 lewat bug asli) | fixed, tapi perlu diwaspadai berulang di B1-B4 (context dict js/django beda tapi pola typo serupa mungkin muncul lagi) |
| 2026-10-07 | A1.1 | Awalnya kira alasan is_valid() sebelum save() itu "biar ga bisa dispam", bukan soal data integrity/cleaned_data | fixed setelah 2x review + contoh konkret password mismatch |
| 2026-10-07 | A1.2 | Salah urutan argumen `AuthenticationForm(request.POST)` vs `AuthenticationForm(data=request.POST)`, belum tau kenapa harus keyword `data=` | fixed setelah dijelasin positional arg request vs data |
| 2026-10-07 | A1.2 | `login_user(request, form.get_user())` manggil dirinya sendiri (rekursif) alih-alih Django `login()`, TypeError di traceback asli saat browser test | fixed |
| 2026-10-07 | - | Sempat salah struktur project: `django-admin startproject quiz2_demo` tanpa titik (`.`) bikin manage.py nested 2x dan folder ganda tabrakan, harus di-reset total (`Remove-Item -Recurse`) dan redo dengan titik | fixed |
| 2026-10-07 | A2.2 | Nama tidak persis: `Projectform` (harus `ProjectForm`), `.exist()` (harus `.exists()`), `redirect('main:projects_list')` dan `'main:projects_form'` (route sebenarnya `project_list` dan `create_project`) | fixed (dikoreksi di review) |
| 2026-10-07 | A2.2 | Kira `redirect('main:create_project')` merujuk nama function, padahal merujuk `name=` di `path(...)` urls.py | fixed (dijelaskan 3 peran: alamat, function, name=) |
| 2026-10-07 | A2.2 | Template `projects.html`: penutup `<li>` ditulis `<li>` (harus `</li>`), bikin bullet kosong | fixed |
| 2026-10-07 | A2.0 | Ketik `Owner` polos di shell (NameError): belum paham Group dibuat lewat `Group.objects.create(...)`, bukan mengetik nama | fixed (diajarkan langsung) |

---

## 7. SESSION LOG (append-only, entri terbaru di bawah)

Format: `YYYY-MM-DD | AI (nama/model) | aktivitas | item disentuh + perubahan status | next`

- 2026-10-06 | Claude | setup file dari notes transkrip | tidak ada | mulai A4.1
- 2026-10-06 | Claude | tambah Section 0B (style + format output + cheatsheet run) | tidak ada | mulai A4.1
- 2026-10-06 | Claude | tambah Read scope, F6 commit log, ProgressLog.md, branch layout, checklist S1-S3; koreksi hitungan Latihan 29 -> 23 (+14 baris S = 37) | tidak ada | bersihkan repo, buat branch latihan, mulai A4.1
- 2026-10-07 | Claude | sesi pertama: setup project `quiz2-latihan` dari nol (venv, startproject, startapp, INSTALLED_APPS, migrate), sempat ada struktur ganda (startproject tanpa titik) direset ulang; kerjakan A1.1 (register), A1.2 (login_user), A1.3 (logout_user) sampai verified browser; user tolak permintaan pakai personal access token GitHub di chat untuk commit/push (ditolak konsisten, alasan keamanan credential leak), AI tetap hanya menulis command, user yang menjalankan | A1.1 Paham [x] Latihan [~], A1.2 Paham [x] Latihan [~], A1.3 Paham [x] Latihan [x] | handoff, lanjut A2.0

- 2026-10-07 | Claude | sesi 2: A2.0 (shell: Group Owner/Editor, owner1/editor1), scaffold Project model + ProjectForm + projects.html + projects_form.html, A2.2 create_project (Owner only, 403 terverifikasi browser); AI clone branch latihan dan push log sendiri atas izin user (token scoped repo, disarankan revoke), kode user tetap user yang commit; user menolak tebakan, recall, dan file kode ditulis via terminal, aturan dicatat di Section 0 rule 13; kode A2.3 diajarkan | A2.0 Paham [~] Latihan [~], A2.1 Paham [~], A2.2 Paham [~] Latihan [~], A2.3 belum | user tulis edit_project + path edit, commit, lanjut A2.3 tes

### 7B. ProgressLog.md (file terpisah, append-only, ditulis lewat F6)

Format baris: `YYYY-MM-DD HH:mm | AI | ID | event | next: ...`

Contoh:

    2026-10-06 14:05 | Claude | S1.1 | READ | next: user coba tulis field title, author, stock
    2026-10-06 14:20 | Claude | S1.1 | REVIEW | next: stock harus PositiveIntegerField default 0, user salah di default
    2026-10-06 14:31 | Claude | S1.1 | PASS-latihan | next: S1.2 (tulis dari kosong, tanpa hint)

---

## 8. CARA SIMPAN PROGRESS KE GITHUB (HANDOFF)

AI mengeluarkan full isi file terbaru, user menjalankan di `...\asistensi-kuis-pbp\Asistensi-1`, branch `latihan` (isi `<<...>>` oleh AI). Pola here-string: penutup harus ada di awal baris tanpa spasi.

    $ErrorActionPreference = 'Stop'
    $f = Join-Path (Get-Location).Path 'StudyPlan.md'
    $c = @'
    <<FULL ISI StudyPlan.md TERBARU DI SINI>>
    '@
    [System.IO.File]::WriteAllText($f, $c, [System.Text.UTF8Encoding]::new($false))
    [System.IO.File]::AppendAllText((Join-Path $PWD.Path 'ProgressLog.md'), ("$(Get-Date -Format 'yyyy-MM-dd HH:mm') | <<AI>> | - | HANDOFF-MERGED | next: <<next>>`n"), [System.Text.UTF8Encoding]::new($false))
    git pull --rebase --autostash origin latihan
    git add StudyPlan.md ProgressLog.md
    git commit -m "progress: <<ringkasan singkat, contoh: A4.1 paham, A2.0 sedang>>"
    git push origin HEAD

(Catatan: di atas, baris `@'` dan `'@` harus ditulis tanpa indentasi saat dijalankan.)

Prompt untuk AI baru (user tinggal paste):
"Baca https://raw.githubusercontent.com/zidan-do-pbp/Asistensi-Kuis-PBP/latihan/Asistensi-1/StudyPlan.md lalu ikuti AI PROTOCOL di dalamnya. Baca juga https://raw.githubusercontent.com/zidan-do-pbp/Asistensi-Kuis-PBP/latihan/Asistensi-1/ProgressLog.md dan https://raw.githubusercontent.com/zidan-do-pbp/Asistensi-Kuis-PBP/main/Asistensi-1/TODO-INDEX.md. Jangan baca file lain kecuali TODO yang saya minta. Lanjutkan dari entri log terakhir. Akhiri setiap balasan dengan blok F6."