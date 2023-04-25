#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body);

  const completedTasksByUserId = {};
  todos.forEach((todo) => {
    if (todo.completed) {
      const userId = todo.userId;
      const completedTasks = completedTasksByUserId[userId] || 0;
      completedTasksByUserId[userId] = completedTasks + 1;
    }
  });

  console.log(completedTasksByUserId);
});
