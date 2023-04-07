#!/usr/bin/node

const args = process.argv;
const numberArg = parseInt(args[2]);

if (!numberArg) {
  console.log('Not a number');
} else {
  console.log(`My number: ${numberArg}`);
}
