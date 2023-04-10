#!/usr/bin/node

let numOfPrintedArgs = 0;

exports.logMe = function (item) {
  const currentArgument = item;
  console.log(`${numOfPrintedArgs}: ${currentArgument}`);
  numOfPrintedArgs++;
};
