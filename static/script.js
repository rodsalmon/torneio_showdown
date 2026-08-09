document.addEventListener("DOMContentLoaded", function () {
  const toggle = document.getElementById("toggle-pagina2");
  const submenu = document.getElementById("submenu-pagina2");

  toggle.addEventListener("click", function (event) {
    event.preventDefault();
    submenu.classList.toggle("aberto");
  });
});
