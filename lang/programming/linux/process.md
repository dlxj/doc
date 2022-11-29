\# run

\#!/bin/bash

nohup node launchcluster.js >outlog &

\# kill

\#!/bin/bash

kill -9 $(lsof outlog | tail -n +2  |  awk '{print $2}' | tr '\n' ' ') && \

kill -9 $(lsof -i:8001 | tail -n +2  |  awk '{print $2}' | tr '\n' ' ')

ps p $(cat /var/run/elasticsearch.pid)

kill -9 $(lsof -i:8888 | tail -n +2  |  awk '{print $2}' | tr '\n' ' ')



jobs 查看后台运行程序



进程所在路径

```
PID为1521，ls -al /proc/1521  , CWD 就是进程所在路径
```





# tmux

```
yum install epel-release
yum install tmux
```

```
tmux
tmux attach # default 0

tmux attach -t 0
Contol + b  后按 d 可以离开环境并不影响当前程序的执行（离开后可以断开 ssh 连接）
ctrl + D # 退出当前 session，中断程序执行
tmux kill-session -t 0 # 在没有进入 session 的情况下 kill 它

```



# 关闭 stopped 进程

```
	docker There are stopped jobs.
	kill -9 $(jobs -p)
		# 可以正常 exit 容器了
```





# 关闭后台进程





```

// 数据库备份时卡了，就会不响应
// ps aux |grep mysql  
// insert into imgs(`md5`,api,ip,userID)VALUES('2ef5f105b39f12a67749a55fd321b671','aliyun','127.0.0.1',0) on duplicate key update ip='127.0.0.1'

(async () => {

    let fs = require('fs')
    let md5 = require('md5')

    let bytes = fs.readFileSync("1032.jpg")  // 'binary'
    let buf = Buffer.from(bytes)
    let m5 = md5(buf)
    let b64 = buf.toString('base64')


    let json = {
        md5: m5,
        imgData: b64,
        guid: '1049a596-fea6-4f0f-863f-62d0b0a2ea55',
        userID:11,
        bookNO: 'lrx333',
        imgName: '1032.jpg',
        originImgData: b64
    }

    // json = {
    //     md5: '7468efae7d7ab7333d0197a8ca1bf32c',
    //     imgData: 'hasTest',
    //     guid: 'abc346eb-aeb1-4759-b885-68052ec34810',
    //     bookNO: 'lrx333',
    //     imgName: '1032.jpg'
    // }

    let bent = require('bent')
    let formurlencoded = require('form-urlencoded')

    let formurlencoded_body = formurlencoded(json)

    //let post = bent('http://192.168.2.88:11112', 'POST', 'json', 200)
    let post = bent('http://127.0.0.1:11112', 'POST', 'json', 200)
    let response = await post('/aliyun/ocr', json)



    data = JSON.parse(response).data.test

    let s = JSON.stringify(response)

    console.log(response)

})()

```



# 最大文件数

```
ulimit -a

```



# docker



