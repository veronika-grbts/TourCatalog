  document.addEventListener("DOMContentLoaded", function () {
        const imageInput = document.querySelector("input[name='image']");
        const currentImage = document.getElementById("current-image");

        imageInput.addEventListener("change", function (event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    currentImage.src = e.target.result;
                };
                reader.readAsDataURL(file);
            }
        });
    });