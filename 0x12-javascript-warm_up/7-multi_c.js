#!/usr/bin/node

const str = 'C is fun';
const n = parseInt(process.argv[2]);

if (!n) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < n; i++) {
    console.log(str);
  }
}
