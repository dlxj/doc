"use strict";

(function() {

	function resize() {
		var r = document.documentElement;
		var b = document.body;
		b.style.position = "relative";

		if (ifr.style.position == "fixed") {
			ifr.style.top = ifr.style.left = div.style.top = div.style.right = 0;
			ifr.style.width = "100%";
		} else {
			var s = style;
			var pxl = s(r, 'marginLeft') + s(r, 'borderLeftWidth') + s(r, 'paddingLeft') + s(b, 'marginLeft') + s(b, 'borderLeftWidth');
			var pxd = document.documentElement.scrollWidth - style(b, 'width') - style(b, 'paddingLeft') - style(b, 'paddingRight');

			ifr.style.left = (-pxl) + 'px';
			ifr.style.width = "100%";
			ifr.style.width = "calc(100% + "+pxd+"px)";
			div.style.right = (-pxd+s(b, 'marginRight')+s(b, 'borderRight')) + 'px';

			b.style.marginTop = (omt+hh)+"px";

			var py = style(r, 'marginTop') + style(r, 'borderTopWidth') + style(r, 'paddingTop') + style(b, 'marginTop') + style(b, 'borderTopWidth');
			div.style.top = ifr.style.top = (-py)+"px";
		}
	}

	// Passare le proprieta` CSS col nome javascript-like (es. marginLeft)
	function style(el, pr, m) {
		var v;
		if (!el)return 0;
		if (document.defaultView && document.defaultView.getComputedStyle) v = document.defaultView.getComputedStyle(el, null)[pr];
		else if (el.currentStyle) v = el.currentStyle[pr];
		else v = el.style[pr];
		return (m ? v : parse(v));
	}

	function bulkElement(tag, d) { var el = document.createElement(tag); for (i in d) el.setAttribute(i, d[i]); return el; };
	function bulkStyle(el, d) { for (i in d) el.style[i] = d[i] };
	function bulkAttr (el, d) { for (i in d) el.setAttribute(i, d[i]) };
	function parse(i) { return isNaN(parseInt(i)) ? 0 : parseInt(i) };
	function hash(u) { for (var c = 0, i = 0; i < u.length; i++) c += u.charCodeAt(i); return c % 255; };

	//this.s = ['width','marginLeft','marginRight','paddingLeft','paddingRight','borderLeftWidth','borderRightWidth'];
	var msie = false;
	var i, p, u, hh = 40, base = "//tb.altervista.org/", omt = style(document.body, 'marginTop');

	var div = document.getElementById('av_toolbar_regdiv');
	div.removeAttribute('style');
	div.style.top = "-40px";
	var link = div.children[0];
	link.className = 'tb-site';

	// Nasconde la toolbar se siamo dentro un iframe (escluso il cloak) o se c'è la variabile av_toolbar_off
	if ((window.parent != window && typeof(av_toolbar_force) == 'undefined' && window.name != 'XYZZY2') || typeof(av_toolbar_off) != 'undefined') { div.style.display = 'none'; return; }

	// Generazione dell'URL della toolbar staticizzata
	if (u = document.location.host.match(/([a-zA-Z0-9]+)\.(ssl\.)?altervista\.org$/)) {
		p = 'tb_html/'+hash(u[1])+'/t2_'+u[1];
	} else {
		u = (document.location.host.match(/[a-zA-Z0-9_-]+\.[a-zA-Z]{2,3}$/))[0];
		p = 't2_dom_html/'+hash(u)+'/'+u;
	}

	var ifr = bulkElement('iframe', {id: "av_toolbar_iframe", marginwidth: "0", marginheight: "0", frameborder: "0", scrolling: "no"});
	bulkStyle(ifr, {height: hh+'px', border: 0, position: 'absolute', left: '0', top: "-40px", zIndex: 10000, maxWidth: 'none'});

	// Iubenda flag
	var iubenda = false, m;
	if (window._iub && (m = document.cookie.match("_iub_cs-"+_iub.csConfiguration.cookiePolicyId+"=(.+?)($|;)"))) try { iubenda = JSON.parse(decodeURIComponent(m[1])).consent; } catch (e) { /* nothing */ }

	if (div.nextSibling) div.parentNode.insertBefore(ifr, div.nextSibling); else div.parentNode.appendChild(ifr);
	if (msie && document.compatMode!='CSS1Compat') ifr.outerHTML = ifr.outerHTML;
	ifr.src = base+p+".html?ref="+encodeURIComponent(location.href)+"&iubenda="+(iubenda?1:0);

	// Modernizr
	if (!document.head) document.head = document.getElementsByTagName('head').item(0);
	if (!window.addEventListener) window.addEventListener = function(ev, func, bubble) { this.attachEvent("on"+ev, func) };
	if (!window.JSON) JSON = { parse: function(s) { return eval("("+s+")"); } };

	// Stile generico per il crea sito
	document.head.appendChild(bulkElement('link', { rel: "stylesheet", type: "text/css", href: base+"css/toolbar-font.css" }));
	document.head.appendChild(bulkElement('link', { rel: "stylesheet", type: "text/css", href: base+"css/toolbar-icons.css" }));
	document.head.appendChild(bulkElement('link', { rel: "stylesheet", type: "text/css", href: base+"css/site.css" }));
	var css = bulkElement('style', { type: "text/css" });
	css.appendChild(document.createTextNode('')); // webkit wordaround
	document.head.appendChild(css);

	var span = bulkElement('span', { "class": "circle" });
	span.appendChild(bulkElement('span', { "class": "tb-icons tb-icon-pencil" }));
	link.children[0].insertBefore(span, link.children[0].firstChild);

	resize();
	window.addEventListener('load', resize, false);

	window.addEventListener("message", function(ev) {
		if (ev.origin.search(/^https?:\/\/tb\.altervista\.org/) == 0) {
			var data = JSON.parse(ev.data);
			if (data._type) {
				ifr.style.position = div.style.position = data.position;
				link.children[0].style.color = data.text_color;
				css.sheet.insertRule('#av_toolbar_regdiv .tb-site a .circle { border-color: '+data.text_color_alt+' !important; }', 0);
				css.sheet.insertRule('#av_toolbar_regdiv .tb-site a:hover .circle { background-color: '+data.text_color+' !important; }', 0);
				css.sheet.insertRule('#av_toolbar_regdiv .tb-site a:hover .tb-icons { color: '+data.background_color+' !important; }', 0);
				if (!data.mobile && screen.width < 768) ifr.style.display = div.style.display = "none";
			}
			resize();
		}
	}, false);
})();
