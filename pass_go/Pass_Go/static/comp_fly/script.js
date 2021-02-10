            
            // Setting Up Canvas

const canvas = document.getElementById('canvas1')
const ctx = canvas.getContext('2d')
canvas.width = 800;
canvas.height = 500;

//Globally defined variables
let score = 0;
//Esentially tracks how long the game is running
let gameFrame = 0;
ctx.font = '50px Georgia'; 


            //Mouse Interaction

//Defining canvasPosition, logging where the canvas is in relative porportion to the page
let canvasPosistion = canvas.getBoundingClientRect()
        // console.log(canvasPosistion)

//Function stores information about the mouse, specifically the x and y coordinates
const mouse = {

    x: canvas.width/2,

    y: canvas.height/2,

    //negates if the mouse is already clicked, by overiding it to false
    click: false, 
}

canvas.addEventListener('mousedown', function(event){
    //Changing the x coordinate of the mouse cursor to where the event happened, in this case the event is a click
    mouse.x = event.x - canvasPosistion.left;
    //We subtract the canvasPosition.left for the x cord because whenever our mouse is on the left wall of the box our x cord should be 0
    mouse.y = event.y - canvasPosistion.top;

    // console.log(mouse.x, mouse.y) 
})

            //Player
class Player {
    //Blueprint for the class, showing what properties it takes in
    constructor(){
        //Have the player move to the mouse coordinates
        this.x = canvas.width/2;
        this.y = canvas.height/2;

        //hitbox
        this.radius = 50;

        //this controls what angle the player is facing
        this.angle = 0;

        //Tracks the players coordinates per frame
        this.frameX = 0;
        this.frameY = 0;

        //Tracks overall frame we are currently on
        this.frame = 0;

        //Got the information from the sprite sheet
        this.spriteWidth = 205;
        this.spriteHeight = 150.4;

    }
    // updating player position
    update(){
        const dx = this.x - mouse.x
        const dy = this.y - mouse.y
        //If our mouse coordinate is not equal to our player coordinate
        if(mouse.x != this.x){
            // Makes this.x which is where the player move the difference of where the mouse is on a coordinate
            this.x -= dx;
        }
        if(mouse.y != this.y){
            this.y -= dy;
        }
    }
}

            //Obstacles

            //Animation Loop