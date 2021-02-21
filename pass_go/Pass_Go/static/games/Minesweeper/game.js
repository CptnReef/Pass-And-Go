const canvas = document.querySelector('canvas')
// get the canvas context
const ctx = canvas.getContext('2d')

const width = canvas.width
const height = canvas.width / 2
// background square
drawRect(0, 0, width, height, "#222222")

// draw a rectangle
function drawRect(x, y, width, height, color) {
    ctx.beginPath()
    ctx.rect(x, y, width, height)
    ctx.fillStyle = color
    ctx.fill()
}