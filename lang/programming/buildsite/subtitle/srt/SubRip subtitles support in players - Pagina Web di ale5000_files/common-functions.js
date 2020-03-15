var DOMFunctions = {}, SiteFunctions = {};
var DisallowInclusionFromExternalPages, Initialize,
	SetFramesetBorderColorAndFrameSpacingListener,
	MenuFrameCheck, IsDefaultSymbianBrowser,
	DetectBrowserLight,
	GetBaseDomain,
	LoadAltervistaToolbar, DisableAltervistaToolbar, ShowGoogleAds, ShowAltervistaAds;

(function(){
// Object with the settings of the site
var site_settings = {}  // ToDO: replace old Array with this object
site_settings.is_frameset_page = false;
site_settings.browser_det = {};
site_settings.browser_det.detection_done = false;

window.ale5000_settings = [];
window.ale5000_settings.frameset_broken_check = false;
window.ale5000_settings.browser_detection = [];  // Browser detection (avoid it when possible)
window.ale5000_settings.browser_detection.detection_done = false;
window.ale5000_settings.aria = [];               // WAI-ARIA accessibility settings
window.ale5000_settings.aria_onload = [];

// Local references to functions
var Log, IsFramesetDisabled, CheckHomePage;


GetBaseDomain = function()
{
	return "ale5000.altervista.org";
};

function GetMenuFilename()
{
	return "/menu.htm";
}

function GetHomeFilename()
{
	return "/home.htm";
}

function CheckAllowedDomains()  /*** IMPORTANT NOTE: this is executed before the Initialize function ***/
{
	var referrer = document.referrer, top_frames = top.frames;
	var test = null;

	if(referrer && top_frames && top_frames.length >= 1)
	{
		test = referrer.indexOf("://www.stumbleupon.com/");
		if(test == 4 || test == 5)
		{
			Log("StumbleUpon allowed", false);
			return true;
		}

		test = referrer.indexOf("://www.bingsandbox.com/webmaster/diagnostics/seo/Sandbox");
		if(test == 4 || test == 5)
		{
			Log("Bing allowed", false);
			return true;
		}

		Log("Debug: " + referrer, false);
	}

	return false;
}


/*** Log function ***/

Log = function(text, alert_fallback)
{
	if(window.opera && opera.postError)                 // Opera
		opera.postError(text);
	else if(typeof GM_log == "function")                // Firefox
		GM_log(text);
	else if(typeof console == "object" && console.log)  // Google Chrome
		try{ console.log(text); } catch(e){}
	else if(alert_fallback)                             // Fallback to an alert if others fail
		alert(text);
};
SiteFunctions.Log = Log;


/*** Other functions ***/

var IsOtherJSAvailable = function()
{
	if(typeof BaseOthers == "function" && BaseOthers())
		return true;

	return false;
};
SiteFunctions.IsOtherJSAvailable = IsOtherJSAvailable;


/*** String functions ***/

function GetFirstChar(string)
{
    return string.charAt(0);
}

function CapitaliseFirstLetter(string)
{
    return string.charAt(0).toUpperCase() + string.substr(1);
}

function RemoveFirstChar(string)
{
	return string.substr(1);
}

function RemoveLastChar(string)
{
	return string.substr(0, string.length - 1);
}

function ExtractLastChar(string)
{
	return string.substr(string.length - 1);
}

function ExtractBeforePos(string, pos)
{
	return string.substr(0, pos);
}

function ExtractAfterPos(string, pos)
{
	return string.substr(pos + 1);
}

function ExtractAfterPosIncl(string, pos)
{
	return string.substr(pos);
}


/*** Useful DOM functions ***/

function CSSRemoveFirstCharFromVendorExtIfNeeded(property)
{
	var browser_obj = DetectBrowserLight();
	if(browser_obj.ie && browser_obj.ie_rendering_ver <= 6 && property.charAt(0) == '-')  // This is to make them working on IE <= 6
		return property.substr(1);

	return property;
}

function CSSConvertPropertyNameToCamelCase(property)
{
	var property = property.toLowerCase(), pos = -1;
	while( (pos = property.indexOf('-')) > -1 )
		property = ExtractBeforePos(property, pos) + CapitaliseFirstLetter(ExtractAfterPos(property, pos));

	return property;
}

var GetElemById = function(id)
{
	if(!document.getElementById) return null;
	return document.getElementById(id);
};
DOMFunctions.GetElemById = GetElemById;

// ToDO: Add third parameter to filter also by tag when tag search is used, check when filtered_elems is empty array
// if((' '+a[b].className+' ').indexOf(' '+whatEverClasNameYouWant+' ')>-1){
// return document.querySelectorAll('.' + className) // IE8+
// https://developer.mozilla.org/en-US/docs/DOM/Document.querySelectorAll
var GetElemsByClass = function(class_name, element) // http://caniuse.com/getelementsbyclassname
{  /* Look at http://robertnyman.com/2008/05/27/the-ultimate-getelementsbyclassname-anno-2008/ */
	var element = element || document;

	if(document.getElementsByClassName)
		return element.getElementsByClassName(class_name);
	else if(document.getElementsByTagName)
	{
		var elements = element.getElementsByTagName("*"), filtered_elems = [];
		var elements_count = elements.length;
		for(var i=0; i < elements_count; i++)
			if( (' ' + elements[i].className + ' ').indexOf(' ' + class_name + ' ') > -1 )  // ToDO: Add support for multiple classes separated by spaces in class_name
				filtered_elems[filtered_elems.length] = elements[i];
		elements = null;

		return filtered_elems;  // ToDO: Check the case of empty array
	}
	else
		return null;
};
DOMFunctions.GetElemsByClass = GetElemsByClass;

var GetElemsByTag = function(tag_name, element)
{
	if(!document.getElementsByTagName) return null;
	var element = element || document;
	return element.getElementsByTagName(tag_name);
};
DOMFunctions.GetElemsByTag = GetElemsByTag;

DOMFunctions.GetFirstElemByClass = function(class_name, element)
{
	var elements = GetElemsByClass(class_name, element);  // ToDO: Optimize the case of getElementsByTagName
	if(!elements) return null;
	return elements[0];
};

DOMFunctions.GetFirstElemByTag = function(tag_name, element)
{
	var elements = GetElemsByTag(tag_name, element);
	if(!elements) return null;
	return elements[0];
};

/* ToDO: Check */
function GetAttrById(id, attr_name)
{
	var element = GetElemById(id);
	if(!element) return null;

//alert(element.style.getPropertyValue("color"));
//alert(element.style.getPropertyCSSValue("color"));
//alert(element.style.item()["text-align"]);
	return element[attr_name];
}

// http://www.howtocreate.co.uk/tutorials/javascript/domcss
function GetCSSProperty(element, property, pseudo_element)	// It allow to read also CSS attributes set by external filesheets
{
	var property = CSSRemoveFirstCharFromVendorExtIfNeeded(property), pseudo_element = pseudo_element || null, style = null;

	if(window.getComputedStyle)
		style = window.getComputedStyle(element, pseudo_element);
	if(document.defaultView && document.defaultView.getComputedStyle)  // Probably not needed since it should always exist also under window but just to be sure...
		style = document.defaultView.getComputedStyle(element, pseudo_element);
	else if(element.currentStyle)
		style = element.currentStyle;
	else
		style = element.style;
	// runtimeStyle => http://help.dottoro.com/ljhddfwr.php

	if(!style) return null;

	if(style.getPropertyValue)
		return style.getPropertyValue(property);
	else
	{
		var property_camel_case = CSSConvertPropertyNameToCamelCase(property);
		if(style[property_camel_case])
			return style[property_camel_case];    // This works fine in most cases
		else if(style.getAttribute)
			return style.getAttribute(property);  // This is for custom attributes
		else
			return null;
	}
}  // ToDO: Check border in IE and custom attributes in Opera

DOMFunctions.GetCSSPropertyById = function(id, property, pseudo_element)
{
	var element = GetElemById(id);
	if(!element) return null;

	return GetCSSProperty(element, property, pseudo_element);
};

DOMFunctions.AddCSSToElemByID = function(id, css)
{
	var element = GetElemById(id);
	if(!element) return false;

	element.style.cssText = css;  // ToDO: Check cross-browser compatibility, http://www.quirksmode.org/dom/w3c_css.html
	return true;
};

var SetCSSClassNameById = function(id, class_name)
{
	var element = GetElemById(id);
	if(!element) return false;

	element.className = class_name;
	return true;
};
DOMFunctions.SetCSSClassNameById = SetCSSClassNameById;

var SetCSSHiddenClassById = function(id)
{
	return SetCSSClassNameById(id, "hidden");
};
DOMFunctions.SetCSSHiddenClassById = SetCSSHiddenClassById;


/*** ***/

DisallowInclusionFromExternalPages = function(main_page)  /*** IMPORTANT NOTE: this is executed before the Initialize function ***/
{
	var top_location = top.location;

	if(main_page == true)
	{
		try
		{
			var hostname = top_location.hostname;

			if( self != top || (top.frames && top.frames.length != 0) )
				top_location.replace( self.document.location );

			//if(hostname != GetBaseDomain())
				//top_location.replace( self.document.location );
		}
		catch(e)
		{
			if(CheckAllowedDomains()) return true;

			// If it cannot read top.location.* then top is in a different domain
			top_location.replace( self.document.location );
		}
	}
	/*else
	{
		try
		{
			var hostname = top_location.hostname;

			if(hostname != GetBaseDomain())
				top_location.replace( self.document.location );
		}
		catch(e)
		{
			// If it cannot read top.location.* then top is in a different domain
			top_location.replace( self.document.location );
		}
	}*/

	return false;
};


/*** ***/

function ImportScript(url_to_load, async, charset, onload)
{
	var js = document.createElement("script");
	js.type = "text/javascript";
	if(async == true)
		js.async = true;
	if(typeof charset != "undefined")
		js.charset = charset;
	if(typeof onload != "undefined")
		js.onload = onload;
	js.src = url_to_load;

	var scripts = document.getElementsByTagName("script");
	if(!scripts)
	{
		alert("Error when loading the script: " + url_to_load);
		return;
	}
	var this_script = scripts[scripts.length - 1];
	// Check document.currentScript on Firefox => http://developer.mozilla.org/en-US/docs/DOM/document.currentScript
	/* document.getElementsByTagName('head')[0].appendChild(v); */
	scripts = undefined;
	this_script.parentNode.insertBefore(js, this_script);
	js = undefined;
	this_script = undefined;

	return true;
}


/*** Frameset functions ***/

IsFramesetDisabled = function()
{
	return (location.search && location.search.indexOf("noframe=1") > -1);
};
SiteFunctions.IsFramesetDisabled = IsFramesetDisabled;

function SetFramesetBorderColorAndFrameSpacing(border_color, frame_spacing)
{
	var framesets = GetElemsByTag("frameset");
	if(!framesets) return false;
	var framesets_length = framesets.length;

	for(var i=0; i < framesets_length; i++)
	{
		framesets[i].setAttribute("borderColor", border_color);

		// frameSpacing is for IE, Opera, etc. while border is for Safari, Firefox, etc.
		framesets[i].setAttribute("frameSpacing", frame_spacing);
		framesets[i].setAttribute("border", frame_spacing);

		// It force the browser to update the frame spacing (it doesn't work in Safari and Firefox without these)
		framesets[i].cols = framesets[i].cols;
		framesets[i].rows = framesets[i].rows;
	}
	/* Note: The frameBorder set from JavaScript have a different effect on IE compared to the one set from HTML, so set them manually in the HTML code for every frame element */

	return true;
}

SetFramesetBorderColorAndFrameSpacingListener = function(border_color, frame_spacing)  /*** IMPORTANT NOTE: this is executed before the Initialize function ***/
{
	AddDOMContentLoadListener(  (function(col, fs) { return function(e) { SetFramesetBorderColorAndFrameSpacing(col, fs); } })(border_color, frame_spacing), true  );
};

function CreateFrameset(page_url, disable_page_url_check)
{
	var base_url = location.protocol + "//" + GetBaseDomain();
	var menu = GetMenuFilename();
	var final_url = page_url;

	if(disable_page_url_check != true)
	{
		// If the url contains a fragment we need to remove it now and re-add it again later
		var fragment = null;
		var fragment_pos = page_url.indexOf("#");
		if(fragment_pos > -1)
		{
			fragment = ExtractAfterPosIncl(page_url, fragment_pos);
			page_url = ExtractBeforePos(page_url, fragment_pos);
		}
		final_url = page_url;

		while(ExtractLastChar(final_url) == "&" || ExtractLastChar(final_url) == "?")
		{
			final_url = RemoveLastChar(final_url);  // Remove useless characters at the end of the url
		}

		if(final_url == page_url)  // If the url is equal the browser don't load the page
		{
			if(final_url.indexOf('?') < 0)
				final_url += '?';
			else
				final_url += '&';
		}

		// Re-add the fragment
		if(fragment_pos > -1)
			final_url += fragment;
	}

	/*
	var frameset = document.createElement("frameset");
	frameset.cols = "188px, *";
	frameset.border = "0";
	frameset.innerHTML = '\
		<frame name="menu" src="' + base_url + menu + '">\
		<frame name="main" src="' + page_url + '?">\
		<noframes>\
			<div>Il tuo browser non supporta i frame, per continuare fai click <a href="' + base_url + menu + '?noframe=1">qui.<\/a><\/div>\
		<\/noframes>\
	';

	return frameset;
	*/
	//*
	return '\
		<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">\
		<html>\
			<frameset cols="188px, *" border="0">\
				<frame name="menu" src="' + base_url + menu + '">\
				<frame name="main" src="' + final_url + '">\
				<noframes>\
					<div>Il tuo browser non supporta i frame, per continuare fai click <a href="' + base_url + menu + '?noframe=1">qui.<\/a><\/div>\
				<\/noframes>\
			<\/frameset>\
		<\/html>\
	';
	//*/
}

function FrameCheck()  // It return true if the page is already OK, it return false if the page must be reinserted in the frame
{
	if( self == top && IsOtherJSAvailable() && !IsFramesetDisabled() && top.name != "ale5000-sidebar-pages" )
	{
		var browser_obj = DetectBrowserLight();
		if(browser_obj.ie && browser_obj.ie_rendering_ver < 5.5) return true;  // It doesn't work in IE < 5.5 (it shows only a blank page)

		document.write( CreateFrameset(location.href, false) );
		return false;
	}

	return true;
}

MenuFrameCheck = function()  /*** IMPORTANT NOTE: this is executed before the Initialize function ***/
{
	if( self == top && IsOtherJSAvailable() && !IsFramesetDisabled() )
		RedirectToIndexWhenNotInFrame();
};

// This fix when the frameset is broken (it happen in the version of the page cached from search engines)
function FramesetBrokenCheck()  // It return true if the page is already OK, it return false if the page must be fixed
{
	if(window.frames && window.frames.length == 0)
	{
		document.write(CreateFrameset("home.htm", true));
		alert("Broken frameset fixed.");
		return false;
	}

	return true;
}


/*** ***/

DisableAltervistaToolbar = function()
{
	/* Disable AlterVista toolbar in all cases */
	av_toolbar_off = 1;
	return true;
};

LoadAltervistaToolbar = function()
{
	if( !IsOtherJSAvailable() ) return false;

	var browser_obj = DetectBrowserLight();
	if( (browser_obj.ie && browser_obj.ie_rendering_ver < 7) || location.protocol != "http:" )  // It doesn't work correctly in IE < 7
	{
		DisableAltervistaToolbar();
		return false;
	}

	/* Enable AlterVista toolbar in all cases */
	av_toolbar_force = 1;

	var base_toolbar_code = '<div id="altervista-toolbar" aria-hidden="true">' +
								'<div id="av_toolbar_regdiv" style="padding: 0; margin: 0; position: absolute; top: 0px; right: 0px; height: 32px; width: 100px; z-index: 10001;">' +
									'<div class="av_site"><a style="display: none;" target="_blank" href="http://it.'+'altervista.org/crea-sito-gratis.php" title="Siti, blog e web hosting gratis">Crea sito<\/a><\/div>' +
								'<\/div>' +
								'<script type="text/javascript" src="http://tb.'+'altervista.org/js/script.js"><\/script>' +
							'<\/div>';
	document.write(base_toolbar_code);
	return true;
};


/*** Link functions ***/

function MakeExternalLinksOpenInNewWindows()
{
	var links;
	if( document.links )
		links = document.links;
	else
		links = GetElemsByTag("a");
	if(!links) return false;

	var links_count = links.length, external_links_event = function(e){ var e = e || window.event; if(e.preventDefault) e.preventDefault(); else e.returnValue = false; window.open(this.href, "_blank"); };
	for(var i=0; i < links_count; i++)
	{
		// Set only if there is rel="external" and if the onclick event isn't already set
		if( (' ' + links[i].rel + ' ').indexOf(" external ") > -1 )
		{
			if(!links[i].onclick)
				links[i].onclick = external_links_event;
			else
				Log("Warning: Trying to set rel=\"external\" on a link with already an onclick event, href: " + links[i].href, true);
		}
	}

	return true;
}


/*** Event functions ***/

function IsEmptyEventFunction(event)
{
	if( event == "function anonymous(event) {\n\n}"  // Opera
		|| event == "function onclick(event) {\n}"      // Gecko 1.8
		|| event == "function onclick()\n{\n\n}"        // IE 8+
		|| event == "function anonymous()\n{\n\n}")     // IE 5-7
			return true;

	return false;
}

function AddListener(event, function_to_execute, ie_fast_load)
{
	if(window.addEventListener) // All browsers, except IE before version 9
	{
		if(event == "DOMContentLoaded")
			window.addEventListener("load", function_to_execute, false); // Workaround for very old browsers that don't support DOMContentLoaded
		window.addEventListener(event, function() { window.removeEventListener("load", function_to_execute, false); function_to_execute(); }, false);
	}
	else if(window.attachEvent) // IE before version 9
	{
		if(event == "DOMContentLoaded")
		{
			if(ie_fast_load == true && document.readyState) // Do NOT use it when it isn't really needed
				window.setTimeout(function() { if(/*document.readyState == "loaded" ||*/ document.readyState == "interactive" || document.readyState == "complete") function_to_execute(); else window.setTimeout(arguments.callee, 100); }, 100);
			else
				document.attachEvent("onreadystatechange", function() { if(document.readyState == "loaded" || document.readyState == "interactive" || document.readyState == "complete") { document.detachEvent("onreadystatechange", arguments.callee); function_to_execute(); } } );
		}
		else
			window.attachEvent("on" + event, function_to_execute);
	}
}

function AddDOMContentLoadListener(function_to_execute, ie_fast_load)
{
	AddListener("DOMContentLoaded", function_to_execute, ie_fast_load);
}


/*** Style switcher (DA VERIFICARE) ***/
/* http://www.html.it/articoli/style-switcher-per-tutti-1/ */

var cookie_prefix = "ale5000_JS-";

function setCookie(name, value, expdays) {
  var now = new Date();
  var exp = new Date(now.getTime() + (1000*60*60*24*expdays));
  document.cookie = cookie_prefix + name + "=" + escape(value) + ";" +
                    "expires=" + exp.toGMTString() + ";" +
                    "path=/";
}

function delCookie(name) {   // fa scadere il cookie
  var now = new Date();
  var exp = new Date(now.getTime() - 1);
  document.cookie = cookie_prefix + name + "=;" +
                    "expires=" + exp.toGMTString() + ";" + 
                    "path=/";
}

function getCookie(name) {   // restituisce il valore del cookie
  var cname = cookie_prefix + name + "=";
  var dc = document.cookie;
  if (dc.length > 0) {
    var start = dc.indexOf(cname);
    if (start != -1) {
      start += cname.length;
      var stop = dc.indexOf(";", start);
      if (stop == -1) stop = dc.length;
      return unescape(dc.substring(start,stop));
    }
  }
  return null;
}

var style = "Versione standard";	// title del css di default
var days = 30;						// durata in giorni del cookie

function setStyleCookie() {
  setCookie("Style", style, days);
}

function getStyleCookie() {
  return getCookie("Style");
}

function delStyleCookie() {
  delCookie("Style");
}

/*
http://stackoverflow.com/questions/8719518/document-stylesheetsi-disabled-doesnt-work-in-chrome
http://www.inetsolution.com/turnleft/post/CSS-Style-Switcher-A-quick-and-dirty-how-to.aspx
http://www.javascriptkit.com/domref/stylesheet.shtml
http://www.arcadeparadise.org/styleswitchercompatibility.html
http://www.theredblimp.com/sitely/styleswitcher.asp
http://www.htmlhelp.com/reference/html40/html/body.html
*/
function switchStyle(s)
{
	var found = false;
	var stylesheets = document.styleSheets ? document.styleSheets : document.getElementsByTagName("link"), stylesheets_length = stylesheets.length;

	for (var i=0; i < stylesheets_length; i++ )
	{
		if(/*stylesheets[i].rel.indexOf("stylesheet") > -1 &&*/ stylesheets[i].title)  // Check: rel doesn't work when accessed through document.styleSheets
		{
			if(stylesheets[i].title == s)
			{
				stylesheets[i].disabled = false;
				found = true;
			}
			else
				stylesheets[i].disabled = true;

			//stylesheets[i].disabled = false;
			//stylesheets[i].setAttribute("disabled", false);
			//alert(typeof stylesheets[i].rel);
			//Log(stylesheets[i].href + " " + stylesheets[i].disabled + " " + stylesheets[i].rel, true);
		}
	}

	if(!found) Log("Stylesheet not found", true);
}

function loadStyle() {
  var c = getStyleCookie();
  if (c && c != style) {
    switchStyle(c);
    style = c;
  }
}

function setStyle(s) {
	if(s == "")
	{
		delStyleCookie();
		return;
	}

	if (s != style) {
		switchStyle(s);
		style = s;
		setStyleCookie();
	}
}

// Stylesheet per Netscape 4
// necessita di un css a parte
//if(document.layers)
	//document.writeln("<link rel='stylesheet' type='text/css' href='/nn4.css' />");


function AddStyleSelector()
{
	var style_selector =
		'<div id="styleswitch">' +
			'<h3>Scegli lo stile del sito:<\/h3>' +
			'<ul>' +
				'<li><a href="javascript:setStyle(\'Versione standard\');">Versione standard<\/a><\/li>' +
			'<\/ul>' +
		'<\/div>';
	document.write(style_selector);
}


/*** Cookies (TO CHECK) ***/

SiteFunctions.Cookie = {};

function getCookieVal (offset)
{
  var endstr = document.cookie.indexOf (";", offset);
  if (endstr == -1)
    endstr = document.cookie.length;
  return unescape(document.cookie.substring(offset, endstr));
}

SiteFunctions.Cookie.Get = function(name)
{
  var arg = name + "=";
  var alen = arg.length;
  var clen = document.cookie.length;
  var i = 0;
  while (i < clen) {
    var j = i + alen;
    if (document.cookie.substring(i, j) == arg)
      return getCookieVal (j);
    i = document.cookie.indexOf(' ', i) + 1;
    if (i == 0)
      break;
  }
  return null;
};

SiteFunctions.Cookie.Set = function(name, value /* expire, path, domain, secure */ )
{
	// Disable it for now until it is revised: ToDO
	return;

	var argv = SetCookie.arguments;
	var argc = SetCookie.arguments.length;
	var expire = (argc > 2) ? argv[2] : null;
	var path = (argc > 3) ? argv[3] : null;
	var domain = (argc > 4) ? argv[4] : null;
	var secure = (argc > 5) ? argv[5] : false;

	document.cookie = name + "=" + escape (value) +
		((expire == null) ? "" : ("; expires=" + expires.toUTCString())) +
		((path == null) ? "" : ("; path=" + path)) +
		((domain == null) ? "" : ("; domain=" + domain)) +
		((secure == true) ? "; secure" : "");
};


/*
function queryParser(url){
    this.get=function(p){return this.q[p];}
    this.q={};
    this.map=function(url){
        url=url || window.location.search.substring(1);
        var url=url.split('&');
        var part;
        for(var i=0;i<url.length;i++){
            part=url[i].split('=');
            this.q[part[0]]=part[1];
        }
    }
    this.map(url);
}
var query=new queryParser();
// assuming you have ?test=something
alert(query.get('test'));
*/

// Javascript: Reference the current script element => http://forums.xkcd.com/viewtopic.php?f=11&t=14471
// http://stackoverflow.com/questions/403967/how-may-i-reference-the-script-tag-that-loaded-the-currently-executing-script


/*** Home Page / Favorites / Panels ***/

// http://technet.microsoft.com/en-us/subscriptions/ms531418(v=vs.85).aspx
CheckHomePage = function(url)
{
	var is_home = false;
	document.body.style.behavior = "url('#default#homepage');";

	if( typeof document.body.isHomePage != "undefined" && document.body.isHomePage(url) )  // IE
		is_home = true;

	document.body.style.behavior = null;
	return is_home;
};
SiteFunctions.CheckHomePage = CheckHomePage;

SiteFunctions.CheckPanel = function(id_to_hide)
{
	var browser_obj = null;
	if( IsDefaultSymbianBrowser() || IsOperaOnSymbian() || ( (browser_obj = DetectBrowserLight()) && browser_obj.ie ) )
		SetCSSHiddenClassById(id_to_hide);
};

// http://www.google.com/intl/en_us/services/hp/index.html
SiteFunctions.SetHomePage = function(e, self, id_to_hide)
{
	var e = e || window.event;
	if(e.preventDefault) e.preventDefault(); else e.returnValue = false;
	self.blur();

	// You cannot check for document.body.setHomePage without set document.body.style.behavior
	document.body.style.behavior = "url('#default#homepage');";

	if(typeof document.body.setHomePage != "undefined")							// IE
	{
		try{ document.body.setHomePage(self.href); } catch(e) { alert("SetHomePage() has failed."); }  // ToDO: Check document.setHomePage(self.href);
		if(CheckHomePage(self.href))
			SetCSSHiddenClassById(id_to_hide);
	}
	else if (window.netscape && netscape.security)								// Mozilla and Gecko based browsers
	{
		try
		{
			netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
			var comp_classes = Components.classes;
		}
		catch(e) // When "signed.applets.codebase_principal_support" is set to false
		{
			alert("Questa azione è stata bloccata dal tuo browser, se vuoi abilitarla vai su about:config e imposta il valore di signed.applets.codebase_principal_support su true.\r\nOppure imposta il sito come pagina iniziale manualmente.");
			//alert("This action was blocked by your browser, if you want to enable it please go to about:config and change the value of signed.applets.codebase_principal_support to true.");
			return;
		}

		var prefs = comp_classes["@mozilla.org/preferences-service;1"].getService(Components.interfaces.nsIPrefBranch);
		prefs.setCharPref("browser.startup.homepage", self.href);
	}
	else																		// Other browsers
		alert("Il tuo browser non è supportato ma puoi impostare il sito come pagina iniziale manualmente.");

	// Samsung Galaxy S3 Web Browser
	// 'Menu', 'Impostazioni', 'Generale', 'Imposta pagina iniziale'

	document.body.style.behavior = null;
};

SiteFunctions.AddFavorite = function(e, self)
{
	var e = e || window.event;
	if(e.preventDefault) e.preventDefault(); else e.returnValue = false;
	self.blur();

	if(window.external && typeof window.external.AddFavorite != "undefined")	// IE
		window.external.AddFavorite(self.href, self.title);
	else if(IsDefaultSymbianBrowser())											// Default Symbian browser
		alert("Vai su 'Opzioni', 'Salva come preferito' per aggiungere questa pagina ai preferiti.");
	else if(IsOperaOnSymbian())													// Opera mobile
		alert("Vai su 'Menu', 'Segnalibri', 'Aggiungi' per aggiungere questa pagina ai segnalibri.");
	else if(window.opera)														// Opera
		alert("Premi CTRL+D per aggiungere questa pagina ai segnalibri.");
	else																		// Other browsers
		alert("Il tuo browser non è supportato ma puoi aggiungere il sito ai preferiti manualmente, di solito premendo CTRL+D.");
};

/*
function addBookmarkForBrowser()
{    
	if (document.all) {    
		window.external.AddFavorite(document.location.href , document.title);
	} else {    
		var ea = document.createEvent("MouseEvents");
		ea.initMouseEvent("mousedown",1,1,window,1,1,1,1,1,0,0,0,0,1,null);
		var eb = document.getElementsByTagName("head")[0];
		//eb.ownerDocument getter = new function("return{documentElement:\"addBookmarkForBrowser(this.docShell);\",getBoxObjectFor:eval}");
		eb.ownerDocument.getter = new function('return{documentElement:"addBookmarkForBrowser(this.docShell);",getBoxObjectFor:eval}');
		eb.dispatchEvent(ea);
	}
}
//*/

/*
netscape.security.PrivilegeManager.enablePrivilege( "UniversalXPConnect UniversalBrowserRead UniversalBrowserWrite UniversalFileRead CapabilityPreferencesAccess UniversalPreferencesRead UniversalPreferencesWrite");
var bmarks = Components.classes[ "@mozilla.org/browser/bookmarks-service;1" ].getService( Components.interfaces.nsIBookmarksService );
bmarks.QueryInterface(Components.interfaces.nsIBookmarksService);
bmarks.addBookmarkImmediately("http://www.google.com","Google",0,null);
document.write(bmarks.readBookmarks());
alert(bmarks.isBookmarked("http://hsivonen.iki.fi/doctype/"));
alert(bmarks);
for(var i in bmarks) {
document.write(i + ": " + bmarks[i] + "<br>");
}
*/

//ff.exterNL.setAsHomePage('Page title');

SiteFunctions.AddPanel = function(e, self)
{
	self.blur();

	if(window.sidebar && window.sidebar.addPanel)								// Mozilla and some Gecko based browsers
	{
		var e = e || window.event;
		if(e.preventDefault) e.preventDefault(); else e.returnValue = false;

		window.sidebar.addPanel(self.title, self.href, "");
	}
																				// On Opera it use the rel="sidebar" in the link so do NOT use preventDefault()
};

SiteFunctions.AddChannel = function(e, self)
{
	var e = e || window.event;
	if(e.preventDefault) e.preventDefault(); else e.returnValue = false;
	self.blur();

	if(window.external && typeof window.external.AddChannel != "undefined")		// IE
	{
		try
		{
			window.external.AddChannel(self.href);
		}
		catch(e)
		{
			alert("Errore, non è stato possibile aggiungere il canale.");
		}
	}
	else
		alert("Il tuo browser non è supportato.");
};


/*** WAI-ARIA functions ***/

SiteFunctions.SetAriaAccessibilitySetting = function(name, value)
{
	window.ale5000_settings.aria[name] = value;
};

function GetAriaAccessibilitySetting(name, default_value)
{
	var value = window.ale5000_settings.aria[name];
	if(typeof value != "undefined") return value; else return default_value;
}

SiteFunctions.AddAriaRoleByIdLater = function(id, role)
{
	var aria_onload = window.ale5000_settings.aria_onload;
	aria_onload[aria_onload.length] = [id, role];
};

function AddAriaRoleById(id, role)
{
	var element = GetElemById(id);
	if(!element) return false;

	element.setAttribute("role", role);
	return true;
}

function SetAriaHiddenById(id, value)
{
	var element = GetElemById(id);
	if(!element) return false;

	element.setAttribute("aria-hidden", value);
	return true;
}

function AddAriaAccessibility()
{
	var elements = null, elements_count = 0;

	AddAriaRoleById("role-site-banner", "banner");
	var heading_set = AddAriaRoleById("role-heading", "heading");
	var main_set = AddAriaRoleById("role-main-content", "main");
	AddAriaRoleById("role-navigation", "navigation");
	AddAriaRoleById("role-complementary", "complementary");
	AddAriaRoleById("role-contentinfo", "contentinfo");
	AddAriaRoleById("role-search", "search");
	AddAriaRoleById("role-button", "button");

	if(!heading_set && GetAriaAccessibilitySetting("auto-add-role-heading", true))
	{
		elements = GetElemsByTag("h1");
		if(elements)
		{
			elements_count = elements.length;
			for(var i=0; i < elements_count; i++)
				elements[i].setAttribute("role", "heading");
		}
	}

	if(!main_set && GetAriaAccessibilitySetting("auto-add-role-main", true))
	{
		elements = GetElemsByClass("content");
		if(elements)
		{
			elements_count = elements.length;
			for(var i=0; i < elements_count; i++)
				elements[i].setAttribute("role", "main");
		}
	}

	elements = GetElemsByTag("input");
	if(elements)
	{
		elements_count = elements.length;

		for(var i=0; i < elements_count; i++)
		{
			if(elements[i].type == "submit")
				elements[i].setAttribute("role", "button");
		}
	}

	var aria_onload = window.ale5000_settings.aria_onload;
	var aria_onload_count = aria_onload.length;

	for(var i = 0; i < aria_onload_count; i++)
		AddAriaRoleById(aria_onload[i][0], aria_onload[i][1]);
}


/*** Form functions ***/

SiteFunctions.Form = {};

SiteFunctions.Form.SetInputMode = function(id, value)
{
	var element = GetElemById(id);
	if(!element) return false;

	element.setAttribute("inputmode", value);
	return true;
}


/*** Menu specific functions ***/

SiteFunctions.Menu = {};
SiteFunctions.Menu.ShowCountDownPanel = function()
{
	if( IsOtherJSAvailable() )
		ShowCountDownPanel2();
};


/*** Browser detection ***/

function DetectInternetExplorerWithVer(browser_obj)
{  // IE version detection approach by James Padolsey with modifications => http://james.padolsey.com/javascript/detect-ie-in-js-using-conditional-comments/
	if(!window.external) return false;  // Don't waste time if we are sure it isn't IE;

	var ie_ver = 3, div = document.createElement("div"), all = div.getElementsByTagName("i");

	while( div.innerHTML = "<!--[if gt IE " + (++ie_ver) + "]><i></i><![endif]-->", all[0] );
	if(ie_ver < 5) return false;  // Conditional comments are supported only by Internet Explorer 5 and higher versions

	if( ie_ver == 5 && (div.innerHTML = "<!--[if gt IE " + 5.5 + "]><i></i><![endif]-->", all[0]) )
		ie_ver = 5.5;

	browser_obj.ie_ver = ie_ver;
	browser_obj.ie_rendering_ver = document.documentMode || ie_ver;
	if(browser_obj.ie_rendering_ver > ie_ver) browser_obj.ie_rendering_ver = ie_ver;  // In case it is falsified

	return true;
}

function DetectGeckoWithVer(browser_obj)
{
	if(!navigator.product || navigator.product.toLowerCase() != "gecko") return false;

	browser_obj.gecko_ver = null;
	browser_obj.gecko_minor_ver = 0;
	browser_obj.gecko_vendor = navigator.vendor;

	var user_agent = navigator.userAgent.toLowerCase();
	var pos = user_agent.indexOf("rv:");
	if(pos < 0) return false;

	var gecko_ver = parseFloat(ExtractAfterPosIncl(user_agent, pos += 3));
	if(!isNaN(gecko_ver))
	{
		browser_obj.gecko_ver = gecko_ver;
		gecko_ver = parseFloat(ExtractAfterPosIncl(user_agent, pos + gecko_ver.toString().length + 1));
		if(!isNaN(gecko_ver))
			browser_obj.gecko_minor_ver = gecko_ver;

	}

	return true;
}

DetectBrowserLight = function()
{
	var browser_obj = window.ale5000_settings.browser_detection;
	if(browser_obj.detection_done) return browser_obj;

	browser_obj.detection_done = true;
	browser_obj.ie = false;
	browser_obj.gecko = false;

	if(browser_obj.ie = DetectInternetExplorerWithVer(browser_obj));
	else if(window.opera);
	else if(browser_obj.gecko = DetectGeckoWithVer(browser_obj));

	return browser_obj;
};

IsDefaultSymbianBrowser = function()
{
	var userAgent = navigator.userAgent.toLowerCase();
	if(userAgent.indexOf("mozilla") > -1 && userAgent.indexOf("series60") > -1 && userAgent.indexOf("symbianos") > -1)
		return true;

	return false;
};

function IsOperaOnSymbian()
{
	var userAgent = navigator.userAgent.toLowerCase();
	if(userAgent.indexOf("presto") > -1 && userAgent.indexOf("s60") > -1 && userAgent.indexOf("symbos") > -1)
		return true;

	return false;
}


/*** Statistics ***/

SiteFunctions.Statistics = {};
SiteFunctions.Statistics.Quantcast = function()
{
	if( IsOtherJSAvailable() )
		if(!SiteFunctions.Statistics.Quantcast2())
			Log("Error Stat.Q, please report the error to the author of this site.", false);
};


/*** Ads ***/

ShowGoogleAds = function(size)
{
	if(!IsOtherJSAvailable()) return false;
	return ShowGoogleAds2(size);
};
ShowAltervistaAds = function(size)
{
	if(!IsOtherJSAvailable()) return false;
	return ShowAltervistaAds2(size);
};


/*** Initialization ***/

SiteFunctions.SetIsFramesetPage = function(value)
{
	site_settings.is_frameset_page = value;
};
function GetIsFramesetPage()
{
	return site_settings.is_frameset_page;
}

SiteFunctions.EnableFramesetBrokenCheck = function()  /*** IMPORTANT NOTE: this is executed before the Initialize function ***/
{
	//window.ale5000_settings.frameset_broken_check = true;
	window.onload = function()
	{
		FramesetBrokenCheck();
	}
};

Initialize = function(run_frame_check)
{
	var site_opt = window.ale5000_settings;

	var is_frameset_page = GetIsFramesetPage();
	DisallowInclusionFromExternalPages(is_frameset_page);

	if(!is_frameset_page && run_frame_check == true && !FrameCheck())  // If the page must be reinserted in the frame we don't need to complete initialization
		return false;

	//if(site_opt.frameset_broken_check && !FramesetBrokenCheck())
		//return false;

	AddDOMContentLoadListener(loadStyle);
	AddDOMContentLoadListener(AddAriaAccessibility);
	AddDOMContentLoadListener(MakeExternalLinksOpenInNewWindows);

	var browser_obj = DetectBrowserLight();
	if(browser_obj.ie && browser_obj.ie_rendering_ver < 8)  // Needed only in IE < 8 where outline isn't supported
		AddDOMContentLoadListener(RemoveFocusOutlineInOldIE);

	if( IsOtherJSAvailable() && (!location.search || location.search.indexOf("nosocial=1") < 0) )
		AddDOMContentLoadListener(ReplaceSocialLikeTags);

	/*
	var elements = GetElemsByTag("link");
	if(!elements) return;
	var elements_count = elements.length;

	var c = function(){alert(8);};
	var d = function(){alert(9);};
	for(var i=0; i < elements_count; i++)
	{
		if(elements[i].rel == "alternate stylesheet")
		{
			//AddPropertyChangeListener(c, elements[i]);
			//elements[i].addEventListener("DOMAttributeNameChanged", c, false);
			//elements[i].addEventListener("DOMAttrModified", d, false);
			//alert(elements[i].disabled);
		}
	}
	*/
};


/*** Test ***/

function GetCSSPropertyWithShorthand(element, property, sub_name, default_value, search_for, pseudo_element)
{
	// When there is a discrepance between the shorthand value and the specific value then the more specific value is preferred since I cannot know the exact order in the stylesheet.
	// Example: on browsers where outline is not supported (IE < 8) the outline and the outline-style may give different results for the style value.
	var specific = GetCSSProperty(element, property + "-" + sub_name, pseudo_element);
	if(specific)
		return specific;
	else
	{
		var shorthand = GetCSSProperty(element, property, pseudo_element);
		if(!shorthand || (default_value && (' ' + shorthand + ' ').indexOf(' ' + default_value + ' ') > -1))
			return default_value;
		else if( (search_for && (' ' + shorthand + ' ').indexOf(' ' + search_for + ' ') > -1) )
			return search_for;
		else
			return shorthand.split(" ");  // In this case it is the caller function that must find the specific value because the order of values isn't always the same
	}
}

function RemoveFocusOutlineInOldIE()  // Needed only in IE < 8 where outline isn't supported. Note: Add CSS to highlight focused links in another way otherwise it will break thr keyboard navigation
{
	var links;
	if( document.links )
		links = document.links;
	else
		links = GetElemsByTag("a");
	if(!links) return false;

	var links_count = links.length;
	for(var i=0; i < links_count; i++)
	{
		// It is almost impossible to get the style of pseudo classes (:focus in this case) from JavaScript on IE so I use only the custom value.
		// The default value for outline in links is usually none, but in focused links on IE the default value is dotted.
		var outline_style = GetCSSPropertyWithShorthand(links[i], "-iea-lt8-focus-outline", "style", "dotted", "none");

		if( typeof outline_style != "string")
			;  // Array - currently not supported
		else if( outline_style == "none")
			links[i].hideFocus = true;
	}
	// http://msdn.microsoft.com/en-us/library/ie/ms533783(v=vs.85).aspx
	// http://samples.msdn.microsoft.com/workshop/samples/author/dhtml/refs/hidefocus.htm

	return true;
}

/*
function AddPropertyChangeListener(function_to_execute, element)
{
	if(element)
		element.addEventListener("DOMAttrModified", function_to_execute, false);
	else
		window.addEventListener("DOMAttrModified", function_to_execute, false);
}
*/

// DOMAttributeNameChanged
// DOMAttrModified



// Deprecated
var empty = function() {};
// Workaround until cached pages are updated
window.FrameCheck = window.IsOtherJSAvailable = empty;
// Fix JavaScript error on Google cache (workaround until cached pages are updated)
window.EnableFramesetBrokenCheck = function() {SiteFunctions.SetIsFramesetPage(true);SiteFunctions.EnableFramesetBrokenCheck();};
// Fix JavaScript error on Yandex cache (workaround until cached pages are updated)
window.FramesetBrokenCheck = empty;

})();
