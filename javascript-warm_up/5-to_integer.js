#!/usr/bin/node

const num = parseInt(process.argv[2], 10);

console.log(!isNaN(num) ? `My number: ${num}` : 'Not a number');