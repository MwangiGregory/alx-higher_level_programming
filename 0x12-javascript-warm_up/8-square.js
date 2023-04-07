#!/usr/bin/node

const args = process.argv;
const squareSize = parseInt(args[2]);

if (!squareSize) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= squareSize; i++) {
    let row = '';
    for (let j = 1; j <= squareSize; j++) {
      row = row + 'X';
    }
    console.log(row);
  }
}
