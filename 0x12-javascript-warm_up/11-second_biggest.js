#!/usr/bin/node

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('0');
} else {
  let numbers = process.argv.slice(2);
  numbers = numbers.map(num => parseInt(num));

  const maxNum = Math.max(...numbers);
  const index = numbers.indexOf(maxNum);

  numbers.splice(index, 1);
  console.log(Math.max(...numbers));
}
