#!/usr/bin/node
// Select the element with id "red_header"
const redHeader = document.getElementById('red_header');
// Add a click event listener
redHeader.addEventListener('click', function() {
    // Select the header element
    const header = document.querySelector('header');
    // Change its text color to red
    header.style.color = '#FF0000';
});