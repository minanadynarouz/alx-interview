#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const urlPeople = data.characters;
    for (let i = 0; i < urlPeople.length; i++) {
      request(urlPeople[i], (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const data = JSON.parse(body);
          console.log(data.name);
        }
      });
    }
  }
});
