console.log(gsap)

const canvas = document.querySelector('canvas')

const c = canvas.getContext('2d')
canvas.width = window.innerWidth
canvas.height = window.innerHeight

const scored = document.querySelector('#scored')
const startGameBtn = document.querySelector('#startGameBtn')
const modalEl = document.querySelector('#modalEl')
const totalScore = document.querySelector('#ttlScore')

// Interchangable
let score = 0
let charge

class Player {
    constructor(x,y,radius,color) {
        this.x = x
        this.y = y
        this.radius = radius
        this.color = color
    }

    draw() {
        c.beginPath()
        //This draws an eclipse.
        c.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false)
        // Fills in player.
        c.fillStyle = this.color
        c.fill()
    }
}

class Projectile {
    constructor(x,y,radius,color,velocity) {
        this.x = x
        this.y = y
        this.radius = radius
        this.color = color
        this.velocity = velocity
    }

    draw() {
        c.beginPath()
        //This draws an eclipse.
        c.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false)
        // Fills in player.
        c.fillStyle = this.color
        c.fill()
    }

    update() {
        this.draw()
        this.x = this.x + this.velocity.x
        this.y = this.y + this.velocity.y
    }
}

class Enemy {
    constructor(x,y,radius,color,velocity) {
        this.x = x
        this.y = y
        this.radius = radius
        this.color = color
        this.velocity = velocity
    }

    draw() {
        
        c.beginPath()
        c.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false)
        c.fillStyle = this.color
        //              top-edge
        c.moveTo(this.x + 30, this.y - 30);
        //              bottom-edge       
        c.lineTo(this.x + 30, this.y + 30);
        //              center arrow
        c.lineTo(this.x, this.y);
        c.fill()
    }

    update() {
        this.draw()
        this.x = this.x + this.velocity.x
        this.y = this.y + this.velocity.y
    }
}

const friction = 0.99
class Particle {
    constructor(x,y,radius,color,velocity) {
        this.x = x
        this.y = y
        this.radius = radius
        this.color = color
        this.velocity = velocity
        this.alpha = 1
    }

    draw() {
        c.save()
        c.globalAlpha = this.alpha
        c.beginPath()
        c.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false)
        c.fillStyle = this.color
        c.fill()
        c.restore()
    }

    update() {
        this.draw()
        this.velocity.x *= friction
        this.velocity.y *= friction
        this.x = this.x + this.velocity.x
        this.y = this.y + this.velocity.y
        this.alpha -= 0.01
    }
}

//Player Position
const x = canvas.width / 2
const y = canvas.height / 2

let player1 = new Player(x, y, 10, 'white')
let projectiles = []
let enemies = []
let particles = []

//Increases Enemy's Spawning
if (score <= 0 && score >= 5000 ) {
    charge = 1000
} else if (score > 5000 && score <= 10000) {
    charge = 800
} else {
    charge = 500
}

//This func holds the Restart value
function init() {
    player1 = new Player(x, y, 10, 'white')
    projectiles = []
    enemies = []
    particles = []
    score = 0
    scored.innerHTML = score
    totalScore.innerHTML = score
}

player1.draw()
//==================================================================================================//
function spawnEnemies() {
    setInterval(() => {
        let randMath = Math.random()
        let quickmaffs = Math.random() < Math.random() ? -1 : 1
        const radius = 30
        let x
        let y 

        if (Math.random() < 0.5) {
            x = randMath < 0.5 ? (canvas.width/2): ((canvas.width) * quickmaffs)
            y = randMath < 0.5 ? (canvas.height * quickmaffs): (canvas.height/2)
        }

        const color = `hsl(${Math.random() * 360}, 50%, 50%)`

        const angle = Math.atan2(
            canvas.height / 2 - y,
            canvas.width / 2 - x)

        const velocity = {
            x: Math.cos(angle) * 2,
            y: Math.sin(angle) * 2
        }
        
        
        enemies.push(new Enemy(x,y,radius,color,velocity))
    }, charge)
}
//==================================================================================================//

let animationID
// let score = 0
function animate() {
    animationID = requestAnimationFrame(animate)
    c.fillStyle = 'rgba(0,0,0,0.1)'
    c.fillRect(0, 0, canvas.width, canvas.height)
    player1.draw()
    particles.forEach((particle, index) => {
        if (particle.alpha <= 0) {
            particles.splice(index, 1)
        } else {
            particle.update()
        }
    })

    projectiles.forEach((projectile, index) => {
        projectile.update()
        //remove offscreen projectiles
        if (projectile.x + projectile.radius < 0 ||
            projectile.x - projectile.radius > canvas.width ||
            projectile.y + projectile.radius < 0 ||
            projectile.y - projectile.radius > canvas.height
        ) {
            setTimeout(() => {
                projectiles.splice(index, 1)
            }, 0)
        }
    })

    enemies.forEach((enemy, index) => {
        enemy.update()
        const dist = Math.hypot(player1.x - enemy.x, player1.y - enemy.y)    
        //player touches    (((END GAME)))
        if (dist - enemy.radius - player1.radius < 1) {
                cancelAnimationFrame(animationID)
                modalEl.style.display = 'flex'
                totalScore.innerHTML = score
            }
            projectiles.forEach((projectile, projectileIndex) => {
            const dist = Math.hypot(projectile.x - enemy.x, projectile.y - enemy.y)
            //objects touches
            if (dist - enemy.radius - projectile.radius < 1) {
                //create explosions
                for (let i = 0; i < enemy.radius * 2; i++) {
                    particles.push(new Particle(projectile.x, projectile.y, Math.random() * 2, enemy.color, {
                        x: (Math.random() - 0.5) * (Math.random() * 6),
                        y: (Math.random() - 0.5) * (Math.random() *  6)
                      })
                    )
                }
                if (enemy.radius - 10 > 5) {
                    //Increase Score
                    score += 100
                    scored.innerHTML = score 

                    gsap.to(enemy, {
                        radius: enemy.radius - 10
                    })
                    setTimeout(() => {
                        projectiles.splice(projectileIndex, 1)
                    }, 0)
                } else {
                    // remove from entire scene
                    score += 250
                    setTimeout(() => {
                        enemies.splice(index, 1)
                        projectiles.splice(projectileIndex, 1)
                    }, 0)    
                }
            }
        })
    })
}

//==================================================================================================//
//Respond to key
addEventListener('click', (event) => {
    const angle = Math.atan2(
        event.clientY - canvas.height / 2,
        event.clientX - canvas.width / 2
        )
    
    const velocity = {
        x: Math.cos(angle) * 5,
        y: Math.sin(angle) * 5
    }
    
    projectiles.push( new Projectile(
        canvas.width / 2, canvas.height / 2, 5, 'white', velocity)
    )
})

startGameBtn.addEventListener('click', () => {
    init()
    animate()
    spawnEnemies()
    modalEl.style.display = 'none'
})