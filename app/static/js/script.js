console.log("Script bien chargé")

// verifiaction du mdp
function ConfirmPasswords() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm-password").value;

    if (password !== confirmPassword) {
      alert("Les mots de passe ne correspondent pas !");
      return false;
    }

    return true;
}

document.addEventListener("DOMContentLoaded", function () {
  const scrollLinks = document.querySelectorAll(".scroll-link");

  function scrollToSection(event) {
      event.preventDefault();

      const targetId = event.currentTarget.getAttribute("href").substring(1);
      const targetSection = document.getElementById(targetId);

      if (targetSection) {
          const offset = 100; // Ajustez le décalage ici
          window.scrollTo({
              top: targetSection.offsetTop - offset,
              behavior: "smooth",
          });
      }
  }

  scrollLinks.forEach(function (link) {
      link.addEventListener("click", scrollToSection);
  });

})


