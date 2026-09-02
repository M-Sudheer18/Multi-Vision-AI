const uploadZone = document.getElementById("uploadZone");
const fileInput = document.getElementById("fileInput");
const previewWrap = document.getElementById("previewWrap");
const previewImg = document.getElementById("previewImg");
const fileName = document.getElementById("fileName");
const fileSize = document.getElementById("fileSize");
const removeBtn = document.getElementById("removeBtn");
const classifyBtn = document.getElementById("classifyBtn");
const emptyState = document.getElementById("emptyState");
const loadingState = document.getElementById("loadingState");
const resultsState = document.getElementById("resultsState");
const topLabel = document.getElementById("topLabel");
const topConfidence = document.getElementById("topConfidence");
const resultsList = document.getElementById("resultsList");
const resetBtn = document.getElementById("resetBtn");

let currentFile = null;

function handleFile(file) {
  if (!file.type.startsWith("image/")) return;
  currentFile = file;
  const reader = new FileReader();
  reader.onload = (e) => {
    previewImg.src = e.target.result;
    previewWrap.style.display = "block";
    uploadZone.style.display = "none";
    fileName.textContent = file.name;
    fileSize.textContent = (file.size / 1024 / 1024).toFixed(2) + " MB";
    classifyBtn.disabled = false;
    hideResults();
  };
  reader.readAsDataURL(file);
}

function hideResults() {
  emptyState.style.display = "none";
  loadingState.style.display = "none";
  resultsState.style.display = "none";
}

function showLoading() {
  emptyState.style.display = "none";
  loadingState.style.display = "flex";
  resultsState.style.display = "none";
}

function reset() {
  currentFile = null;
  fileInput.value = "";
  previewImg.src = "";
  previewWrap.style.display = "none";
  uploadZone.style.display = "block";
  classifyBtn.disabled = true;
  hideResults();
  emptyState.style.display = "flex";
}

// Event Listeners for Drag and Drop
uploadZone.addEventListener("click", () => fileInput.click());
uploadZone.addEventListener("dragover", (e) => {
  e.preventDefault();
  uploadZone.classList.add("dragover");
});
uploadZone.addEventListener("dragleave", () => {
  uploadZone.classList.remove("dragover");
});
uploadZone.addEventListener("drop", (e) => {
  e.preventDefault();
  uploadZone.classList.remove("dragover");
  const file = e.dataTransfer.files[0];
  if (file) handleFile(file);
});
fileInput.addEventListener("change", (e) => {
  const file = e.target.files[0];
  if (file) handleFile(file);
});
removeBtn.addEventListener("click", reset);
resetBtn.addEventListener("click", reset);

// --- THE REAL API CONNECTION ---
classifyBtn.addEventListener("click", async () => {
  if (!currentFile) return;
  
  // Disable button and show the loading spinner
  classifyBtn.disabled = true;
  showLoading();

  // Package the image file
  const formData = new FormData();
  formData.append("file", currentFile);

  try {
    // Send the image to your Flask Backend
    const response = await fetch("/api/v1/predict", {
      method: "POST",
      body: formData
    });
    
    // Catch the JSON response from your prediction_service.py
    if (!response.ok) {
      throw new Error(`Server returned ${response.status}`);
    }
    const data = await response.json();

    if (data.success) {
      // Map the dictionary of probabilities into an array for the UI
      const apiResults = Object.entries(data.probabilities).map(([label, conf]) => ({
        label: label,
        confidence: (conf * 100).toFixed(1)
      }));

      // Update the big text at the top
      topLabel.textContent = data.predicted_class;
      topConfidence.textContent = (data.confidence * 100).toFixed(1);

      // Dynamically build the progress bars using the real model data
      resultsList.innerHTML = apiResults
        .map(
          (r, i) => `
          <div class="result-row">
            <div class="result-label">
              <span>${i + 1}. ${r.label}</span>
              <span>${r.confidence}%</span>
            </div>
            <div class="bar-bg">
              <div class="bar-fill" style="width: 0%;" data-target="${r.confidence}%"></div>
            </div>
          </div>
        `
        ).join("");

      // Switch the UI views
      emptyState.style.display = "none";
      loadingState.style.display = "none";
      resultsState.style.display = "block";

      // Animate the progress bars filling up
      requestAnimationFrame(() => {
        setTimeout(() => {
          document.querySelectorAll(".bar-fill").forEach((bar) => {
            bar.style.width = bar.getAttribute('data-target');
          });
        }, 50);
      });
    } 
    else {
      alert("Classification failed: " + data.error);
      reset();
    }
  } 
  catch (error) {
    console.error("API Error:", error);
    alert("Failed to connect to the prediction server. Is your Flask app running?");
    reset();
  } 
  finally {
    classifyBtn.disabled = !currentFile;
  }
});

// HOW IT WORKS POPUP
const howItWorksBtn = document.getElementById("howItWorksBtn");
const howItWorksModal = document.getElementById("howItWorksModal");
const closeHowItWorks = document.getElementById("closeHowItWorks");
const howItWorksOverlay = document.querySelector(".how-it-works-overlay");

// Open popup
howItWorksBtn.addEventListener("click", () => {
  howItWorksModal.classList.add("active");
  document.body.style.overflow = "hidden";
});
// Close popup using X
closeHowItWorks.addEventListener("click", () => {
  howItWorksModal.classList.remove("active");
  document.body.style.overflow = "";
});

// Close popup by clicking outside
howItWorksOverlay.addEventListener("click", () => {
  howItWorksModal.classList.remove("active");
  document.body.style.overflow = "";
});

// Close popup using Escape key
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    howItWorksModal.classList.remove("active");
    document.body.style.overflow = "";
  }
});