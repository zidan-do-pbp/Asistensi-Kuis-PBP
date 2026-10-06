---
type: lecture-knowledge-map
source: GMT20261004-133647_Recording_transcript.vtt (zoom auto-captions, ID/EN mix, ~1h20m)
recorded: 2026-10-04 (from filename)
topic: Django authentication/authorization + JS web interactivity. Quiz 2 prep (Tutorial 4 + 5)
speakers: Jaysen Lestari (Django A1-A2), Neal (A4 + quiz intel), Angelo "Fuun" (B1, B4), Amelia Juliawati (B2, B3)
style: caveman-lite + graph map (see section 6 for provenance)
---

# 0. LEGEND (read first)

Rules for Claude using this file:
1. Trust `[EXT]`. Treat `[INF]` and `[AMB]` as unverified. Before writing code that depends on one, check user's repo or slides.
2. Info not in file -> say "not in notes". Do not fill gaps from memory.
3. Quiz spec text beats this file.

Style: articles/filler dropped. `->` = leads to / causes. Identifiers, code, strings kept exact.

Confidence tags (graphify-style):
- `[EXT]` said in recording. Timestamp `@mm:ss` or `@h:mm:ss` points to transcript.
- `[INF]` ASR repaired, or standard API filled by note-taker. Not shown on screen in transcript.
- `[AMB]` transcript unclear. Do not rely on it.

Node id = `kind:name`. kinds: `fn` `route` `tmpl` `concept` `rule` `trap` `why` `tip`.
Edge = `A -rel-> B [tag]`. All edges in section 3. Grep node id there.

Read order: section 1 -> community in section 2 -> grep id in section 3 -> check section 5 before trusting any identifier.

Task naming: A1-A4 = Django tutorial tasks. B1-B4 = JS tutorial tasks.

---

# 1. REPORT (entry point)

## Communities

| id | name | tasks | speaker |
|----|------|-------|---------|
| C1 | django-auth-cookies | A1 | Jaysen |
| C2 | django-authz-roles-login-required | A2, A4 | Jaysen, Neal |
| C3 | js-render-filter-modal | B1, B2 | Angelo, Amelia |
| C4 | js-ajax-fetch | B3, B4 | Amelia, Angelo |
| C5 | quiz-intel-lab-logistics | - | Neal |

A3 not explained. Jaysen: practice only, description + code on GitHub (@24:10).

## God nodes (most connected, learn first)

1. `rule:server_side_check` : every permission rule enforced in backend, UI hiding is cosmetic.
2. `concept:role_group` : Django `Group` = Owner / Editor. Drives create/edit/delete.
3. `rule:post_csrf` : all data-changing actions = POST + CSRF token. Django forms and JS fetch both.
4. `fn:renderReports` + `fn:applyFilters` : JS core pair. Every state change ends in `renderReports(applyFilters())`.
5. `concept:busy_flag` : `isLoading` / `isSubmitting` + `try/catch/finally`. Same guard pattern in B3 and B4.

## Surprising connections

- `why:textContent_not_innerHTML` (B1) and `rule:server_side_check` (A2) = same idea: never trust client-side/user input.
- `fn:logout_user` (A1) and `fn:delete_project` (A2) = same shape: POST only, else 405/403.
- `trap:parentheses_on_handler` (B2) is why `fn:openModal` works only when passed, not called.

## Quiz signals (full list in C5)

- Lecturer-confirmed topics: JavaScript, login page (incl. CSRF token + send data to DB), restrict page to logged-in users.
- Jaysen @12:18: restricting feature/endpoint by user = core of auth material, "pasti keluar di kuis".

## Suggested questions this map answers

- Which HTTP status for which failure in A1/A2? (405 wrong method, 403 no permission, 404 missing object)
- Why `textContent` not `innerHTML`? Why `submit` not `click`? Why `finally`?
- What must happen before `closeModal()` in B4 and why?
- How to protect one view from anonymous users, fastest way in lab?
- What breaks in lab when internet restricted, and how to fix?

---

# 2. NODES

## C1 django-auth-cookies (A1, @00:32-@08:37)

`concept:a1_scope` [EXT @00:45, @02:44]
- Implement register / login / logout. Edit `views.py` only. Do not touch template, settings, model.
- Use Django built-in auth, same as Tutorial 4.

