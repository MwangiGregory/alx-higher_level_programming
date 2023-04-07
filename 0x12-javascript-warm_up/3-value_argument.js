#!/usr/bin/node

const args = process.argv;
const minArgsLength = 2;
const argsLength = args.length - minArgsLength;

if (argsLength === 0) {
  console.log('No argument');
} else if (argsLength >= 1) {
  console.log(args[2]);
}
