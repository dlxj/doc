# 定时备份



```
apt-get install cron
```



```
backup.sh
dir="/root/ak148_backup/$(date +'%Y-%m-%d')"
mkdir -p $dir
cp /root/echodict/pandora/ak148_script.xlsx $dir
cp /root/echodict/pandora/pre_ak148_script.xlsx $dir

crontab -e
00   00    *      *   *  sh /root/backup.sh
```







```
crontab -e # edit
crontab -l # list all task

00   07    *      *   *	    python3.8 -u /root/sign.py > /root/log_sign.txt

```





```
00   01    11      12   *   echo 'say hi from auto.'>/root/hi.txt
```





```
30   5    8      6   *   ls     指定每年的6月8日5：30执行ls命令
分   时    日     月
```



```
5   *    *      *   *   ls     指定每小时的第5分钟执行一次ls命令
30   5    *      *   *   ls     指定每天的 5:30 执行ls命令
30   7    8      *   *   ls     指定每月8号的7：30分执行ls命令
30   5    8      6   *   ls     指定每年的6月8日5：30执行ls命令
30   5    8      6   *   ls     指定每年的6月8日5：30执行ls命令
30   6    *      *   0   ls     指定每星期日的6:30执行ls命令
30   3   10,20     *   *   ls     每月10号及20号的3：30执行ls命令
25   8-11  *      *   *   ls     每天8-11点的第25分钟执行ls命令
*/15  *    *      *   *   ls     每15分钟执行一次ls命令
30   6   */10     *   *   ls     每个月中，每隔10天6:30执行一次ls命令
22   4    *      *   *   root   run-parts   /etc/cron.daily
#每天4：22以root身份执行/etc/cron.daily目录中的所有可执行文件，run-parts参数表示，执行后面目录中的所有可执行文件。
```



```
注意 

* *1 * * * 命令表示是每小时之内的每一分钟都执行。

必须指定在每个小时的第几分钟执行，也就是说第一个*号必须改成一个数值。

因为*号表示的就是每一分钟。

另外小时位的/1和没有区别，都是每小时一次。

如果是设置*/2，实际上是能被2整除的小时数而不是从定时设置开始2小时后执行，比如9点设的到10点就会执行。

最后可能会遇到下面这个问题

root用户下 输入 crontab -l 显示

no crontab for root 例如：

[root@CentOS ~]# crontab -l

no crontab for root

这个问题非常简单，同样在 root 用户下输入 crontab -e

按 Esc 按： wq 回车

在输入 crontab -l 就没有问题了

主要原因是由于这个liunx服务器 第一次使用 crontab ，还没有生成对应的文件导致的，执行了 编辑（crontab -e）后 就生成了这个文件
```



```
1.安装crontab

[root@CentOS ~]# yum install cronie
[root@CentOS ~]# yum install crontabs
cronie软件包是cron的主程序；

crontabs软件包是用来安装、卸装、或列举用来驱动 cron 守护进程的表格的程序。

2.开启crontab服务

service crond start //启动服务
用以下的方法启动、关闭这个cron服务：

service crond start //启动服务

service crond stop //关闭服务

service crond restart //重启服务

service crond reload //重新载入配置

查看crontab服务状态：service crond status

手动启动crontab服务：service crond start

查看crontab服务是否已设置为开机启动，执行命令：ntsysv
```



```
设置开机自动启动crond服务: 

[root@CentOS ~]# chkconfig crond on

查看各个开机级别的crond服务运行情况

[root@CentOS ~]# chkconfig –list crond

crond 0:关闭 1:关闭 2:启用 3:启用 4:启用 5:启用 6:关闭

可以看到2、3、4、5级别开机会自动启动crond服务

取消开机自动启动crond服务: 

[root@CentOS ~]# chkconfig crond off

3.设置需要执行的脚本 

新增调度任务可用两种方法：

1)、在命令行输入: crontab -e 然后添加相应的任务，wq存盘退出。
	crontab -e
	20   18    10      12   *   echo 'hi from crontab.' >sayhi.txt
	
2)、直接编辑/etc/crontab 文件，即vi /etc/crontab，添加相应的任务。

crontab -e配置是针对某个用户的，而编辑/etc/crontab是针对系统的任务

查看调度任务

crontab -l //列出当前的所有调度任务

crontab -l -u jp //列出用户jp的所有调度任务

删除任务调度工作

crontab -r //删除所有任务调度工作

直接编辑 vim /etc/crontab ,默认的文件形式如下：
```



# 检查接口不好就重启

```
check.sh
http_code=$(curl -m 5 -s -o /dev/null -w %{http_code} http://127.0.0.1:8005/gettest?appename=ZC_ZXYJHNKX_YTMJ)
if [ "$http_code" -eq 200 ]; then
  echo "Success" > /dev/null
else
  echo "$(date +%Y%m%d-%H:%M:%S) gettest api test fail, restart ksbaiexam_8005 right now!!!" >/root/ksbao_logs.txt
  pm2 restart ksbaiexam_8005
fi

crontab -e
*   *    *      *   *   sleep 5;sh /root/check.sh
*   *    *      *   *   sleep 10;sh /root/check.sh
*   *    *      *   *   sleep 15;sh /root/check.sh
*   *    *      *   *   sleep 20;sh /root/check.sh
*   *    *      *   *   sleep 25;sh /root/check.sh
*   *    *      *   *   sleep 30;sh /root/check.sh
*   *    *      *   *   sleep 35;sh /root/check.sh
*   *    *      *   *   sleep 40;sh /root/check.sh
*   *    *      *   *   sleep 45;sh /root/check.sh
*   *    *      *   *   sleep 50;sh /root/check.sh
*   *    *      *   *   sleep 55;sh /root/check.sh

```





