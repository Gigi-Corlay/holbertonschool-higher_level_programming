#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  const unique = [...new Set(args)];
  if (unique.length < 2) {
    console.log(0);
  } else {
    unique.sort((a, b) => b - a);
    console.log(unique[1]);
  }
}
