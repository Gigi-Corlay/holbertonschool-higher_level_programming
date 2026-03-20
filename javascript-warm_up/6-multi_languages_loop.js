#!/usr/bin/node

// Create an array containing all the lines to print
const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

// Initialize an empty string to store all lines
let output = '';

// Loop through the array
for (const language of languages) {
  output += language + '\n'; // Add each line followed by a newline
}

// Print all lines at once using a single console.log
console.log(output.trim()); // trim() removes the extra newline at the end