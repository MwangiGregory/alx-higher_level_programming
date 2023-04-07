#!/usr/bin/node

const args = process.argv;
const list = [];

for (let i = 2; i < args.length; i++) {
  const num = parseInt(args[i]);
  list.push(num);
}

let largestNum;
let secondLargestNum;

if (list.length === 2 || list.length === 3) {
  secondLargestNum = 0;
} else if (list.length > 3) {
  for (let i = 0; i < list.length; i++) {
    if (i === 0) {
      largestNum = list[i];
      continue;
    }
    if (list[i] > largestNum) {
      secondLargestNum = largestNum;
      largestNum = list[i];
    }
  }
}

console.log(secondLargestNum);
