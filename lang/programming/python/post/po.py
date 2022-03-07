
import json, os, requests, urllib.parse, html, http.cookiejar
from tkinter.messagebox import NO


def getcookies(jp):
    cookieFile = "cookies/{}.txt".format(jp)
    cj = http.cookiejar.MozillaCookieJar(cookieFile)
    cj.load()
    cookies = {}
    for cookie in cj:
        cookie.value = urllib.parse.unquote(html.unescape(cookie.value))
        cookies[cookie.name] = cookie.value
    return cookies

cookies = getcookies('jp')
data = requests.get(url=url, params=params, data=None, json=None, headers=headers, proxies=None, cookies=cookies)
Jdata = json.dumps(data.text)
a = 1
