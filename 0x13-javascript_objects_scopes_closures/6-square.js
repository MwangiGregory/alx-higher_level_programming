#!/usr/bin/node
const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let h = 0; h < this.height; h++) {
        let row = '';
        for (let w = 0; w < this.width; w++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
}

module.exports = Square;
