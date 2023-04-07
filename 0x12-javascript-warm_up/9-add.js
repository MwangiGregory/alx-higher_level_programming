#!/usr/bin/node

const args = process.argv;
const numOne = parseInt(args[2]);
const numTwo = parseInt(args[3]);

function add (a, b) {
  return a + b;
}

console.log(add(numOne, numTwo));
