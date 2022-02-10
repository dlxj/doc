# ish 后台免杀

```
There actually has been a way discovered to allow iSH to run in the background:

RUN: cat /dev/location > /dev/null &

Allow iSH to always track location. What this does is:

cat /dev/location > /dev/null: Writes location to the special null device (essentially making the data go nowhere)

& : Adds the command to an infinite background loop, making it run in the background forever

Allowing iSH to always track your location: Then it won't stop letting iSH track location after closing the app
```



