#!/usr/bin/node

const args = process.argv;
const number_arg = parseInt(args[2]);

if (!number_arg) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number_arg}`);
}
