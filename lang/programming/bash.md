

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





