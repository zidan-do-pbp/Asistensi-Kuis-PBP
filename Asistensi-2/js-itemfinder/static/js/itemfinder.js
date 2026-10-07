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

let reports = JSON.parse(
  document.getElementById("initial-reports").textContent
);

let isLoading = false;


// SOAL 1
function renderReports(data) {
  // TODO: SOAL 1: kosongkan #report-list, buat card per laporan (article.card, badge, judul, lokasi), append.
}


// SOAL 2
function applyFilters() {
  // TODO: SOAL 2: return laporan yang cocok judul (trim, huruf kecil) AND status (all = semua).
}

function openModal() {
  // TODO: SOAL 2: kosongkan pesan form lama, buka modal.
}

function closeModal() {
  // TODO: SOAL 2: tutup modal kecuali sedang submit.
}

// SOAL 3
async function loadReports() {
  // TODO: SOAL 3: fetch GET BASE_REPORTS_ENDPOINT, guard isLoading, try/catch/finally.
}

async function submitReport(event) {
  // TODO: SOAL 4: preventDefault, guard, validasi, fetch POST JSON + X-CSRFToken, finally.
}


// EVENT HANDLER
function init() {
  // TODO: SOAL 2 dan 3: pasang semua event listener, muat data saat halaman dibuka.
}

init();