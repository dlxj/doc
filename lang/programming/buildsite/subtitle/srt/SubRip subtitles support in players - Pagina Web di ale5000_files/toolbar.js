"use strict";

try { var referer = decodeURIComponent(location.search.match(/ref=(.+?)(&|$)/)[1]).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); } catch(e) {}

var T = {
	$: function(id) { return document.getElementById(id); },
	clockWidgets: [],
	clockCount: 0,
	rankCount: 0,
	marqueeWidgets: [],
	counterWidgets: [],
	friendWidgets: [],
	rankWidgets: [],
	referer: referer,
	iubenda: (location.search.search(/iubenda=\d/) > -1) ? parseInt(location.search.match(/iubenda=(\d)/)[1]) : 0,
	init: function() {
		var dx = T.$('tb-dx'), sx = T.$('tb-sx');
		var ls = (dx.children.length && dx.children[0].className == 'tb-tools') ? [ dx.children[0], sx.children[1] ] : [ dx, sx ];
		for (var i = 0; i < ls.length; i++) {
			var ch = ls[i].children;
			for (var j = 0; j < ch.length; j++) switch (ch[j].getAttribute('data-type')) {
				case 'clock':
					T.clockWidgets.push(ch[j]);
					break;
				case 'marquee':
					var w = 0;
					var ul = ch[j].getElementsByTagName('ul')[0];
					var lis = ch[j].getElementsByTagName('li');
					for (var k = 0; k < lis.length; k++) w += lis[k].offsetWidth;
					ul.style.width = (w+10)+"px";
					ul.style.left = '0px';
					T.marqueeWidgets.push(ul);
					break;
				case 'counter':
					T.counterWidgets.push(ch[j]);
					break;
				case 'rank':
					T.rankWidgets.push(ch[j]);
					break;
				case 'friend':
					T.friendWidgets.push(ch[j]);
					break;
			}
		}

		window.parent.postMessage(JSON.stringify(TC), '*');

		if (T.clockWidgets.length) setInterval(T.clock, 1000);
		if (T.marqueeWidgets.length) setInterval(T.marquee, 50);
		if (T.rankWidgets.length) {
			T.ajaxRequest('//tb.altervista.org/tb_js/'+TC.userhash+'/tb_hits_'+TC.username+'.js?'+(new Date()).getTime(), 'rank');
			setInterval(T.rank, 2000);
		}
		if (T.friendWidgets.length) T.friend();
		if (T.counterWidgets.length) T.ajaxRequest('//tb.altervista.org/fcgi/counter.pl?&'+TC.username+'&99&'+(new Date()).getTime(), 'counter');

		if (!T.iubenda) {
			var els = document.getElementsByClassName('tooltip left');
			for (i = 0; i < els.length; i++) {
				els[i].style.display = "none";
				var l = els[i].previousElementSibling;
				l.target = "_blank";
				var src = l.getAttribute('data-src')
				src = encodeURIComponent(src ? src : T.referer);
				switch (l.parentNode.className) {
					case 'tb-facebook':
						l.href = "https://www.facebook.com/sharer/sharer.php?u="+src;
						break;
					case 'tb-twitter':
						l.href = "https://www.twitter.com/share?url="+src;
						break;
					case 'tb-google-plus':
						l.href = "https://plus.google.com/share?url="+src;
						break;
					case 'tb-youtube':
						l.href = "https://www.youtube.com/channel/"+src;
						break;
				}
			}
		}
	},

	aggiungi: function() {
		if (document.documentElement.lang == "en") {
			alert('Press CTRL+D to add this page to your bookmarks');
		} else {
			alert('Premi CTRL+D per aggiungere questa pagina ai segnalibri');
		}
		return false;
	},

	zeroFill: function(value) {
		if (value < 10) value = "0" + value;
		return value;
	},

	clock: function() {
		T.clockCount = ++T.clockCount % 6;
		var currentTime = new Date();
		for (var i = 0; i < T.clockWidgets.length; i++) {
			var span = T.clockWidgets[i].getElementsByTagName('span')[0];
			if (T.clockCount < 3) {
				span.firstChild.nodeValue = T.zeroFill(currentTime.getDate()) + "/" + T.zeroFill(currentTime.getMonth() + 1) + "/" + currentTime.getFullYear();
			} else {
				span.firstChild.nodeValue = T.zeroFill(currentTime.getHours()) + ":" + T.zeroFill(currentTime.getMinutes()) + ":" + T.zeroFill(currentTime.getSeconds());
			}
		}
	},

	rank: function() {
		T.rankCount = ++T.rankCount % 3;
		for (var i = 0; i < T.rankWidgets.length; i++) {
			for (var j = 0; j < 3; j++) {
				T.rankWidgets[i].children[j].className = (j == T.rankCount ? 'tb-transition-active' : 'tb-transition-hidden');
			}
		}
	},

	marquee: function() {
		for (var i = 0; i < T.marqueeWidgets.length; i++) {
			var x = parseInt(T.marqueeWidgets[i].style.left)-1;
			if (-x == T.marqueeWidgets[i].offsetWidth) x = 0;
			T.marqueeWidgets[i].style.left = x+'px';
		}
	},

	friend: function() {
		for (var i = 0; i < T.friendWidgets.length; i++) {
			var w = T.friendWidgets[i];
			var f = JSON.parse(w.getElementsByTagName('script')[0].firstChild.nodeValue);
			w.getElementsByTagName('a')[0].href = f.length ? "http://"+f[Math.floor(Math.random() * f.length)]+".altervista.org" : '#';
		}
	},

	ajaxRequest: function(url, type) {
		var xhr = new XMLHttpRequest();
		xhr.av_type = type;
		if (xhr.addEventListener) xhr.addEventListener('load', T.ajaxResponse, false); else xhr.onreadystatechange = function() { if (xhr.readyState == 4 && (xhr.status == 200 || xhr.status == 0)) T.ajaxResponse };
		xhr.open('GET', url, true);
		xhr.send();
	},

	ajaxResponse: function(ev) {
		try {
			switch (this.av_type) {
				case 'counter':
					var value = (this.status == 200 && this.responseText) ? this.responseText : '••••••';
					for (var j = 0; j < T.counterWidgets.length; j++) {
						T.counterWidgets[j].getElementsByTagName('span')[0].firstChild.nodeValue = value;
					}
					break;
				case 'rank':
					var value = {catpos: "n/a", hitspos: "n/a"}
					if (this.status == 200 && this.responseText) {
						try {
							value = JSON.parse(this.responseText.replace(/'/g, '"'));
							value.catpos += "°";
							value.hitspos += "°";
						} catch (e) {
							console.error(e);
						};
					}
					for (var j = 0; j < T.rankWidgets.length; j++) {
						var s = T.rankWidgets[j].getElementsByTagName('span');
						s[1].firstChild.nodeValue = value.catpos;
						s[2].firstChild.nodeValue = value.hitspos;
					}
					break;
			}
		} catch (e) {
			console.error(e);
		};
	}
}

if (window.addEventListener) {
	window.addEventListener('load', T.init, false);
} else {
	window.attachEvent('onload', T.init);
}
