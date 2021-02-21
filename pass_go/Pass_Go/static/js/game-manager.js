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
                // let gameScript = document.createElement("script")
                // gameScript.type = "text/javascript"
                // gameScript.src = url
                // add game js file to document
                //document.head.appendChild(gameScript);



                // Remove game library display
                let gameChooser = document.getElementById("game-container")
                gameChooser.classList.add("hidden")

                // find parent for canvas
                let canvasContainer = document.getElementById("canvas-container")

                async function fetchHtmlAsText(url) {
                    canvasContainer.innerHTML = await (await fetch(url)).text();
                }
                fetchHtmlAsText(url)

                // Canvas Only Games
                // // Remove game library display
                // let gameChooser = document.getElementById("game-container")
                // gameChooser.classList.add("hidden")

                // // create game canvas
                // let canvas = document.createElement("canvas")

                // // find parent for canvas
                // let canvasContainer = document.getElementById("canvas-container")

                // canvas.width = canvasContainer.parentElement.offsetWidth
                // canvas.height = canvasContainer.parentElement.offsetHeight
                // canvas.id = "canvas"

                // // add the canvas to the page
                // canvasContainer.appendChild(canvas)

            })
            .catch(error => console.error(error));
    })
}