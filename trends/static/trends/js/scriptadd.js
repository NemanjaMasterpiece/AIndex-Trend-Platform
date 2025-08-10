document.addEventListener("DOMContentLoaded", function () {
    const updateButton = document.getElementById("update-button");
    if (updateButton) {
        updateButton.addEventListener("click", function (event) {
            event.preventDefault();
            addArticle();
        });
    }

    function addArticle() {
        fetch("/trends/update-one/", {
            method: "POST",
            headers: {
                "X-CSRFToken": getCSRFToken(),
                "Content-Type": "application/json"
            },
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            if (data.message.includes("dodat")) {
                location.reload();
            }
        })
        .catch(error => console.error("Greška:", error));
    }

    function getCSRFToken() {
        return document.querySelector('[name=csrfmiddlewaretoken]').value;
    }
});