`fn:register` [EXT @03:08-@04:48]
- Methods: GET + POST.
- `form = UserCreationForm(request.POST or None)`
- POST + `form.is_valid()` -> `form.save()` -> redirect to login route (spoken "main login", `[INF]` `main:login`).
- Else -> `render` register template with `form`. GET = empty form. POST invalid = form + errors, no user created.
- Template path prefix unclear `[AMB]`.

`fn:login_user` [EXT @04:48-@07:08]
- `form = AuthenticationForm(data=request.POST or None)`
- POST + valid -> `login(request, form.get_user())` -> `response = redirect(home)` -> `response.set_cookie('last_login', <timestamp>)` -> return response.
- Invalid or GET -> `render` login template with `form`.
- Cookie name `last_login`. Value = timestamp in format the task spec demands. Jaysen read it as year-month-date hour minute seconds, with timezone helper. Exact format string `[AMB]`.
- Bonus (all three in `set_cookie`): `max_age=3600`, `httponly=True`, `samesite='Lax'`.

`fn:logout_user` [EXT @07:14-@08:23]
- POST only. Not POST -> `HttpResponseNotAllowed` (405) `[INF]` exact call `HttpResponseNotAllowed(['POST'])`.
- POST -> `logout(request)` -> `response = redirect(home)` -> `response.delete_cookie('last_login')` -> return.
- Order matters: delete cookie on same response that redirects.

`rule:no_secrets_in_cookie` [EXT @02:09]
- Never store password, username, or other credentials in cookie.

`concept:cookie_flags` [EXT @02:19-@02:44 + INF]
- `max_age=3600` = lifetime 3600 s = 1 h `[INF unit]`.
- `httponly=True` = JS cannot read cookie `[INF standard]`.
- `samesite='Lax'` : Jaysen gloss = cookie not applied when user enters site via redirect from another app. This is simplified and imprecise. Verify real semantics on MDN `Set-Cookie`, SameSite.

## C2 django-authz-roles-login-required (A2 @08:45-@24:03, A4 @27:50-@32:48)

`concept:role_group` [EXT @08:45-@09:16]
- Role stored as Django `Group`. No `is_superuser` check in app logic. Ignore superuser.
- Roles heard: user with no special role (visitor), Editor, Owner. Jaysen said "four roles", listed three. Fourth likely anonymous `[INF]`.

`rule:no_superuser` [EXT @08:45, @17:37-@17:54]
- Jaysen slipped and wrote superuser check live, then corrected. Do not copy that.

`tip:lab_prep_a2` [EXT @09:16-@09:54]
- Run `migrate` and load project data first.
- Quiz may need role testing: create users from Django shell (`python manage.py shell`). Learn this.
- Group assignment API not shown `[INF]` standard Django (`user.groups.add(...)`).

`fn:create_project` [EXT @10:40, @14:04-@15:09]
- Allowed: Owner only `[INF]`. Spoken "anggota grup user", confirmed Owner by template rule @11:33 and @22:15.
- Logged-in user without role -> 403.
- `form = ProjectForm(request.POST or None)`; POST + valid -> `form.save()` -> redirect to project list. Else render `project_form.html` with `form`.

`fn:edit_project` [EXT @15:51-@18:52]
- Allowed: Editor or Owner. Else 403.
- Permission check FIRST, then fetch object by `project_id` with get-or-404 (`[INF]` `get_object_or_404`).
- `form = ProjectForm(request.POST or None, instance=project)`. POST + valid -> save -> redirect list. Else render `project_form.html`, heading "Edit Project".

`fn:delete_project` [EXT @18:57-@19:50]
- POST only. Owner only. Not owner -> 403 immediately. Owner -> fetch by id -> delete -> redirect to list.

`fn:toggle_star` [EXT @19:50-@21:41]
- POST only + login required (`[INF]` `@login_required`).
- Fetch project. If `project.starred_by.filter(pk=request.user.pk).exists()` -> `project.starred_by.remove(request.user)`. Else `.add(request.user)`. Redirect list.

`fn:project_list_bonus` [EXT @11:52, @13:14-@13:52]
- Replace `Project.objects.all()` with `Project.objects.prefetch_related('starred_by')`. Spoken "private related" `[INF]`.
- Reason: cut per-row queries for stars `[INF]`.

