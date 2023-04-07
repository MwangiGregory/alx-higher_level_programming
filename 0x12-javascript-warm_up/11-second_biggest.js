#!/usr/bin/node

const args = process.argv;
const list = args.map((arg) => parseInt(arg));

let largestNum;
let secondLargestNum;

if (list.length === 2 || list.length === 3) {
  secondLargestNum = 0;
} else if (list.length > 3) {
  for (let i = 2; i < list.length; i++) {
    if (i === 2) {
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
