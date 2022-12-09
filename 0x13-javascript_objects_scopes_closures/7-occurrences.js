#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  if (list && searchElement) {
    for (let i = 0; i <= list.length - 1; i++) {
      if (list[i] === searchElement) {
        count++;
      }
    }
  }
  return count;
};
