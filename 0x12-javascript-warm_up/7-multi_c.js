#!/usr/bin/node

const args = process.argv;
const numberOfOccurrences = parseInt(args[2]);

if (!numberOfOccurrences) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numberOfOccurrences; i++) {
    console.log('C is fun');
  }
}
