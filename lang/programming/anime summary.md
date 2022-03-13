

# Pokemon

- amazon.jp prime video

  - https://github.com/dlxj/Amazon-video-downloader/blob/main/how.to.use.txt

    - 视频 字幕下载

      > B01IEFPVKG
      >
      > python amazon.py -r us -p jp -a B01IEFPVKG
      >
      > >   print(sys.argv)
      > >
      > >   sys.argv += ['-r', 'jp', '-p', 'jp', '-a', 'B01IEFPVKG']
      >
      > - https://www.cnblogs.com/hanmk/p/10786271.html
      >   - Postman 获取cookie
      > - https://github.com/psf/requests/issues/5740
      > - https://github.com/Azure/azure-cli/issues/19456

- https://myanimelist.net/anime/527/Pokemon?q=pokemon&cat=anime
  - 声优 OP 信息

- Amazon Prime Video台区港区是有中字的
- Tuneboto Amazon Video Downloader

> Search a french website (like a normal streaming website) or change the language (for french obviously) in your settings.
>
> For the sub :
>
> - VOSTFR : version originale sous-titrée (original version subtitled) if the movie you’re looking for is in englich or something else
>
> or
>
> - add “sous-titré” to the name of your movie
>
> It’s the best I can do, I doubt there is a lot of websites in english (I assume you’re american or english) that offers movies in french.



- https://www.reddit.com/r/languagelearning/comments/r08bnx/pokemon_tv_has_free_streaming_in_spanish_french/

> Pokemon TV has free streaming in Spanish, French, German, Dutch, Portuguese and more



- 为什么在中国，第一代数码宝贝动画，比第一代神奇宝贝（宝可梦）动画的人气高那么多？
  https://www.zhihu.com/question/65234016/answer/499330254

- 黑白原版实况
https://www.bilibili.com/video/BV1UE41167Sx?from=search&seid=11723934711246746449&spm_id_from=333.337.0.0

> **3ds精灵宝可梦作品一览**
>
> 《精灵宝可梦：XY》
>
> 《精灵宝可梦：OMEGA红/蓝宝石》
>
> 《精灵宝可梦：日月》
>
> 《精灵宝可梦：究极日月》



## 请求



```
https://atv-ps-fe.amazon.co.jp/cdp/catalog/GetPlaybackResources?asin=B01IEFPVKG&consumptionType=Streaming&desiredResources=AudioVideoUrls%2CCatalogMetadata%2CPlaybackSettings%2CSubtitleUrls%2CForcedNarratives&deviceID=520ca3d5cb83a1e64073a33af6f9223d71b7df8d5d04af339491b272&deviceTypeID=AOAGZA014O5RE&firmware=1&marketplaceID=A1VC38T7YXB528&resourceUsage=ImmediateConsumption&videoMaterialType=Feature&deviceDrmOverride=CENC&deviceStreamingTechnologyOverride=DASH&deviceProtocolOverride=Https&supportedDRMKeyScheme=DUAL_KEY&operatingSystemName=Windows&operatingSystemVersion=10.0&customerID=A18CCOQSEH5B6B&token=dc080fd66f01cbcb73751fd8c12b8832&deviceBitrateAdaptationsOverride=CVBR%2CCBR&audioTrackId=all&playbackSettingsFormatVersion=1.0.0&titleDecorationScheme=primary-content&&gascEnabled=False
```

```
{'User-Agent': 'Mozilla/5.0 (Windows...ari/537.36', 'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.8', 'Origin': 'https://atv-ps-fe.amazon.co.jp'}

```



```
# Amazon-video-downloader\pyamazon\Helpers\requesthelper.py

import json, logging, os, requests, urllib.parse, html, http.cookiejar

    def getcookies(self, user):
        try:
            cookieFile = "cookies/{}.txt".format(user)
            cj = http.cookiejar.MozillaCookieJar(cookieFile)
            cj.load()
            cookies = {}
            for cookie in cj:
                cookie.value = urllib.parse.unquote(html.unescape(cookie.value))
                cookies[cookie.name] = cookie.value
            return cookies

    def getItems(self, url, params=None, data=None, json_data=None, headers=None, proxies=None, user=None):

        data = requests.get(url=url, params=params, data=data, json=json_data, headers=headers, proxies=proxies,
            cookies=self.getcookies(user) if user is not None else None)
        Jdata = json.dumps(data.text)
```

## 代理



```
        proxies = {
            'http': 'http://127.0.0.1:4780',
            'https': 'http://127.0.0.1:4780',
        }

        data = requests.get(url=url, params=params, data=data, json=json_data, headers=headers, proxies=proxies,
            cookies=self.getcookies(user) if user is not None else None)
        Jdata = json.dumps(data.text)
        #with open('cc.txt', 'a', encoding='utf-8') as handler:
        #    handler.write(data.text)
        if data.status_code == 200:
```





## Solution

For a proxy that only supports HTTP,

- If proxy is configured via `HTTPS_PROXY` environment variable, `HTTPS_PROXY` should point to an `http://` URL.
- On Windows, this can also be set in **Control Panel -> Internet Options -> Connections -> LAN settings -> Proxy server -> Advanced**, set **Secure** to an `http://` URL. (There is a UI bug that after reopening the dialogue, the protocol is lost.)



# JP-Subtitles

- https://github.com/Matchoo95/JP-Subtitles





- 梵语

  - https://www.bilibili.com/video/BV1Qi4y1V7fu?from=search&seid=8739930114286513927&spm_id_from=333.337.0.0
    - 梵明院 - 梵语字母认读入门系列

  - https://www.bilibili.com/video/BV1H4411R7Hf/?spm_id_from=333.788.recommend_more_video.5
    - 阿含书斋梵文梵语天城体字母基础发音课程



- 俄语语音语调基础教程
  
  - https://www.bilibili.com/video/BV1Kv411W7FF/?spm_id_from=333.788.recommend_more_video.7
    - 大舌
  
  - https://www.wanmen.org/courses/5c19a5843f74d971c6cdef20/lectures/5c6143cd4a76e877c665e71d
  > 俄语的语音韵律感十足
  
- 万门大学 吴石磊

  

- 刘雯雯 蜗牛法语

  - https://www.youtube.com/watch?v=05zr3qMciIQ
    - 关于小舌音可能你90%的理解都是错的+零难度练习方法
  
  - https://www.woniufr.vip/detail/v_59cdcdbe45e6a_88vMcwKF/3?from=p_5e267bda30490_PXgrZ3r8&type=5&parent_pro_id=
  
  > 法语属拉丁系语言，所见即所读，每个字母或者字母组合有固定的读音，像汉语拼音一样，可以拼读出来
  >
  > 法语讲究连音联诵读，需要把一个节奏组中的所有可以连在一起读的发音串联起来读，这样有些原来不发音的字母，就需要发音

​     
