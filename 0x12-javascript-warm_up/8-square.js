#!/usr/bin/node

const squareSize = parseInt(process.argv[2]);
let row;

if (!squareSize) {
  console.log('Missing size');
} else {
  for (let i = 0; i < squareSize; i++) {
    row = '';
    for (let j = 0; j < squareSize; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
