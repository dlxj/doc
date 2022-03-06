

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
      > - https://github.com/Azure/azure-cli/issues/19456
      > - https://github.com/psf/requests/issues/5740

- https://myanimelist.net/anime/527/Pokemon?q=pokemon&cat=anime
  - 声优 OP 信息



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



- 为什么在中国，第一代数码宝贝动画，比第一代神奇宝贝（宝可梦）动画的人气高那么多？ - 灿若莲花的回答 - 知乎
  https://www.zhihu.com/question/65234016/answer/499330254



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
import json, logging, os, requests, urllib.parse, html, http.cookiejar

data = requests.get(url=url, params=params, data=data, json=json_data, headers=headers, proxies=proxies,
            cookies=self.getcookies(user) if user is not None else None)
        Jdata = json.dumps(data.text)
```

