#!/usr/bin/node

// Convert first argument to integer
const x = parseInt(process.argv[2]);

// Check if the argument is not a number
if (isNaN(x)) { 
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}