#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function(){
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        const helloDiv = document.getElementById('hello');
        helloDiv.textContent = data.hello;
    })
    .catch(function(error) {
        console.log('Error:', error);
    });
});
