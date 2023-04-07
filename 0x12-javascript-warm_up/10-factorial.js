#!/usr/bin/node

const args = process.argv;
const num = parseInt(args[2]);

function factorial (n) {
  if (n === 1) {
    return 1;
  }
  if (Number.isNaN(n)) {
    return 1;
  }
  return (n * factorial(n - 1));
}

console.log(factorial(num));
