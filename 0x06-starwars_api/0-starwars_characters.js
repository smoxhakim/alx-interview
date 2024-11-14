#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (error, res, body) => {
    if (error) console.log(error);
    const json = JSON.parse(body);
    const characters = json.characters.map(
      (item) => new Promise((resolve, reject) => {
        request(item, (error, res, body) => {
          if (error) reject(error);
          resolve(JSON.parse(body).name);
        });
      }));

    Promise.all(characters)
      .then((names) => console.log(names.join('\n')))
      .catch((error) => console.log(error));
  });
}