interface Window {
    Music: any;
}

function Play(element, flag) {
    var dom = document.querySelector(element);
    if (flag) {
        dom.play();
    }
    else {
        dom.pause();
    }
}

function GetMusicTime(element) {
    var dom = document.querySelector(element);
    let obj = {
        currentTime: dom.currentTime,
        duration: dom.duration
    }
    let json = JSON.stringify(obj);

    return json
}

function SetMusicTime(element, time) {
    var dom = document.querySelector(element);
    dom.currentTime = time;
}

window.Music = {
    //print: Print,
    play: Play,
    getMusicTime: GetMusicTime,
    setMusicTime: SetMusicTime
}