'use strict'

// get all game tiles
const tiles = document.getElementsByClassName('gameTile')

// on click of a game tile
for (let i = 0; i < tiles.length; i++) {
    tiles[i].addEventListener('click', function () {
        // get game javascript file url
        axios.get(`/get_game_url/${i}`)
            .then(response => {
                // get response data
                let url = response.data.url

                //create game js file
                let gameScript = document.createElement("script")
                gameScript.type = "text/javascript"
                gameScript.src = url
                // add game js file to document
                document.head.appendChild(gameScript);

            })
            .catch(error => console.error(error));
    })
}