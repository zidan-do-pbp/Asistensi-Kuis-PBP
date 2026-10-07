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

let isLoading = false;
let isSubmitting = false;


// SOAL 1
function renderReports(data) {
  list.innerHTML = "";

  let hilang = 0;
  let ditemukan = 0;

  data.forEach((report) => {
    const card = document.createElement("article");
    card.classList.add("card");

    const badge = document.createElement("span");
    const isLost = report.status === "hilang";
    badge.className = isLost ? "badge badge-hilang" : "badge badge-ditemukan";
    badge.textContent = isLost ? "Hilang" : "Ditemukan";

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

  resultCount.textContent =
    `${data.length} laporan (${hilang} hilang, ${ditemukan} ditemukan)`;
  emptyMessage.hidden = data.length !== 0;
}


// SOAL 2
function applyFilters() {
  const keyword = searchInput.value.trim().toLowerCase();
  const status = statusFilter.value;

  return reports.filter((report) => {
    const matchTitle = report.title.toLowerCase().includes(keyword);
    const matchStatus = status === "all" || report.status === status;
    return matchTitle && matchStatus;
  });
}

function openModal() {
  formMessage.textContent = "";
  modal.showModal();
  form.elements["title"].focus();
}

function closeModal() {
  if (isSubmitting) {
    return;
  }
  modal.close();
}

// SOAL 3
async function loadReports() {
  if (isLoading || isSubmitting) {
    return;
  }

  isLoading = true;
  loadMessage.textContent = "Memuat data...";
  refreshButton.disabled = true;
  openButton.disabled = true;

  try {
    const response = await fetch(app.dataset.listUrl, {
      headers: { Accept: "application/json" },
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const data = await response.json();

    if (!Array.isArray(data.reports)) {
      throw new Error("Format data tidak valid");
    }

    reports = data.reports;
    renderReports(applyFilters());
    loadMessage.textContent = "";
  } catch (error) {
    loadMessage.textContent = "Gagal memuat data. Coba lagi.";
  } finally {
    isLoading = false;
    refreshButton.disabled = false;
    openButton.disabled = false;
  }
}

// SOAL 4
async function submitReport(event) {
  event.preventDefault();

  if (isSubmitting || isLoading) {
    return;
  }

  const title = form.elements["title"].value.trim();
  const location = form.elements["location"].value.trim();
  const status = form.elements["status"].value;

  if (!title || !location || !["hilang", "ditemukan"].includes(status)) {
    formMessage.textContent =
      "Judul dan lokasi wajib diisi, status harus hilang atau ditemukan.";
    return;
  }

  const csrfToken = form.elements["csrfmiddlewaretoken"].value;

  isSubmitting = true;
  formMessage.textContent = "";
  submitButton.disabled = true;
  submitButton.textContent = "Mengirim...";

  try {
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

    form.reset();
    isSubmitting = false;
    closeModal();
    await loadReports();
  } catch (error) {
    formMessage.textContent = error.message;
  } finally {
    isSubmitting = false;
    submitButton.disabled = false;
    submitButton.textContent = "Simpan";
  }
}


// EVENT HANDLER
function init() {
  searchInput.addEventListener("input", () => renderReports(applyFilters()));
  statusFilter.addEventListener("change", () => renderReports(applyFilters()));
  openButton.addEventListener("click", openModal);
  closeButton.addEventListener("click", closeModal);
  refreshButton.addEventListener("click", loadReports);
  form.addEventListener("submit", submitReport);

  renderReports(applyFilters());
  loadReports();
}

init();
