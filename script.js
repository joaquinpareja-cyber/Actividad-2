document.addEventListener("DOMContentLoaded", () => {
    const titulo = document.querySelector(".logo h1");
    titulo.style.opacity = 0;
    setTimeout(() => {
        titulo.style.transition = "opacity 2s ease-in-out";
        titulo.style.opacity = 1;
    }, 500);

    console.log("Proyecto Residencial El Expreso iniciado por el Líder.");
});
