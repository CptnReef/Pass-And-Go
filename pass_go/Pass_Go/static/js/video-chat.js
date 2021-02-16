// Config variables: change them to point to your own servers
const SIGNALING_SERVER_URL = 'https://rtc.pass-go.net';
const TURN_SERVER_URL = 'turn:rtc.pass-go.net:3478';
const TURN_SERVER_USERNAME = 'username';
const TURN_SERVER_CREDENTIAL = 'credential';
// WebRTC config: you don't have to change this for the example to work
// If you are testing on localhost, you can just use PC_CONFIG = {}
const PC_CONFIG = {

};

// Signaling methods
let socket = io(SIGNALING_SERVER_URL,
    {
        autoConnect: false
    });

socket.on('data', (data) => {
    console.log('Data received: ', data);
    handleSignalingData(data);
});

socket.on('ready', (data) => {
    console.log('Ready');
    // Connection with signaling server is ready, and so is local stream
    createPeerConnection();
    sendOffer();
});

let sendData = (data) => {
    socket.emit('data', data);
};

// WebRTC methods
let pc;
let localStream;
let localStreamNoAudio;
let remoteStreamElement = document.querySelector('#remoteStream');
let localStreamElement = document.querySelector('#localStream');
let getLocalStream = () => {
    navigator.mediaDevices.getUserMedia({ audio: true, video: true })
        .then((stream) => {
            console.log('Stream found');
            localStream = stream;
            localStreamNoAudio = stream.clone();

            var audioTrackList = localStreamNoAudio.getAudioTracks();
            while (audioTrackList.length > 0) {
                localStreamNoAudio.removeTrack(audioTrackList[0]);
                audioTrackList = localStreamNoAudio.getAudioTracks();
            }
            console.log('Remove Audio from user display stream');

            localStreamElement.srcObject = localStreamNoAudio;
            console.log('Set self stream');
            // Connect after making sure that local stream is availble
            socket.connect();
        })
        .catch(error => {
            console.error('Stream not found: ', error);
        });
}


let createPeerConnection = () => {
    try {
        pc = new RTCPeerConnection(PC_CONFIG);
        pc.onicecandidate = onIceCandidate;
        pc.onaddstream = onAddStream;
        pc.addStream(localStream);
        console.log('PeerConnection created');
    } catch (error) {
        console.error('PeerConnection failed: ', error);
    }
};

let sendOffer = () => {
    console.log('Send offer');
    pc.createOffer().then(
        setAndSendLocalDescription,
        (error) => { console.error('Send offer failed: ', error); }
    );
};

let sendAnswer = () => {
    console.log('Send answer');
    pc.createAnswer().then(
        setAndSendLocalDescription,
        (error) => { console.error('Send answer failed: ', error); }
    );
};

let setAndSendLocalDescription = (sessionDescription) => {
    pc.setLocalDescription(sessionDescription);
    console.log('Local description set');
    sendData(sessionDescription);
};

let onIceCandidate = (event) => {
    if (event.candidate) {
        console.log('ICE candidate');
        sendData({
            type: 'candidate',
            candidate: event.candidate
        });
    }
};

let onAddStream = (event) => {
    console.log('Add stream');
    remoteStreamElement.srcObject = event.stream;
};

let handleSignalingData = (data) => {
    switch (data.type) {
        case 'offer':
            createPeerConnection();
            pc.setRemoteDescription(new RTCSessionDescription(data));
            sendAnswer();
            break;
        case 'answer':
            pc.setRemoteDescription(new RTCSessionDescription(data));
            break;
        case 'candidate':
            pc.addIceCandidate(new RTCIceCandidate(data.candidate));
            break;
    }
};

// Start connection
getLocalStream();
