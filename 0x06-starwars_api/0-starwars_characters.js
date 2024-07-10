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
    const peopleName = urlPeople.map(
      url => new Promise((resolve, reject) => {
        request(url, (promError, _, promBody) => {
          if (promError) {
            reject(promError);
          } else {
            resolve(JSON.parse(promBody).name);
          }
        });
      })
    );
    Promise.all(peopleName)
      .then(names => console.log(names.join('\n')))
      .catch(Err => console.log(Err));
  }
});
