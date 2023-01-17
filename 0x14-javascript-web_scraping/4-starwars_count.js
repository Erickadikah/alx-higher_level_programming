#!/usr/bin/node
// script prints the number of movies where
// the character "Wedge Antilles" is present

const req = require('request');
const url = process.argv[2];

req.get(url,
  function (err, response, body) {
    if (err) console.error(err); else {
      const jsonBody = JSON.parse(body);
      const results = jsonBody.results;
      let count = 0;
      results.forEach(function (movie, idx) {
        const characters = movie.characters;
        characters.forEach(function (character, idx) {
          if (character.includes('18')) {
            count++;
          }
        });
      });
      console.log(count);
    }
  });
