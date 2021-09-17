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
    var obj = {
        currentTime: dom.currentTime,
        duration: dom.duration
    };
    var json = JSON.stringify(obj);
    return json;
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
};
//# sourceMappingURL=main.js.map