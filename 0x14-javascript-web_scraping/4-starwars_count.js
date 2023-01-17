#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = 18;

request({ url: url, encoding: 'utf-8' }, (err, res, body) => {
  if (err) console.log(err);
  let count = 0;
  const results = JSON.parse(body).results;

  for (let i = 0; i < results.length; i++) {
    const filmDetails = results[i];
    const characters = filmDetails.characters;

    for (let j = 0; j < characters.length; j++) {
      const url = characters[j];

      if (url.endsWith(characterId.toString().concat('/'))) {
        count++;
      }
    }
  }
  console.log(count);
});