`tmpl:project_list` [EXT @21:49-@24:03]
- Create button: Owner only. Edit button: Editor or Owner. Delete button: Owner only.
- Spoken helpers `user.is_owner`, `user.is_editor` in `{% if %}`. Where defined (models) not shown `[AMB]`. Check models before using.
- Delete form needs `{% csrf_token %}`.

`rule:server_side_check` [EXT @11:33-@11:52]
- Hiding buttons in template is not security. Backend check mandatory. HTML-only or JS-only validation insufficient.

`rule:post_csrf` [EXT @12:36-@12:47]
- Every data-changing action = POST + `{% csrf_token %}`. Tutorial also covers CSRF settings `[AMB]` exact setting.

`concept:a2_scope` [EXT @12:27]
- Edit only `views.py` (main app) + `project_list.html`.

`fn:dashboard_protected` (A4, Neal) [EXT @27:50-@32:48]
- Demo site: home, dashboard, login. Problem: dashboard reachable without login.
- Fix: import Django `login_required` (`[INF]` `from django.contrib.auth.decorators import login_required`). Wrap dashboard view with it. Set `login_url` to the login URL defined in `urls.py`. Spoken value "login" `[AMB]` path vs name.
- Result: logged-out visit blocked, sent to login `[INF]`.
- Dashboard shows username after login: take user from `request` in render context. Exact expression `[AMB]` (`user.username` or `request.user.username`, both normally available `[INF]`).
- Lab shortcut: skip building register/login. Create hardcoded accounts via `manage.py shell` with ~5 lines, paste, `exit` (@28:09-@28:37). Snippet not in transcript `[INF]` standard `create_user`.

## C3 js-render-filter-modal (B1 @41:54-@47:39, B2 @47:47-@1:00:08)

`fn:renderReports` (B1) [EXT @41:54-@47:39]
- Scope: change only `renderReports`. Data already in `reports` array. No fetch yet.
- Steps:
  1. `reportList.innerHTML = ''` on every call. Reason: no stale/accumulated items.
  2. per report: `const card = document.createElement('article')`, `card.className = 'card'`. Element lives in memory until appended.
  3. status badge: `report.status === 'hilang'` -> lost badge class + text. Else found badge class + text. Class names `[INF]` (`badge-hilang`, `badge-ditemukan`). "batch" in transcript = badge.
  4. `card.innerHTML` = skeleton with badge, empty `<h2>`, empty `<p>`.
  5. `card.querySelector('h2').textContent = report.title`; `p` `.textContent` = location.
  6. append card to `reportList`.
- Bonus summary: `lostCount = data.filter(r => r.status === 'hilang').length`. `foundCount = data.length - lostCount`. Write into element id `result-count` (spoken "result Count"), example "3 laporan: 2 hilang, 1 ditemukan".
- Empty message: `emptyMessage.hidden = data.length !== 0`. Has data -> hidden `true`. Empty -> `false` -> message shows. Element id `[AMB]` (spoken "Mt Message", likely `empty-message`).
- Elements fetched with `document.getElementById`.

`why:textContent_not_innerHTML` [EXT @44:36-@45:29]
- `textContent` treats value as plain text. Injected script shows as text, never runs. Blocks XSS (Angelo: "setahuku" = hedged recall, concept correct).
- `innerHTML` with user value is parsed as HTML. Script may run.

`fn:applyFilters` (B2) [EXT @49:55-@54:48]
- Returns filtered array. Does not render.
- `const query = searchInput.value.trim().toLowerCase()`
- `const status = statusFilter.value` : `'all' | 'hilang' | 'ditemukan'`. Values from HTML `<option>`.
- `return reports.filter(report => titleMatch && statusMatch)`.
  - `titleMatch` = `report.title.toLowerCase().includes(query)` (case-insensitive, edge spaces ignored).
  - `statusMatch` = status is `'all'` OR `report.status === status`.
- Combine with AND (`&&`): both filters must pass.
- Arrow `=>` = "what to do with each item".

`trap:eq_vs_strict` [EXT @54:14-@54:39]
- `==` loose, `===` compares value AND type. Use `===` for comparison. (`=` assigns.)

