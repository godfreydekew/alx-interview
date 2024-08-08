#!/usr/bin/node
const request = require('request-promise-native'); // Use request-promise-native for promises

// Function to get character names asynchronously
async function getCharacterNames (movieId) {
  const filmsEndpoint = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  try {
    // Fetch the film data
    const filmData = await request(filmsEndpoint);
    const film = JSON.parse(filmData);

    // Iterate over the characters and fetch each one's data
    for (const characterUrl of film.characters) {
      const characterData = await request(characterUrl);
      const character = JSON.parse(characterData);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as an argument.');
  process.exit(1);
}

getCharacterNames(movieId);