```

yum whatprovides ifconfig
yum install net-tools

docker run -tid --name centos7_server_6006 -p 222:22 --privileged=true centos:7 /sbin/init
	# 此命令会自动下载镜像
	# -p 222:22 表示将宿主的222端口映射容器的22端口


docker exec -it centos7_server_6006 /bin/bash
	# 运行docker 的shell


docker ps
docker stop centos7_server_6006
docker start centos7_server_6006
	# 关闭和重启

yum install openssh-server -y
	# 安装ssh

vi /etc/ssh/sshd_config
	# 修改配置
	PermitRootLogin yes # 改成这个
	UsePAM no # 改成这个


systemctl start sshd
	# 启动ssh

eixt
	# 退出容器



docker inspect centos7_server_6006 | grep IPAddress
	# 查看IP
	--> "IPAddress": "10.88.0.2"
	
passwd root
	# 修改密码，容器名就是密码
	centos7_server_6006

systemctl stop firewalld
	# 关闭防火墙

ssh root@10.88.0.2 -p 22
	# 登录看看
	--> 成功


yum install nmap
	# 扫描指定端口是否开放	
	nmap 118.178.137.176 -p222
		PORT    STATE  SERVICE
		222/tcp closed rsh-spx	
			# 端口并没有开放

	netstat -aptn | grep -i 222
		tcp        0      0 0.0.0.0:222             0.0.0.0:*               LISTEN      45594/conmon
			# 好像本地 222 端口是开放了的

	lsof -i:222
		conmon  45594 root    5u  IPv4 446985      0t0  TCP *:rsh-spx (LISTEN)
			# 也是显示开放了


	https://blog.csdn.net/qq_39176597/article/details/111939051
		# linux关闭防火墙了，但端口还是访问不了

		systemctl  start  firewalld
			# 启动防火墙
			systemctl  status  firewalld

		firewall-cmd --zone=public --add-port=222/tcp --permanent
		firewall-cmd --zone=public --add-port=222/tcp --permanent
		firewall-cmd --zone=public --add-port=6006/tcp --permanent
			# 开放端口
	
		firewall-cmd --reload
			# 重新加载配置文件
		
		firewall-cmd --list-ports
			# 查看已经开放的端口

		systemctl status polkit
		/usr/lib/polkit-1/polkitd --no-debug &

		docker ps
		docker stop centos7_server_6006

nginx 80 转 6006

map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

upstream centos7_server_6006 {
  server localhost:6006;
}


#####            测试          #####
server {
  listen 80;
  server_name localhost;

  location / {
    location / {
      proxy_pass http://centos7_server_6006;
    }
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    proxy_read_timeout 9999999;
    proxy_connect_timeout 9999999;
    proxy_send_timeout 9999999;
  }
}


nginx -s reload


npm i -g pm2@4.5.1


/usr/local/node-v14.17.0-linux-x64/bin/pm2-dev -> /usr/local/node-v14.17.0-linux-x64/lib/node_modules/pm2/bin/pm2-dev
/usr/local/node-v14.17.0-linux-x64/bin/pm2 -> /usr/local/node-v14.17.0-linux-x64/lib/node_modules/pm2/bin/pm2
/usr/local/node-v14.17.0-linux-x64/bin/pm2-docker -> /usr/local/node-v14.17.0-linux-x64/lib/node_modules/pm2/bin/pm2-docker
/usr/local/node-v14.17.0-linux-x64/bin/pm2-runtime -> /usr/local/node-v14.17.0-linux-x64/lib/node_modules/pm2/bin/pm2-runtime


ln -s /usr/local/node-v14.17.0-linux-x64/lib/node_modules/pm2/bin/pm2 /usr/local/bin/pm2




传文件

docker ps
	# 显示容器 ID
	6f7dcc6f9fa3  quay.io/centos/centos:7  /sbin/init  8 hours ago  Up 8 hours ago  0.0.0.0:222->22/tcp  centos7_server_6006


docker cp /yingedu/project/aicbyserver_v2 centos7_server_6006:/project
	# 复制代码
docker cp /usr/local/node-v14.17.0-linux-x64 centos7_server_6006:/usr/local
	# 复制node


进 docker 启动服务

	docker exec -it centos7_server_6006 /bin/bash
	cd /usr/local
	ln -s /usr/local/node-v14.17.0-linux-x64/bin/node /usr/local/bin/node && \
	ln -s /usr/local/node-v14.17.0-linux-x64/bin/npm /usr/local/bin/npm && \
	ln -s /usr/local/node-v14.17.0-linux-x64/bin/npx /usr/local/bin/npx && \
	ln -s /usr/local/node-v14.17.0-linux-x64/bin/cnpm /usr/local/bin/cnpm && \
	ln -s /usr/local/node-v14.17.0-linux-x64/bin/pm2 /usr/local/bin/pm2
	
	systemctl stop firewalld

	cd /project/aicbyserver_v2
	pm2 --name aicbyserver_v2_6006 start "node server.js"
	
	docker There are stopped jobs.
	kill -9 $(jobs -p)
		# 可以正常 exit 容器了
	exit


退出docker, 在宿主机 访问 docker 服务

	docker inspect centos7_server_6006 | grep IPAddress
	ping 10.88.0.2
		# docker ip

	
固定容器 IP   https://cloud.tencent.com/developer/article/1418033


	docker network create --subnet=172.18.0.0/16 custom
	docker network create --subnet 10.10.10.10/16 custom
		docker run -d --name target-service --net static --ip 10.10.10.10 py:test
		docker run -tid --name centos7_server_6006 --net=custom --ip=172.18.0.2 -p 222:22 --privileged=true centos:7 /sbin/init
		# 创建自定义网络				

	docker network ls


	--net=es-network --ip=172.18.0.1

	# 删除容器
	docker stop centos7_server_6006
	docker rm centos7_server_6006
	docker network rm custom
		# 删除网络

	# 创建容器
	docker run -tid --name centos7_server_6006 --net=bridge --ip=10.88.0.2 -p 222:22 --privileged=true centos:7 /sbin/init
		# 使用默认网络，并固定 IP
		
	docker run -tid --name centos7_server_6006 --net=custom --ip=172.18.0.2 -p 222:22 --privileged=true centos:7 /sbin/init

		# 此命令会自动下载镜像
		# -p 222:22 表示将宿主的222端口映射容器的22端口

```

