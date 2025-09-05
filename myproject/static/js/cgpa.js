document.addEventListener("DOMContentLoaded", () => {
  const toast = document.getElementById("toast");
  const cgpaValue = document.getElementById("cgpa-value");

  // Show toast if CGPA was calculated
  if (window.CGPA_RESULT) {
    cgpaValue.textContent = window.CGPA_RESULT;

    toast.classList.remove("opacity-0", "translate-y-5");
    toast.classList.add("opacity-100", "translate-y-0");

    // Auto hide after 3s
    setTimeout(() => {
      toast.classList.remove("opacity-100", "translate-y-0");
      toast.classList.add("opacity-0", "translate-y-5");
    }, 3000);
  }
});
