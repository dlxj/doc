# ish 后台免杀

```
There actually has been a way discovered to allow iSH to run in the background:

RUN: cat /dev/location > /dev/null &

Allow iSH to always track location. What this does is:

cat /dev/location > /dev/null: Writes location to the special null device (essentially making the data go nowhere)

& : Adds the command to an infinite background loop, making it run in the background forever

Allowing iSH to always track your location: Then it won't stop letting iSH track location after closing the app
```



# torrent



```
First you will need iSH Shell app from https://apps.apple.com/us/app/ish-shell/id1436902243

Second, you will need to have a way to view page source to copy the "magnet:" magnet link address, because apparently somehow we couldn't simply copy the magnet address as link without special workarounds, it could very well be Apple imposing this limitation.

I have the text editor I developed with Shortcuts I can use to view page source, if you're interested:

Have Shortcuts app installed, then grab New Text (and Save Text if you want save support) from https://redd.it/ho37cs

If it said this shortcut is untrusted: Settings app > Shortcuts > Allow untrusted shortcuts

If grayed out: Open Shortcuts app, create a random shortcut, the button will become available afterwards

Visit a webpage, open share sheet and choose New Text, your clipboard will be updated, paste into the text editor, then use Safari's address to find "magnet:" in the page. For difficult magnet link, try select around it on the normal page then open New Text, the source will shrink to there.

Finally open iSH, type and enter

first time:

apk add --upgrade transmission-cli

every session (to enable running torrent in background for this session):

cat /dev/location > /dev/null &

every torrent:

transmission-cli (paste magnet link)

So you know, you can use Files app to access recently torrented files in /root/Downloads/

That's it!

UPDATE 2022/01/15 (bit late but never too late): way to stop seeding upon completion. Create a kill file into /root/ dir containing

#!/bin/sh

killall transmission-cli

Open iSH, type and enter to change permission for the kill file

chmod +x /root/kill

Then for next torrent do this

transmission-cli -f /root/kill (paste magnet link)
```



# postgresql 

- https://github.com/ish-app/ish/issues/521

```
I am running PostgreSQL in a FreeBSD jail. The standard way to solve this in that environment is to add:

allow.sysvipc = 1;
to the jail configuration. Perhaps your environment also has a way to make SysV primitives available.
```



What I've done:

- I edited `/etc/rc.conf` (on the host machine) and added the line `jail_sysvipc_allow="YES"`
- In the jail machine's `/etc/sysctl.conf`, I add line `security.jail.sysvipc_allowed=1`

I restarted the jail machine multiple times. I haven't restarted the host machine and don't want to.

```


root@xxxxx:/home/xxxx# sysctl security.jail.sysvipc_allowed=1
 security.jail.sysvipc_allowed: 0
 sysctl: security.jail.sysvipc_allowed: Operation not permitted

   root@xxxxx:/home/xxxx# sysctl -a | grep 'sysvipc'
   security.jail.param.allow.sysvipc: 0
   security.jail.sysvipc_allowed: 1


Solution found. The following does work for me. On the host, do:

root@host# jls
   JID  IP Address      Hostname                      Path
     3  -               some.jail                     /usr/jails/somejail
Find the correct JID, 3 in my example. Then, on the host, issue:

jail -m jid=3 allow.sysvipc=1
```



# browser 

- https://github.com/ish-app/ish/discussions/1486

