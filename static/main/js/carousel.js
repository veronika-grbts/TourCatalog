document.addEventListener('DOMContentLoaded', function () {
    const leftArrow = document.querySelector('.left-arrow');
    const rightArrow = document.querySelector('.right-arrow');


    if (leftArrow) {
        leftArrow.addEventListener('click', function (event) {
            event.preventDefault();
            loadTours(leftArrow.getAttribute('data-url'));
        });
    }


    if (rightArrow) {
        rightArrow.addEventListener('click', function (event) {
            event.preventDefault();
            loadTours(rightArrow.getAttribute('data-url'));
        });
    }

    function loadTours(url) {

        fetch(url)
            .then(response => response.text())
            .then(html => {
                const newContent = document.createElement('div');
                newContent.innerHTML = html;


                const newTours = newContent.querySelector('.tour-grid');
                if (newTours) {
                    const tourGrid = document.querySelector('.tour-grid');
                    tourGrid.innerHTML = newTours.innerHTML;
                }


                const newPagination = newContent.querySelector('.carousel');
                if (newPagination) {
                    const carousel = document.querySelector('.carousel');
                    carousel.innerHTML = newPagination.innerHTML;
                }
            })
            .catch(error => {
                console.error('Ошибка при загрузке туров:', error);
            });
    }
});