`fn:openModal` [EXT @54:48-@56:10]
- First clear leftover state (old text, error messages, old input) so nothing carries over or duplicates.
- Then show modal if not already open. Mechanism `[AMB]` (native dialog vs class toggle).
- Bonus "focus first input" = cosmetic, Amelia skipped, "nice to know".

`fn:closeModal` [EXT @56:16-@56:26]
- Just close. No submit logic yet (added in B4).

`concept:init_wiring` [EXT @56:39-@1:00:08]
- Defining a function does nothing until registered. Put listeners in the init/initiator function.
- `searchInput` and `statusFilter` listeners -> on change: `renderReports(applyFilters())`. Event names not stated `[INF]` `input` / `change`.
- Open/close buttons: `addEventListener('click', openModal)`.
- Without listeners filter does not react (@1:00:08).

`trap:parentheses_on_handler` [EXT @58:57-@59:59]
- `addEventListener('click', openModal)` : NO parentheses. Passes function reference, runs on click.
- `openModal()` runs immediately at registration. Wrong.
- Calling `applyFilters()` inside handler body is fine, that runs when handler fires.

## C4 js-ajax-fetch (B3 @1:00:23-@1:08:19, B4 @1:10:02-@1:18:58)

`concept:busy_flag` [EXT]
- `isLoading` (B3), `isSubmitting` (B4). Guard at top: if busy -> `return`. Prevents duplicate requests and duplicated data on spam click.

`fn:loadReports` (B3, GET) [EXT @1:00:23-@1:08:19]
- Goal: refresh data without page reload. DB seeded via shell, sqlite pushed to repo.
- Order:
  1. `if (isLoading) return;`
  2. `isLoading = true`; `refreshButton.disabled = true`; status message "memuat laporan" style text.
  3. `try`: `const response = await fetch(REPORTS_URL, { headers: { Accept: 'application/json' } })`. Constant name `[INF]`. If JS inline in Django template use `{% url ... %}` (@1:03:01).
  4. `if (!response.ok) throw new Error('Gagal mengambil data laporan')`.
  5. `const data = await response.json()`.
  6. Bonus: check payload is array (`Array.isArray`) before replacing state, else `throw new Error('Format data laporan tidak valid')`. Reason: bad payload (one string/value) would crash render.
  7. `reports = <array>`; `renderReports(applyFilters())`. Keeps active filter after reload.
  8. success message "laporan dimuat".
  9. `catch (error)`: show message or `console.error`. Either accepted.
  10. `finally { isLoading = false; refreshButton.disabled = false; }`.
- Payload key (`data.reports` vs bare array) `[AMB]`.
- Init: call `loadReports()` on page open. Refresh button -> `addEventListener('click', loadReports)`.

`concept:async_await` [EXT @1:04:23-@1:04:44]
- `await` only inside `async function`. No `await` -> plain function ok.

`why:finally` [EXT @1:06:23-@1:06:52]
- `finally` runs after try OR catch. Resets busy flag + re-enables button always.

`fn:submitReport` (B4, POST) [EXT @1:10:02-@1:18:58]
- Listener: `form.addEventListener('submit', submitReport)`. Not `click`: submit fires on button click AND Enter key.
- Order:
  1. `event.preventDefault()` : stop default form navigation/reload.
  2. `if (isSubmitting || isLoading) return;` : stops double-click duplicates, and incomplete list when load is slow.
  3. Payload `{ title, location, status }`, each from `form.elements.<name>.value`, `.trim()`. Field names `[INF]`.
  4. Validate: all three present, `status` is `hilang` or `ditemukan`. Else show error + `return`.
  5. Get CSRF token. `const originalLabel = submitButton.textContent`.
  6. `isSubmitting = true`; `submitButton.disabled = true`; `submitButton.textContent` = "Mengirim..." style text.
  7. `fetch` POST with CSRF header, payload in body. Header name and body encoding not stated `[AMB]` (`X-CSRFToken` + `JSON.stringify` likely `[INF]`).
  8. Not ok (spoken "bukan 200") -> read error JSON with safe fallback to empty object `[INF]` `.catch(() => ({}))`, so parse failure does not throw.
     - Error object keyed by field. Key `__all__` = non-field error -> no prefix. Other key -> prefix with field name. `join` all into one message. If `details` exists, use it as message. Then `throw new Error(message)`.
  9. Ok -> parse data. Invalid -> `throw new Error('Respons server tidak valid')`.
  10. `reports = [data.report, ...reports]` : new report first (backend order `-id`).
  11. Reset form. Clear form message. `isSubmitting = false` BEFORE `closeModal()`. Then `renderReports(applyFilters())` so filters stay.
  12. `catch`: `console.error`. If `error instanceof TypeError` show generic network-style message, else show `error.message`. Message text `[INF]`.
  13. `finally`: `isSubmitting = false`; button enabled; `submitButton.textContent = originalLabel` (back to "Simpan", not stuck on "Mengirim").

