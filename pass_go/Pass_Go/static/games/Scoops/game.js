const canvas = document.querySelector('canvas')
// get the canvas context
const ctx = canvas.getContext('2d')

const width = canvas.width
canvas.height = canvas.width / 4
const height = canvas.height
// background square
drawRect(0, 0, width, height, "#E6E6FA")

// draw a rectangle
function drawRect(x, y, width, height, color) {
    ctx.beginPath()
    ctx.rect(x, y, width, height)
    ctx.fillStyle = color
    ctx.fill()
}