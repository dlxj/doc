



# grep



```
# grep -q by design returns no output
while true;
do
    if tail -2 /var/log/auth.log | grep -q "exit";
    then
            echo "true"
            break
    fi
done
```





```
if tail -10 /root/.pm2/logs/pandora-ak148-explain-error.log | grep -q  'json.decoder.JSONDecodeError';
then
    echo "###found pm2 logs: JSONDecodeError restart pandora_ak148_explain now..."
    rm -f /root/.pm2/logs/pandora-ak148-explain-error.log
    pm2 restart pandora_ak148_explain
fi


crontab -e
*   *    *      *   *  sh /root/restart.sh
	# 每分钟执行一次

