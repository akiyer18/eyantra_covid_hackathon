const responsiveNav = document.getElementById("responsiveMenu");
const hamburger = document.getElementById("hamburger")
let toggleCounter = 0
function responsiveMenu() {
  if (toggleCounter == 0) {
    responsiveNav.style.display = "flex";
    toggleCounter++;
    hamburger.innerHTML = '<i class="fas fa-times"></i>';
  }
  else {
    responsiveNav.style.display = "none";
    toggleCounter--;
    hamburger.innerHTML = '<i class="fas fa-bars"></i>';
  }
}