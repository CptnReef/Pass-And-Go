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
                let jsFiles = response.data.js
                let htmlFile = response.data.html

                // Get container for custom html
                let container = document.getElementById("canvas-container")
                // appendHTMLToElem(htmlFile, container).then(() => appendJavascript(jsFiles));
                appendHTMLToElem(htmlFile, container).then(
                    () => appendCanvas()).then(
                        () => appendJavascript(jsFiles));

            })
            .catch(error => console.error(error));
    })
}

function appendJavascript(jsFiles) {
    //create game js file
    for (let j = 0; j < jsFiles.length; j++) {

        let gameScript = document.createElement("script")
        gameScript.type = "text/javascript"
        gameScript.src = jsFiles[j]
        // add game js file to document
        document.head.appendChild(gameScript);
    }
}

// Append Custom HTML
async function appendHTMLToElem(htmlFile, elem) {
    elem.innerHTML = await (await fetch(htmlFile)).text();
}

// Append The Canvas Element
function appendCanvas() {

    // Remove game library display
    let gameChooser = document.getElementById("game-container")
    gameChooser.classList.add("hidden")

    // create game canvas
    let canvas = document.createElement("canvas")

    // find parent for canvas
    let canvasContainer = document.getElementById("canvas-container")

    canvas.width = canvasContainer.parentElement.offsetWidth
    canvas.height = canvasContainer.parentElement.offsetHeight
    canvas.id = "canvas"

    // add the canvas to the page
    canvasContainer.appendChild(canvas)
}