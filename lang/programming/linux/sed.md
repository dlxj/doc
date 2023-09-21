```
grep AllowTcpForwarding /etc/ssh/sshd_config
--> #AllowTcpForwarding yes

sed -i 's/#\?AllowTcpForwarding.*/AllowTcpForwarding yes/' /etc/ssh/sshd_config

sed 工具将匹配模式 #\?AllowTcpForwarding.* 替换为 AllowTcpForwarding yes 。其中 # 被用于匹配可选的注释符号，所以即使配置行前面有 # ，它也会被替换成 AllowTcpForwarding yes。
```

