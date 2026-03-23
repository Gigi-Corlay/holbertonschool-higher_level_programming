#!/usr/bin/node
// Select the element that will trigger adding a new item
const addItemDiv = document.getElementById('add_item');

// Add click event listener
addItemDiv.addEventListener('click', function() {
    // Select the ul element with class 'my_list'
    const myList = document.querySelector('ul.my_list');

    // Create a new li element
    const newItem = document.createElement('li');

    // Set its text content
    newItem.textContent = 'Item';

    // Append the new li to the ul
    myList.appendChild(newItem);
});