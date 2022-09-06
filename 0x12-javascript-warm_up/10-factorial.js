#!/usr/bin/node

function factorial (integer) {
  if (!integer || integer === 1) {
    return (1);
  }
  return (integer * factorial(integer - 1));
}

const integer = parseInt(process.argv[2]);

console.log(factorial(integer));
