#!/usr/bin/node
const request = require('request');

// API URL and character ID
const apiUrl = process.argv[2];
const characterId = 18;

// Make the API request
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const numFilmsWithWedge = films.filter((film) => {
      return film.characters.includes(
        `https://swapi-api.alx-tools.com/api/people/${characterId}/`
      );
    }).length;
    console.log(`${numFilmsWithWedge}`);
  }
});
