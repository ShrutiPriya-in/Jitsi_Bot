const domain = 'meet.jit.si';
const options = {
    roomName: 'CBDNS_Meeting',
    width: "100%",
    height: "100%",
    parentNode: document.querySelector('#meet'),
    lang: 'en'
};
const api = new JitsiMeetExternalAPI(domain, options);

let roomName = "";
let userName = "";
api.addEventListeners({

    videoConferenceJoined: function (e) {
        roomName = e.roomName;
        userName = e.displayName;
        const options = {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(e)
        };
        fetch("http://127.0.0.1:5500/meet-start", options)
            .then(res => {});
    },

    videoConferenceLeft: function (e) {
        e.userName = userName;
        const options = {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(e)
        };
        fetch("http://127.0.0.1:5500/meet-end", options)
            .then(res => {
            });
    },

    videoMuteStatusChanged:function(e)
    {
        e.roomName = roomName;
        e.userName = userName;

        const options = {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(e)
        };
        if(e.muted){           
            fetch("http://127.0.0.1:5500/video-off", options)
                .then(res => {
                });
        }
        else{
            fetch("http://127.0.0.1:5500/video-on", options)
            .then(res=>{
            });
        }
    },

    audioMuteStatusChanged: function(e)
    {
        e.roomName=roomName;
        e.userName = userName;

        const options = {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(e)
        };
        if(e.muted){
            fetch("http://127.0.0.1:5500/audio-off", options)
                .then(res => {
                });
        }
        else{
            fetch("http://127.0.0.1:5500/audio-on", options)
            .then(res=>{
            });
        }
    },

    screenSharingStatusChanged:function(e)
    {
        e.roomName=roomName;
        e.userName = userName;

        const options = {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(e)
        };
        
        if(e.on){
            fetch("http://127.0.0.1:5500/screen-on", options)
                .then(res => {
                });
        }
        else{
            fetch("http://127.0.0.1:5500/screen-off", options)
            .then(res=>{
            });
        }
    },
});
