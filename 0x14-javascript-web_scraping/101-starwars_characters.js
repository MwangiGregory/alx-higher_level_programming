#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request({ uri: url, encoding: 'utf-8' }, (err, res, body) => {
  if (err) console.log(err);
  const filmDetails = JSON.parse(body);
  const characters = filmDetails.characters;
  
  let names = {};
  characters.forEach((url, index) => {
    let r = request({ uri: url, encoding: 'utf-8' }, (err, res, body) => {
      if (err) console.log(err);
      const characterDetails = JSON.parse(body);
      const name = characterDetails.name;
      console.log(index);
      names[name] = index;
    });
    console.log(r);
  });
  console.log(names);
});



