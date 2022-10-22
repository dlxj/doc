// ==UserScript==
// @name         animelon-subtitle-downloader
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  download animelon subtitles
// @author       mescyn#5794
// @match        https://animelon.com/video/*
// @grant        unsafeWindow
// @grant        GM_registerMenuCommand
// @require     https://cdn.jsdelivr.net/npm/file-saver-es@2.0.5/dist/FileSaver.min.js
// ==/UserScript==

GM_registerMenuCommand("Download Subtitles", AnimelonSubtitleDownloader);

// downloads all subtitle options (english, hiragana, katakana, japanese romaji)
function AnimelonSubtitleDownloader()
{
    var subtitles = angular.element(dialogueHistoryLists).scope().$parent.subtitlesArray;

    for (var i = 0; i < subtitles.length; i++)
    {
        var s = subtitles[i].assString;
        var decodedSubtitles = CryptoJS.AES.decrypt(s.substring(8,s.length-5),s.substring(0,8).split("").reverse().join("")).toString(CryptoJS.enc.Utf8).replace(/undefined/g,"");
        var blob = new Blob([decodedSubtitles], {type: "text/plain;charset=utf-8"});
        var subtitle_name = "animelon_" + document.URL.split('/').reverse()[0] + '_' + subtitles[i].language + '.ass';
        saveAs(blob, subtitle_name);
    }
}
