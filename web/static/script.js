document.getElementById("uploadForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const formData = new FormData();
    const fileInput = document.getElementById("videoInput");

    formData.append("video", fileInput.files[0]);

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const box = document.getElementById("responseBox");
        box.innerHTML = data.message || data.error;
        box.style.marginTop = "20px";
        box.style.fontWeight = "bold";
    })
    .catch(error => {
        console.error("Error:", error);
    });
});