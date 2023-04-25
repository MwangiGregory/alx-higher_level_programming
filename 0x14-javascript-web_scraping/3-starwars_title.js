#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2]; // get the movie ID from the command-line arguments
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
