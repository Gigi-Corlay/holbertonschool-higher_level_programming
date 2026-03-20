#!/usr/bin/node

function factorial(nbr) {
  if (isNaN(nbr) || nbr <= 0) {
    return 1;
  }
  return nbr * factorial(nbr - 1);
}

const n = parseInt(process.argv[2]);
console.log(factorial(n));
