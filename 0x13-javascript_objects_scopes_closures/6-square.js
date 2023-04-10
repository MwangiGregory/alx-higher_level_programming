#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint (C) {
    if (!C) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(C.repeat(this.width));
      }
    }
  }
};
