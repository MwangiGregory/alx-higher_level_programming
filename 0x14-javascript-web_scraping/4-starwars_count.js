#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request({ url: url, encoding: 'utf-8' }, (err, res, body) => {
  if (err) console.log(err);

  const filmDetails = JSON.parse(body).results;
  let count = 0;

  for (let i = 0; i < filmDetails.length; i++) {
    const film = filmDetails[i];
    const characters = film.characters;

    for (let j = 0; j < characters.length; j++) {
      const url = characters[j];
      if (url === characterUrl) {
        count++;
      }
    }
  }
  console.log(count);
});
