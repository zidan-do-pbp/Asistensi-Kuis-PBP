// ALUR JS: semua kerja di static/js/itemfinder.js. Soal 1 -> 2 -> 3 -> 4, tiap soal berhenti di init() untuk memasang listener-nya
// Urutan umum: (1) tulis fungsi, (2) pasang listener di init(), (3) uji di browser
// Variabel tambahan di bawah ini hanya pengambilan elemen DOM, bukan bagian dari batas scope soal

const list = document.getElementById("report-list");
const searchInput = document.getElementById("search-input");
const statusFilter = document.getElementById("status-filter");
const modal = document.getElementById("report-modal");
const form = document.getElementById("report-form");
const formMessage = document.getElementById("form-message");
const loadMessage = document.getElementById("load-message");
const refreshButton = document.getElementById("refresh-button");
const closeButton = document.getElementById("close-modal");
const BASE_REPORTS_ENDPOINT = window.REPORTS_URL;

const app = document.getElementById("app");
const openButton = document.getElementById("open-modal");
const submitButton = document.getElementById("submit-button");
const resultCount = document.getElementById("result-count");
const emptyMessage = document.getElementById("empty-message");

let reports = JSON.parse(
  document.getElementById("initial-reports").textContent
);

// isLoading dipakai soal 3, isSubmitting dipakai soal 2 (closeModal) dan soal 4
let isLoading = false;
let isSubmitting = false;


// SOAL 1
//TODO: (urutan 1) renderReports(data). Ubah HANYA fungsi ini, belum perlu fetch
function renderReports(data) {
  //TODO: (urutan 1a) kosongkan #report-list sebelum render agar kartu tidak dobel
  list.innerHTML = "";

  let hilang = 0;
  let ditemukan = 0;

  //TODO: (urutan 1b) per laporan: article.card berisi badge status, judul, lokasi, lalu append ke list
  data.forEach((report) => {
    const card = document.createElement("article");
    card.classList.add("card");

    const badge = document.createElement("span");
    const isLost = report.status === "hilang";
    badge.className = isLost ? "badge badge-hilang" : "badge badge-ditemukan";
    badge.textContent = isLost ? "Hilang" : "Ditemukan";

    //TRAP: pakai textContent untuk data laporan, bukan innerHTML (XSS)
    const title = document.createElement("h3");
    title.textContent = report.title;

    const location = document.createElement("p");
    location.textContent = report.location;

    card.append(badge, title, location);
    list.appendChild(card);

    if (isLost) {
      hilang += 1;
    } else {
      ditemukan += 1;
    }
  });

  //BONUS soal 1: rincian jumlah status, misal "3 laporan (2 hilang, 1 ditemukan)"
  resultCount.textContent =
    `${data.length} laporan (${hilang} hilang, ${ditemukan} ditemukan)`;
  emptyMessage.hidden = data.length !== 0;
}


// SOAL 2
//TODO: (urutan 2) applyFilters(), openModal(), closeModal(), lalu listener di init()
function applyFilters() {
  //TODO: (urutan 2a) judul: trim + huruf kecil. Status "all" = semua. Gabung dengan AND. Jangan filter via backend
  const keyword = searchInput.value.trim().toLowerCase();
  const status = statusFilter.value;

  return reports.filter((report) => {
    const matchTitle = report.title.toLowerCase().includes(keyword);
    //TRAP: bandingkan dengan ===, bukan == atau =
    const matchStatus = status === "all" || report.status === status;
    return matchTitle && matchStatus;
  });
}

function openModal() {
  //TODO: (urutan 2b) bersihkan pesan form lama, buka modal
  formMessage.textContent = "";
  modal.showModal();
  //BONUS soal 2: fokus ke input judul
  form.elements["title"].focus();
}

function closeModal() {
  //TODO: (urutan 2c) jangan tutup modal selama submit berjalan
  if (isSubmitting) {
    return;
  }
  modal.close();
}