`trap:close_modal_order` [EXT @1:17:30-@1:17:50]
- `closeModal` early-returns while `isSubmitting` is true. So set `isSubmitting = false` first, then call `closeModal()`. Else modal never closes.

`concept:let_vs_const` [EXT @1:14:10-@1:14:55]
- `const`: must have value at declaration, cannot reassign (reassign -> TypeError). `let`: can start empty, can reassign.
- Use `let` for `message` (changes). `const` for error status / data (not changed).

## C5 quiz-intel-lab-logistics

`rule:quiz2_topics` [EXT @25:43-@26:20, @38:01-@38:41]
- Source: TAs asked lecturer for hints. Exactly 3 points:
  1. JavaScript.
  2. Build login page, incl. CSRF token. Make form and send data to database.
  3. Restrict a page so only logged-in users can access.
- All three taught in Tutorial 4 + 5. Advice: redo them thoroughly.
- Tutorial 5 JS is broad. Quiz JS requirement will differ from tutorial. Know the pieces, not the exact solution.
- Unit testing: lecturer did not mention. May or may not appear.
- Selenium: optional, TA thinks should not appear (@39:30-@40:14). It is functional testing, opens Chrome and fills credentials. Useful later in industry.

`tip:quiz_env` [EXT @30:34-@30:50, @38:51-@39:24]
- Template given, same as quiz 1.
- Quiz 1 bottleneck: downloading dependencies after activating Python venv in lab. Lots of people hit it.
- Seats not fixed for quizzes (unlike UTS/UAS). Check lab setup 1-2 days before: network, keyboard, monitor, which user/account `[AMB]` ("intervensi" likely internet).

`tip:lab_restricted_network` [EXT @34:50-@37:31]
- Lab network restricts external sites. Favicon and Google Fonts can error.
- Favicon is static, should not crash Django, shows as broken box.
- If external `<link>` (font/favicon) causes error and is not tied to `settings.py`, `urls.py`, or `views.py` -> delete that line in HTML.
- Ask lecturer/TA on spot. Reports help them fix.

`concept:quiz_date` [AMB]
- Spoken "kuis besok" (@33:25), "two days prep Monday to Tuesday" (@25:43). Recording dated 2026-10-04. Exact quiz date not stated.

`tip:contact` [EXT @24:49, @1:20:24]
- Questions -> Jaysen via Discord. Jaysen will share recording.

---

# 3. EDGES

C1
```
fn:register        -uses->      UserCreationForm                [EXT]
fn:register        -redirects-> route:login                     [INF main:login]
fn:login_user      -uses->      AuthenticationForm              [EXT]
fn:login_user      -calls->     login(request, form.get_user()) [EXT]
fn:login_user      -sets->      cookie:last_login               [EXT]
cookie:last_login  -has->       concept:cookie_flags            [EXT bonus]
cookie:last_login  -forbids->   rule:no_secrets_in_cookie       [EXT]
fn:logout_user     -requires->  method:POST (else 405)          [EXT]
fn:logout_user     -deletes->   cookie:last_login               [EXT]
fn:logout_user     -calls->     logout(request)                 [EXT]
concept:a1_scope   -limits->    fn:register, fn:login_user, fn:logout_user [EXT]
```

