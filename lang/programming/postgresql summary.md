Success. You can now start the database server using:

```bash
pg_ctlcluster 13 main start
```



登录 [u](https://www3.ntu.edu.sg/home/ehchua/programming/sql/PostgreSQL_GetStarted.html)

```mysql
sudo -u postgres psql
select version();
\password postgres  # 修改密码
\q
```



Added the line as below in `pg_hba.conf`:

```sql
# vi /etc/postgresql/13/main/pg_hba.conf
# 加在最后面
hostnossl    all          all            0.0.0.0/0  trust        
```

and this was modified in `postgresql.conf`, as shown:

```sql
# vi /etc/postgresql/13/main/postgresql.conf
listen_addresses = '*'  
```

