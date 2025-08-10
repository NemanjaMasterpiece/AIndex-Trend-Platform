document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.getElementById("theme-switch");
    const header = document.querySelector("header");
    const body = document.body;

    if (localStorage.getItem("theme") === "dark") {
        body.classList.add("dark-mode");
        header.classList.add("dark-mode");
    } else {
        body.classList.add("light-mode");
        header.classList.add("light-mode");
    }

    themeToggle.addEventListener("click", function () {
        const isDarkMode = body.classList.toggle("dark-mode");
        body.classList.toggle("light-mode", !isDarkMode);
        header.classList.toggle("dark-mode", isDarkMode);
        header.classList.toggle("light-mode", !isDarkMode);

        localStorage.setItem("theme", isDarkMode ? "dark" : "light");
    });
});