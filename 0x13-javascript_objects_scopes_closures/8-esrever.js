#!/usr/bin/node

exports.esrever = function (list) {
  if (list) {
    const reversedList = [];
    for (let i = 0; i <= list.length - 1; i++) {
      reversedList.unshift(list[i]);
    }
    return reversedList;
  }
};
