#!/usr/bin/node

const n = parseInt(process.argv[2]);

function factorial(x) {
  if (isNaN(x) || x <= 0) {
    return 1;
  }
  return x * factorial(x - 1);
}

console.log(factorial(n));
