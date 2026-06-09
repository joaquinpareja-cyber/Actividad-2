document.addEventListener("DOMContentLoaded", () => {
    // Animación del título principal
    const titulo = document.querySelector(".logo h1");
    titulo.style.opacity = 0;
    setTimeout(() => {
        titulo.style.transition = "opacity 2s ease-in-out";
        titulo.style.opacity = 1;
    }, 500);

    console.log("Proyecto Residencial El Expreso iniciado por el equipo.");

    // Interactividad: destacar tarjeta seleccionada
    const cards = document.querySelectorAll(".card");
    cards.forEach(card => {
        card.addEventListener("click", () => {
            alert(`Has seleccionado: ${card.querySelector("h3").textContent}`);
        });
    });
});
