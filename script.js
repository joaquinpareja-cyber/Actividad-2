document.addEventListener("DOMContentLoaded", () => {
    // --- Líder (Header) ---
    // Animación del título principal
    const titulo = document.querySelector(".logo h1");
    titulo.style.opacity = 0;
    setTimeout(() => {
        titulo.style.transition = "opacity 2s ease-in-out";
        titulo.style.opacity = 1;
    }, 500);

    console.log("Proyecto Residencial El Expreso iniciado por el equipo.");

    // --- Colaborador 1 (Body) ---
    // Interactividad: destacar tarjeta seleccionada
    const cards = document.querySelectorAll(".card");
    cards.forEach(card => {
        card.addEventListener("click", () => {
            alert(`Has seleccionado: ${card.querySelector("h3").textContent}`);
        });
    });

    // --- Colaborador 2 (Footer) ---
    // Animación para botones de redes sociales
    const redes = document.querySelectorAll(".btn-red");
    redes.forEach(btn => {
        btn.addEventListener("mouseover", () => {
            btn.style.transform = "rotate(-3deg) scale(1.1)";
        });
        btn.addEventListener("mouseout", () => {
            btn.style.transform = "rotate(0) scale(1)";
        });
    });
});
