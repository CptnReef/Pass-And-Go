// thpace setup for homepage hero animation
const canvas = document.querySelector('#hero-image');

const settings = {
    // Settings
    colors: ['#4c8fef', '#424959', '#c844ff'],
    triangleSize: 100,
    pointAnimationSpeed: 10000,
    particleSettings: {
        interval: 5000,
        color: "#CCCCCC"
    }

};

Thpace.create(canvas, settings);