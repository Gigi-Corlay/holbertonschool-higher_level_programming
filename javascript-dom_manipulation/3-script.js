#!/usr/bin/node
// Select the toggle element
const toggleDiv = document.getElementById('toggle_header');
// Add a click event listener
toggleDiv.addEventListener('click', function() {
    // Select the header element
    const header = document.querySelector('header');

    // Toggle the class between 'red' and 'green'
    if (header.classList.contains('red')){
        header.classList.remove('red');
        header.classList.add('green');
    } else {
        header.classList.remove('green');
        header.classList.add('red');
    }    
});
