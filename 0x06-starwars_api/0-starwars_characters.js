#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];
const filmsEndpoint = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

request.get(filmsEndpoint, (error, response, body) => {
  if (error) console.log(error);
  const filmData = JSON.parse(body);

  filmData.characters.forEach(function (peopleEndpoint) {
    request.get(peopleEndpoint, (error, response, body) => {
      if (error) console.log(error);
      const peopleData = JSON.parse(body);
      console.log(peopleData.name);
    });
  });
});
