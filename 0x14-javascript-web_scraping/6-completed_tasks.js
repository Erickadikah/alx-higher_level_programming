#!/usr/bin/node
// computing the number of tasks completed by user id
const request = require('request');
const url = process.argv[2];

request.get(
  url,
  function (err, res, body) {
    if (err) console.error(err);
    const todos = JSON.parse(body);
    const output = {};
    todos.forEach(function (todo, idx) {
      if (todo.completed) {
        if (todo.userId in output) {
          output[todo.userId]++;
        } else {
          output[todo.userId] = 1;
        }
      }
    });
    console.log(output);
  });