// SOAL 3
//TODO: (urutan 3) loadReports() lalu listener tombol Muat ulang + pemanggilan pertama di init()
async function loadReports() {
  //TODO: (urutan 3a) cegah request baru jika loading atau submit sedang berjalan
  if (isLoading || isSubmitting) {
    return;
  }

  //TODO: (urutan 3b) set state loading, tampilkan pesan, nonaktifkan tombol pemicu request
  isLoading = true;
  loadMessage.textContent = "Memuat data...";
  refreshButton.disabled = true;
  openButton.disabled = true;

  //TODO: (urutan 3c) fetch GET ke app.dataset.listUrl dengan async/await, cek response.ok SEBELUM response.json()
  try {
    const response = await fetch(app.dataset.listUrl, {
      headers: { Accept: "application/json" },
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const data = await response.json();

    //BONUS soal 3: pastikan data.reports array sebelum menimpa data lama
    if (!Array.isArray(data.reports)) {
      throw new Error("Format data tidak valid");
    }

    //TODO: (urutan 3d) sukses: perbarui reports lalu render dengan filter aktif
    reports = data.reports;
    renderReports(applyFilters());
    loadMessage.textContent = "";
  } catch (error) {
    //TODO: (urutan 3e) gagal: tampilkan pesan error, data lama dipertahankan
    loadMessage.textContent = "Gagal memuat data. Coba lagi.";
  } finally {
    //TODO: (urutan 3f) selalu kembalikan state dan tombol, sukses maupun gagal
    isLoading = false;
    refreshButton.disabled = false;
    openButton.disabled = false;
  }
}

// SOAL 4
//TODO: (urutan 4) submitReport(event) lalu listener submit di init(). Jangan ubah fungsi soal 1 sampai 3
async function submitReport(event) {
  //TODO: (urutan 4a) cegah submit default agar halaman tidak reload
  event.preventDefault();

  //TODO: (urutan 4b) cegah submit baru jika sedang submit atau loading
  if (isSubmitting || isLoading) {
    return;
  }

  //TODO: (urutan 4c) validasi: judul dan lokasi tidak kosong setelah trim, status hilang/ditemukan. Gagal: pesan error, tanpa request
  const title = form.elements["title"].value.trim();
  const location = form.elements["location"].value.trim();
  const status = form.elements["status"].value;

  if (!title || !location || !["hilang", "ditemukan"].includes(status)) {
    formMessage.textContent =
      "Judul dan lokasi wajib diisi, status harus hilang atau ditemukan.";
    return;
  }

  //TODO: (urutan 4d) token CSRF diambil dari input csrfmiddlewaretoken di form
  const csrfToken = form.elements["csrfmiddlewaretoken"].value;

  //TODO: (urutan 4e) state submit aktif, tombol nonaktif, teks "Mengirim..."
  isSubmitting = true;
  formMessage.textContent = "";
  submitButton.disabled = true;
  submitButton.textContent = "Mengirim...";

  try {
    //TODO: (urutan 4f) POST JSON: header Content-Type + X-CSRFToken, body JSON.stringify(...)
    const response = await fetch(app.dataset.createUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify({ title, location, status }),
    });

    if (!response.ok) {
      let message = "Gagal menyimpan laporan. Coba lagi.";
      //BONUS soal 4: HTTP 400 tampilkan pesan dari data.errors
      if (response.status === 400) {
        const data = await response.json();
        const details = Object.values(data.errors || {}).flat();
        if (details.length > 0) {
          message = details.join(" ");
        }
      }
      throw new Error(message);
    }

    await response.json();

    //TODO: (urutan 4g) sukses: kosongkan form, tutup modal, perbarui daftar. Gagal (catch): modal tetap terbuka, isi form dipertahankan
    form.reset();
    //TRAP: isSubmitting harus false SEBELUM closeModal(), kalau tidak modal tidak pernah menutup
    isSubmitting = false;
    closeModal();
    await loadReports();
  } catch (error) {
    formMessage.textContent = error.message;
  } finally {
    //TODO: (urutan 4h) kembalikan state submit dan tombol, sukses maupun gagal
    isSubmitting = false;
    submitButton.disabled = false;
    submitButton.textContent = "Simpan";
  }
}


// EVENT HANDLER
//TODO: (urutan 5) init(): tempat semua listener dikumpulkan. Isi bertahap sesuai urutan soal
function init() {
  //TODO: (urutan 2d, soal 2) listener pencarian (input), filter status (change), tombol buka dan tutup modal
  searchInput.addEventListener("input", () => renderReports(applyFilters()));
  statusFilter.addEventListener("change", () => renderReports(applyFilters()));
  //TRAP: handler tanpa kurung (openModal, bukan openModal()), kalau tidak langsung jalan saat dipasang
  openButton.addEventListener("click", openModal);
  closeButton.addEventListener("click", closeModal);
  //TODO: (urutan 3g, soal 3) listener tombol Muat ulang data, lalu muat data sekali saat init
  refreshButton.addEventListener("click", loadReports);
  //TODO: (urutan 4i, soal 4) listener submit pada form
  form.addEventListener("submit", submitReport);

  renderReports(applyFilters());
  loadReports();
}

init();
