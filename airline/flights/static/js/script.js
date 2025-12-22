document.addEventListener('DOMContentLoaded', function() {
    // 1. Select the search input and the table rows
    const searchInput = document.querySelector('#flight-search');
    const tableRows = document.querySelectorAll('table tbody tr');

    // 2. Add an event listener for when the user types
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = searchInput.value.toLowerCase();

            tableRows.forEach(row => {
                // Get all text within the row (origin, destination, etc.)
                const rowText = row.innerText.toLowerCase();

                // 3. If the query matches any text in the row, show it; otherwise hide it
                if (rowText.includes(query)) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        });
    }
});