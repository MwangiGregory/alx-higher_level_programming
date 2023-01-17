#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request({ uri: url, encoding: 'utf-8' }, (err, res, body) => {
  if (err) console.log(err);

  const todos = JSON.parse(body);
  const temp = {};
  for (let i = 0; i < todos.length; i++) {
    const todo = todos[i];
    const userId = todo.userId;
    const completed = todo.completed;

    if (!(userId.toString() in temp)) {
      temp[userId.toString()] = 0;
    }
    if (completed) {
      temp[userId.toString()] = temp[userId.toString()] + 1;
    }
  }
  for (const key in temp) {
    if (temp[key] === 0) delete temp[key];
  }
  console.log(temp);
});
