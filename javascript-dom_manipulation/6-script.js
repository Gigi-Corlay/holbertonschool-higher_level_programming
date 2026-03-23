#!/usr/bin/node

// Fetch data from the API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        // Select the element with id "character"
        const characterDiv = document.getElementById('character');

        // Display the character name
        characterDiv.textContent = data.name;
    })
    .catch(function(error) {
        console.log('Error:', error);
    });
