
function showMoreCountries() {
        const hiddenCountries = document.querySelectorAll('.country-hidden');
        hiddenCountries.forEach(function(country) {
            country.classList.remove('country-hidden');
        });

        document.getElementById('show-more').style.display = 'none';
        document.getElementById('show-less').style.display = 'inline-block';
    }

function showLessCountries() {
        const visibleCountries = document.querySelectorAll('.country-label');
        for (let i = 10; i < visibleCountries.length; i++) {
            visibleCountries[i].classList.add('country-hidden');
        }

        document.getElementById('show-more').style.display = 'inline-block';
        document.getElementById('show-less').style.display = 'none';
}

function toggleFilters() {
        const sidebar = document.getElementById('filter-sidebar');
        sidebar.classList.toggle('open');
    }

    const minPriceInput = document.getElementById('min-price');
    const maxPriceInput = document.getElementById('max-price');
    const minPriceValue = document.getElementById('min-price-value');
    const maxPriceValue = document.getElementById('max-price-value');

    if (minPriceInput && maxPriceInput) {
        minPriceInput.addEventListener('input', () => {
            minPriceValue.textContent = minPriceInput.value;
        });

        maxPriceInput.addEventListener('input', () => {
            maxPriceValue.textContent = maxPriceInput.value;
        });
    }

    function debounce(func, delay) {
        let timeout;
        return function() {
            clearTimeout(timeout);
            timeout = setTimeout(func, delay);
        };
    }

    const searchInput = document.getElementById('search-input');
    const searchForm = document.getElementById('search-form');

    function handleSearchInput() {
        if (searchInput.value.trim() === '') {
            searchForm.submit();
        } else {
            searchForm.submit();
        }
    }

    const debouncedSearch = debounce(function() {
        handleSearchInput();
    }, 500);

    searchInput.addEventListener('input', debouncedSearch);

