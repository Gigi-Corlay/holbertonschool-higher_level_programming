#!/usr/bin/node

// Fetch movies from API
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        const listMovies = document.getElementById('list_movies');

        // Loop through movies and add each title to the list
        data.results.forEach(function(movie) {
            const li = document.createElement('li');
            li.textContent = movie.title;
            listMovies.appendChild(li);
        });
    })
    .catch(function(error) {
        console.log('Error:', error);
    });