C2
```
concept:role_group     -drives->     fn:create_project           [EXT]
concept:role_group     -drives->     fn:edit_project             [EXT]
concept:role_group     -drives->     fn:delete_project           [EXT]
fn:create_project      -requires->   role:Owner (else 403)       [INF]
fn:edit_project        -requires->   role:Editor|Owner (else 403)[EXT]
fn:delete_project      -requires->   role:Owner + method:POST    [EXT]
fn:toggle_star         -requires->   login + method:POST         [EXT]
fn:edit_project        -checks_perm_before-> get_object_or_404   [EXT]
fn:project_list_bonus  -uses->       prefetch_related('starred_by') [INF]
tmpl:project_list      -mirrors->    concept:role_group          [EXT]
tmpl:project_list      -is_not_substitute_for-> rule:server_side_check [EXT]
rule:no_superuser      -constrains-> concept:role_group          [EXT]
fn:dashboard_protected -uses->       login_required              [EXT]
fn:dashboard_protected -needs->      login_url == urls.py login  [EXT/AMB value]
rule:post_csrf         -applies_to-> fn:create_project, fn:edit_project, fn:delete_project, fn:toggle_star [EXT]
fn:logout_user         -same_shape_as-> fn:delete_project        [INF]
```

C3
```
fn:renderReports        -clears->    reportList.innerHTML        [EXT]
fn:renderReports        -uses->      textContent                 [EXT]
textContent             -prevents->  XSS                         [EXT]
fn:renderReports        -writes->    #result-count, empty-message [EXT/AMB id]
fn:applyFilters         -returns->   filtered reports            [EXT]
fn:applyFilters         -joins->     titleMatch AND statusMatch  [EXT]
fn:applyFilters         -uses->      trap:eq_vs_strict (===)     [EXT]
concept:init_wiring     -registers-> fn:applyFilters, fn:openModal, fn:closeModal [EXT]
concept:init_wiring     -ends_with-> renderReports(applyFilters())[EXT]
fn:openModal            -clears->    stale modal state           [EXT]
trap:parentheses_on_handler -explains-> why openModal passed bare [EXT]
```

C4
```
fn:loadReports   -guarded_by->  concept:busy_flag(isLoading)     [EXT]
fn:loadReports   -uses->        fetch + concept:async_await      [EXT]
fn:loadReports   -ends_with->   why:finally                      [EXT]
fn:loadReports   -then->        renderReports(applyFilters())    [EXT]
fn:submitReport  -guarded_by->  concept:busy_flag(isSubmitting, isLoading) [EXT]
fn:submitReport  -listens_on->  'submit' (not 'click')           [EXT]
fn:submitReport  -calls->       event.preventDefault()           [EXT]
fn:submitReport  -sends->       POST + CSRF                      [EXT]
fn:submitReport  -prepends->    data.report to reports           [EXT]
fn:submitReport  -before->      closeModal  via trap:close_modal_order [EXT]
fn:submitReport  -ends_with->   why:finally                      [EXT]
fn:submitReport  -uses->        concept:let_vs_const             [EXT]
fn:submitReport  -reuses->      fn:closeModal, fn:renderReports, fn:applyFilters [EXT]
rule:post_csrf   -applies_to->  fn:submitReport                  [EXT]
```

Cross-community
```
rule:server_side_check -same_principle_as-> why:textContent_not_innerHTML  [INF]
fn:submitReport        -validates_client_side_but_server_must_too-> rule:server_side_check [INF]
rule:quiz2_topics      -covers->  C1, C2, C3, C4                 [EXT]
```

---

# 4. HTTP + PATTERN CHEAT TABLE

| situation | response | source |
|-----------|----------|--------|
| wrong method (logout/delete need POST) | 405 `HttpResponseNotAllowed` | @07:47 `[INF name]` |
| logged-in, lacks role | 403 permission denied | @10:40, @13:01 |
| object id missing | 404 | @18:00 |
| invalid form POST | re-render form + errors, no write | @01:10 |
| valid form POST | save -> redirect (PRG) | @04:08, @14:47 |

| JS situation | pattern |
|--------------|---------|
| show user text in DOM | `textContent` |
| prevent duplicate fetch | busy flag + early `return` |
| always cleanup | `finally` |
| refresh list, keep filter | `renderReports(applyFilters())` |
| form submit via JS | `'submit'` + `preventDefault()` |
| pass handler | no `()` |

---

# 5. AMBIGUOUS + ASR DICTIONARY

Captions are auto-generated. When reading raw transcript, apply:

