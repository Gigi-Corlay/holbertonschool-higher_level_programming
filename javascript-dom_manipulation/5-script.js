#!/usr/bin/node
// Select the element with id update_header
const updateHeader = document.getElementById('update_header');

// Add click event listener
updateHeader.addEventListener('click', function() {
    // Select the header element
    const header = document.querySelector('header');

    // Update the text
    header.textContent = "New Header!!!";
});