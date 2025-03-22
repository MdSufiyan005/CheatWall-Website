document
.querySelector(".mobile-menu-btn")
.addEventListener("click", function () {
  document.querySelector(".nav-links").classList.toggle("active");
  document.querySelector(".cta-buttons").classList.toggle("active");
  this.classList.toggle("active");
});