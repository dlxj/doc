

sudo apt-get --purge autoremove packagename

dpkg --get-selections | grep 'mysql'

apt-get --purge autoremove mysql*





cmake .. -DCMAKE_INSTALL_PREFIX=/usr/local/mysql \

-DMYSQL_DATADIR=/data/mysql \

-DDOWNLOAD_BOOST=1 \  #从MySQL 5.7.5开始Boost库是必需的

-DWITH_BOOST=/root/local/boost_1_59_0 \

-DSYSCONFDIR=/etc \

-DWITH_INNOBASE_STORAGE_ENGINE=1 \

-DWITH_PARTITION_STORAGE_ENGINE=1 \

-DWITH_FEDERATED_STORAGE_ENGINE=1 \

-DWITH_BLACKHOLE_STORAGE_ENGINE=1 \

-DWITH_MYISAM_STORAGE_ENGINE=1 \

-DENABLED_LOCAL_INFILE=1 \

-DENABLE_DTRACE=0 \

-DDEFAULT_CHARSET=utf8mb4 \

-DDEFAULT_COLLATION=utf8mb4_general_ci \

-DWITH_EMBEDDED_SERVER=1

apt-get install libncurses5-dev