| heard | meant |
|-------|-------|
| Jenggo, Jinggo | Django |
| Fuse, Views Dot P White, Pi White | `views.py` |
| Road, Roadmin, Roadmint | route / URL name (`main:...`) `[INF]` |
| Phuki, Kooki, Scooki | cookie |
| Kue, Kuis | quiz |
| Lex | `Lax` (SameSite) |
| Aids, Max X | `max_age` |
| Sale | shell |
| Star by | `starred_by` |
| Private related | `prefetch_related` `[INF]` |
| Kttp | Http |
| Batch | badge |
| Fatch, Fast Ci | fetch |
| Away wait, Asing | await, async |
| Jason | JSON (also name of speaker "Jaysen") |
| Led, Kons, Konst | let, const |
| Tuduh | TODO |
| Fav ikon, Fluff Ikon | favicon |
| Lamda | lambda / arrow function |
| Ejax | AJAX |
| Pai Carm | PyCharm |
| Nildy, Nil | Neal |
| Fuun, Full On | Angelo (alias) |
| Seb | web (lab network context) `[INF]` |
| intervensi | probably internet `[AMB]` |

Open items to verify against repo/slides before relying:
- cookie timestamp format string (A1)
- `login_url` value form (A4)
- `user.is_owner` / `user.is_editor` definitions (A2)
- exact DOM ids: `result-count`, empty message id (B1)
- CSRF header name + body encoding (B4)
- JSON payload key for list (B3: `data.reports`?)
- exact quiz date

---

# 6. TIMELINE INDEX (transcript pointer)

| time | node/section |
|------|--------------|
| @00:32 | A1 spec: `concept:a1_scope` |
| @03:08 | `fn:register` |
| @04:48 | `fn:login_user` |
| @07:14 | `fn:logout_user` |
| @08:45 | A2 spec: `concept:role_group`, `rule:no_superuser` |
| @09:16 | `tip:lab_prep_a2` (migrate, shell users) |
| @12:02 | quiz emphasis on restricting endpoints by user |
| @12:47 | A2 code start |
| @14:04 | `fn:create_project` |
| @15:56 | `fn:edit_project` |
| @18:57 | `fn:delete_project` |
| @19:50 | `fn:toggle_star` |
| @21:49 | `tmpl:project_list` |
| @24:10 | A3 skipped, practice |
| @25:28 | Neal takes over |
| @25:43 | `rule:quiz2_topics` |
| @27:50 | A4 `fn:dashboard_protected` |
| @34:46 | `tip:lab_restricted_network` |
| @38:01 | lecturer's 3 points (confirmed) |
| @38:51 | `tip:quiz_env` seat/lab check |
| @39:30 | Selenium aside |
| @41:26 | JS part starts (Angelo) |
| @41:54 | B1 `fn:renderReports` |
| @47:47 | B2 start (Amelia) |
| @49:55 | `fn:applyFilters` |
| @54:48 | `fn:openModal` / `fn:closeModal` |
| @56:39 | `concept:init_wiring` |
| @58:57 | `trap:parentheses_on_handler` |
| @1:00:23 | B3 `fn:loadReports` |
| @1:10:02 | B4 `fn:submitReport` (Angelo) |
| @1:14:10 | `concept:let_vs_const` |
| @1:19:57 | close |

---

# 7. FORMAT PROVENANCE

- Caveman style: drop articles/pleasantries/hedging, fragments ok, `->` for cause, keep code/commands/paths/error strings exact, intensity levels (lite/full/ultra), `caveman-compress` targets memory files. Source: Better Stack guide on JuliusBrussee/caveman (betterstack.com/community/guides/ai/caveman-llm/) + corroborating summaries. Primary SKILL.md not opened.
- Graph map: nodes = concepts, typed edges, `EXTRACTED`/`INFERRED`/`AMBIGUOUS` confidence, god nodes, communities, "why" as own nodes, suggested questions, report file as entry point. Source: Graphify-Labs/graphify README (opened).
- Symbol-level addressing + per-topic memories: Serena (oraios) uses symbol names, overview-first then drill, memory files read by name. Source: secondary pages only (rywalker.com/research/serena, skills.cat Serena entries, glama tool list). Primary repo not opened. Applied here as: stable `kind:name` ids, section 1 overview first, self-contained community sections.
- Deviation from caveman: ambiguous speech kept and tagged, not compressed away.
