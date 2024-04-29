```
babel.config.js
module.exports = {
    presets: [
        //'@vue/cli-plugin-babel/preset'
        ["@vue/app",{useBuiltIns:"entry"}]
    ]
}
```



```
# node 默认 1.5G 内存上限，超出会报错 
luanch.json
{
    "version": "0.61742.0",
    "configurations": [
        {
            "type": "node",
            "request": "launch",
            "name": "Launch Program",
            "skipFiles": [
                "<node_internals>/**"
            ],
            "program": "${workspaceFolder}\\boom_memory.js",
            "runtimeArgs": ["--max-old-space-size=8192"]
        }
    ]
}

{
            "args":["a"],
            "runtimeArgs": [
                "run-script",
                "app",
                "b"
            ],
        }
打印参数可以发现 args 、runtimeArgs都会传给程序，但是runtimeArgs参数会紧跟可执行文件


```





```
多线程爆内存 ERR_WORKER_OUT_OF_MEMORY

https://zhuanlan.zhihu.com/p/167920353    worker threads 

https://juejin.cn/post/6844903937355563022
注意这3句：每个线程都拥有独立的事件循环
每个线程都拥有一个 JS 引擎实例
每个线程都拥有一个 Node.js 实例

https://juejin.cn/post/6844903953759469581
	干货
const { Worker, isMainThread, parentPort, MessageChannel, threadId } = require('worker_threads');

if (isMainThread) {
    const worker1 = new Worker(__filename);
    const worker2 = new Worker(__filename);
    
    const { port1, port2 } = new MessageChannel();
    const sharedUint8Array = new Uint8Array(new SharedArrayBuffer(4));
	// 输出一下sharedUint8Array
    console.log(sharedUint8Array);
    worker1.postMessage({ uPort: port1, data: sharedUint8Array }, [ port1 ]);
    worker2.postMessage({ uPort: port2, data: sharedUint8Array }, [ port2 ]);

    worker2.once('message', (message) => {
        console.log(`${message}, 查看共享内存:${sharedUint8Array}`);
    });
} else {
    parentPort.once('message', ({ uPort, data }) => {
        uPort.postMessage(`我是${threadId}号线程`);
        uPort.on('message', (msg) => {
            console.log(`${threadId}号收到:${msg}`);
            if (threadId === 2) {
                data[1] = 2;
                parentPort.postMessage('2号线程修改了共享内存!!!');
            }
            console.log(`${threadId}号查看共享内存:${data}`);
        })
    })
}

=>
Uint8Array [ 0, 0, 0, 0 ]
2号收到:我是1号线程
2号线程修改了共享内存!!!, 查看共享内存:0,2,0,0
1号收到:我是2号线程
2号查看共享内存:0,2,0,0
1号查看共享内存:0,2,0,0


I check settings which relates vm.max_map_count

# sysctl vm.max_map_count
vm.max_map_count = 65530
# sysctl kernel.threads-max
kernel.threads-max = 2060362
# sysctl kernel.pid_max
kernel.pid_max = 4194304
I guess that vm.max_map_count should be twice of kernel.threads-max, thus, I set as follows.

# sysctl -w vm.max_map_count=4120724

```



## install nodejs



```
wget https://nodejs.org/download/release/v14.21.1/node-v14.21.1-linux-x64.tar.gz && \
tar xvf node-v14.21.1-linux-x64.tar.gz && \
cd node-v14.21.1-linux-x64/bin && \
chmod +x node npm npx && \
cd ../.. && \
mv node-v14.21.1-linux-x64 /usr/local && \
ln -s /usr/local/node-v14.21.1-linux-x64/bin/node /usr/local/bin/node && \
ln -s /usr/local/node-v14.21.1-linux-x64/bin/npm /usr/local/bin/npm && \
ln -s /usr/local/node-v14.21.1-linux-x64/bin/npx /usr/local/bin/npx

npm install cnpm@7.1.0 -g --registry=https://registry.npm.taobao.org && \
npm install pm2@5.1.2 -g --registry=https://registry.npm.taobao.org 

ln -s /usr/local/node-v14.21.1-linux-x64/lib/node_modules/pm2/bin/pm2 /usr/local/bin/pm2

```



```
version=v20.11.0 && \
version=v18.9.1 && \
version=v20.11.1 && \
wget https://nodejs.org/download/release/$version/node-$version-linux-x64.tar.gz && \
tar xvf node-$version-linux-x64.tar.gz && \
cd node-$version-linux-x64/bin && \
chmod +x node npm npx && \
cd ../.. && \
mv node-$version-linux-x64 /usr/local && \
ln -s /usr/local/node-$version-linux-x64/bin/node /usr/local/bin/node && \
ln -s /usr/local/node-$version-linux-x64/bin/npm /usr/local/bin/npm && \
ln -s /usr/local/node-$version-linux-x64/bin/npx /usr/local/bin/npx

npm i -g pm2 && \
ln -s /usr/local/node-$version-linux-x64/lib/node_modules/pm2/bin/pm2 /usr/local/bin/pm2



pm2 --name chatgpt_server_506 start "proxychains4 node server.js"

pm2 save
pm2 dump // 此时会备份 pm2 list 中的所有项目启动方式
pm2 resurrect // 重启备份的所有项目
pm2 update    // 清空重启次数等（疑难杂症可以试试）


pm2 monit
	# 实时监视进程

```





## vscode 附加参数

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "node",
            "request": "launch",
            "name": "Launch Program",
            "skipFiles": [
                "<node_internals>/**"
            ],
            //"program": "${workspaceFolder}\\t.js",
            "args": ["--experimental-wasm-threads", "${file}"]
        }
    ]
}
```



### 代理运行 node

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "node",
            "request": "launch",
            "name": "Launch Program",
            "skipFiles": [
                "<node_internals>/**"
            ],
            "program": "${workspaceFolder}/server.js",
            "runtimeExecutable": "proxychains4",
            "runtimeArgs": [
                "node"
            ]
        }
    ],
}

# 实际运行命令是这样：/usr/bin/proxychains4 node ./server.js

```



### deepspped vcode 调试

```
# see 
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "/root/miniconda3/envs/internlm-env/bin/deepspeed",
            "console": "integratedTerminal",
            "justMyCode": true,
            "args": [
                "--num_gpus=1",
                "--master_port=7777",
                "main.py",
                "--deepspeed",
                "zero2_config.json",
                "--do_train",
                "True",
                "--do_eval",
                "True",
                "--train_file",
                "belleMath.json",
                "--validation_file",
                "belleMath-dev1K.json",
                "--prompt_column",
                "conversations",
                "--overwrite_cache",
                "True",
                "--model_name_or_path",
                "/root/autodl-tmp/chatglm2-6b",
                "--output_dir",
                "./output/adgen-chatglm-6b-ft-6e-6-0704",
                "--overwrite_output_dir",
                "True",
                "--max_length",
                "16",
                "--per_device_eval_batch_size",
                "1",
                "--gradient_accumulation_steps",
                "4",
                "--predict_with_generate",
                "True",
                "--num_train_epochs",
                "3",
                "--logging_steps",
                "20",
                "--save_steps",
                "1000",
                "--learning_rate",
                "6e-6",
                "--fp16",
                "True",
                "--save_total_limit",
                "5"
            ]
        }
    ]
}
```





## vscode C++ 附加调试

[Debugging a Shared Library](https://nilrt-docs.ni.com/cross_compile/call_shared_library.html)

[gdb 笔记](https://blog.csdn.net/wohu1104/article/details/125067910)

```
git clone --recursive  https://github.com/redis/redis.git && \
cd redis/src && \
vi Makefile
	# OPTIMIZATION?=-O3
	# OPTIMIZATION?=-O0  
		# 改成这个

make distclean && \
make USE_SYSTEMD=yes V=1


vi /root/redis/redis.conf
bind 0.0.0.0
daemonize yes
enable-module-command yes
	# 改成这样 

./redis-server /root/redis/redis.conf
	# 正常运行，记下它的 PID
	# 它有可能会直接后台运行，如果 lsof 6379 有输出说明正常

# 这里只用 gdb ，不用 vscode ，因为 vscode 附加调试不能断下共享库的函数
cd /root/redis/src
gdb -ex r --args ./redis-server --loadmodule /root/RediSearch/bin/linux-x64-release/search/redisearch.so --loadmodule /root/RedisJSON/bin/linux-x64-release/rejson.so
	# https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/gdb.html
	# 成功跑起来以后 ctrl + Z 回到 gdb
	
/root/RediSearch/src/tokenize.c
	GetTokenizer

(gdb) break GetTokenizer
(gdb) info b
(gdb) r
	# 重新运行
delete
	# 删除所有断点
c
	# 继续运行

redis-cli
	# 这里执行中文搜索，可以成功触发断点

# 试着修改中文分词模块，每次都只返回中中中中中
cd /root/RediSearch
make build SLOW=1 VERBOSE=1


vscode 先安装 C++ 插件, 再装 makefile tool
	# "processId": "771184" 
		# 改成前面记下来的 PID

vi /etc/environment
LANG=en_US.utf-8
LC_ALL=en_US.utf-8

/root/redis/.vscode/tasks.json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "shell",
            "type": "shell",
            "command": "source /etc/environment"
        }
    ]
}
	# lanuch 之前会自动执行task 里定义的命令

launch.json	
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "C/C++ Runner: Debug Session",
      "type": "cppdbg",
      "request": "attach",
      "processId": "771184",
      "program": "/root/redis/src/redis-server",
      "MIMode": "gdb",
      "miDebuggerPath": "gdb",
      "setupCommands": [
        {
          "description": "Enable pretty-printing for gdb",
          "text": "-enable-pretty-printing",
          "ignoreFailures": true
        },
        {
          "text": "-gdb-set follow-fork-mode child",
          "ignoreFailures": true
        },
        "preLaunchTask": "shell",
        "sourceFileMap": {
        "/root/RediSearch/bin/linux-x64-release/search/redisearch.so": "/root/RediSearch/src"
      }
      ]
    }
  ]
}	

# 正常附加调试

vscode 在这里下一个断点，redis-cli 一连上就会成功断下
	/root/redis/src/networking.c
	client *createClient(connection *conn) {
		    if (conn) {


vscode 上开另外一个 bash

cd /src
./redis-cli --raw
keys *
MODULE LOAD /root/RedisJSON/bin/linux-x64-release/rejson.so
MODULE LOAD /root/RediSearch/bin/linux-x64-release/search/redisearch.so
	# 成功加载两个模块
MODULE LIST
	# 列出已加载模块
	# 奇怪的是，vscode 附加调试后，再加载模块就会出错，所以只能写入配置后再运行
	loadmodule /root/RedisJSON/bin/linux-x64-release/rejson.so
	loadmodule /root/RediSearch/bin/linux-x64-release/search/redisearch.so
		# 配置文件试入这两行，再 MODULE LIST 就可以看到正常加载了
		# 然事，这时再用 vscode 附加调试就 OK 了
		
JSON.SET product:1 $ '{"id":1,"productSn":"7437788","name":"小米8","subTitle":"全面屏游戏智能手机 6GB+64GB 黑色 全网通4G 双卡双待","brandName":"小米","price":2699,"count":1}'

JSON.SET product:2 $ '{"id":2,"productSn":"7437789","name":"红米5A","subTitle":"全网通版 3GB+32GB 香槟金 移动联通电信4G手机 双卡双待","brandName":"小米","price":649,"count":5}'

JSON.SET product:3 $ '{"id":3,"productSn":"7437799","name":"Apple iPhone 8 Plus","subTitle":"64GB 红色特别版 移动联通电信4G手机","brandName":"苹果","price":5499,"count":10}'

JSON.SET product:4 $ '{"id":4,"productSn":"7437801","name":"小米8","subTitle":"他の全文検索シリーズでも同じデータを使うので、他の記事も試す場合は wiki.json.bz2 を捨てずに残しておくことをおすすめします。","brandName":"小米","price":2699,"count":1}'

JSON.GET product:1

JSON.GET product:1 name subTitle

FT.CREATE productIdx ON JSON PREFIX 1 "product:" LANGUAGE chinese SCHEMA $.id AS id NUMERIC $.name AS name TEXT $.subTitle AS subTitle TEXT $.price AS price NUMERIC SORTABLE $.brandName AS brandName TAG

ft.search productIdx "全网通" language "chinese"

ft.search productIdx "捨てずに" language "chinese"

ft.search productIdx "てずに" language "english"

exit

```



```

# 不知道为什么，运行到一半 redis-server 自已就退出了
# 只能附加调试现在
tasks.json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "shell",
            "type": "shell",
            "command": "/usr/bin/make"
        }
    ]
}

launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "C/C++ Runner: Debug Session",
      "type": "cppdbg",
      "request": "launch",
      "args": [
        "redis.conf"
      ],
      "stopAtEntry": false,
      "externalConsole": false,
      "cwd": "${workspaceFolder}",
      "program": "${workspaceFolder}/src/redis-server",
      "MIMode": "gdb",
      "miDebuggerPath": "gdb",
      "setupCommands": [
        {
          "description": "Enable pretty-printing for gdb",
          "text": "-enable-pretty-printing",
          "ignoreFailures": true
        }
      ],
      "environment": [],
      "preLaunchTask": "shell"
    }
  ]
}

"preLaunchTask": "shell"
	# 这一句是在调试时先执行 tasks.json 里面的命令
	
	
	# git submodule update --init --recursive
```



### 写一个redis模块

[date module](https://github.com/diegopacheco/redis_date_module/blob/master/src/date.c)



### 调试 redis 模块



```
echodict\friso_vs2019\src\friso_UTF8.c

/root/RediSearch/deps/friso/friso_UTF8.c
#define FRISO_CJK_CHK_C
#define FRISO_CJK_CHK_J
	# 开启 JP 字符检测
	
/root/RediSearch/deps/friso/friso.h
	# 147 行  } friso_task_entry;
	
	char text2[8192];
    char NGram[8192];
    uint_t currPos;
		# 结构体后面加这三行 

/root/RediSearch/deps/friso/friso.c
	next_mmseg_token(
		# 这个函数整个替换成下面这样

// http://www.unicode.org/cgi-bin/GetUnihanData.pl?codepoint=%E4%B8%A5
// https://www.sqlite.org/c3ref/create_function.html
// https://github.com/schuyler/levenshtein

# define min(x, y) ((x) < (y) ? (x) : (y))
# define max(x, y) ((x) > (y) ? (x) : (y))


static int utf8len(char* c) {
    unsigned char c1 = c[0];
    int len = -1;
    if ((c1 & 0x80) == 0) {  // 0b10000000
        len = 1;
    }
    else if ((c1 & 0xF0) == 0xF0) {  // 0b11110000
        len = 4;
    }
    else if ((c1 & 0xE0) == 0xE0) {  // 0b11100000
        len = 3;
    }
    else if ((c1 & 0xC0) == 0xC0) {  // 0b11000000 
        len = 2;
    }
    else {
        return -1;
    }
    return len;
}

/*
** Assuming z points to the first byte of a UTF-8 character,
** advance z to point to the first byte of the next UTF-8 character.
*/
static int utf8strlen(char* str) {
    int len;
    const unsigned char* z = str;
    if (z == 0) {
        return -1;
    }
    len = 0;
    while (*z) {
        len++;
        //SQLITE_SKIP_UTF8(z);
        if ((*(z++)) >= 0xc0) {
            while ((*z & 0xc0) == 0x80) { z++; }
        }
    }
    return len;
}

// 
/*
1 0xxxxxxx
2 110xxxxx 10xxxxxx 0xC0 0x80
3 1110xxxx 10xxxxxx 10xxxxxx
4 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
5 111110xx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx
6 1111110x 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx
*/
// 
static char* nextc(char* z) {
    if (z == 0) { return 0; }
    if (*z == 0) {
        return 0;
    }
    ++z;
    while ((*z & 0xC0) == 0x80) { ++z; }  // 
    return z;
}

static char* at(char* z, int pos) {
    char* t = z;
    int i;
    for (i = 0; i < pos; i++) {
        t = nextc(t);
    }
    return t;
}

static int utf8eq(char* c1, char* c2) {
    int i;
    if (c1 == 0 || c2 == 0 || *c1 == 0 || *c2 == 0) {
        return -1;
    }
    int len1 = utf8len(c1);
    int len2 = utf8len(c2);
    if (len1 != len2) {
        return 0;
    }
    else {
        for (i = 0; i < len1; i++) {
            if (c1[i] != c2[i]) {
                return 0;
            }
        }
    }
    return 1;
}



/* {{{ get the next segmentation.
 *     and also this is the friso enterface function.
 *
 * @param     friso.
 * @param    config.
 * @return    task.
 */
FRISO_API friso_token_t next_mmseg_token( 
        friso_t friso, 
        friso_config_t config, 
        friso_task_t task ) 
{

    /**/
    if (task->idx == 0) { // 
        memset(task->NGram, 0, 8192);
        memset(task->text2, 0, 8192);
        task->currPos = 0;
        sprintf(task->NGram, "");
        sprintf(task->text2, task->text);

        //assert(utf8eq(task->text, task->text2) == 1);

        char tmp[8192] = { 0 };
        char ngram[8192] = { 0 };
        //memcpy( tmp, at(task->text2, 0), at(task->text2, 1) - at(task->text2, 0));
        //printf("%s", tmp);

        int curPos = 0;

        int len = utf8strlen(task->text2);      // 

        for (int i = 0; i < len; i++) {       // 
            for (int j = 0; j < 6; j++) {      // 
                if (i + j < len) {
                    char * starti = at(task->text2, i);
                    char * startj = at(task->text2, i+j);
                    int lenj = utf8len(startj);
                    char* end = startj + lenj;
                    int bytes = end - starti;
                    memcpy(tmp, starti, bytes);

                    sprintf(ngram + curPos, "%s", tmp);
                    //printf("%s ", ngram + curPos);
                    
                    curPos = curPos + bytes + 1;
                    memset(tmp, 0, 8192);

                }
                else {
                    break;
                }
            }
        }

        memcpy(task->NGram, ngram, 8192);

        int findNext = 0;
        for (int k = 0; k < 8192 - 1; k++) {
            
            if (ngram[k] == '\0' && ngram[k + 1] == '\0') {
                break;
            }

            if (findNext) {
                if (ngram[k] == '\0' && ngram[k + 1] != '\0') {
                    findNext = 0;
                    continue;
                }
                else {
                    continue;
                }
                
            }
            
            if (ngram[k] != '\0') {
                //printf("\n->%s ", & ngram[k]);
                findNext = 1;
                
                int len2 = strlen(&task->NGram[k]);
                memcpy(task->token->word, &task->NGram[k], len2);
                //task->token->type = lex->type;
                task->token->length = len2;
                task->token->rlen = len2;
                task->token->word[len2] = '\0';

                task->currPos = k;

                task->idx = 1;

                return task->token;

            }
        }
        
        //printf(":");

        //int len2 = strlen(&task->NGram[0]);
        //memcpy(task->token->word, &task->NGram[0], len2);
        ////task->token->type = lex->type;
        //task->token->length = len2;
        //task->token->rlen = len2;
        //task->token->word[len2] = '\0';

        //task->currPos = 0 + len2 + 1;

        //task->idx = 1;

        //return task->token;

    }
    else {

        int findNext = 1;
        for (int k = task->currPos; k < 8192 - 1; k++) {

            if (task->NGram[k] == '\0' && task->NGram[k + 1] == '\0') {
                return NULL;
                //break;
            }

            if (findNext) {
                if (task->NGram[k] == '\0' && task->NGram[k + 1] != '\0') {
                    findNext = 0;
                    continue;
                }
                else {
                    continue;
                }

            }

            if (task->NGram[k] != '\0') {
                //printf("\n->%s ", &task->NGram[k]);
                findNext = 1;

                int len2 = strlen(&task->NGram[k]);
                memcpy(task->token->word, &task->NGram[k], len2);
                //task->token->type = lex->type;
                task->token->length = len2;
                task->token->rlen = len2;
                task->token->word[len2] = '\0';

                task->currPos = k;

                task->idx = 1;

                return task->token;

            }
        }
    }



    uint_t j, len = 0;
    string_buffer_t sb = NULL;
    lex_entry_t lex = NULL, tmp = NULL, sword = NULL;

    /* {{{ task word pool check */
    if ( ! link_list_empty( task->pool ) ) {
        /*
         * load word from the word pool if it is not empty.
         *  this will make the next word more convenient and efficient.
         *     often synonyms, newly created word will be stored in the pool.
         */
        lex = ( lex_entry_t ) link_list_remove_first( task->pool );

        //lex->word = "中";
        //lex->length = strlen(lex->word);
        //lex->rlen = lex->length;

        memcpy(task->token->word, lex->word, lex->length);
        task->token->type = lex->type;
        task->token->length = lex->length;
        task->token->rlen = lex->rlen;
        task->token->offset = lex->offset;
        task->token->word[lex->length] = '\0';

        //printf(" %s:", task->token->word);

        /* check and handle the english synonyms words append mask.
         *     Also we have to close the mask after finish the operation.
         *
         * 1. we've check the config->add_syn before open the 
         *         _LEX_APPENSYN_MASK mask.
         * 2. we should add the synonyms words of the curren 
         *         lex_entry_t from the head.
         *
         * @since: 1.6.0
         * */
        if ( lex_appensyn_check(lex) ) {
            lex_appensyn_close(lex);
            append_en_syn(lex, tmp, 1);
        }

        /*
         * __LEX_NCSYN_WORDS__:
         *  these lex_entry_t was created to store the the synonyums words.
         *     and its word pointed to the lex_entry_t's synonyms word of
         *         friso->dic, so :
         *     free the lex_entry_t but not its word here.
         *
         * __LEX_OTHER_WORDS__:
         *  newly created lexicon entry, like the chinese and english mixed word.
         *     during the invoke of function next_basic_latin.
         *
         * other type:
         *  they must exist in the dictionary, so just pass them.
         */
        switch ( lex->type ) {
        case __LEX_OTHER_WORDS__: 
            FRISO_FREE( lex->word );
            free_lex_entry( lex );
            break;
        case __LEX_NCSYN_WORDS__:
            free_lex_entry( lex );
            break;
        }

        return task->token;
    }
    /* }}} */

    while ( task->idx < task->length ) {
        //read the next word from the current position.
        task->bytes = readNextWord( friso, task, &task->idx, task->buffer );
        if ( task->bytes == 0 ) break;

        //clear up the whitespace.
        if ( friso_whitespace( friso->charset, task ) ) continue;

        /* {{{ CJK words recongnize block. */
        if ( friso_cn_string( friso->charset, task ) ) {
            /* check the dictionary.
             * and return the unrecognized CJK char as a single word.
             * */
            if ( ! friso_dic_match( friso->dic, 
                        __LEX_CJK_WORDS__, task->buffer) ) {
                
                //memcpy(task->buffer, "中", strlen("中") );
                //task->bytes = strlen("中");

                memcpy(task->token->word, task->buffer, task->bytes );
                task->token->type = __LEX_PUNC_WORDS__;
                task->token->length = task->bytes;
                task->token->rlen = task->bytes;
                task->token->offset = task->idx - task->bytes;
                task->token->word[(int)task->bytes] = '\0';
                return task->token;
            }

            //specifield mode split.
            //if ( config->mode == __FRISO_COMPLEX_MODE__ ) 
            //    lex = next_complex_cjk( friso, config, task );
            //else lex = next_simple_cjk( friso, config, task );
            lex = config->next_cjk(friso, config, task);

            if ( lex == NULL ) continue;    //find a stopwrod.
            lex->offset = task->idx - lex->rlen;

            /*
             * try to find a chinese and english mixed words, like 'xxok'
             *     keep in mind that is not english and chinese mixed words
             *         like 'xxx'.
             *     
             * @reader:
             * 1. only if the char after the current word is an english char.
             * 2. if the first point meet, friso will call next_basic_latin() to
             *         get the next basic latin. (yeah, you have to handle it).
             * 3. if match a CE word, set lex to the newly match CE word.
             * 4. if no match a CE word, we will have to append the basic latin
             *         to the pool, and it should after the append of synonyms words.
             * 5. do not use the task->buffer and task->unicode as the check 
             *         condition for the CE word identify.
             * 6. Add friso_numeric_letter check so can get work like '高3'
             *
             * @date 2013-09-02
             */
            if ( ( task->idx < task->length ) 
                    && ((int)task->text[task->idx]) > 0 
                    && ( friso_en_letter( friso->charset, task ) 
                        || friso_numeric_letter(friso->charset, task) ) ) {
                //create a string buffer
                sb = new_string_buffer_with_string(lex->word);

                //find the next basic latin.
                task->buffer[0] = task->text[task->idx++];
                task->buffer[1] = '\0';
                tmp = next_basic_latin(friso, config, task);
                tmp->offset = task->idx - tmp->length;
                string_buffer_append( sb, tmp->word );

                //check the CE dictionary.
                if ( friso_dic_match( friso->dic, 
                            __LEX_CEM_WORDS__, sb->buffer ) ) {
                    j = lex->offset; //bakup the offset.
                    lex = friso_dic_get( friso->dic, 
                            __LEX_CEM_WORDS__, sb->buffer );
                    lex->offset = j;
                    check_free_otlex_entry(tmp);
                    free_string_buffer(sb);
                    tmp = NULL; sb = NULL;
                }
            }

            /*
             * copy the lex_entry to the result token
             *
             * @reader: (boodly lession, added 2013-08-31):
             *     don't bother to handle the task->token->offset problem.
             *         is has been sovled perfectly above. 
             */
            len = (int) lex->length;
            memcpy(task->token->word, lex->word, lex->length);
            task->token->type = lex->type;
            task->token->length = lex->length;
            task->token->rlen = lex->rlen;
            task->token->offset = lex->offset;
            task->token->word[len] = '\0';

            //check and append the synonyms words
            if ( config->add_syn && lex->syn != NULL ) {
                if ( config->spx_out == 1 ) {
                    token_sphinx_output(task, lex);
                } else {
                    token_normal_output(task, lex, 0);
                }
            }

            /* {{{ here: handle the newly found basic latin created when 
             * we try to find a CE word.
             *
             * @reader:
             * when tmp is not NULL and sb will not be NULL too
             *     except a CE word is found.
             *
             * @TODO: finished append the synonyms words on 2013-12-19.
             */
            if ( tmp != NULL && sb != NULL ) {
                //check the secondary split.
                if ( config->en_sseg == 1 
                        && task_ssseg_check(task) ) {
                    en_second_seg(friso, config, task, tmp, 0);
                }

                free_string_buffer( sb );
                link_list_add( task->pool, tmp );

                //check if append synoyums words.
                if ( config->add_syn == 1 ) {
                    lex_appensyn_open(tmp);
                }

            }
            /* }}} */

            return task->token;
        } 
        /* }}} */

        /* {{{ basic english/latin recongnize block. */
        else if ( friso_halfwidth_en_char( friso->charset, task ) 
                || friso_fullwidth_en_char( friso->charset, task ) ) {
            /*
             * handle the english punctuation.
             *
             * @todo:
             * 1. commen all the code of the following if 
             *     and uncomment the continue to clear up the punctuation directly.
             *
             * @reader: 
             * 2. keep in mind that ALL the english punctuation will be handled here,
             *  (when a english punctuation is found during the other process, we will
             *      reset the task->idx back to it and then back here)
             *     except the keep punctuation(define in file friso_string.c) 
             *     that will make up a word with the english chars around it.
             */
            if ( friso_en_punctuation( friso->charset, task ) ) {
                if ( config->clr_stw 
                        && friso_dic_match(friso->dic, 
                            __LEX_STOPWORDS__, task->buffer) ) {
                    continue;
                }

                //count the punctuation in.
                task->token->word[0] = task->buffer[0];
                task->token->type    = __LEX_PUNC_WORDS__;
                task->token->length  = task->bytes;
                task->token->rlen    = task->bytes;
                task->token->offset  = task->idx - task->bytes;
                task->token->word[1] = '\0';
                return task->token;

                //continue
            }    

            //get the next basic latin word.
            lex = next_basic_latin( friso, config, task );
            lex->offset = task->idx - lex->rlen;

            /* @added: 2013-12-22
             * check and do the secondary segmentation work.
             * this will split 'qq2013' to 'qq, 2013'
             * */
            sword = NULL;
            if ( config->en_sseg == 1 
                    && task_ssseg_check(task) ) {
                sword = en_second_seg(friso, config, task, lex, 1);
            }

            //check if it is a stopword.
            if ( config->clr_stw 
                    && friso_dic_match( friso->dic, 
                        __LEX_STOPWORDS__, lex->word ) ) {
                //free the newly created lexicon entry.
                check_free_otlex_entry( lex );
                if ( sword == NULL ) continue;
                lex = sword;
            } else if ( sword != NULL ) {
                if ( config->add_syn == 1 ) lex_appensyn_open(lex);
                link_list_add(task->pool, lex);

                /* If the sub token is not NULL:
                 * add the lex to the task->pool if it is not NULL 
                 * and return the sub token istead of lex so
                 *     the sub tokens will be output ahead of lex.
                 * */
                lex = sword;
            }

            //if the token is longer than __HITS_WORD_LENGTH__, drop it 
            //copy the word to the task token buffer.
            //if ( lex->length >= __HITS_WORD_LENGTH__ ) continue;
            memcpy(task->token->word, lex->word, lex->length);
            task->token->type   = lex->type;
            task->token->length = lex->length;
            task->token->rlen   = lex->rlen;
            task->token->offset = lex->offset;
            task->token->word[lex->length] = '\0';

            /* If sword is NULL, continue to check and append 
             * tye synoyums words for the current lex_entry_t.
             * */
            if ( sword == NULL 
                    && config->add_syn == 1 ) {
                append_en_syn(lex, tmp, 0);
            }

            //free the newly create lex_entry_t
            check_free_otlex_entry( lex );

            return task->token;
        } 
        /* }}} */

        /* {{{ Keep the chinese punctuation.
         * @added 2013-08-31) */
        else if ( friso_cn_punctuation( friso->charset, task ) ) {
            if ( config->clr_stw 
                    && friso_dic_match(friso->dic, 
                        __LEX_STOPWORDS__, task->buffer) ) {
                continue;
            }

            //count the punctuation in.
            memcpy(task->token->word, task->buffer, task->bytes);
            task->token->type   = __LEX_PUNC_WORDS__;
            task->token->length = task->bytes;
            task->token->offset = task->idx - task->bytes;
            task->token->word[task->bytes] = '\0';
            return task->token;
        }
        /* }}} */
        //else if ( friso_letter_number( friso->charset, task ) ) 
        //{
        //} 
        //else if ( friso_other_number( friso->charset, task ) ) 
        //{
        //}

        /* {{{ keep the unrecognized words?
        //@date 2013-10-14 */
        else if ( config->keep_urec ) {
            memcpy(task->token->word, task->buffer, task->bytes);
            task->token->type = __LEX_UNKNOW_WORDS__;
            task->token->length = task->bytes;
            task->token->offset = task->idx - task->bytes;
            task->token->word[task->bytes] = '\0';
            return task->token;
        }
        /* }}} */
    }

    return NULL;
}



```





```
# 成功生成 NGram
typedef struct {
    ...
    ...
    char buffer[7];         //word buffer. (1-6 bytes for an utf-8 word in C).
    char text2[8192];
    char NGram[8192];       // NGram分词结果
    uint_t currPos;
} friso_task_entry;
FRISO_API friso_token_t next_mmseg_token( 
        friso_t friso, 
        friso_config_t config, 
        friso_task_t task ) 
{
    /**/
    if (task->idx == 0) { // 首次分词，生成 NGram
        memset(task->NGram, 0, 8192);
        memset(task->text2, 0, 8192);
        task->currPos = 0;
        sprintf(task->NGram, "");
        sprintf(task->text2, task->text);

        assert(utf8eq(task->text, task->text2) == 1);

        char tmp[8192] = { 0 };
        char ngram[8192] = { 0 };
        //memcpy( tmp, at(task->text2, 0), at(task->text2, 1) - at(task->text2, 0));
        //printf("第一个字符：%s", tmp);

        int curPos = 0;

        int len = utf8strlen(task->text2);      // 整个utf8 字符串长度

        for (int i = 0; i < len; i++) {       // 编历字符串，第 0 个字符 到 第 len - 1 个字符
            for (int j = 0; j < 6; j++) {      // NGram 长度从 1 到 6
                if (i + j < len) {
                    char * starti = at(task->text2, i);
                    char * startj = at(task->text2, i+j);
                    int lenj = utf8len(startj);
                    char* end = startj + lenj;
                    int bytes = end - starti;
                    memcpy(tmp, starti, bytes);

                    sprintf(ngram + curPos, "%s", tmp);
                    //printf("%s ", ngram + curPos);
                    
                    curPos = curPos + bytes + 1;
                    memset(tmp, 0, 8192);

                }
                else {
                    break;
                }
            }
        }

        memcpy(task->NGram, ngram, 8192);

        int findNext = 0;
        for (int k = 0; k < 8192 - 1; k++) {
            
            if (ngram[k] == '\0' && ngram[k + 1] == '\0') {
                break;
            }

            if (findNext) {
                if (ngram[k] == '\0' && ngram[k + 1] != '\0') {
                    findNext = 0;
                    continue;
                }
                else {
                    continue;
                }
                
            }
            
            if (ngram[k] != '\0') {
                //printf("\n->%s ", & ngram[k]);
                findNext = 1;
                
                int len2 = strlen(&task->NGram[k]);
                memcpy(task->token->word, &task->NGram[k], len2);
                //task->token->type = lex->type;
                task->token->length = len2;
                task->token->rlen = len2;
                task->token->word[len2] = '\0';

                task->currPos = k;

                task->idx = 1;

                return task->token;

            }
        }
        
        //printf(":");

        //int len2 = strlen(&task->NGram[0]);
        //memcpy(task->token->word, &task->NGram[0], len2);
        ////task->token->type = lex->type;
        //task->token->length = len2;
        //task->token->rlen = len2;
        //task->token->word[len2] = '\0';

        //task->currPos = 0 + len2 + 1;

        //task->idx = 1;

        //return task->token;

    }
    else {

        int findNext = 1;
        for (int k = task->currPos; k < 8192 - 1; k++) {

            if (task->NGram[k] == '\0' && task->NGram[k + 1] == '\0') {
                return NULL;
                //break;
            }

            if (findNext) {
                if (task->NGram[k] == '\0' && task->NGram[k + 1] != '\0') {
                    findNext = 0;
                    continue;
                }
                else {
                    continue;
                }

            }

            if (task->NGram[k] != '\0') {
                //printf("\n->%s ", &task->NGram[k]);
                findNext = 1;

                int len2 = strlen(&task->NGram[k]);
                memcpy(task->token->word, &task->NGram[k], len2);
                //task->token->type = lex->type;
                task->token->length = len2;
                task->token->rlen = len2;
                task->token->word[len2] = '\0';

                task->currPos = k;

                task->idx = 1;

                return task->token;

            }
        }
    }

```





```

RediSearch\src\document.c
	aCtx->tokenizer->Start
	# 这里应该就是分词最开始的地方

friso
config->next_token = next_mmseg_token;
config->next_cjk = next_complex_cjk;
	# next_token 每次返回一个词，返回 NULL 表示结束
	

RediSearch\src\tokenize_cn.c
static uint32_t cnTokenizer_Next(RSTokenizer *base, Token *t) {
	friso_token_t tok = config_g->next_token(friso_g, config_g, self->fTask);
		# RediSearch 对 next_token 封装了一下


redis\src\config.c
if (!strcasecmp(argv[0],"loadmodule") && argc >= 2) {
	# 这是从服务端读取配置文件，然后添加进待加载列表
	
redis\src\module.c
	void moduleCommand(client *c) {
		if (!strcasecmp(subcmd,"load") && c->argc >= 3) {
			# 这是从客户端加载模块
redis\src\module.c
int moduleLoad(const char *path, void **module_argv, int module_argc, int is_loadex) {
	# 实际加载模块在这里


/root/redis/src/module.c
    onload = (int (*)(void *, void **, int))(unsigned long) dlsym(handle,"RedisModule_OnLoad");
	# 加载模块的代码在这里

RedisModuleCmdFunc cmdfunc
	# 模块代码的执行可能和这个有关

执行命令 ft.search productIdx "全网通" language "chinese"
void RedisModuleCommandDispatcher(client *c) {
	# 会在这里断下来
	/root/redis/src/server.c
		c->cmd->proc(c);
			# 上层调用在这里

RediSearch\src\module-init\module-init.c
	int RedisModule_OnLoad(RedisModuleCtx *ctx, RedisModuleString **argv, int argc) {

E:\t\RediSearch\src\aggregate\aggregate_exec.c
	int RSSearchCommand(RedisModuleCtx *ctx, RedisModuleString **argv, int argc) {
		# 实际执行搜索可能是这里


```



```

# gdb -ex r --args redis-server --loadmodule /root/RediSearch/bin/linux-x64-release/search/redisearch.so --loadmodule /root/RedisJSON/bin/linux-x64-release/rejson.so

# redis-cli --raw

MODULE LOAD /root/RedisJSON/bin/linux-x64-release/rejson.so
MODULE LOAD /root/RediSearch/bin/linux-x64-release/search/redisearch.so
	# 成功加载两个模块
	loadmodule /root/RedisJSON/bin/linux-x64-release/rejson.so
	loadmodule /root/RediSearch/bin/linux-x64-release/search/redisearch.so
		# 配置文件试加这两行

JSON.SET product:1 $ '{"id":1,"productSn":"7437788","name":"小米8","subTitle":"全面屏游戏智能手机 6GB+64GB 黑色 全网通4G 双卡双待","brandName":"小米","price":2699,"count":1}'

JSON.SET product:2 $ '{"id":2,"productSn":"7437789","name":"红米5A","subTitle":"全网通版 3GB+32GB 香槟金 移动联通电信4G手机 双卡双待","brandName":"小米","price":649,"count":5}'

JSON.SET product:3 $ '{"id":3,"productSn":"7437799","name":"Apple iPhone 8 Plus","subTitle":"64GB 红色特别版 移动联通电信4G手机","brandName":"苹果","price":5499,"count":10}'

JSON.SET product:4 $ '{"id":4,"productSn":"7437801","name":"小米8","subTitle":"他の全文検索シリーズでも同じデータを使うので、他の記事も試す場合は wiki.json.bz2 を捨てずに残しておくことをおすすめします。","brandName":"小米","price":2699,"count":1}'

JSON.GET product:1

JSON.GET product:1 name subTitle

FT.CREATE productIdx ON JSON PREFIX 1 "product:" LANGUAGE chinese SCHEMA $.id AS id NUMERIC $.name AS name TEXT $.subTitle AS subTitle TEXT $.price AS price NUMERIC SORTABLE $.brandName AS brandName TAG

ft.search productIdx "香槟金" language "chinese"
	# 中文 OK
ft.search productIdx "て" language "chinese"
	# 开启 JP 字符检测后 搜 JP 字符看
		# 不行
		# 改完 NGram 编译后，成功！

ft.search productIdx "全文" language "chinese"
	# 成功
	
ft.search productIdx "他の" language "chinese"
	# 可以 是因为 JP 字符被忽略了，没用
		# 还得是上 NGram
        
ft.search productIdx "じデータ" language "chinese"
	# 不行
	# 改完 NGram 编译后，成功！


/root/RediSearch/src/tokenize.c
	GetTokenizer

(gdb) break next_mmseg_token  # GetTokenizer
(gdb) info b
(gdb) r
	# 重新运行

redis-cli
	# 这里执行中文搜索，可以成功触发断点


# 下载改写 redisearch 的 friso，先开启JP字符识别，再让中文分词变成 NGram 分词

git clone --recursive https://github.com/RediSearch/RediSearch.git
make build SLOW=1 VERBOSE=1
	https://redis.io/docs/stack/search/development/
	/root/RediSearch/bin/linux-x64-release/search/redisearch.so

/root/RediSearch/deps/friso/friso_UTF8.c
#define FRISO_CJK_CHK_J
	# 206 行 前面的注释取消



./autogen.sh
make install
friso -init /usr/local/etc/friso/friso.ini
歧义和同义词:研究生命起源，混合词: 做B超检查身体

"-lm" linux vscode 的 gcc 配置要加一个 -lm 参数

next_mmseg_token
next_complex_cjk

```



### gdb 调试利器

[gdb 调试利器](https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/gdb.html)

[vimspector](https://github.com/puremourning/vimspector)

> - run：简记为 r ，其作用是运行程序，当遇到断点后，程序会在断点处停止运行，等待用户输入下一步的命令。
> - continue （简写c ）：继续执行，到下一个断点处（或运行结束）
> - next：（简写 n），单步跟踪程序，当遇到函数调用时，也不进入此函数体；此命令同 step 的主要区别是，step 遇到用户自定义的函数，将步进到函数中去运行，而 next 则直接调用函数，不会进入到函数体内。
> - step （简写s）：单步调试如果有函数调用，则进入函数；与命令n不同，n是不进入调用的函数的
> - until：当你厌倦了在一个循环体内单步跟踪时，这个命令可以运行程序直到退出循环体。
> - until+行号： 运行至某行，不仅仅用来跳出循环
> - finish： 运行程序，直到当前函数完成返回，并打印函数返回时的堆栈地址和返回值及参数值等信息。
> - call 函数(参数)：调用程序中可见的函数，并传递“参数”，如：call gdb_test(55)
> - quit：简记为 q ，退出gdb

#### 断点

> - break n （简写b n）:在第n行处设置断点
>
>   （可以带上代码路径和代码名称： b OAGUPDATE.cpp:578）
>
> - b fn1 if a＞b：条件断点设置
>
> - break func（break缩写为b）：在函数func()的入口处设置断点，如：break cb_button
>
> - delete 断点号n：删除第n个断点
>
> - disable 断点号n：暂停第n个断点
>
> - enable 断点号n：开启第n个断点
>
> - clear 行号n：清除第n行的断点
>
> - info b （info breakpoints） ：显示当前程序的断点设置情况
>
> - delete breakpoints：清除所有断点：



### 显示eigen变量

https://github.com/fandesfyf/EigenGdb

C++  线代库



## vscode + MSYS2 +  Mingw-w64 

[vscode 在windows下使用gcc+mingw调试 c/c++程序](https://www.jianshu.com/p/ebc74e2d09f1)

```
Ctrl+Shift+X -> search "C++" ->安装C/C++扩展

安装 msys2 from https://www.msys2.org/

按 win 键 -> 找到 MSYS2 UCRT64 图标 -> 运行

pacman -S mingw-w64-ucrt-x86_64-gcc \
	mingw-w64-ucrt-x86_64-gdb \
	mingw-w64-ucrt-x86_64-boost

加入 path 环境变量 C:\msys64\ucrt64\bin

git clone https://github.com/Dobiasd/FunctionalPlus
cmake -S FunctionalPlus -B FunctionalPlus/build && \
cmake --build FunctionalPlus/build && \
cmake --install FunctionalPlus/build
	# CPP Monads
	--> -- Installing: /usr/local/include/fplus

gcc --version
gdb --version
g++ --version

t.cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main() {
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};
    for (const string& word : msg) {
        cout << word << " ";
    }
    cout << endl;
}

vscode 中点找 t.cpp 文件 -> Ctrl + Shift + P 
	-> 选择 C/C++: Debug C/C++ File -> 选择 C/C++:g++.exe build and debug active file preLaunchlask: C/C++: g++.exe build active fileDetected Task(compiler: C:\msys64\ucrt64\bin\g++.exe)

会自动生成一个 tasks.json 文件:
{
    "tasks": [
        {
            "type": "cppbuild",
            "label": "C/C++: g++.exe build active file",
            "command": "C:\\msys64\\ucrt64\\bin\\g++.exe",
            "args": [
                "-fdiagnostics-color=always",
                "-g",
                "${file}",
                "-o",
                "${fileDirname}\\${fileBasenameNoExtension}.exe"
            ],
            "options": {
                "cwd": "${fileDirname}"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "detail": "Task generated by Debugger."
        }
    ],
    "version": "2.0.0"
}

在 main 下断点，F5 运行，成功断下

```



### vscdoe + MSVC

[VS Code for Microsoft C++](https://code.visualstudio.com/docs/cpp/config-msvc)

```
解决 vscode 调试窗口 utf8 显示乱码
win键 -> 设置 -> 时间和语言 -> 最右边"日期、时间和区域格式设置" 
  ->其他日期、时间和区域设置 ->区域 更改日期、时间或数字格式
  -> 管理 ->更改系统区域设置 ->Beta版:使用Unicode UTF-8提供全球语言支持


打开 Developer Command Prompt for VS 2019 命令行
在这个命令行运行 code ，会打开 vscode
打开目录 -> 打开文件t.cpp -> ctrl + shift + P -> 输入C++ 
  -> 选 C/C++:Debug C/C++File
  	# 会自动生成 task.json

{
    "tasks": [
        {
            "type": "cppbuild",
            "label": "C/C++: cl.exe build active file",
            "command": "cl.exe",
            "args": [
                "/Zi",
                "/EHsc",
                "/nologo",
                "/Fe${fileDirname}\\${fileBasenameNoExtension}.exe",
                "${file}"
            ],
            "options": {
                "cwd": "${fileDirname}"
            },
            "problemMatcher": [
                "$msCompile"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "detail": "Task generated by Debugger."
        }
    ],
    "version": "2.0.0"
}




```





[vscode使用visual studio编译工具MSVC构建C++工程](https://blog.csdn.net/qq_37429313/article/details/120588483)

```
ctrl + shift + x -> 输入 easy c
	# 安装 Easy C++ projects 插件

ctrl + shit + p -> 输入 c json
	# 会生成 c_cpp_properties.json

ctrl + shit + p -> 输入 easy -> 选新建工程
	# 选 x64 visual studio 2019
	# 会自动生成 .vscode 下的各种配置

```



```
# 自动生成的 build.bat 修改成这样
@echo off
if exist "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" (
    call "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" x64
) else (
    if exist "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat" (
        call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
    ) else (
        call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Enterprise\VC\Auxiliary\Build\vcvarsall.bat" x64
    )
)
set compilerflags=/Od /Zi /EHsc /std:c++latest /I include /I C:\src\vcpkg\packages\fplus_x64-windows\include
set linkerflags=/OUT:bin\main.exe
cl.exe %compilerflags% src\*.cpp /link %linkerflags%
del bin\*.ilk *.obj *.pdb
```



```
# 自动生成的(不是) main.cpp 修改成这样
#include <fplus/fplus.hpp>
#include <iostream>
using namespace std;

bool is_odd_int(int x) { return x % 2 != 0; }

int main(){
    typedef vector<int> Ints;
    Ints values = { 24, 11, 65, 44, 80, 18, 73, 90, 69, 18 };
    auto odds = fplus::keep_if(is_odd_int, values);
    std::cout << "done." << std::endl;
}
```



```
# 对比 MSYS32 MINGW64 或许可以改进一下
{
    "tasks": [
        {
            "type": "cppbuild",
            "label": "C/C++: g++.exe build active file",
            "command": "C:\\msys64\\ucrt64\\bin\\g++.exe",
            "args": [
                "-fdiagnostics-color=always",
                "-g",
                "${file}",
                "-o",
                "${fileDirname}\\${fileBasenameNoExtension}.exe",
                "-IC:\\Program Files (x86)\\FunctionalPlus\\include"
            ],
            "options": {
                "cwd": "${fileDirname}"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "detail": "Task generated by Debugger."
        }
    ],
    "version": "2.0.0"
}
```







## vs studio WSL Linux 开发

[使用VS 2017进行Linux C/C++远程GDB调试](https://zhuanlan.zhihu.com/p/30950892)



### utf8 处理

[C语言utf8判断中文](https://blog.csdn.net/liu0808/article/details/81743462)



```
doc\lang\programming\cpp\c64\similar\similar.c

// visual studio 源文件utf-8 编码必须要有BOM 才行
// http://www.unicode.org/cgi-bin/GetUnihanData.pl?codepoint=%E4%B8%A5
// https://www.sqlite.org/c3ref/create_function.html
// https://github.com/schuyler/levenshtein

# define min(x, y) ((x) < (y) ? (x) : (y))
# define max(x, y) ((x) > (y) ? (x) : (y))

// 某个utf8 字符占几个字节
// c: 必须指向utf8 字符串
static int utf8len(char *c) {
	unsigned char c1 = c[0];
	int len = -1;
	if ((c1 & 0x80) == 0) {  // 0b10000000
		len = 1;
	}
	else if ((c1 & 0xF0) == 0xF0) {  // 0b11110000
		len = 4;
	}
	else if ((c1 & 0xE0) == 0xE0) {  // 0b11100000
		len = 3;
	}
	else if ((c1 & 0xC0) == 0xC0) {  // 0b11000000 
		len = 2;
	}
	else {
		return -1;
	}
	return len;
}

/*
** Assuming z points to the first byte of a UTF-8 character,
** advance z to point to the first byte of the next UTF-8 character.
*/
// 计算字符个数
// 实现参考sqlite3 的lengthFunc 函数
static int utf8strlen(char *str) {
	int len;
	const unsigned char *z = str;
	if (z == 0) {
		return -1;
	}
	len = 0;
	while (*z){
		len++;
		//SQLITE_SKIP_UTF8(z);
		if ((*(z++)) >= 0xc0) {
			while ((*z & 0xc0) == 0x80){ z++; }
		}
	}
	return len;
}

// utf8 编码规则
/*
1字节 0xxxxxxx
2字节 110xxxxx 10xxxxxx 0xC0 0x80
3字节 1110xxxx 10xxxxxx 10xxxxxx
4字节 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
5字节 111110xx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx
6字节 1111110x 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx
*/
// 假定z 指向第一个utf8 字符，函数执行完以后z 指向下一个字符
static char *nextc(char *z) {
	if (z == 0) { return 0; }
	if (*z == 0) {
		return 0;
	}
	++z;
	while ((*z & 0xC0) == 0x80) { ++z; }  // 只要最高位是10 开头就继续移动指针
	return z;
}

static char *at(char *z, int pos) {
	char *t = z;
	int i;
	for (i = 0; i < pos; i++) {
		t = nextc(t);
	}
	return t;
}

static int utf8eq(char *c1, char *c2) {
	int i;
	if (c1 == 0 || c2 == 0 || *c1 == 0 || *c2 == 0) {
		return -1;
	}
	int len1 = utf8len(c1);
	int len2 = utf8len(c2);
	if (len1 != len2) {
		return 0;
	} else {
		for (i = 0; i < len1; i++) {
			if (c1[i] != c2[i]) {
				return 0;
			}
		}
	}
	return 1;
}

static unsigned int levenshtein(const char *word1_in, const char *word2_in) {
	const char *word1 = word1_in;
	const char *word2 = word2_in;
	int len1 = utf8strlen(word1),
		len2 = utf8strlen(word2);
	unsigned int *v = calloc(len2 + 1, sizeof(unsigned int));
	unsigned int i, j, current, next, cost;

	/* strip common prefixes */
	while (len1 > 0 && len2 > 0 && utf8eq(word1, word2)) {
		word1 = nextc(word1);
		word2 = nextc(word2);
		len1--;
		len2--;
	}

	/* handle degenerate cases */
	if (!len1) return len2;
	if (!len2) return len1;

	/* initialize the column vector */
	for (j = 0; j < len2 + 1; j++)
		v[j] = j;

	for (i = 0; i < len1; i++) {
		/* set the value of the first row */
		current = i + 1;
		/* for each row in the column, compute the cost */
		for (j = 0; j < len2; j++) {
			/*
			* cost of replacement is 0 if the two chars are the same, or have
			* been transposed with the chars immediately before. otherwise 1.
			*/
			cost = !(utf8eq(at(word1,i), at(word2,j)) || (i && j &&
				utf8eq(at(word1, i - 1), at(word2, j)) && utf8eq(at(word1,i), at(word2, j - 1))));
			/* find the least cost of insertion, deletion, or replacement */
			next = min(min(v[j + 1] + 1,
				current + 1),
				v[j] + cost);
			/* stash the previous row's cost in the column vector */
			v[j] = current;
			/* make the cost of the next transition current */
			current = next;
		}
		/* keep the final cost at the bottom of the column */
		v[len2] = next;
	}
	free(v);
	return next;
}

__declspec(dllexport) double __stdcall sim(char *word1, char *word2)  {
	int len1 = utf8strlen(word1);
	int len2 = utf8strlen(word2);
	int len = max(len1, len2);
	if (len == 0) {
		return -1;
	}
	int distance = levenshtein(word1, word2);
	//return distance;
	return 1 - distance / (double)len;
}

__declspec(dllexport) int __stdcall add(int a, int b) {
	return a + b;
}


#pragma execution_character_set("utf-8")  // "string 以utf-8 编码"
int main() {
	system("chcp 65001");
	//printf ("%s", at("严严ab", 0));
	char z1[] = "严严b";
	char z2[] = "严严a";
	printf("%s", at(z1, 0));
	printf("相似度：    %f\n", sim(z1, z2));
	getchar();
}


```



## vscode + gradio

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
# python 直接运行 run.py 就可以直接断下了
# 前端用 cd demo/xx && pnpm dev
# {interactive} 直接在页面上显示变量的值
# http://localhost:9876/  用前端地址可以实时显示前端热修改的结果，用后端地址不行。
# 因它只显示编译后的前端？


vscode + vite
{
    "configurations": [
        {
            "type": "chrome",
            "request": "launch",
            "name": "Launch Chrome against localhost",
            "url": "http://localhost:9876",
            "webRoot": "${workspaceFolder}"
        }
    ]
}
# 运行前端


// {
//     "version": "0.2.0",
//     "configurations": [
//         {
//             "name": "Python Debugger: Current File",
//             "type": "debugpy",
//             "request": "launch",
//             "program": "/root/miniconda3/bin/gradio",
//             "console": "integratedTerminal",
//             "args": [
//                 "${file}"
//             ]

//         }
//     ]
// }
```





## vscode + jupyter 

[1](https://zhuanlan.zhihu.com/p/500571676)

```
pip install --upgrade ipykernel
pip install jupyterlab

jupyter lab
	# 先运行，后下断点
	# 成功单步调试
	
Developer Command Prompt for vS 2019
	# pip install spacy==3.2
		# 没有少头文件，但是少链接库
		#  linalg.obj : error LNK2001: 无法解析的外部符号 __imp__PyBaseObject_Type
		
		D:\usr\Python311\python.exe -m pip install -U pip setuptools wheel
		pip install -U spacy
	
```





## vscode+colab

[vscode+colab](https://github.com/amitness/colab-connect)



## vscode 权限错误

Bad owner or permissions on C:\\Users\\i/.ssh/config 

找到.ssh文件夹。它通常位于C:\Users，例如C:\Users\i。
右键单击.ssh文件夹，然后单击“属性”。
找到并点击“安全”标签。
然后单击“高级”。 单击“禁用继承”，单击“确定”。 将出现警告弹出窗口。单击“从此对象中删除所有继承的权限”。
你会注意到所有用户都将被删除。让我们添加所有者。在同一窗口中，单击“编辑”按钮。
接下来，单击“添加”以显示“选择用户或组”窗口。
单击“高级”，然后单击“立即查找”按钮。应显示用户结果列表。 选择您的用户帐户。
然后单击“确定”（大约三次）以关闭所有窗口。
完成所有操作后，再次关闭并打开VSCode 并尝试连接到远程SSH主机。
现在这个问题应该解决了。



## vscode genie

[chat.lmsys.org  claude VS gpt4](https://chat.lmsys.org/)

[double](https://docs.double.bot/introduction)

[chatgpt-vscode](https://github.com/ai-genie/chatgpt-vscode)

[CopilotForXcode](https://github.com/intitni/CopilotForXcode)


### vscode 代理

https://www.aahgo.com/post/328.html



```
windows 设置这两个环境变量，vscode 的　terminal 就走代理了
HTTP_PROXY 和 HTTPS_PROXY
http://172.16.6.253:8118
```






## pm2



```
systemctl start postgresql.service  # ubuntu 18.04 
systemctl status postgresql-13      # centos7
systemctl enable postgresql-13 # 自启动

npm i -g pm2
	# node18 用这个
	
ln -s /usr/local/node-v18.9.1-linux-x64/lib/node_modules/pm2/bin/pm2 /usr/local/bin/pm2	

pm2 --name chatgpt_server_506 start "proxychains4 node server.js"


npm i -g pm2@5.1.2
	# node14 用这个

pm2 save
pm2 dump // 此时会备份 pm2 list 中的所有项目启动方式
pm2 resurrect // 重启备份的所有项目
pm2 update    // 清空重启次数等（疑难杂症可以试试）

pm2 restart id --name newName
	# 改名

pm2 monit
	# 实时监视进程

pm2 reload explainteam_server_7114 --name my_new_name --max-old-space-size 4096

pm2 delete processID  // 删除一项

pm2 flush 进程ID | 进程名  // 清空日志

# 关闭防火墙
systemctl stop firewalld
# 关闭 apache 
service httpd stop

yum install nginx
nginx -t # 显示主配置文件路径，并检查语法错误
systemctl start nginx
	# ubuntu 这样启动 /etc/init.d/nginx start
nginx -s reload

# atuto run when reboot
chmod +x /etc/rc.d/rc.local
vi /etc/rc.d/rc.local
mount /dev/sda1 /mnt  # 加一句，挂载存储块

```



### 每五秒检查一次接口，不好就重启

```
check.sh
http_code=$(curl -m 5 -s -o /dev/null -w %{http_code} https://evaluaing.ksxxx.com/gettest?appename=ZC_ZXYJHNKX_YTMJ)
if [ "$http_code" -eq 200 ]; then
  echo "Success" > /dev/null
else
  echo "$(date +%Y%m%d-%H:%M:%S) gettest api test fail, restart ksbaiexam_8005 right now!!!" >/root/ksbao_logs.txt
  pm2 restart ksbaiexam_8005
fi

crontab -e
00   00    *      *   *   pm2 restart ksbaiexam_8005
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



### node-gpy 下载出错

```

npm config set tarball /root/node-v18.9.1-headers.tar.gz 
	# 让它使用本地文件，不要下载
	#　node-v18.9.1-headers.tar.xz　下载这个，tar zxvf 解压，再 tar czvf 压缩成 .tar.gz 
npm i
	# 成功安装

# download for private repo, probably you're behind firewall
curl -k -o node-v8.9.4-headers.tar.gz -L https://nexus.com/repository/binaries/node/v8.9.4/node-v8.9.4-headers.tar.gz

# capture the absolute path
TARBALL_PATH=$(pwd)

# configure tarball in npm config
npm config set tarball ${TARBALL_PATH}/node-v8.9.4-headers.tar.gz

# The below command should pass without gyp error
npm install
```



### primordials 奇奇怪怪的错误

[primordials is not defined](https://bobbyhadz.com/blog/referenceerror-primordials-is-not-defined)

```
package.json if node >= 16.14
{
  "overrides": {
    "graceful-fs": "^4.2.11"
  }
}

package.json if node < 16.14
{
  "resolutions": {
    "graceful-fs": "^4.2.11"
  },
  "scripts": {
    "preinstall": "npx npm-force-resolutions"
  }
}

```



## npm 镜像

```
一、修改成腾讯云镜像源
1、命令

npm config set registry http://mirrors.cloud.tencent.com/npm/

2. 验证命令

npm config get registry

如果返回http://mirrors.cloud.tencent.com/npm/，说明镜像配置成功。

二、修改成淘宝镜像源
1. 命令

npm config set registry https://registry.npmmirror.com

2. 验证命令

npm config get registry

如果返回https://registry.npmmirror.com，说明镜像配置成功。

三、修改成华为云镜像源
1. 命令

npm config set registry https://mirrors.huaweicloud.com/repository/npm/

2. 验证命令

npm config get registry
```





## cnpm



```
管理员身份运行 powershell
	set-executionpolicy remotesigned

# cnpm
 原因：cnpm版本太高了，npm全局安装的cnpm是最新版的，所以卸载原来的cnpm再装一个指定版本即可

卸载cnpm:

npm uninstall -g cnpm

安装指定版本：7.1.0

npm install cnpm@7.1.0 -g --registry=https://registry.npm.taobao.org
	# 配套 node14 ok



npm install -g cnpm --registry=https://registry.npm.taobao.org
	# 安装是最新版 会有兼容问题
	
	
```



### Rprimordials is not defined

- https://blog.csdn.net/qiqi_zhangzz/article/details/106599233

```

先把 node_modules 全删了

package.json 同级目录新建 npm-shrinkwrap.json

{
  "dependencies": {
    "graceful-fs": {
      "version": "4.2.3"
    }
  }
}

npm i
	# 注意只有这一次有效果，再 npm i 就没效果了

```



## nginx

- https://linuxize.com/post/how-to-install-nginx-on-centos-7/
- https://www.bbwho.com/dockerrong-qi-hua-nginx-node-js-and-redis/  基于Nginx, Node.js 和 Redis的Docker容器化工作流
- https://blog.csdn.net/yeguxin/article/details/94020476



```
# 关闭防火墙
systemctl stop firewalld
# 关闭 apache 
service httpd stop

yum install nginx  && \
nginx -t && \
systemctl restart nginx && \
nginx -s reload

systemctl restart  postgresql-13 && systemctl status postgresql-13 && systemctl stop firewalld && pm2 resurrect && systemctl restart nginx && nginx -s reload


# ubuntu 这样启动 /etc/init.d/nginx start



/etc/nginx/nginx.conf

user  root;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}
```



### 根据域名转发

```
# 不同域名实现转后端接口和前端

/etc/nginx/conf.d/docker_6006.conf

map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

upstream centos7_server_6006 {
  server 172.20.0.2:6006;
}


server {
  listen 80;
  server_name xxapi.yy.cn;

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

server {
  listen 80;
  server_name xx.yy.cn;

  location / {
     root   /home/data;
     index  index.html index.htm;
  }
}
```



#### gpt4_browser_8080

```

# vi /etc/nginx/conf.d/gp4_browser_8080.conf

map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

upstream gpt4_browser_8080 {
  server 127.0.0.1:8080;
}


server {
  listen 8880;
  server_name echodict.com;

  location / {
    location / {
      proxy_pass http://gpt4_browser_8080;
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



vi /etc/nginx/nginx.conf
	# 保持安装时的默认值就行



```





###　转发websokect

```
# websokect 消息的转发也是和上面一样的写法
# server_name xxx.176; 
 # 这里 server_name 直接指定指定，表示如果不用域名而是直接用 IP 访问，就转发到 127.0.0.1:8880

map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

upstream llama_server_8880 {
  server 127.0.0.1:8880;
}


server {
  listen 80;
  server_name xxx.176;

  location / {
    location / {
      proxy_pass http://llama_server_8880;
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
```



### 转发ssh

```
yum install nginx-mod-stream.x86_64
ll /usr/lib64/nginx/modules
	--> -rwxr-xr-x 1 root root 179856 Nov 11 00:58 ngx_stream_module.so

/etc/nginx/nginx.conf
load_module /usr/lib64/nginx/modules/ngx_stream_module.so;
user  root;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;


}

stream {
   upstream ssh_server {
     server 127.0.0.1:22;
   }
   server {
     listen 222;
     proxy_pass ssh_server;
   }
}

	# cf 过来的 请求，ssh连接不上，还必须用 ip 连
```



### 正向代理 Chatgpt

[Nginx实现ChatGPT API代理](https://blog.csdn.net/sinat_34104446/article/details/130527167)

```
vercel -A route.json --prod
直接在 route.json 里配置路由去反代，不要服务器，只要域名就 ok
```





### cloudflare ssh反代

[cloudflare ssh反代](https://github.com/tsl0922/ttyd)



### 负载均衡

```
# 同时转发http 和 websocket 
# /etc/nginx_conf.d/testDiff.conf
map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

upstream diffServer {
  server localhost:10000;
  server localhost:10001;
  server localhost:10002;
  server localhost:10003;
  server localhost:10004;
  server localhost:10005;
  server localhost:10006;
  server localhost:10007;
  server localhost:10008;
  server localhost:10009;
}

server {
  listen 7116;
  server_name localhost;

  location / {
    location / {
      proxy_pass http://diffServer;
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
```



### 网络压力测试

[dperf 网络压测](https://github.com/baidu/dperf)



### openresty nginx+luajit

[openresty](https://github.com/openresty/openresty)

- [ltui](https://github.com/tboox/ltui) 字符UI库
- [xmake](https://github.com/xmake-io/xmake-vscode)

[vimspector](https://github.com/puremourning/vimspector) neovim



#### skynet

[skynet](https://github.com/cloudwu/skynet)



### nginx for windows

[nginx](https://nginx.org/en/download.html) [1](https://www.cnblogs.com/taiyonghai/p/9402734.html)

```
cmd.exe
cd D:\usr\nginx-1.25.3
start nginx
tasklist /fi "imagename eq nginx.exe"
nginx -t -c /nginx-1.15.2/conf/nginx.conf

```





## 安装代理

```
git clone https://github.com/rofl0r/proxychains-ng.git && \
cd proxychains-ng && \
./configure --prefix=/usr --sysconfdir=/etc && \
make && \
make install && \
make install-config

vi /etc/proxychains.conf
localnet 127.0.0.0/255.0.0.0
localnet 172.16.0.0/255.240.0.0
localnet 192.168.0.0/255.255.0.0
[ProxyList]
socks5  127.0.0.1 1080
	# 改成这样

yum install epel-release -y && \
yum update && \
yum install libsodium -y && \
pip3 install shadowsocksr-cli -i https://pypi.tuna.tsinghua.edu.cn/simple
	# yum 是依赖 python2.7 的，不要替换系统的默认python


vi ~/.bashrc
alias setproxy="export ALL_PROXY=socks5h://127.0.0.1:1080"
alias setproxy="export ALL_PROXY=socks5h://172.16.6.253:1080"
alias setproxy="export ALL_PROXY=socks5h://192.168.1.119:1080"
alias unsetproxy="unset ALL_PROXY"
alias ip="curl http://ip-api.com/json/?lang=zh-CN"



source ~/.bashrc


# https://maplege.github.io/2017/09/04/socksTOhttp/
	# socks转为http代理
	apt update && apt-get install privoxy
	vi /etc/privoxy/config
	forward-socks5   /               172.16.6.253:1080 .
	listen-address 0.0.0.0:1080
    service privoxy restart
    http_proxy=http://127.0.0.1:1080 curl google.com
    	# 成功访问 google
   

vi ~/.condarc
proxy_servers:
  http: http://172.16.6.253:8118
  https: http://172.16.6.253:8118
ssl_verify: false
	# 康达设置代理

conda clean -a
	# 代理是OK 的，出错执行这个就可以了
	

export PATH=/usr/local/cuda-11.8/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH


curl --socks5 192.168.1.3:57882 google.com

In curl >= 7.21.7, you can use

curl -x socks5h://localhost:8001 http://www.google.com/

In curl >= 7.18.0, you can use

curl --socks5-hostname 192.168.1.3:57882 google.com
	# 实测成功


	# https://www.hostnextra.com/kb/how-to-install-openssl-1-1-1i-in-centos-8/
	dnf install perl-core zlib-devel -y
		# centos8
    wget https://www.openssl.org/source/openssl-1.1.1i.tar.gz && \
    tar -xzvf openssl-1.1.1i.tar.gz && \
    cd openssl-1.1.1i && \
    ./config && \
    make && \
    make install
  	cd /etc/ld.so.conf.d/
  	vi openssl-1.1.1i.conf
  	/usr/local/lib64
  		# 改成这个
  		# 后面装好shadowsocksr-cli以后各种错误，那就再删掉这配置
  	ldconfig -v
  		# 重新加载动态链接

apt-get update -y && \
apt-get install -y libsodium-dev && \
pip install shadowsocksr-cli 


shadowsocksr-cli --add-url https://www.ftwnet.net/sub/xxxxx?sub=1
	# ftwc.cc 找 ssr订阅地址

shadowsocksr-cli -u
	# 更新订阅

shadowsocksr-cli -l
	# 列出所有可用代理地址
	
shadowsocksr-cli -s 1
	# 开启代理， 1 是前面打印出来的 编号

shadowsocksr-cli --setting-address 0.0.0.0
	# 修改监听地址
	
shadowsocksr-cli --list-address && \

	
shadowsocksr-cli -S 1
	# 停止代理

shadowsocksr-cli --test-speed 15
	# 测速
	# ldconfig -p | grep libcrypto
		# 出错的话，看一下这个

shadowsocksr-cli --list-address
	# 打印监听地址
	# 默认监听端口是 1080
	
vi /etc/resolv.conf  # 临时修改 DNS，配置会实时生效，重启后失效
nameserver 1.1.1.1
nameserver 8.8.8.8
	# 改成这样
	vi /etc/sysconfig/network-scripts/ifcfg-eth0
		# 这个是永久的
	
	nameserver 172.16.7.1
	nameserver 114.114.114.114
		# 原来的值
		

proxychains4 curl https://www.youtube.com
	# 成功
```



### 学术加速

```

cat /etc/network_turbo

export no_proxy=localhost,127.0.0.1
export http_proxy=http://172.16.70.52:12798 && export https_proxy=http://172.16.70.52:12798
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
echo 设置成功

# see echodict\chatglm_v2_6b_lora\readme.txt
https://github.com/yuanzhoulvpi2017/zero_nlp/tree/main/chatglm_v2_6b_lora

source /etc/network_turbo
    # 学术加速
    # unset http_proxy && unset https_proxy
        # 取消

cd chatglm_v2_6b_lora && \
pip install -r requirements.txt && \
pip install jieba rouge_chinese nltk peft

```



#### pip 镜像

[清华镜像](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

```
临时使用
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
注意，simple 不能少, 是 https 而不是 http

设为默认
升级 pip 到最新的版本 (>=10.0.0) 后进行配置：

python -m pip install --upgrade pip && \
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
如果您到 pip 默认源的网络连接较差，临时使用本镜像站来升级 pip：

python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
配置多个镜像源
如果您想配置多个镜像源平衡负载，可在已经替换 index-url 的情况下通过以下方式继续增加源站：

pip config set global.extra-index-url "<url1> <url2>..."
请自行替换引号内的内容，源地址之间需要有空格

可用的 pypi 源列表（校园网联合镜像站）：https://mirrors.cernet.edu.cn/list/pypi
```





#### pytorch镜像 

[pytorch安装-国内镜像源](https://blog.csdn.net/gg864461719/article/details/112259806)



```
https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/linux-64/


conda install pytorch==2.0.0 torchvision==0.15.1 cudatoolkit=11.8 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/linux-64/
	# 实测可以

pip install torch==2.0.0+cu118 torchvision==0.15.1+cu118 torchaudio==2.0.1 --index-url
https://download.pytorch.org/whl/cu118


```





#### 改DNS

[完美解决绝大部分域外名的学术网站访问缓慢问题](https://blog.csdn.net/Xiao_Bai_hh/article/details/125983176)



```

cat /etc/hosts

https://sites.ipaddress.com/github.com/

140.82.112.3 github.com
18.172.134.4 huggingface.co
185.199.108.153 pytorch.org
	# 实测有用
	# ban ip 应该就没用了



```



### 异地组网

```

zerotier tailscale 


我找到了解决方案，重点在小火箭的配置文件。下面把总流程说一下：
1 ，把自己的公网 ip 绑定动态域名。
2 ，在 OpenWrt 的 Passwall 上服务器端开启 Socks 服务器。
3 ，在小火箭添加 Socks5 节点，地址就填动态域名，其他信息就填 Socks 服务器的信息即可，备注名随便填一个方便让自己识别的就好了。
4 ，重点就是小火箭配置文件。用默认的也可以，找其他更多分流规则的也可以。下面要修改一下配置文件，这是重点，在配置文件的“通用”里，分别在“跳过代理”和 tun 旁路路由”下把“192.168.0.0/16”删除。然后在配置文件的“规则”里添加一条规则，类型选 IP- CIDR ，策略选上面第 3 步添加的 Socks5 节点，不解析域名开启，地址填 192.168.0.0/16 。

这样修改后，访问局域网时就会通过 socks5 节点连接到家里的 Passwall 服务器上了，就可以访问所有局域网设备。至于小火箭主页的节点可以随便选其他的，不影响局域网访问！

最终实现的效果就是只用一个 vpn 工具（小火箭）同时解决了外网访问局域网段（ 192.168.x.x ）和国内外分流，使用体验像在家一样。
第 2 条附言  ·  2023-03-07 10:14:41 +08:00
补充：一般小火箭配置文件的规则都自带有“192.168.0.0/16”这个规则了，搜索找到这条规则，然后进行修改就可以，不需要重新添加这条规则了，不然会导致规则重复！如果配置文件的“规则”里没有这条规则才需要重新添加！
```



#### candy

https://github.com/lanthora/candy

https://v2ex.com/t/1035681#reply73



```
dnf install spdlog openssl uriparser libconfig-devel.x86_64 poco*


```





### vscode 代理

https://blog.csdn.net/m0_57236802/article/details/132169445



```
/C:/Users/i/AppData/Roaming/Code/User/settings.json

    "http.proxy": "http://172.16.6.14:5782",
    "https.proxy": "https://172.16.6.14:5782",
    "http.proxyStrictSSL": false

```







### WSL 使用 win10 代理

```
ip 端口 都指向 win10

```





### win10 重置网络

```
netsh winsock reset
```



### 透明代理

[透明代理](https://xtls.github.io/document/level-2/transparent_proxy/transparent_proxy.html#%E4%BB%80%E4%B9%88%E6%98%AF%E9%80%8F%E6%98%8E%E4%BB%A3%E7%90%86)

[netch](https://github.com/netchx/netch)

```
netch 模式选 Bypass LAN 就是全局模式

```



### 调试利器 SSH隧道

[调试利器-SSH隧道](https://github.com/gwuhaolin/blog/issues/11)



#### autodl 6006 端口服务

```
ssh -CNg -L 6006:127.0.0.1:6006 root@connect.beijinga.seetacloud.com -p 33243
	# 输入密码回车后无任何其他输出既为正常

打开 http://localhost:6006 访问自定义服务
	

```





### SSH隧道代理

[利用SSH搭建隧道-流量伪装](https://zhuanlan.zhihu.com/p/561589204)

```
grep AllowTcpForwarding /etc/ssh/sshd_config
sed -i 's/#\?AllowTcpForwarding.*/AllowTcpForwarding yes/' /etc/ssh/sshd_config
	# ssh 服务端 修改AllowTcpForwarding 为 YES
	
ssh -CNg -L 6006:127.0.0.1:6006 root@connect.bjb1.seetacloud.com -p 53862
http://localhost:6006
	# 成功访问 gradio
```

http://httpbin.org/ip

​	# 不配置代理，本地访问显示 IP: 13.229.84.151



putyy，在session 中配置 ssh 服务端地址

Connection -> SSH -> Tunnels

Destination 填 123.150.76.218:80 这是qq.com 的IP

Souce port 填 9090

点 Open 登录服务端

这样在客户端只要访问  127.0.0.1:9090 就相当于访问了 123.150.76.218:80



```
0x02 动态端口转发
动态端口转发允许你在本地（ssh客户端）机器扮演一个socks代理客户端。当客户端连接到该端口，流量会被转发到远程（ssh服务器）机器上，然后转发到目标机器的动态端口上。

这种方法中，所有使用socks代理的客户端程序将连接到ssh服务器，然后服务器将流量转发到真实的目的机器上。

在Linux、macOS和其他Unix系统中，使用ssh客户端的 -D 选项来建立动态端口转发命令如下：

$ ssh -D [LOCAL_IP:]LOCAL_PORT [USER@]SSH_SERVER
[LOCAL_IP:]LOCAL_PORT - 本地机器IP地址和端口号。当LOCAL_IP被省略，ssh客户端绑定在localhost上。
[USER@]SERVER_IP - 远程ssh用户和服务器IP地址。
动态端口转发可用于代理上网的需求中。
```





### centos8 没有软件源



```
docker 退出方法
	# kill -9  $(jobs -p)
	# exit

# centos8 没有软件源
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-8.repo

sed -i -e"s|mirrors.cloud.aliyuncs.com|mirrors.aliyun.com|g " /etc/yum.repos.d/CentOS-*

sed -i -e "s|releasever|releasever-stream|g" /etc/yum.repos.d/CentOS-*

yum clean all && yum makecache

yum update --allowerasing

```



### 光帆

https://lightsail.aws.amazon.com/



```
AWS Lightsail 光帆 3.5$ 每月

目前靠谱的就是 hyestria+端口跳跃，Xray-vision ，有闲心也可以上 naiveproxy 。

前两个可以用 mack-a 的一键脚本，谷歌一下就有。

```



Hysteria科学上网

https://mephisto.cc/tech/hysteria/



### 美国家宽代理

[美国家宽代理](https://iproyal.cn)



### CDN

[大风云](https://www.dfyun.com.cn/)



### VPN 企业专线

[橙汁科技](http://www.osase.net/pricing/arcus-he-gui-kua-jing-jia-su-chan-pin-jie-ge.html)

[连天通](https://www.zhuoyuehd.com/)



### lightsocks-nodejs 

[lightsocks-nodejs ](https://github.com/chrisyer/lightsocks-nodejs) [你也能写个 Shadowsocks](https://github.com/gwuhaolin/blog/issues/12)







## pandora

[新地址](https://github.com/zhile-io/pandora)

[另一个开源替代](https://github.com/gngpp/ninja) [2](https://github.com/flyingpot/chatgpt-proxy)

```
# restart.sh
if tail -10 /root/.pm2/logs/pandora-ak148-explain-error.log | grep -q  'json.decoder.JSONDecodeError';
then
    echo "###found pm2 logs: JSONDecodeError restart pandora_ak148_explain now..."
    rm -f /root/.pm2/logs/pandora-ak148-explain-error.log
    pm2 restart pandora_ak148_explain
fi
if tail -10 /root/.pm2/logs/pandora-ak148-explain-error.log | grep -q  'httpx.RemoteProtocolError';
then
    echo "###found pm2 logs: httpx.RemoteProtocolError restart pandora_ak148_explain now..."
    rm -f /root/.pm2/logs/pandora-ak148-explain-error.log
    pm2 restart pandora_ak148_explain
fi

# backup.sh
dir="/root/ak148_backup/$(date +'%Y-%m-%d')"
mkdir -p $dir
cp /root/echodict/pandora/ak148_script.xlsx $dir
cp /root/echodict/pandora/pre_ak148_script.xlsx $dir


# crontab -e
00   00    *      *   *  sh /root/backup.sh
*   *    *      *   *  sh /root/restart.sh
@reboot  mount /dev/sda1 /mnt
@reboot  pm2 resurrect
```



```
# restart2.sh use tmux to run
while true;
do
    last1="$(tail -1 /root/.pm2/logs/pandora-ak148-explain-out.log)"
    if grep -q "saving excel" <<<"$last1"; then
        echo "last1 saving, so sleep 60s"
        sleep 60
        last1="$(tail -1 /root/.pm2/logs/pandora-ak148-explain-out.log)"
    else
        echo "last1 sleep 30s"
        sleep 30	
    fi

    last2="$(tail -1 /root/.pm2/logs/pandora-ak148-explain-out.log)"
    if grep -q "saving excel" <<<"$last2"; then
        echo "last2 saving, so sleep 60s"
        sleep 60
        last2="$(tail -1 /root/.pm2/logs/pandora-ak148-explain-out.log)"
    else
        echo "last2 sleep 30s"
        sleep 30	
    fi

    if [[ $last1 = $last2  ]]; then
        if grep -q "saving excel" <<<"$last2"; then
            echo "@@@@@@@@@restart2.sh NOTHING TO DO"
        elif grep -q "switch account:" <<<"$last2"; then 
            echo "@@@@@@@@@restart2.sh NOTHING TO DO2"
        else
            filename="/root/echodict/pandora/ak148_script.xlsx"
            echo "@@@@@@@@@checking excel size if 3 minutes not change........."
            size1=$(wc -c <"$filename")
            sleep 180  
            size2=$(wc -c <"$filename")
            if [[ $size2 -eq $size1 ]]; then
                echo "#####Waring: pandora stuning, restart now..."
                pm2 restart 0
                echo "#####sleep 3 minute"
                sleep 180 
            fi        
        fi
    fi
done

```



### gngpp/ninja

[gngpp/ninja](https://github.com/gngpp/ninja) 试试这个登录能不能用

- [chatgpt-web-share wss 可用](https://github.com/chatpire/chatgpt-web-share)

[/to/v1/chat/completions](https://github.com/gngpp/ninja/issues/171) [1](https://github.com/openai/openai-node)

- ```
  npm install --save openai
  ```

  

```
http://127.0.0.1:7999/backend-api/

./target/debug/ninja run --arkose-chat4-har-file /mnt/huggingface/ninja/HAR/chat.openai.com.har

./ninja.exe run --arkose-gpt4-har-dir E:/huggingface/ChatGPT-to-API/harPool --bind 0.0.0.0:80
	# see .77 E:\huggingface\ChatGPT-to-API  
	# 让它配合 ChatGPT-to-API 使用
	# 新版改成这样了 （新版已闭源）




run.ps1
# 修改工作目录
Set-Location "E:\usr\Ninja"
# 执行程序
Start-Process ".\ninja.exe run --arkose-gpt4-har-dir E:\usr\Ninja\HAR"


# 它支持官方 openai 官方 api 接口的格式
curl --location --request POST 'http://xxx:7999/v1/chat/completions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 真tokeon' \
--data-raw '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "请记住我的名字叫小芳"}],
    "temperature": 0.7
}'


# 成功 post 会话
curl --location --request POST 'http://209.141.34.77:7999/backend-api/conversation' \
--header 'Content-Type: application/json' \
--header 'Accept: text/event-stream' \
--header 'Authorization: Bearer 要填真实 token' \
--data-raw '{
  "action": "next",
  "messages": [
    {
      "id": "aaa29866-4aa0-488d-81d1-88c54319b9f4",
      "author": {
        "role": "user"
      },
      "content": {
        "content_type": "text",
        "parts": [
          "你会几种语言"
        ]
      },
      "metadata": {}
    }
  ],
  "conversation_id": "06b17fd4-1dc3-47f6-a5f9-9ac71fc78631",
  "parent_message_id": "aaa29866-4aa0-477d-81d1-88c54319b9f4",
  "model": "gpt-4",
  "timezone_offset_min": -480,
  "suggestions": [],
  "history_and_training_disabled": false,
  "arkose_token": "从 ninja 前端调接口找",
  "conversation_mode": {
    "kind": "primary_assistant"
  },
  "force_paragen": false,
  "force_rate_limit": false
}'

首次消息这样传
{
  "action": "next",
  "messages": [
    {
      "id": "aaa2e633-7363-466c-98b3-4f3a7e282fcf",
      "author": {
        "role": "user"
      },
      "content": {
        "content_type": "text",
        "parts": [
          "how are you"
        ]
      },
      "metadata": {}
    }
  ],
  "parent_message_id": "aaa2e633-7363-466c-98b3-4f3a7e282fcf",
  "model": "gpt-4",
  "timezone_offset_min": -480,
  "suggestions": [],
  "history_and_training_disabled": false,
  "arkose_token": "",
  "conversation_mode": {
    "kind": "primary_assistant"
  },
  "force_paragen": false,
  "force_rate_limit": false
}


launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug executable 'ninja'",
            "cargo": {
                "args": [
                    "build",
                    "--bin=ninja",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "ninja",
                    "kind": "bin"
                }
            },
            "args": [
                "run",
                "--arkose-chat4-har-file",
                "E:/huggingface/ninja/HAR/chat.openai.com.har"
                //"/mnt/huggingface/ninja/HAR/chat.openai.com.har"
            ],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in executable 'ninja'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--bin=ninja",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "ninja",
                    "kind": "bin"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug example 'chatgpt'",
            "cargo": {
                "args": [
                    "build",
                    "--example=chatgpt",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "chatgpt",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in example 'chatgpt'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--example=chatgpt",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "chatgpt",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug example 'auth'",
            "cargo": {
                "args": [
                    "build",
                    "--example=auth",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "auth",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in example 'auth'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--example=auth",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "auth",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug example 'crypto'",
            "cargo": {
                "args": [
                    "build",
                    "--example=crypto",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "crypto",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in example 'crypto'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--example=crypto",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "crypto",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug example 'funcaptcha'",
            "cargo": {
                "args": [
                    "build",
                    "--example=funcaptcha",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "funcaptcha",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in example 'funcaptcha'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--example=funcaptcha",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "funcaptcha",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug example 'har'",
            "cargo": {
                "args": [
                    "build",
                    "--example=har",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "har",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in example 'har'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--example=har",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "har",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug example 'pow'",
            "cargo": {
                "args": [
                    "build",
                    "--example=pow",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "pow",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in example 'pow'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--example=pow",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "pow",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug example 'print_image'",
            "cargo": {
                "args": [
                    "build",
                    "--example=print_image",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "print_image",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in example 'print_image'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--example=print_image",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "print_image",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug example 'upgrade'",
            "cargo": {
                "args": [
                    "build",
                    "--example=upgrade",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "upgrade",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in example 'upgrade'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--example=upgrade",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "upgrade",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        }
    ]
}
```



####  PandoraNext

[PandoraNext](https://github.com/pandora-next/deploy) 

- [gpt3.5 api 能正常调用](https://github.com/pandora-next/deploy/issues/142)

  - ```
    echodict/pandora/ninja_chatgpt_nlpp
    	# gpt4 也是可以成功调用的，正确传参也可以见这里
    
    # 必须以 proxy 模式启动，但是这样就没有前端了
    # arkose_token 从 pandoraNext（必须改用ninja） 前端用gpt4聊一次接口找出来
    PandoraNext/config.json
    {
      "bind": "0.0.0.0:8181",
      "timeout": 600,
      "proxy_url": "",
      "public_share": false,
      "site_password": "",
      "setup_password": "",
      "whitelist": null,
      "server_mode": "proxy",
      "server_tokens": true
    }
    
    # 
    {
      "action": "next",
      "messages": [
        {
          "id": "随机生成",
          "author": {
            "role": "user"
          },
          "content": {
            "content_type": "text",
            "parts": [
              "你会几种语言"
            ]
          },
          "metadata": {}
        }
      ],
      "parent_message_id": "既使是第一次聊天也可以随机生成",
      "model": "gpt-4",
      "timezone_offset_min": -480,
      "suggestions": [
        "Show me a code snippet of a website's sticky header in CSS and JavaScript.",
        "Can you explain the concept of \"nostalgia\" to a kindergartener?",
        "Give me 3 ideas about how to plan good New Years resolutions. Give me some that are personal, family, and professionally-oriented.",
        "Create a charter to start a film club that hosts weekly screenings and discussions"
      ],
      "history_and_training_disabled": false,
      "arkose_token": "从pandoraNext前端用gpt4聊天从接口找出来",
      "conversation_mode": {
        "kind": "primary_assistant"
      },
      "force_paragen": false,
      "force_rate_limit": false
    }
    
    ```

    



```

https://ai.fakeopen.com/auth1
	# 获取 access_token
	

通过proxy模拟api向/v1/chat/completions发请求，提问一次算4条的额度

/echodict8181/api/arkose/token
	type=gpt-4
	# 成功获取 arkose_token

/echodict8181/api/token/register
	# 先生成 Share Token


/echodict8181/v1/chat/completions
	# 成功聊天 # gpt-3.5-turbo 或 gpt-4
{
    "model": "gpt-4",
    "messages": [
        {"role": "system","content": "You are a helpful assistant."},
        {"role": "user", "content": "请记住我的名字叫小芳"},
        {"role": "assistant","content": "好的，我会记住你叫小芳。有什么我可以帮助你的吗？"},
        {"role": "user", "content": "我的名字叫什么"}
    ],
    "temperature": 0.7
}


`/api/token/register` 接口是用于注册或更新 Share Token 的。这个接口的详细参数如下：

1. **HTTP方法**：`POST`
2. **请求类型**：`application/x-www-form-urlencoded`
3. **请求字段**：
   - `unique_name`：一个唯一的名字。请注意，相同 `unique_name` 和 `access_token` 会始终生成相同的 Share Token。
   - `access_token`：ChatGPT 账号的 Access Token。
   - `site_limit`：限制 Share Token 使用的站点，格式为 `https://xxx.yyy.com`。可以留空不作限制。
   - `expires_in`：Share Token 的有效期，单位为秒。设置为 `0` 表示与 Access Token 同效，设置为 `-1` 时会吊销 Share Token。
   - `show_conversations`：是否进行会话隔离，可选 `true` 或 `false`，默认为 `false`。
   - `show_userinfo`：是否隐藏邮箱等账号信息，可选 `true` 或 `false`，默认为 `false`。

这些参数允许你灵活地控制 Share Token 的行为，包括其有效期、使用限制、会话隔离和用户信息的显示。

wget https://github.com/pandora-next/deploy/releases/download/v0.2.0/PandoraNext-v0.2.0-linux-amd64-f1585a2.tar.gz && \
tar xvf PandoraNext-v0.2.0-linux-amd64-f1585a2.tar.gz && \
cd PandoraNext-v0.2.0-linux-amd64-f1585a2
	# linux

https://github.com/pandora-next/deploy/releases/download/v0.2.3/PandoraNext-v0.2.3-windows-amd64-ba29c70.zip
	# win10

run.ps1
# 修改工作目录
Set-Location "E:\usr\PandoraNext"
# 执行程序
Start-Process ".\PandoraNext.exe"


https://dash.pandoranext.com/
	# 获取授权
	
	
curl -fLO "https://dash.pandoranext.com/data/xxxx/license.jwt"
	# 放 netx 根目录

vi tokens.json
{
  "xxx@gmail.com": {
    "token": "",
    "password": "12345",
    "show_user_info": true,
    "plus": true
  }
}

vi config.json
{
  "bind": "0.0.0.0:8181",
  "timeout": 600,
  "proxy_url": "",
  "public_share": false,
  "site_password": "",
  "setup_password": "",
  "whitelist": null
}

./PandoraNext
	# 成功运行

xx.xx.xx.77:8181
	# 成功显示前端

https://ai.fakeopen.com/auth1
	# 这里直接用　gpt4 账号密码登录, 得到 token 填到　tokens.json　账号下面

xxx@gmail.com
	# 用账号，密码 12345 成功登录前端，选 GPT4 能正常聊天　

```



##### 自制前端

```
# see vue3
# see huggingface\pandoraNext_web\top\echodict.com\auth
使用 Save all resources 插件 保存https://chdct.com/auth/login
	# 存整个登录页

chrome -> f12 -> 顶部 Page 标签 后面找到 Overrides , 导入刚才保存的整个文件夹（注意结构要和page显示出来的一模一样, 选top 然后导入）

在login 的 script 下断，成功断下
	# 小技巧: 可以在 page 那里选中 login 右键 -> override content
	# 解决里面有特殊字符，不知道本地文件名怎么起
	# ? 的 urlencode是 %3F , 就是这样起

https://segmentfault.com/q/1010000014959790
	# VSCode前端文件（html文件）如何以服务器模式打开？

安装Live Server 插件
	# html 右键 -> open with live server
	
npm install http-server -g
	# 在html项目目录执行 http-server


# 调 ninja 前端
if ("[DONE]" === Y.data)
	# 这里能断下，且是输出最后一个字符后
	# 不知道为什么, ninja override 后就断不下来了
	# see .77 E:\usr\Python311\chat_with_pandoraNext.py
	# 换 selenium 爬前端方案

e_("".concat(et.dataset.id, "-nextPrompt"), eo, {
	# 这里可能是关键
	


```







## 抱抱脸 

[如何上传大文件](https://zhuanlan.zhihu.com/p/473651876)

[Huggingface上传自己的模型](https://juejin.cn/post/7081452948550746148)

[cli doc](https://huggingface.co/docs/huggingface_hub/main/guides/cli) 

[remove-credentials-from-git-windows](https://linuxhint.com/remove-credentials-from-git-windows/)

- ```
  
  注意：windows linux .gitconfig 
  autocrlf = true
  	# 都设成这样，坏处是拉代码时 proxychain 要临时改 autocrlf = false ，pull 完再改回去
  	# 否则 CRLF 的代码编译出错
  	# linux 下 git pull rwkv5-jp-explain 代码时 vscode 里的源码控制那里刚开始会显示茫茫多的修改，等它更新一下就好了，其实并没有真被修改
  	
  
  win图标旁搜索 Credential Manager -> 删掉 huggingface
  
  C:\Users\Administrator\.git-credentials
  	# 密码在这
  C:\Users\Administrator\.gitconfig
  	# 代理在这 
  	
  [http]
  	proxy = http://127.0.0.1:57882
  [https]
  	proxy = https://127.0.0.1:57882
  	# 实测有效，必须不能指定 huggingface，全部走代理才行 	
  
  vi ~/.condarc
  proxy_servers:
    http: http://172.16.6.253:8118
    https: http://172.16.6.253:8118
  ssl_verify: false
  	# 康达设置代理
  
  conda clean -a
  	# 代理是OK 的，出错执行这个就可以了
  
  ssh -CNg -L 6006:127.0.0.1:6006 root@connect.bjb1.seetacloud.com -p 53862
  http://localhost:6006
  	# 成功访问 gradio
  
  
  # 重要, windows linux 全都这样设置
  .gitconfig
  	autocrlf = true
  
  坏处：
  	proxychain-ng 签出的时侯会把 .sh 转成了 crlf，运行报错。解决方法临时改 autocrlf = false
  
  vscode -> 左下角 -> setting -> 搜 git.autofetch -> 设成 false
  
  
  GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/spaces/dlxjj/rwkv5-jp-explain
  
  .gitattributes
  # Set the default behavior, in case people don't have core.autocrlf set.
  * text=auto
  
  # Explicitly declare text files you want to always be normalized and converted
  # to native line endings on checkout.
  *.c text
  *.h text
  *.py text
  *.js text
  *.mjs text
  *.md text
  
  # Declare files that will always have CRLF line endings on checkout.
  *.sln text eol=crlf
  
  # Denote all files that are truly binary and should not be modified.
  *.png binary
  *.jpg binary
  *.jpeg binary
  *.gif binary
  *.png binary
  *.db binary
  *.mp4 binary
  *.mp3 binary
  *.pth binary
  
  ```
  
  

```

# git-lfs
apt/deb repos: curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash

yum/rpm repos: curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.rpm.sh | sudo bash

yum install git-lfs
	# apt-get install git-lfs



git lfs clone https://huggingface.co/datasets/dlxjj/gradio

git-lfs 3.4.0         
	# 这个片本正常
	
wget https://github.com/git-lfs/git-lfs/releases/download/v3.4.0/git-lfs-linux-amd64-v3.4.0.tar.gz
	# 这样装才行
	# ok 这样设置 .gitconfig 后就正常了
	
.gitconfig
[credential]
        helper = store
[user]
        name = dlxjj
        email = 12345@qq.com

[http]
        proxy = socks5h://127.0.0.1:1080
[https]
        proxy = socks5h://127.0.0.1:1080	
	

vi ~/.bashrc
alias setproxy="export ALL_PROXY=socks5h://172.16.6.185:1080"
alias unsetproxy="unset ALL_PROXY"
alias ip="curl http://ip-api.com/json/?lang=zh-CN"
	# curl 正常

source ~/.bashrc
	
unsetproxy && \
pip install pysocks && \
setproxy && \
ip

ssh -CNg -L 6006:127.0.0.1:6006 root@connect.bjb1.seetacloud.com -p 53862
http://localhost:6006
	# 成功访问 gradio


git config --global user.name "dlxjj" && \
git config --global user.email "12345@qq.com"

git config --global push.default matching  

git config --system --list
	# 查看系统config
　　
git config --global  --list
	# 查看当前用户（global）配置

git config --local  --list
	# 查看当前仓库配置信息

git clone -c http.proxy="socks5h://127.0.0.1:1080"  https://huggingface.co/datasets/dlxjj/transformer
	# 能行
	
	git clone -c http.proxy="socks5h://127.0.0.1:57882" https://huggingface.co/datasets/dlxjj/InternLM-SFT
	
git config --global http.https://huggingface.co.proxy socks5://127.0.0.1:57882
git config --global https.https://huggingface.co.proxy socks5://127.0.0.1:57882
	# 实测不可行，必须不能指定 huggingface，全部走代理才行


git config --global http.proxy http://127.0.0.1:57882
git config --global https.proxy https://127.0.0.1:57882
	# windows 针对 huggingface 设置全局代理

	C:\Users\Administrator\.gitconfig
[http]
	proxy = http://127.0.0.1:57882
[https]
	proxy = https://127.0.0.1:57882
	# 实测有效，必须不能指定 huggingface，全部走代理才行 	
	

git config --global http.https://huggingface.co.proxy socks5h://127.0.0.1:57882

git config --global --unset http.https://huggingface.co.proxy
	# 取消代理

git clone -c http.proxy="socks5h://192.168.1.8:57882"  https://huggingface.co/datasets/dlxjj/transformer


.git/config
	# 实际代理配置在这里，有问题打开直接编缉它 
	

dlxjj pwd email same as github's dlxj

pip install huggingface_hub && \
git config --global credential.helper store && \
huggingface-cli login
	# 用 token 登录
	# Your token has been saved to 
		/root/.cache/huggingface/token


git fetch --all && \
git lfs fetch --all && \
git reset --hard origin/main && \
git pull && \
git lfs pull
	# 强制恢复远程


apt-get install git-lfs

huggingface-cli repo create pandora --type dataset
	# --type {model, dataset, space}
	# 创建创库 完了以后在官网把它设为 私有
	# huggingface-cli repo create InternLM-SFT --type dataset
	# huggingface-cli repo create chatglm_v2_6b_lora --type dataset
	# huggingface-cli repo create InternLM-SFT --type dataset
	# huggingface-cli repo create Finetune-ChatGLM2-6B --type dataset
	# huggingface-cli repo create transformer --type dataset 
	# huggingface-cli repo create ninja --type dataset 
	# huggingface-cli repo create InternLM --type dataset 
	# huggingface-cli repo create chatglm-tiny --type dataset
    # huggingface-cli repo create RWKV-LM --type dataset
    	# RWKV-v4 暂时只看这个，调通先
    # huggingface-cli repo create chat_with_chatgpt --type dataset
    # huggingface-cli repo create pandoraNext --type dataset
    # huggingface-cli repo create ninja_web --type dataset
    # huggingface-cli repo create pandoraNext_web --type dataset
    # huggingface-cli repo create RWKV-v4neo --type dataset
	# huggingface-cli repo create numpy-transformer --type dataset
	# huggingface-cli repo create annotated-transformer --type dataset
	# huggingface-cli repo create win10_dev --type dataset
	# huggingface-cli repo create ChatGPT-to-API --type dataset
	# huggingface-cli repo create wpf --type dataset
	# huggingface-cli repo create ffmediaelement --type dataset
	# huggingface-cli repo create elly_videoplayer --type dataset
	# huggingface-cli repo create CleanReader.Desktop --type dataset
	# huggingface-cli repo create RWKV-v5 --type dataset
	# huggingface-cli repo create dict --type dataset
	# huggingface-cli repo create simpleGPT --type dataset
	# huggingface-cli repo create nanoRWKV --type dataset
	# huggingface-cli repo create gradio --type dataset
	# huggingface-cli repo create vite_gradio_video --type dataset
	# huggingface-cli repo create gradio_video --type dataset
	# huggingface-cli repo create gradio_bbcode --type dataset
	# huggingface-cli repo create myvideo --type dataset
	# huggingface-cli repo create mysimpletextbox --type dataset
	# huggingface-cli repo create release --type dataset
	# huggingface-cli repo create todo_fix_imageeditor --type dataset
	# huggingface-cli repo create vite_gradio_imageeditor --type dataset
	# huggingface-cli repo create PaddleOCR --type dataset
	# huggingface-cli repo create autoscreen --type dataset 
	# huggingface-cli repo create video-subtitle-extractor --type dataset 
		# 执行此命令需要设置全局代码 .gitconifg 里的不起作用
		# setproxy 这样

git config --global core.safecrlf true
	# 拒绝提交包含混合换行符的文件

git config --global core.autocrlf input
	# 提交时转换为LF，签出时不转换
git config --global core.autocrlf false
	# 提交签出均不转换


huggingface-cli.exe lfs-enable-largefiles 这里填.git所在路径
git lfs track "*.pth"
git lfs track "*.webm"
git add .
git commit -m "add 50.pth"
git push
	# 配置完就可以正常提交，不要再用暴力提交了


git lfs install && \
git add . && \
git commit -m 'm' && \
git lfs migrate import --everything && \
git push && \
git pull && git lfs pull
	# 成功提交大文件

# 每次都新建分支，删除原分支 main, 重命名分支（避免 .git 超大）
cd E:\huggingface\pandoraNext
git checkout --orphan  new_branch
git add -A
git commit -am "m"
git branch -D main
git branch -m main
git push -f origin main
xcopy E:\Github\echodict\pandora\*.xlsx E:\huggingface\pandoraNext /k /e /d /Y
git lfs install
git add .
git commit -m 'm'
git lfs migrate import --everything
git push
git pull
git LFS pull
git lfs prune
	# 成功
	
Rename-Item -Path "E:\huggingface\pandoraNext" -NewName "E:\huggingface\pandoraNext__"
git clone https://huggingface.co/datasets/dlxjj/pandoraNext
pause
	# 每次都必须重新拉
	
	
schtasks /Create /SC MINUTE /MO 10 /TN "MyTask" /TR "powershell.exe -ExecutionPolicy Bypass -File E:\huggingface\push.ps1"
	# 每隔十分钟执行一次脚本

schtasks /Delete /TN "MyTask" /F
	# 删除任务


git pull && git LFS pull
	# 本地是文件指针时，可以这样恢复成实际文件


# 不行就用这个
git checkout -f && \
git clean -df && \
git pull
	# 强制恢复成远程文件


vi sync_huggingface.sh
cd /mnt/huggingface/pandora && \
/usr/bin/cp -rf /root/echodict/pandora/* . && \
git add . && \
git commit -m 'm' && \
git lfs migrate import --everything && \
git push
	# 备份 pandora 到 huggingface

crontab -e
00   00    *      *   *  sh /root/backup.sh
00   *    *      *   *  sh /root/sync_hubggingface.sh
15   *    *      *   *  sh /root/sync_hubggingface.sh
30   *    *      *   *  sh /root/sync_hubggingface.sh
45   *    *      *   *  sh /root/sync_hubggingface.sh
@reboot  mount /dev/sda1 /mnt
@reboot  pm2 resurrect
	# 每半 15 分钟自动备份一次



huggingface-cli lfs-enable-largefiles /mnt/hubggingface/pandora
	# 大于5G 文件 需要这样设置
	
	

安装好 git-lfs 后：

git lfs install
git lfs clone https://huggingface.co/datasets/dlxjj/pandora

git lfs clone https://huggingface.co/datasets/dlxjj/echodict

git restore --source=HEAD :/
	# retry

pip3.9 install huggingface_hub
https://huggingface.co/settings/tokens
	# copy token 
	
huggingface-cli login



huggingface-cli lfs-enable-largefiles /root/hugface/echodict


git clone -c http.proxy="socks5h://127.0.0.1:1080" https://github.com/

如果只想对 GitHub 进行代理，则可以这么做：

# 以代理端口 7890 为例
git config --global http.https://github.com.proxy socks5h://127.0.0.1:7890

# 取消代理
git config --global --unset http.https://github.com.proxy

```





### huggingface 镜像

[hf-mirror 镜像](https://hf-mirror.com/)





### 自制GIT LFS服务

[自行构建GIT LFS服务](https://zhuanlan.zhihu.com/p/511750788)



### git lfs pull

```

version https://git-lfs.github.com/spec/v1
oid sha256:bdd225c8380928ccaab2b677269066db80e06807fe0911d362df4d85d5c08afd
size 1601
	# 文件指针，需要替换为实际文件


git lfs install && \
git pull && \
git lfs pull
	# 这样拉一次，本地文件就正确了



```



### sapce 推理

[REST API with Gradio and Hugging Face Spaces](https://www.tomsoderlund.com/ai/building-ai-powered-rest-api) [1](https://www.gradio.app/docs/interface)

[godot-python godot集成](https://github.com/touilleMan/godot-python/tree/godot4-meson)

[流式输出](https://juejin.cn/post/7237386183612760125)

[chatgpt](https://huggingface.co/spaces/simpx/chatdemo)

[RWKV 官方 Gradio](https://huggingface.co/spaces/BlinkDL/RWKV-Gradio-2)



```

# README.md
python_version: 3.10.13
	# 加上这个指定 python 版本，保证它和本地环境一致

# gradio
git clone https://huggingface.co/spaces/dlxjj/rwkv5-jp-explain && \
cd rwkv5-jp-explain

# app.py
import gradio, time

def my_inference_function(name):
    tmp = ""
    for i in range(10):
      time.sleep(0.3)
      tmp += str(i) + name
      yield tmp

gradio_interface = gradio.Interface(
  fn = my_inference_function,
  inputs = "text",
  outputs = "text"
)
gradio_interface.launch(server_name="0.0.0.0")
	# 流式输出





# wsl 执行
conda create -n spaceKV5 pip python=3.10.13 -y && \
conda activate spaceKV5 && \
pip3 install gradio && \
git clone https://huggingface.co/spaces/dlxjj/rwkv5-jp-explain && \
cd rwkv5-jp-explain && \
pip3 freeze > requirements.txt




# nodejs 调用
# npm i -D @gradio/client
import { client } from "@gradio/client";

const app = await client("https://dlxjj-rwkv5-jp-explain.hf.space/--replicas/rxopk/");
const result = await app.predict("/predict", [		
				"Hello!!", // string  in 'name' Textbox component
	]);

console.log(result.data);



You can add a requirements.txt file at the root of the repository to specify Python dependencies

If needed, you can also add a packages.txt file at the root of the repository to specify Debian dependencies.

The gradio package is pre-installed and its version is set in the sdk_version field in the README.md file.
```





```
选 streamlit

app.py
import streamlit as st
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
	# 提交, 要是一直 building 就重启


$ curl -X POST https://yourspace.hf.space/run/predict -H 'Content-Type: application/json' -H 'Authorization: Bearer put_your_bearer_token_here' -d '{"data": ["Paul"]}'


```



#### gpt

```
from PyPDF2 import PdfReader
import gradio as gr
import openai
import os

 # The first line contains the OpenAI key, while the second line provides the OpenAI URL, which is useful when the OpenAI server is hidden behind a proxy server.
 # eg. first line "sk-xxxxxxxxxx", second line "http://PROXY-URL"
if os.path.isfile('config'):
    config = open("config").readlines()
else:
    config = ""
api_key_from_config = ""
if len(config) > 0 and len(config[0].strip()) > 0:
    api_key_from_config = config[0].strip()
if len(config) > 1 and len(config[1].strip()) > 0:
    openai.api_base = config[1].strip()

# config
DEBUG = True

'''
 gradio: [['first question', 'No'], ['second question', 'Yes']]
 openai: [{"role": "user", "content": "first question"}, {"role": "assistant", "content": "No"}
          {"role": "user", "content": "second question"}, {"role": "assistant", "content": "Yes"}]
'''
def gradio_messages_to_openai_messages(g):
    result = []
    for pair in g:
        result.append({"role": "user", "content": pair[0]})
        result.append({"role": "assistant", "content": pair[1]})
    return result

def respond(chat_history, message, system_message, key_txt, url_txt, model, temperature):
    messages = [
            {"role": "system", "content": system_message},
            *gradio_messages_to_openai_messages(chat_history),
            {"role": "user", "content": message}
    ] 
    openai.api_key = key_txt if key_txt else api_key_from_config
    if url_txt:
        openai.api_base = url_txt
    if DEBUG:
        print("messages:", messages)
        print("model:", model)
        print("temperature:", temperature)
    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    if DEBUG:
        print("completion:", completion)
    response = completion['choices'][0]['message']['content']
    result = chat_history + [[message, response]]
    return result

def parse_pdf(prompt, pdfs, system_message, key_txt, url_txt, model, temperature):
    result = ""
    full_text = ""
    for pdf in pdfs:
        print("parse: ", pdf)
        text = ""
        reader = PdfReader(pdf.name)
        for page in reader.pages:
            text = text + page.extract_text()
        full_text = text + "\n----------\n"
    messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt + "\n\n###\n\n " + full_text}
    ]
    openai.api_key = key_txt if key_txt else api_key_from_config
    if url_txt:
        openai.api_base = url_txt
    if DEBUG:
        print("messages:", messages)
        print("model:", model)
        print("temperature:", temperature)
    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    if DEBUG:
        print("completion:", completion)
    response = completion['choices'][0]['message']['content']

    return response

with gr.Blocks() as demo:
    with gr.Tab("Config"):
        with gr.Row():
            key_txt = gr.Textbox(label = "Openai Key", placeholder="Enter openai key 'sk-xxxx'%s" %
                    (", Leave empty to use value from config file" if api_key_from_config else ""))
            url_txt = gr.Textbox(label = "Openai API Base URL", placeholder="Enter openai base url 'https://xxx', Leave empty to use value '%s'" % openai.api_base)
        system_message = gr.Textbox(label = "System Message:", value = "You are an assistant who gives brief and concise answers.")
        model = gr.Dropdown(label="Model", choices=["gpt-3.5-turbo", "gpt-3.5-turbo-0301", "gpt-4"], multiselect=False, value="gpt-3.5-turbo", type="value")
        temperature = gr.Slider(0, 2, value=1, label="Temperature", step=0.1, info="What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.")
    with gr.Tab("Chat"):
        gr.Markdown("## Chat with GPT")
        chatbot = gr.Chatbot()
        message = gr.Textbox(label = "Message:", placeholder="Enter text and press 'Send'")
        message.submit(
            respond,
            [chatbot, message, system_message, key_txt, url_txt, model, temperature],
            chatbot,
        )
        with gr.Row():
            clear = gr.Button("Clear")
            clear.click(lambda: None, None, chatbot)
            send = gr.Button("Send")
            send.click(
                respond,
                [chatbot, message, system_message, key_txt, url_txt, model, temperature],
                chatbot,
            )
    with gr.Tab("PDF"):
        gr.Markdown("## Parse PDF with GPT")
        prompt = gr.Text(label="Prompt")
        pdfs = gr.File(label="Upload PDF", file_count="multiple", file_types=[".pdf"])
        markdown = gr.Markdown(label="Output")
        with gr.Row():
            clear = gr.Button("Clear")
            clear.click(lambda: None, None, markdown)
            submit = gr.Button("Upload")
            submit.click(
                    parse_pdf,
                    [prompt, pdfs, system_message, key_txt, url_txt, model, temperature],
                    markdown
            )


if __name__ == "__main__":
    demo.launch()
else:
    # run with "gradio app.py"
    demo.launch(server_name="0.0.0.0")

```



### vscode 代理

https://blog.csdn.net/m0_57236802/article/details/132169445



```
/C:/Users/i/AppData/Roaming/Code/User/settings.json

    "http.proxy": "http://172.16.6.14:5782",
    "https.proxy": "https://172.16.6.14:5782",
    "http.proxyStrictSSL": false

```





### socks5 转 http

```
# https://maplege.github.io/2017/09/04/socksTOhttp/
	# socks转为http代理
	apt update && apt-get install privoxy
	dnf update && dnf install privoxy
	vi /etc/privoxy/config
forward-socks5   /               127.0.0.1:1080 .
listen-address 172.16.6.253:8118
	# 注意：直接写 ip 可以, 写 0.0.0.0 不可以！！！
    service privoxy restart
    http_proxy=http://127.0.0.1:8118 curl google.com
    	# 成功访问 google
    	
    	
vi ~/.bashrc
alias setproxy="export ALL_PROXY=http://127.0.0.1:8118"
alias unsetproxy="unset ALL_PROXY"
alias ip="curl http://ip-api.com/json/?lang=zh-CN"
	# curl 正常    	
    	
    	
vi ~/.condarc
proxy_servers:
  http: http://172.16.6.253:8118
  https: http://172.16.6.253:8118
ssl_verify: false
	# 康达设置代理

conda clean -a
	# 代理是OK 的，出错执行这个就可以了
	

```











## ssh 端口映射

```
ssh -CNg -L 6006:127.0.0.1:6006 root@connect.bjb1.seetacloud.com -p 53862
http://localhost:6006
	# 成功访问 gradio
```





## 内网转外网

```
162xxx50  162xxx50@qq.com
vv*C*****

cpolar.com

OTU2NWE0YjxxxRjMzA2NzQ1ODIz

cpolar authtoken OTU2NxxxxxxxxmRjMzA2NzQ1ODIz
	# Authtoken saved to configuration file: /usr/local/etc/cpolar/cpolar.yml

cpolar http 506
	# 仅对这个端口开放外网访问
	https://11be991c.r8.cpolar.top/test
		#  成功访问 /test 是 chatgpt_server 的测试页面

wget https://www.cpolar.com/static/downloads/install-release-cpolar.sh && 
bash install-release-cpolar.sh && 
systemctl enable cpolar && 
systemctl start cpolar && 
systemctl status cpolar
```





##　异地组网

https://github.com/omniedgeio/omniedge

https://github.com/tailscale/tailscale

https://github.com/kaaass/ZerotierFix



```
公司+家里都需要开启 ipv6 ，然后去注册个域名，家里电脑开启个 ddns 把域名和 ipv6 地址绑定上。
并且在家里的路由器配置好转发啥的。
然后就可以在公司通过 rdp 访问域名+端口 访问到家里内网的 pc 了
```





## 阿里云上传

https://github.com/tickstep/aliyunpan/blob/main/docs/manual.md#1-%E5%A6%82%E4%BD%95%E8%8E%B7%E5%8F%96RefreshToken



```
# ubuntu install
curl -fsSL http://file.tickstep.com/apt/pgp | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/tickstep-packages-archive-keyring.gpg > /dev/null && echo "deb [signed-by=/etc/apt/trusted.gpg.d/tickstep-packages-archive-keyring.gpg arch=amd64,arm64] http://file.tickstep.com/apt aliyunpan main" | sudo tee /etc/apt/sources.list.d/tickstep-aliyunpan.list > /dev/null && sudo apt-get update && sudo apt-get install -y aliyunpan

aliyunpan
login

upload /mnt/chatglm2-6b-32k /

```



- almalinux

sudo curl -fsSL http://file.tickstep.com/rpm/aliyunpan/aliyunpan.repo | sudo tee /etc/yum.repos.d/tickstep-aliyunpan.repo > /dev/null && sudo yum install aliyunpan -y

 \# 这样安装



从网页端获取 refresh_token



aliyunpan



login

 \# 输入刚才的 token

ls

 \# 列出目录



mkdir chatglm2-6b-32k

 \# 创建目录



upload /mnt/chatglm2-6b-32k /

 \# 上传整个文件夹到阿里盘的根目录



upload /mnt/text2vec-large-chinese /

 \# 上传 embeding 模型



pip download -d /mnt/whl protobuf transformers==4.30.2 cpm_kernels torch>=2.0 gradio mdtex2html sentencepiece accelerate

 \# 只下载不安装





\```





\```

1、临时使用

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

2、永久更改pip源

升级 pip 到最新的版本 (>=10.0.0) 后进行配置：

pip install pip -U pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

如果您到 pip 默认源的网络连接较差，临时使用镜像站来升级 pip：

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U

3、离线安装python3及依赖包

将pip3 list的信息生成文档

pip3 freeze >requirements.txt

将requirement.txt文档中列出的模块信息下载到指定目录

pip3 download -r requirements.txt -d /tmp/packages/ #推荐使用 或 pip3 install --download /tmp/packages -r requirements.txt

将下载好的模块copy到离线服务器

pip3 install xxx.tar.gz pip3 install xxx.whl pip3 install xxx.xx #是什么格式就安装什么格式的文件即可。

如果有要安装的包和依赖包有多个，且不知道先装哪个，那么就把这些文件放在一个目录中，然后进入该目录使用下面命令一起安装

pip3 install ./*

批量离线安装requirments.txt中的模块，需要将下载好的模块和requirments.txt都copy到一个目录，然后执行下面的命令

pip3 install --no-index --find-links=/tmp/packages -r requirments.txt

\```



## mega

[mega linux 命令行工具](https://github.com/meganz/MEGAcmd)

- [示例](https://github.com/meganz/MEGAcmd/blob/master/UserGuide.md#login-logout-whoami-mkdir-cd-get-put-du-mount-example)

[mega linux GUI](https://github.com/meganz/MEGAsync)



```

https://mega.io/zh-hans/cmd
	# 下载

https://help.mega.io/zh-hans/installs-apps/desktop-syncing/download-install

wget https://mega.nz/linux/repo/CentOS_7/x86_64/megacmd-CentOS_7.x86_64.rpm && \
yum localinstall "$PWD/megacmd-CentOS_7.x86_64.rpm"

wget https://mega.nz/linux/repo/xUbuntu_22.04/amd64/megacmd-xUbuntu_22.04_amd64.deb && \
sudo apt install "$PWD/megacmd-xUbuntu_22.04_amd64.deb"



mega-cmd
login 1234xxxxx@qq.com

mount
ROOT on /                                                         
INBOX on //in

put /mnt/huggingface/pythia-1.4b-deduped
	# 上传本地文件夹到网盘
	# put /mnt/huggingface/InternLM-SFT

get 
	# 从网盘下载


sync --help
	# 同步文件夹

sync /mnt/huggingface/InternLM-SFT /InternLM-SFT
	# 成功添加同步，原理：.77 同步到 mega,  mega 同步到 windows ，
	# 或着反向
	# sync localpath remotepath 


```





## Cloudflare



### R2对象存储

https://juejin.cn/post/7331584783611281444

```python
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3'

const S3 = new S3Client({
  region: 'auto',
  endpoint: `https://${ACCOUNT_ID}.r2.cloudflarestorage.com`,
  credentials: {
    accessKeyId: ACCESS_KEY_ID,
    secretAccessKey: SECRET_ACCESS_KEY,
  },
})

const input = {
  Body: 'file content',
  Bucket: 'web',
  Key: '1.png',
}

const command = new PutObjectCommand(input)
const response = await S3.send(command)

```



```
结合 Cache API 和 Workers，可对内容进行动态缓存
```



### KV存储

https://fast.v2ex.com/t/969197



### D1 数据库

https://www.cloudflare.com/zh-cn/developer-platform/d1/



基于 SQLite





### Warp

[Warp+ Plus 24PB流量及Zero trust无限流量](https://mailberry.com.cn/2023/07/free-use-warp-plus-24pb-and-zero-trust-unlimitl/)

[Warp 彻底解决 Google IP 定位中国的问题](https://www.v2ex.com/t/800581)



https://developers.cloudflare.com/learning-paths/replace-vpn/



### [Cloudflare tunnel 实现内网穿透SSH,SMB](https://www.nanguoyu.com/cloudflare-tunnel-ssh-smb-web)





### [Cloudflare Tunnel内网穿透](https://bra.live/setup-home-server-with-cloudflare-tunnel/)

[Cloudflare Pro SSH加速](https://hostloc.com/thread-674147-1-1.html)

- ```
  Spectrum是CloudFlare最近推出的新业务，官方的宣传标语是“SPECTRUM — 比常规的Cloudflare多了65,533个端口，为所有应用提供 DDoS保护！”
  Cloudflare Spectrum为全协议反代加速服务，可以为任意 TCP/UDP 应用提供安全防护与加速。普通付费用户仅支持常见应用协议（SSH 、Minecraft，5G免费流量），企业版支持全协议（SSH 、Minecraft、RDP，10G免费流量）。
  
  ucloud的gloabssh不好用吗，还是全免费的，也不用实名，就是要7天跑2M流量，不然就要删除重建
  ```

  



## nmap测试端口

```
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
```







## Get



```javascript
let bent = require('bent')
let get = bent('https://xxxxxx', 'GET', 'json', 200)
let ssss = JSON.stringify(response)
```



```


const express = require('express')
var mysql = require('mysql');
const port = process.argv[2] || 666;


async function getUserids(){
    var connection = mysql.createConnection({
        host:'xxxx',
        user:'xxxx',
        password:'xxxx',
        database:'xxxxx'
    });
    
    connection.connect();
    
    let query = function( sql, values ) {
        return new Promise(( resolve, reject ) => {
            connection.query(sql, values, function (error, results, fields) {
                if (error)  reject( error );
                resolve( results )
            });
        })
    }
    
    row = await query("SELECT xxxxx", [xxx])
    
    connection.end();
    
    return row
}

const app = express()
// http://xxxxx/xxxxx?xxx=xx&xxx=xx
app.get('/gendifficulty', async (req, res) => {
  
    if ( !('AppID' in req.query) || !('KsbaoAppID' in req.query)){
        res.writeHead(300, {"Content-Type": "text/plain"});
        res.write("err\n");
        res.end();
        return
    }

    AppID = req.query['AppID']
    KsbaoAppID = req.query['KsbaoAppID']

    AppID = Number(AppID)
    KsbaoAppID = Number(KsbaoAppID)

    if (Number.isNaN(AppID) || Number.isNaN(KsbaoAppID)) {
        res.writeHead(300, {"Content-Type": "text/plain"});
        res.write("err\n");
        res.end();
        return
    }

    row = await getUserids()

    res.send(row)
  
})

app.listen(port, function() {
  console.log('ok');
})

```



## Post



 request 已弃用，用这个  https://github.com/mikeal/bent



```
express 端

import express from 'express'
import bodyParser from 'body-parser'
import cors from 'cors'
import bent from 'bent'
import { resolve } from 'node:path'
import { pathToFileURL } from 'node:url'

const app = express()

app.use(cors())
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))



app.post('/wenxin/chat_post', async (req, res) => {

    if ( !req.body || !req.body.text ){
        res.writeHead(300, {"Content-Type": "text/plain"})
        res.write("params err\n")
        res.end()
        return
    }

    let text = req.body['text']
})
```





```
  
  let bent = require('bent')
  let formurlencoded = require('form-urlencoded')
   
  let tests = [] 
 
  let json = {
    tests:JSON.stringify(tests)
  }

  let formurlencoded_body = formurlencoded(json)

  let post = bent('http://127.0.0.1:9007', 'POST', 'json', 200)
  let response = await post('/api/verify/verifyTestJson', formurlencoded_body, { 'Content-Type': 'application/x-www-form-urlencoded'})
  
```





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

    //let post = bent('http://xxx:11112', 'POST', 'json', 200)
    let post = bent('http://127.0.0.1:11112', 'POST', 'json', 200)
    let response = await post('/aliyun/ocr', json)



    data = JSON.parse(response).data.test

    let s = JSON.stringify(response)

    console.log(response)

})()
```





```
const post = bent('http://localhost:666', 'POST', 'json', 200) # 返回类型是 json
const response = await post('/gettest', { appename: 'ZC_ZXYJHNKX_YTMJ' })
```





```
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "appEName=ZC_HLXHS_YTMJ&SessionKey=38B0535F89F1A02ED984B7888048D392&idArray=[{"AllTestID":6004390,"ChildTableID":-1,"CptID":459,"Enabled":1},{"AllTestID":6004391,"ChildTableID":-1,"CptID":459,"Enabled":1},{"AllTestID":6004392,"ChildTableID":-1,"CptID":459,"Enabled":1}]" 
http://10.94.183.7:9013/api/test/findAll
http://120.27.142.68:9013/api/test/findAll
```





```javascript
var request = require('request')

module.exports =
{
  name: `getTestbyids`,
  author: `gd`,
  params: {
    appEName: {
      type: 'string',
      remark: ''
    },
    idArray:{
      type: 'string',
      remark: ''
    }
  },
  async handler({appEName, idArray}) {

    

    var data = await new Promise(function (resolve) {

      url = 'http://xxxxx:xx/api/xxxxx'
      request.post(url, {
        'form': {
          SessionKey: "xxxxx",
          appEName: appEName,
          idArray: idArray
        }
      },
      function(err, response, result) {
        if (err || response.statusCode != 200) {
          console.log(url + err + response.statusCode)
          //throw (url + err + response.statusCode)
          return resolve({})
        }
  
        return resolve(result)
      })

    })

    data = JSON.parse(data).data

    // var testids = {}

    // data.forEach(d => {
    //   let key = d.AllTestID + "/" + d.ChildTableID
    //   testids[key] = 0
    // });

    return data
    
    
  },
  remark: ``
}

```





```
    let data = await new Promise(function (resolve) {
      request.post({
        timeout: 6000000,
        url: 'http:xxxxxxxxx',
        form: {
          word, type, enable,
        },
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded;',
        }, callback(erro, response, body) {
          console.log(body);
          if (erro) {
            throw erro;
          }
          resolve(body);
        },
      });
    });
```



### bent



```
const fs = require('fs')
const { promisify } = require('util')
const stream = require('stream')
const pipeline = promisify(stream.pipeline)
const bent = require('bent')

const main = async () => {
  const readable = await bent('https://images.unsplash.com/photo-1595132938692-83ad2c098e47')()
  const writable = fs.createWriteStream('./image.jpg')
  await pipeline(readable, writable)
}

main()
```

```
import bent from "bent";
import { createWriteStream } from "fs";
import { resolve } from "path";
import { pipeline } from "stream";
import { promisify } from "util";

const pipe = promisify(pipeline);

const URL = "http://***/1.txt";

export const run = async () => {
  const readable = (await bent(URL)("")) as NodeJS.ReadableStream;
  const writeable = await createWriteStream(resolve(__dirname, "../2.txt"));

  await pipe(readable, writeable);

  console.log("0");
};
```



```
async function f() {
  let bent = require('bent')
  let formurlencoded = require('form-urlencoded')
  
  let url = `https://api.openai.com`
  
  let json = {
    "model": "text-davinci-003",
    "prompt": "What is the meaning of life?"
  }
  
  let formurlencoded_json = formurlencoded(json)
  
  let post = bent(url, 'POST', 'json', 200)
  try {

    // let response = await post('/v1/completions', formurlencoded_json, { 'Content-Type': 'application/json', 'Authorization': '里填openai key'} )
    let response = await post('/v1/completions', json, { 'Content-Type': 'application/json', 'Authorization': 'Bearer 这里填openai key'} )

    let a = 1

  } catch (e) {
    console.log(e)
  }

  let a = 1
}

f()
```





```
	# 新版好像要自已处理 form-urlencoded 了
	let bent = require('bent')
    let formurlencoded = require('form-urlencoded')
    let mysql = require('./mysql')

    let host = 'localhost:62137'

    async function Convert2GIF(str_base64) {
    
        let url = `http://${host}`

        let json = {
            image_base64: str_base64
        }

        let formurlencoded_json = formurlencoded(json)

        let post = bent(url, 'POST', 'json', 200)
        let response = await post('/Convert2GIF', formurlencoded_json, { 'Content-Type': 'application/x-www-form-urlencoded'})

        if (response.status == 200) {
            return [ response.data, '']
        } else {
            return [null, response.msg]
        }

        return response

    }


    let [str_base64_gif, ms] = await Convert2GIF('aaa')
    if (str_base64 === null) {

        throw 'Error: convert image to GIF fail! ' + ms

    }
```





```
# 参数太长也会出错

( async ()=>{

  let bent = require('bent')
  let _ = require('lodash')

  let host = `xxxx`
  let appename = 'xxxxx'
  
  let json = {
    SessionKey: "xxxx",
    appEName: xxxx
  }

  let url = `http://${host}`

  let post = bent(url, 'POST', 'json', 200)
  let response = await post('/Convert2GIF', json)

  var idArray = response.data

  let arr_chunks = _.chunk(idArray, 10000)

  idArray = [ idArray[0] ]

  idArray = JSON.stringify(arr_chunks[0])


  json = {
      SessionKey: "xxxx",
      appEName: xxxx,
      idArray:xxxx
  }

  var tests = []
  
  let response2 = await post('xxxxx', json)

  tests =tests.concat(response2.data.test)

  

  a = 1


}) ()
```



#### keda



```
// https://blog.csdn.net/sueRimn/article/details/100134349

( async ()=>{

    // https://www.xfyun.cn/doc/words/xf-printed-word-recognition/API.html#%E6%8E%A5%E5%8F%A3%E8%A6%81%E6%B1%82

async function ocr(imgPath) {

    let bent = require('bent')
    let formurlencoded = require('form-urlencoded')
    
    let X_Param = {
        "language": "cn|en",
        "location": "true"
    }
    
    X_Param = Buffer.from(JSON.stringify(X_Param)).toString('base64')
    //X_Param = Buffer.from(X_Param, 'base64').toString('ascii')
    
    let APIKey = "xxxxxx"
    let X_CurTime = parseInt(new Date().getTime() / 1000).toString()
    let X_CheckSum = require('md5')(APIKey + X_CurTime + X_Param)
    
    let headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'X-Appid': "xxxx",
        'X-CurTime': X_CurTime,
        'X-Param': X_Param,
        'X-CheckSum': X_CheckSum
    }
    
    let buffer = require('fs').readFileSync(imgPath)
    let b64 = buffer.toString('base64')
    
    let body = {
        image: b64
    }
    
    let host = 'webapi.xfyun.cn'
    let url = `https://${host}`
    
    let formurlencoded_body = formurlencoded(body)
    
    let post = bent(url, 'POST', 'json', 200)
    let response = await post('/v1/service/v1/ocr/general', formurlencoded_body, headers)

    return response
}


async function ocr2(imgPath) {
    // npm install moment
    // npm install crypto-js

    let bent = require('bent')
    let formurlencoded = require('form-urlencoded')
    let fs = require('fs')

    if (!fs.existsSync(imgPath)) {
        throw `图片不存在 ${imgPath}`    
    }

    let bytes = fs.readFileSync(imgPath)  // 'binary'
    let img_b64 = Buffer.from(bytes).toString('base64')

    let dateFormat = 'ddd, DD MMM YYYY HH:mm:ss'
    let dateString =  new Date().toUTCString() //'Mon, 01 Jan 0001 00:00:01 GMT'
    let date = require('moment').utc(dateString, dateFormat)._i

    let APPId = "xxx"
    let APISecret = "xxx"
    let APIKey = "xxx"

    let host = 'api.xf-yun.com'
    let method = 'POST'
    let path = '/v1/private/s00b65163'

    let url = `https://${host}${path}`

    let signature_origin = `host: ${host}\ndate: ${date}\n${method} ${path} HTTP/1.1`

    let signature_sha = require("crypto-js").HmacSHA256(signature_origin, APISecret)

    let HmacSHA1 = signature_sha.toString()

    signature_sha = require("crypto-js").enc.Base64.stringify(signature_sha)

    let authorization_origin = `api_key="${APIKey}", algorithm="hmac-sha256", headers="host date request-line", signature="${signature_sha}"`

    let authorization = Buffer.from(authorization_origin).toString('base64')

    let values = {
        "host": host,
        "date": date,
        "authorization": authorization
    }

    let urlencode_values = formurlencoded(values)

    let request_url = url + "?" + urlencode_values

    let headers = {'content-type': "application/json", 'host': 'api.xf-yun.com', 'app_id': APPId}

    //headers = JSON.stringify(headers)

    let body = {
        "header": {
            "app_id": APPId,
            "status": 3,
        },
        "parameter": {
            "s00b65163": {
                "category": "mix0",
                "result": {
                    "encoding": "utf8",
                    "compress": "raw",
                    "format": "json"
                }
            }
        },
        "payload": {
            "s00b65163_data_1": {
                "encoding": "png",
                "image": img_b64,
                "status": 3
            }
        }
    }

    let formurlencoded_body = formurlencoded(body)

    body = JSON.stringify(body)

    let benthost = `https://${host}`
    let bentpath = `${path}`+ "?" + urlencode_values

    let post = bent(benthost, 'POST', 'json', 200)
    let response = await post(bentpath, body, headers)

    let text = response.payload.result.text

    text = Buffer.from(text, 'base64').toString()

    fs.writeFileSync('./re.json', text)

    return [signature_origin, signature_sha, authorization_origin, authorization, urlencode_values, request_url, headers, body]

}

let imgPath = './韩语.png'
let imgPath2 = './双栏.bmp'
let imgPath3 = './双栏.jpg'
let imgPath4 = './漏字很多.jpg'

let [signature_origin, signature_sha, authorization_origin, authorization, urlencode_values, request_url, headers, body] = await ocr2(imgPath)

let re = body  // signature_origin + "|" + signature_sha

process.stdout.write(re)

let a = 1

})()




/// python begin

from datetime import datetime
from wsgiref.handlers import format_date_time
from time import mktime
import hashlib
import base64
import hmac
from urllib.parse import urlencode
import os,subprocess
import traceback
import json
import requests

imgeName = './韩语.png'
imgeName2 = './双栏.bmp'

if os.path.exists("./韩语.png"):
    a = 1
else:
    a = 1


'''
appid、apiSecret、apiKey请到讯飞开放平台控制台获取并填写到此demo中；
图像数据，base64编码后大小不得超过4M
'''
# 请到控制台获取以下信息，并填写
APPId = "xxx"
APISecret = "xxx"
APIKey = "xxx"
# 图片位置
with open(imgeName2, "rb") as f:
    imageBytes = f.read()


class AssembleHeaderException(Exception):
    def __init__(self, msg):
        self.message = msg


class Url:
    def __init__(this, host, path, schema):
        this.host = host
        this.path = path
        this.schema = schema
        pass


# calculate sha256 and encode to base64
def sha256base64(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    digest = base64.b64encode(sha256.digest()).decode(encoding='utf-8')
    return digest


def parse_url(requset_url):
    stidx = requset_url.index("://")
    host = requset_url[stidx + 3:]
    schema = requset_url[:stidx + 3]
    edidx = host.index("/")
    if edidx <= 0:
        raise AssembleHeaderException("invalid request url:" + requset_url)
    path = host[edidx:]
    host = host[:edidx]
    u = Url(host, path, schema)
    return u


# build websocket auth request url
def assemble_ws_auth_url(requset_url, method="POST", api_key="", api_secret=""):
    u = parse_url(requset_url)
    host = u.host
    path = u.path
    now = datetime.now()
    date =  format_date_time(mktime(now.timetuple()))
    print(date)
    # date = "Thu, 12 Dec 2019 01:57:27 GMT"
    signature_origin = "host: {}\ndate: {}\n{} {} HTTP/1.1".format(host, date, method, path)
    print(signature_origin) # 'host: api.xf-yun.com\ndate: Mon, 07 Feb 2022 09:05:53 GMT\nPOST /v1/private/s00b65163 HTTP/1.1'

    # out_bytes = subprocess.check_output(["node", "keda2.js"])
    # out_text = out_bytes.decode('utf-8') # 'host: api.xf-yun.com\ndate: Mon, 07 Feb 2022 09:05:53 GMT\nPOST /v1/private/s00b65163 HTTP/1.1'

    #signature_origin = out_text

    signature_origin = signature_origin.encode('utf-8')

    #signature_origin = signature_origin.decode('utf-8')

    signature_sha = hmac.new(api_secret.encode('utf-8'), signature_origin, # .encode('utf-8'),
                             digestmod=hashlib.sha256).digest()
    
    signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8') # 'JJBIEpM9jKzqDpTL9QEFgoqUzSiLb4YUai+MYP576yc='  '3xJqUrRTgpTopAamjDptLvNK5a0d+/iOxu6rf8tg3N0='


    #signature_sha = out_text

    authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
        api_key, "hmac-sha256", "host date request-line", signature_sha)

    #authorization_origin = out_text
    
    authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')

    #authorization = out_text

    print(authorization_origin)
    values = {
        "host": host,
        "date": date,
        "authorization": authorization
    }

    urlencode_values = urlencode(values)

    # urlencode_values = out_text

    re = requset_url + "?" + urlencode_values  # urlencode(values)

    # re = out_text

    return  re


url = 'https://api.xf-yun.com/v1/private/s00b65163'

body = {
    "header": {
        "app_id": APPId,
        "status": 3,
    },
    "parameter": {
        "s00b65163": {
            "category": "mix0",
            "result": {
                "encoding": "utf8",
                "compress": "raw",
                "format": "json"
            }
        }
    },
    "payload": {
        "s00b65163_data_1": {
            "encoding": "png",
            "image": str(base64.b64encode(imageBytes), 'UTF-8'),
            "status": 3
        }
    }
}

body = json.dumps(body)

# out_bytes = subprocess.check_output(["node", "keda2.js"])
# out_text = out_bytes.decode('utf-8')
#body = out_text

request_url = assemble_ws_auth_url(url, "POST", APIKey, APISecret)

headers = {'content-type': "application/json", 'host': 'api.xf-yun.com', 'app_id': APPId}
print(request_url)
response = requests.post(request_url, data=body, headers=headers) # json.dumps(body)
print(response)
# print(response.content)
print("resp=>" + response.content.decode())
tempResult = json.loads(response.content.decode())
finalResult = base64.b64decode(tempResult['payload']['result']['text']).decode()
finalResult = finalResult.replace(" ", "").replace("\n", "").replace("\t", "").strip()
print("text字段Base64解码后=>" + finalResult)

// python end
```



#### form-data

- https://github.com/mikeal/bent/issues/121

```
let FormData = require('form-data')
let bent = require('bent')

     let postData = new FormData()
      postData.append('OperateUserID', userID)
      postData.append('OperateUserName', `${userID}`)
      postData.append('bookID', bookID)
      postData.append('type', 3)
      postData.append('beginpath', `${bookID}/`)
      postData.append('filepath', `小截图/basename`)
      postData.append('fileName', basename)
      postData.append('fileName', basename)
      postData.append('file', fs.createReadStream(fullpath))
      
      let post = bent('http://xxxx:xxxx', 'POST', 'json', 200)
      let response = await post('/api/xxxxx', postData, postData.getHeaders())

      if (response.status == 200) {
        let b = 1
      } else {
        return this.msg(301, `${fullpath} ${response.msg}`)
      }
```



#### json

```
async function chat(content_test, content_book) {

    let json = {
        "come_from": "xxx",
        "question": content_test,
        "text":content_book, 
        "model": "gpt-4-1106-preview"
    }

    return new Promise(async function (resolve, reject) {
        console.log(`triple AiExplain: ${content_test}\n${content_book}`)
        
        let bent = require('bent')
        let post = bent("https://xxx.xxx.top", 'POST', 'json', 200)

        let response = await post('/all/getAnswer', JSON.stringify(json), { 'Content-Type': "application/json;chart-set:utf-8" })

        if (response.answer && response.token > 0) {
            return resolve([response.answer, ''])
        } else {
            return resolve([null, JSON.stringify(response)])
        }
    })
}
```





#### src

```
This is how the lib was designed. You should pass to bent all the statuses the server might respond:

const client = bent(200,201,202,203,204,301,302...);
This not an issue, but rather a design decision.
```



#### pipe stream

```
const fs = require('fs')
const { promisify } = require('util')
const stream = require('stream')
const pipeline = promisify(stream.pipeline)
const bent = require('bent')

const main = async () => {
  const readable = await bent('https://images.unsplash.com/photo-1595132938692-83ad2c098e47')()
  const writable = fs.createWriteStream('./image.jpg')
  await pipeline(readable, writable)
}

main()
```



#### 文心

```
(async () => {
    let bent = require('bent')
    let post = bent("https://xxx.co", 'POST', 'json', 200)
    
    let response = await post('/teach/getAnswer', JSON.stringify({"userid":123,"question":"你是谁"}), { 'Content-Type': "application/json;chart-set:utf-8" })

    if (response.status == 0) {
        return [response.data, '']
    } else {
        return [null, response.msg]
    }
})()
```





### axios



#### 通过代理发送请求

```
const axios = require('axios')
const { SocksProxyAgent } = require('socks-proxy-agent')

async function sendPostRequestThroughSocks5Proxy() {
  try {
    const data = {
        "model": "text-davinci-003",
        "prompt": "What is the meaning of life?"
    };

    const proxyUrl = 'socks5://127.0.0.1:57882'
    const proxyAgent = new SocksProxyAgent(proxyUrl)

    const config = {
      method: 'post',
      url: 'https://api.openai.com/v1/completions',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 这里填openai key'
      },
      data: data,
      httpAgent: proxyAgent,
      httpsAgent: proxyAgent,
    };

    const response = await axios(config)
    console.log(response.data)
  } catch (error) {
    console.error(error)
  }
}

sendPostRequestThroughSocks5Proxy()
```



### node-fetch

[node-fetch](https://www.npmjs.com/package/node-fetch)



```
npm install node-fetch

import fetch from 'node-fetch'

const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method:"post", 
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer api key here"
    },
    body: JSON.stringify({
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "你会说中文吗"}]
    })
})

try {
	for await (const chunk of response.body) {
		console.dir(JSON.parse(chunk.toString()))
	}
} catch (err) {
	console.error(err.stack)
}

```



#### 流式输出



##### 后端



```
import OpenAI from 'openai';

const openai = new OpenAI({
    apiKey:"",
    baseURL:"http://xxx.77:7999/to/v1"
});

async function main() {
  const stream = await openai.chat.completions.create({
    model: 'gpt-4',
    messages: [{ role: 'user', content: 'Say this is a test' }],
    stream: true,
  });
  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
}

main();
```





```

// npm install node-fetch
// npm i express body-parser cors --save

// curl -H Accept:text/event-stream http://localhost:2052/t

import fetch from 'node-fetch'
import { createWriteStream } from 'node:fs'
import { pipeline } from 'node:stream'
import { promisify } from 'node:util'

const streamPipeline = promisify(pipeline)

import express from 'express'
import bodyParser from 'body-parser'
import cors from 'cors'

const app = express()

app.use(cors())
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))

app.get('/t', async (req, res) => {
    const headers = {
        'Content-Type': 'text/event-stream',
        'Connection': 'keep-alive',
        'Cache-Control': 'no-cache'
    }
    res.writeHead(200, headers)

    const response = await fetch('https://api.openai.com/v1/chat/completions', {
        method: "post",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer api_here"
        },
        body: JSON.stringify({
            "model": "gpt-3.5-turbo",
            "messages": [{ "role": "user", "content": "你会说中文吗" }],
            "stream": true
        })
    })

    streamPipeline(response.body, res)
    // curl -H Accept:text/event-stream http://et.com:2052/t  成功接收到流
})

app.get('/t2', async (req, res) => {
    const headers = {
        'Content-Type': 'text/event-stream',
        'Connection': 'keep-alive',
        'Cache-Control': 'no-cache'
    }
    res.writeHead(200, headers)

    const response = await fetch('http://et.com:8880/v1/chat/completions', {
        method: "post",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer api_key"
        },
        body: JSON.stringify({
            "model": "gpt-4",
            "messages": [{ "role": "user", "content": "你会说中文吗" }],
            "stream": true
        })
    })

    // try {
    //     for await (const chunk of response.body) {
    //         let str = Buffer.from(chunk).toString('utf8')
    //         let matches = str.matchAll(/(\{\"id\"\:.+?\})\n\n/g)
    //         let arr = Array.from(matches)
    //         if (arr.length > 0) {
    //             for (let ar of arr) {
    //                 let jstr = ar[1]
    //                 let j = JSON.parse(jstr)
    //                 let { delta, finish_reason } = j.choices[0]
    //                 if (delta.content) {
    //                     console.log(`${delta.content} `)
    //                 }
    //             }
    //         }
    //         //fs.writeFileSync('./lines', str, {encoding:'utf8', flag:'w'} )
    //     }
    //     console.log(`\n`)
    // } catch (err) {
    //     console.error(err.stack)
    // }

    streamPipeline(response.body, res)
    // curl -H Accept:text/event-stream http://et.com:2052/t2  成功收到流
})

let port = 2052
app.listen(port, () => {
    console.log(`service listening at http://localhost:${port}`)
})

```





##### 前端

```
// c.mjs
import fetch from 'node-fetch'
import fs from 'fs'

const response = await fetch(`http://127.0.0.1:2052/t`, { method:"get"})

try {
	for await (const chunk of response.body) {
        let str = Buffer.from(chunk).toString('utf8')
        let matches = str.matchAll(/(\{\"id\"\:.+?\})\n\n/g)
        let arr = Array.from(matches)
        if (arr.length > 0) {
            for (let ar of arr) {
                let jstr = ar[1]
                let j = JSON.parse(jstr)
                let { delta, finish_reason } = j.choices[0]
                if (delta.content) {
                    console.log(`${delta.content} `)
                }
            }
        }
        //fs.writeFileSync('./lines', str, {encoding:'utf8', flag:'w'} )
	}
    console.log(`\n`)
} catch (err) {
	console.error(err.stack)
}
```





```
import fetch from 'node-fetch'
import {createWriteStream} from 'node:fs'
import {pipeline} from 'node:stream'
import {promisify} from 'node:util'

const streamPipeline = promisify(pipeline)

const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method:"post", 
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer api_key here"
    },
    body: JSON.stringify({
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "你会说中文吗"}],
        "stream":true
    })
})

await streamPipeline(response.body, createWriteStream('./out.txt'))

```



[Server-Sent Events in Node.js to Build a Realtime App](https://www.digitalocean.com/community/tutorials/nodejs-server-sent-events-build-realtime-app)

```


mimetype='text/event-stream'
```



#### 文心

```
// 必须是 .mjs
import fetch from 'node-fetch'

const response = await fetch('https://xxx.co/teach/getAnswer', {
    method:"post", 
    headers: {
        "Content-Type": "application/json;chart-set:utf-8",
    },
    body: JSON.stringify({"userid":123,"question":"你是谁"})
})

try {
	for await (const chunk of response.body) {
		console.dir(JSON.parse(chunk.toString()))
	}
} catch (err) {
	console.error(err.stack)
}
```



### 浏览器中的 fetch

#### 流式输出

```
// 不知道为什么，流式输出并没有成功
const response = await fetch('http://et.com:8880/v1/chat/completions', {
      method: "post",
      headers: {
        "Content-Type": "application/json",
        "accept": `text/event-stream`,
        "Authorization": "Bearer api_key"
      },
      body: JSON.stringify({
        "model": "gpt-4",
        "messages": [{ "role": "user", "content": message }],
        "stream": true
      })
    })
    //"你会说中文吗"
    const reader = response.body.getReader();

    while (true) {
      const { value, done } = await reader.read();
      if (done) break;

      chunk = new TextDecoder().decode(value);

      let matches = chunk.matchAll(/(\{\"id\"\:.+?\})\n\n/g)
      let arr = Array.from(matches)
      if (arr.length > 0) {
        for (let ar of arr) {
          let jstr = ar[1]
          let j = JSON.parse(jstr)
          let { delta, finish_reason } = j.choices[0]
          if (delta.content) {
            text += delta.content
            console.log(`${delta.content} `)
          }
        }
      }
```



#### 文心

```
curl --location --request POST 'https://xxx.co/teach/getAnswer' \
--header 'Content-Type: application/json;chart-set:utf-8' \
--data-raw '{"userid":123,"question":"你是谁"}'


// fetch in browser
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json;chart-set:utf-8");

var raw = "{\"userid\":123,\"question\":\"你是谁\"}";

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://xxx.co/teach/getAnswer", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```



## 两条sql 语句写一起



```javascript

'use strict'

const request = require('request');

module.exports = {

  params: {
    word: {
      type: 'String',
      remark: 'xx'
    }
  },
  remark: '',
  action: async function (req, res) {
    let { word, type, testID, childTestID, appID, enable } = req.body;

    let sql = `
    insert into xx.xx(appID,testID,childTestID,word,type)values(?,?,?,?,?);
    insert into xx.xx(word,type,\`enable\`)values(?,?,?) 
    on duplicate key update 
    type=values(type),
    \`enable\`=values(\`enable\`);
    `;

    await new Promise((resolve) => {
      this.DB.query(sql, [appID, testID, childTestID, word, type, word, type, enable], (erro, result) => {
        if (erro) {
          res.send(201, erro.message);
          return;
        }
        resolve(result);
      });
    });
```



# live debug 



## vscode 远程调试

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "node",
            "request": "launch",
            "name": "Launch Program",
            "skipFiles": [
                "<node_internals>/**"
            ],
            "program": "${workspaceFolder}/server.js",
            "runtimeExecutable": "/usr/local/bin/node14"
        }
    ]
}

https://matpool.com/supports/doc-vscode-connect-matpool/
    Remote Development 安装插件
    VS Code 远程连接矩池云机器教程
# train.py 添加命令行参数，并用vscode 远程调试K80 服务器上的 conda 环境(ctrl+shift+p 选conda的python)，vscode 中修改train.py 在main 函数下加入：
```





```
# https://medium.com/the-node-js-collection/live-debugging-node-js-apps-at-the-command-line-cd5b58f883e1

# http://www.ruanyifeng.com/blog/2018/03/node-debugger.html

# https://juejin.cn/post/6844904098618163207
	# VSCode 远程调试

# https://zhuanlan.zhihu.com/p/100092504

	# http://www.baiguangnan.com/2019/03/13/vscoderemotedebugnodejs/

		# vscode node remote debug

# https://nodejs.org/api/debugger.html
node inspect -p 9436  # 进程ID
	# help # 打印帮助

	# debug> setBreakpoint('main.js', 4, 'num < 0')  # 条件断点

list(100): shows the first 100 lines of code
setBreakpoint(17): sets a breakpoint on the 17th line
clearBreakpoint(17): removes a breakpoint on the 17th line
exec body: evaluates the body variable and prints out its result
cont: continues the program's execution

Resume execution(continue): c or cont
Next line: n or next
Step into a function: s or step
Step out: o or out
Set breakpoint: sb or setBreakpoint
Clear breakpoint: sc or clearBreakpoint

watch('counter')



# https://betterprogramming.pub/how-to-debug-using-node-js-built-in-debugger-f3ab3ba6e7c8
	# Debug Using Node.js’s Built-In Debugger
	
setBreakpoint('xxxxxx.js', 45)
setBreakpoint('xxxxxx.js', 142)
clearBreakpoint('xxxx.js', 45)

# 可能是这一句的错误
let retSaveExam = await this.services.saveExamgather({examgahters})

n # 下一行

break in file:////yingedu/project_test/ksbaiexam/http/api/submit.js


# https://zhuanlan.zhihu.com/p/98571113
	# chrome 远程调试node


node14 --inspect-brk=0.0.0.0:9229 server.js

chrome://inspect/#devices

```



## chrome 远程调试



- https://zhuanlan.zhihu.com/p/338287139

1. chrome 打开： chrome://inspect
2. 点击 Open dedicated DevTools for Node
3. xxxx.77:9229  # Add connection # 这样只要服务器脚本运行后就后自动进入调试状态

```
# centos7 待调试脚本（非服务端，跑一次就结束的脚本）
node --inspect-brk=xxx.77:9229 insert.cjs # 指定IP端口

```



## vue 在vscode 下断点


- https://cn.vuejs.org/v2/cookbook/debugging-in-vscode.html

  > vscode 安装插件 JavaScript Debugger
  >
  > ```
  > 新建 launch.json， 弹出的选项选择 chrome
  > 重点是：先在终端 npm run dev，看它的端口是什么，下面的url 端口就填什么，然后在vscode F5，会打开浏览器, 就可以在vscode 下断了
  > {
  >     "version": "0.2.0",
  >     "configurations": [
  >         {
  >             "type": "chrome",
  >             "request": "launch",
  >             "name": "vuejs: chrome",
  >             "url": "http://localhost:8080",
  >             "webRoot": "${workspaceFolder}/src",
  >             "sourceMapPathOverrides": {
  >                 "webpack:///src/*": "${webRoot}/*"
  >             },
  >             "resolveSourceMapLocations": [
  >                 "${workspaceFolder}/**",
  >                 "!**/node_modules/**"
  >             ]
  >         }
  >     ]
  > }
  > ```
  >
  > ```
  > vue.config.js # 注意配了这个 F5 后断点才真的断了下来
  > 
  > module.exports = {
  >    runtimeCompiler: true,
  >     configureWebpack: {
  >         devtool: 'source-map'
  >     }
  > }
  > 
  > 
  > var titme = Date.now();
  > var d = {
  > //可在浏览器中调试 说明： https://cn.vuejs.org/v2/cookbook/debugging-in-vscode.html
  > configureWebpack: {
  > devtool: 'source-map',
  > output: { // 输出重构  打包编译后的 文件名称  【模块名称.版本号.时间戳】
  > filename: `js/[name].${titme}.js`,
  > chunkFilename: `js/[name].${titme}.js`
  > },
  > },
  > // 是否在构建生产包时生成 sourceMap 文件，false将提高构建速度
  > productionSourceMap: false,
  > // // 设置生成的 HTML 中 <link rel="stylesheet"> 和 <script> 标签的 crossorigin 属性（注：仅影响构建时注入的标签）
  > publicPath: './', // 设置打包文件相对路径
  > // 输出文件目录
  > outputDir: "webv2",
  > }
  > console.log(`${process.env.NODE_ENV}`)
  > if( process.env.NODE_ENV.match(/build/g) ){ 
  > delete d.configureWebpack.devtool
  > d.productionSourceMap = false;
  > }
  > module.exports = d
  > ```
  >
  > vue 在vscode 下断点
  >
  > file --> preferences --> setting 找到eslint ，找到几个  check box 勾上



- https://www.bbwho.com/visual-studio-codeduan-dian-diao-shi-vue/



## v8 profiler

- https://fed.taobao.org/blog/taofed/do71ct/nodejs-memory-leak-analyze/

```
v8 prof
使用 V8 自带的 profiler 功能，分析 JavaScript 各个函数的消耗和 GC 部分。

npm install profiler
node --prof xxx.js
会生成 xxxx-v8.log，之后使用工具转换成可读的。

npm install tick
node-tick-processor xxxx-v8.log
就可以查看相关的数据了。
```



## v8 source map

- https://github.com/evanw/node-source-map-support



# gpt api

- https://github.com/waylaidwanderer/node-chatgpt-api



# Syntax

- https://www.ruanyifeng.com/blog/2020/08/how-nodejs-use-es6-module.html



```
node --input-type=module
```





## commonjs

```
import 导入的变量无论是否为基本类型都是引用传递
module.exports 很像 export default 所以 ES6模块 可以很方便兼容 CommonJs
```



### .mjs .cjs



```
.mjs 和 .cjs 后缀名保证分别解析为 ECMAScript modules 和 ComandJS 
```





```
// ffmpeg.mjs
import { execa } from 'execa'
import path from 'path'
import { dirname } from 'path'
//global.__dirname = process.cwd()
import { fileURLToPath } from 'url'
const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

export default {

    extractSubtitle: async function (vdpath, type, nth) {

        try {

            // let args = `ffmpeg -i ${vdpath} -y -map 0:s:${nth} ${path.join( __dirname, 'tmp.srt' )}` // write file
            let cmd = `ffmpeg -i ${vdpath} -y -map 0:s:${nth} -f srt pipe:1`   // write stdout

            let childProcess = execa(cmd, {shell:true, 'encoding': 'utf8'})
            childProcess.stdout.pipe(process.stdout)
            let { stdout } = await childProcess

            return { srt:stdout, msg:'' }

        } catch(err) {
           return { srt:null, msg : err }
        }
    },
    extractAudio: async function (vdpath, type, begin_time, end_time) {

        try {

            let cmd = `ffmpeg -i ${vdpath} -y -vn -ss ${begin_time} -to ${end_time} -acodec mp3 -ar 44100 -ac 2 -b:a 192k -f ${type} pipe:1`   // write stdout

            let childProcess = execa(cmd, {shell:true})
            childProcess.stdout.pipe(process.stdout)
            let { stdout } = await childProcess

            return { au: Buffer.from(stdout) }

        } catch(err) {
           return { audi:null}
        }

        return { au:1 }
    }

}

// test.js
let { default: libff } = await import('./ffmpeg.mjs')
let { srt: str_jp, msg:msg_jp } = await libff.extractSubtitle(vdpath, 'srt', 2)  // the nth subtitle stream
let { srt: srt_chs, msg:msg_chs } = await libff.extractSubtitle(vdpath, 'srt', 0)
```





```
// ff.mjs 必须是 .mjs
// node --experimental-modules .\ff.mjs  成功运行
import {execa} from 'execa';
const {stdout} = await execa('dir', []);
console.log(stdout);
console.log(111)
```

- https://github.com/chrisveness/geodesy/issues/79
  
- 各种示例
  
- https://juejin.cn/post/6972006652631318564

  - Node 最新 Module 导入导出规范

    

- https://zhuanlan.zhihu.com/p/337796076
  
  - ES Modules 的加载、解析和执行都是异步的



- https://depth-first.com/articles/2019/01/17/debugging-es-modules-with-mocha-in-vs-code/

```
服务器端开发用require/exports ，浏览器端使用import/export


方式二  通过Node原生支持ES Module

步骤一、 更改js文件后缀为.mjs

步骤二、 import js的时候，如import './core';不能省略后缀名，需要写成import './core.mjs';

执行：node --experimental-modules ./bin/index.mjs

步骤三、 由于是实验性质特性，所以需要配置开启 --experimental-modules，否则会报如下错误

```



```
var exec = require('child_process').exec;  // 出错
	//   "type": "commonjs",  // package.json 加上这一句
	
let execa = import('execa')  // 这样可以
	// 出错：Must use import to load ES Module
```



```
node --experimental-modules ./bin/www

launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
          "type": "node",
          "request": "launch",
          "name": "Launch Program",
          "program": "${workspaceFolder}\\bin\\www",
        }
    ]
}

```



###  dir.mjs

```javascript
import { eachFileFilterSync } from 'rd'
import path from 'path'

export default {

    allmkv : function(dir, filter) {

        var paths = []

        // 目录下的所有文件名
        eachFileFilterSync(dir, /\.mkv$/, function (fullpath, stats) {

            let basename = path.basename(fullpath)
            if (filter != undefined && fullpath.indexOf(filter) != -1) {
                paths.push(fullpath)
            } else if (filter == undefined ) {
                paths.push(fullpath)
            }
            
        })

        return paths

    }

}

let { default: libdir } = await import('./dir.mjs')
let mkvs = libdir.allmkv(root, 'Pokemon')
```



### cjs 导入mjs



```javascript
// es.mjs
let foo = {name: 'foo'};
export default foo;

export let a = 1

// cjs
let { execa } = await import('execa')  // execa 库这样导入

import('./es').then((res)=>{
  console.log(res) // { get default: {name: 'foo'}, a: 1 }
})
```



### mjs 导入cjs



```javascript
// config.js
module.exports = {

    host:'xxx.77',
    passwd:'xxx.com',
    port: '5432'
}

// insert.mjs
let { default:config }  = await import('./config.js')


// 跨平台写法， resolve 里的 . 代表 程序运行的目录
import { resolve } from 'node:path'
import { pathToFileURL } from 'node:url';
let { default:config }  = await import(pathToFileURL(resolve('.', 'config.js')))


import { pathToFileURL } from 'node:url';
let { default:config }  = await import(pathToFileURL(`D:\\GitHub\\echodict\\chatgpt_server\\config.js`))
	// windows 导入需要特殊处理

```



### mjs 导入标准库

```javascript
import pg from 'pg'
let { Pool, Client } = pg
// import { Pool, Client } from 'pg'  // 原 cjs 的导入方式是这样

import path from 'path'
```





### mjs 导入 json

```
// 真 json 可以，原来的 module.exports = { 还要另相办法
let a = resolve('.', 'config.js')
import { pathToFileURL } from 'node:url';
let d = pathToFileURL(a)
let c = await import(d, {
    assert: { type: "json" },
})


import { pathToFileURL } from 'node:url';
let { default:config }  = await import(pathToFileURL(`D:\\GitHub\\echodict\\chatgpt_server\\config.js`))
	// 这样可以

```





### mjs 使用 require

```
// 需要 node 20
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);

// sibling-module.js is a CommonJS module.
const siblingModule = require('./sibling-module'); 
```





### export default 用this互引用

```javascript
export default {

	funtion a {
	
	},
	function b {
		this.a()
	}
}
```



### 自定义包

```
npm i ws # 安装这个包来观察包的组织结构

目录结构
- ws
	- lib        # 这里放所有 js 实现文件
    index.js     # 导出符号，cjs 方式 
	wrapper.mjs  # 导出符号，mjs 方式
    package.json # 指定导出文件：index.js 和 wrapper.mjs
    
```



```
index.js
'use strict';

const WebSocket = require('./lib/websocket');

WebSocket.createWebSocketStream = require('./lib/stream');
WebSocket.Server = require('./lib/websocket-server');
WebSocket.Receiver = require('./lib/receiver');
WebSocket.Sender = require('./lib/sender');

WebSocket.WebSocket = WebSocket;
WebSocket.WebSocketServer = WebSocket.Server;

module.exports = WebSocket;
```



```
wrapper.mjs
import createWebSocketStream from './lib/stream.js';
import Receiver from './lib/receiver.js';
import Sender from './lib/sender.js';
import WebSocket from './lib/websocket.js';
import WebSocketServer from './lib/websocket-server.js';

export { createWebSocketStream, Receiver, Sender, WebSocket, WebSocketServer };
export default WebSocket;
```



```
package.json
{
  "name": "ws",
  "version": "8.12.0",
  "description": "Simple to use, blazing fast and thoroughly tested websocket client and server for Node.js",
  "keywords": [
    "HyBi",
    "Push",
    "RFC-6455",
    "WebSocket",
    "WebSockets",
    "real-time"
  ],
  "homepage": "https://github.com/websockets/ws",
  "bugs": "https://github.com/websockets/ws/issues",
  "repository": "websockets/ws",
  "author": "Einar Otto Stangvik <einaros@gmail.com> (http://2x.io)",
  "license": "MIT",
  "main": "index.js",
  "exports": {
    ".": {
      "import": "./wrapper.mjs",
      "require": "./index.js"
    },
    "./package.json": "./package.json"
  },
  "browser": "browser.js",
  "engines": {
    "node": ">=10.0.0"
  },
  "files": [
    "browser.js",
    "index.js",
    "lib/*.js",
    "wrapper.mjs"
  ],
  "scripts": {
    "test": "nyc --reporter=lcov --reporter=text mocha --throw-deprecation test/*.test.js",
    "integration": "mocha --throw-deprecation test/*.integration.js",
    "lint": "eslint --ignore-path .gitignore . && prettier --check --ignore-path .gitignore \"**/*.{json,md,yaml,yml}\""
  },
  "peerDependencies": {
    "bufferutil": "^4.0.1",
    "utf-8-validate": ">=5.0.2"
  },
  "peerDependenciesMeta": {
    "bufferutil": {
      "optional": true
    },
    "utf-8-validate": {
      "optional": true
    }
  },
  "devDependencies": {
    "benchmark": "^2.1.4",
    "bufferutil": "^4.0.1",
    "eslint": "^8.0.0",
    "eslint-config-prettier": "^8.1.0",
    "eslint-plugin-prettier": "^4.0.0",
    "mocha": "^8.4.0",
    "nyc": "^15.0.0",
    "prettier": "^2.0.5",
    "utf-8-validate": "^6.0.0"
  },
  "__npminstall_done": true,
  "_from": "ws@8.12.0",
  "_resolved": "https://registry.npmmirror.com/ws/-/ws-8.12.0.tgz"
}
```



#### 生成包

- https://cloud.tencent.com/developer/article/1485591





### 异步转同步

- https://blog.kaciras.com/article/22/convert-async-to-sync-in-node

- https://github.com/Kaciras/deasync

- https://github.com/nodejs/node/issues/40898

  ```
  vm.runInThisContext runs a script and therefore does not support top level await. if you want to use that you'll need to use the experimental vm.Module api. the repl is just transpiling code with top level await into async functions.
  ```

  

```
const { deasync } = require("@kaciras/deasync");
const { performance } = require('perf_hooks')

const sleep = deasync((timeout, done) => {
    (async ()=>{
        let { default:wrapper } = await import('./wrapper.mjs')  # 成功执行
        let { name } = wrapper
        done(null, "wake up!")
    })()
});

console.log("Timestamp before: " + performance.now());
let re = sleep(1000)
console.log("Timestamp after: " + performance.now());
```





```
cnpm install @kaciras/deasync

const { deasync } = require("@kaciras/deasync");
const { performance } = require('perf_hooks')

const sleep = deasync((timeout, done) => {
	setTimeout(() => done(null, "wake up!"), timeout);
});

console.log("Timestamp before: " + performance.now());
console.log(sleep(1000));
console.log("Timestamp after: " + performance.now());
```







```
// 些方法是开启另一个进程，并等待它结束，不好用

const { execSync } = require('child_process')

const code = `
const { stdout } = require('process')
const dns = require('dns')
dns.lookup('www.baidu.com', (err, address, family) => {
  stdout.write(address)
})
`

console.log('start')

const lookupResult = execSync('node', { input: code })
console.log(lookupResult.toString()) // 结果

console.log('end')
```



### vm替代eval

- https://stackoverflow.com/questions/34160216/how-to-retrieve-async-results-from-a-node-js-vm-script-using-es7-syntax

- https://zhuanlan.zhihu.com/p/128090873
- https://nodejs.org/api/vm.html#modulelinklinker
- https://github.com/pierrec/node-eval
- https://blog.csdn.net/qq_42709514/article/details/121925095 vm2 jsdom
- https://github.com/semlinker/node-deep/blob/master/module/%E6%B7%B1%E5%85%A5%E5%AD%A6%E4%B9%A0%20Node.js%20Module.md#nodejs-vm
- https://fed.taobao.org/blog/taofed/do71ct/nodejs-memory-leak-analyze/
- https://github.com/agracio/edge-js/issues/163  edge-js 如何使用高版本的 node



```

# 真的完全解决问题了

// npm config set python D:\usr\Python38\python.exe
// npm install @kaciras/deasync  // 依赖 node-gyp https://github.com/nodejs/node-gyp
// npm install franc

const { deasync } = require("@kaciras/deasync")

async function vmrun(code, params, callback) {

    let imports = params.imports
    for (let model of imports) {
        params[model] = await import(model)
    }

    const vm = require('vm')
    const options = {}
    const { timeout = 120 * 1000, breakOnSigint = true } = options
    const script = new vm.Script(`(async()=>{${code}})()`);
    script.runInContext(vm.createContext({
        ...params,
        callback
    }), {
        timeout,
        breakOnSigint,
    })
}

// 同步运行，在 vm 里跑传入的 nodejs 代码, 约定代码里调用 callback(null, { msg:'hi,,,' }) 来返回结果
const vmrunSync = deasync((code, params, callback) => {
    vmrun(code, params, callback)
})


let code = `
    console.log(fs)  // fs 是事先 import 好的模块，这里可以直接用  所有可用参数都在这里展开了：  ...params
    console.log('hello, from vm')
    return callback(null, { msg:'hi,,,' })
`

let re = vmrunSync( code, { imports: ['fs'] } ) // deasync 的作用是去掉了最最外层的 await
```







```

# 这个好 好像完全解决问题了
(async()=>{

  // npm config set python D:\usr\Python38\python.exe
  // npm install @kaciras/deasync  // 依赖 node-gyp https://github.com/nodejs/node-gyp
  // npm install franc

  const { deasync } = require("@kaciras/deasync")

  const syncify = deasync((code, params, done) => {
    (async ()=>{
      const vm = require('vm')
      const { timeout = 120 * 1000, breakOnSigint = true } = {}
      const script = new vm.Script(`(async()=>{${code}})()`)
      script.runInContext(vm.createContext({
        ...params,
        done,
      }), {
        timeout,
        breakOnSigint,
      })

    })()
  })
  
  let c = syncify(`
    result = 1
    console.log(msg)
    fs.writeFileSync('hi.txt', 'hi, from vm!', {encoding:'utf8', flag:'w'} )
    lang = francAll('Alle menslike wesens word vry', { only: ['jpn', 'cmn', 'eng'] })
    done(null, {result, lang})
  `, { msg:'hi, from vm!', fs : await import ('fs'), ... await import('franc') })

  async function runScript(code, context = {}, options = {}) {
      return new Promise((resolve, reject) => {
        const vm = require('vm')
        const { timeout = 120 * 1000, breakOnSigint = true } = options;
        const script = new vm.Script(`(async()=>{${code}})()`);
        script.runInContext(vm.createContext({
          ...context,
          resolve,
          reject,
        }), {
          timeout,
          breakOnSigint,
        });
      });
  }
  
  //let { franc, francAll } = await import('franc')
  
  let re = await runScript(`
    result = 1
    console.log(msg)
    fs.writeFileSync('hi.txt', 'hi, from vm!', {encoding:'utf8', flag:'w'} )
    lang = francAll('Alle menslike wesens word vry', { only: ['jpn', 'cmn', 'eng'] })
    resolve({result, lang})
    `, 
    { msg:'hi, from vm!', fs : await import ('fs'), ... await import('franc') })  // 利用 context 传参


  let a = 1

  })()
  
```





```

# vm 内部成功 hook vm 外部的 promise 执行

const vm = require('vm')

const context = vm.createContext({
  require,
  console
})

vm.runInContext(`
  const ah = require('async_hooks')

  ah.createHook({
    init (asyncId, type, triggerAsyncId, resource) {
      if (type === 'PROMISE') {
        console.log('I stole a promise from outside my context!', resource)
      }
    }
  }).enable()
`, context)

Promise.resolve()

```





```
const vm = require('vm')  # 如果这里要 import 可以用异步转同步

async function add(n) {
    
    return n + 1
}

let sandbox = {
  add: add,
  number: 10
};

const code = `
    (async ()=>{
        await import('fs')
        result = await add(number)
    })()
`
const script = new vm.Script(code)
let ctx = vm.createContext(sandbox)
script.runInContext(ctx)
```





```
var code = `
var fn = () => {}
I = 100; while(I--) { fn(); }
`;

const vm = require('vm');
const context = vm.createContext();
const script = new vm.Script(code);

console.time('vm');
script.runInContext(context);
console.timeEnd('vm');
```



```
// https://stackoverflow.com/questions/34160216/how-to-retrieve-async-results-from-a-node-js-vm-script-using-es7-syntax


(async()=>{

const vm = require('vm')

async function runScript(code, context = {}, options = {}) {
    return new Promise((resolve, reject) => {
      const { timeout = 120 * 1000, breakOnSigint = true } = options;
      const script = new vm.Script(`(async()=>{${code}})()`);
      script.runInContext(vm.createContext({
        ...context,
        resolve,
        reject,
      }), {
        timeout,
        breakOnSigint,
      });
    });
}

let re = await runScript('result = 1; resolve();')

let a = 1

})()
```



## babel

```
// npm install --save @babel/runtime@latest
const Mdict = require('js-mdict')
	// 这项目没babel 就出错
const dict = new Mdict.default('./ECD.mdx')
let d = dict.lookup('red')
```





## typeof



```javascript
            if (typeof content == 'object') {

            } else if (typeof content == 'string') {
                var j = { "title":title, "content":content, childs:[] }
                
            }
```



## global 



global 是内置的全局对象，任意地方可用（可以把任意东西装进出，制造一个合局入口）



## 三目运算符



```javascript
# 连续判断
	const color = d.added ? 'green' :
        d.removed ? 'red' : 'grey'
```



## !!

```javascript
const scale = !!options.full ? "scale=1280:720,setsar=1:1":"scale=640:360,setsar=1:1";

!!是一个逻辑操作，不论它的后面接的是什么数值，它的结果会被强制转换成bool类型，之所以用两个感叹号，主要是为了让结果不会逻辑反过来
```



## ...



array, json 展开

```javascript
function f(v,w,x,y,z){ }
var args = [2,3]
f(1,...args,4,...[5]) # args 展开成 2, 3
```



## sign

```
	# 标签可以像for 一样 break
	getAuthorize:
    {
      const dict = await xxx
      if (dict['0'] !== undefined) {
        break getAuthorize;
    }
```



## 函数偷梁换柱

```
// 解决重复点击路由报错的BUG
import router from './router'
const originalPush = router.prototype.push
router.prototype.push = function push(location) {
  return originalPush.call(this, location).catch((err) => {
   console.log(err)
  })
}
```



## 还可以样这定义变量

```
const { timeout = 120 * 1000, breakOnSigint = true } = {}
```





## 定义属性

```
#　D:\GitHub\node-14.21.1\lib\repl.js

function REPLServer(prompt,
                    stream,
                    eval_,
                    useGlobal,
                    ignoreUndefined,
                    replMode) {
  if (!(this instanceof REPLServer)) {
    return new REPLServer(prompt,
                          stream,
                          eval_,
                          useGlobal,
                          ignoreUndefined,
                          replMode);
  }

  ObjectDefineProperty(this, 'inputStream', {
    get: pendingDeprecation ?
      deprecate(() => this.input,
                'repl.inputStream and repl.outputStream are deprecated. ' +
                  'Use repl.input and repl.output instead',
                'DEP0141') :
      () => this.input,　　// 当作函数直接执行
    set: pendingDeprecation ?
      deprecate((val) => this.input = val,
                'repl.inputStream and repl.outputStream are deprecated. ' +
                  'Use repl.input and repl.output instead',
                'DEP0141') :
      (val) => this.input = val,  // 代参数的函数执行
    enumerable: false,
    configurable: true
  });
```



## 看情况是否 await

```
//进入API
let result = api.handler(paramsData)
if (result instanceof Promise) {
	result = await result
}
```



## 保留两位小数

```
一、四舍五入相关
1、toFixed()方法
需注意，保留两位小数，将数值类型的数据改变成了字符串类型

var num =2.446242342;
num = num.toFixed(2);
console.log(num); //2.45
console.log(typeof num); // string

2、Math.floor()，不四舍五入 ，向下取整
注意，不改变数据类型
num = Math.floor(num * 100) / 100;
console.log(num); //2.44
console.log(typeof num); // number
```



## 时间

```

let timestamp = moment().format('YYYY-MM-DD HH:mm:ss')

// chatgpt_server/script/sparkApi.js
    let dateFormat = 'ddd, DD MMM YYYY HH:mm:ss',
        dateString = new Date().toUTCString(),          // 'Tue, 13 Jun 2023 01:20:45 GMT'
        date = moment.utc(dateString, dateFormat)._i

    let signature_origin = "host: " + host + "\n"
    signature_origin += "date: " + date + "\n"
    signature_origin += "GET " + path + " HTTP/1.1"

```



## 定时器



```
            // 正在计算, 给前端发消息报告进度
            let t = setInterval(async () => {

            try {
                let p = await this.redis.defaultDB.xxx.state.get(`${ID}_`)
                let msg = JSON.parse(p)
                __ws__.send(msg)
                if (msg && msg.msg == '计算已完成') {
                    clearInterval(t)
                } else if (!msg) {
                    clearInterval(t)
                }
            } catch (e) {
                console.log(e)
                clearInterval(t)
            }

            }, 2000)
```



```
    //一秒一次心跳包
    let task = setInterval(() => {
      try {
        __ws__.send("{}")
      } catch (ex) {
        clearInterval(task)
      }

    }, 1000)

    __ws__.on("close", () => {
      clearInterval(task)
    })
```



```
setTimeout(function () {
	console.log('boo')
}, 1000 * 3)
```



## throw

```
throw new Error(errMsg)
```





# Regex



> https://javascript.info/regexp-groups



## 高级选项

- https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions

| 标志 | 描述                                                        |
| :--- | :---------------------------------------------------------- |
| `g`  | 全局搜索。                                                  |
| `i`  | 不区分大小写搜索。                                          |
| `m`  | 多行搜索。                                                  |
| `s`  | 允许 `.` 匹配换行符。                                       |
| `u`  | 使用 unicode 码的模式进行匹配。                             |
| `y`  | 执行“粘性 (`sticky`)”搜索，匹配从目标字符串的当前位置开始。 |



## test



```javascript
// 是否匹配
const regex = new RegExp('foo*');
const globalRegex = new RegExp('foo*', 'g');
console.log(regex.test(str));
// expected output: true
```



## string.match



```javascript
> '###'.match(/#+/)
[ '###', index: 0, input: '###', groups: undefined ]
> 'a'.match(/#+/)
null
```





## dotAll

. 默认不匹配换行符

```
const regex1 = new RegExp('foo', 's');  // 's' 选项开启 . 增加匹配换行符功能
console.log(regex1.dotAll);
// expected output: true
```



## new RegExp



```
new RegExp(String.raw`^(?!.*E\.).*$`, 'gs')  // 参数g 全局匹配，参数s 让. 匹配 \n
```



## escapeRegExp

```
      let escape = _.escapeRegExp(k)
      if (escape != k) {
        console.log(`Waring: 题型含有正则字符`)
        continue
      }
```





## 匹配以特殊字符开头的字符

- 比如说 ( ，会出错， 所以需要转义

```nodejs
            let wd = c.lineWords    // 该字符所在行的全部字符

            try {

              let ww = c.word
              let regstr = '^\\'+ String.raw`${ww}\s*`

              let ddd = wd; debugger 

              c.lineWords = wd.replace(new RegExp(regstr), '')  // 从该字符所在行的全部字符中把自已删掉
                // c.word 有可能是特殊字符，比如 ( 所以这里进行转义

            } catch(e){

              let wdd = c.word; debugger

            }
```





## 匹配所有





```
# 更方便的方法,match 有index（注意：str, re 要在while 的外面定义，否则死循环）
let str = 'axxaxxa'
let re = /a/g
while( ( match = re.exec(str)) != null ) {
  a = 1
}
```





## matchAll



```
    let chinese_sequence = Array.from(s.matchAll(/[\u3007\u2E80-\u2FFF\u3100-\u312F\u31A0-\u31EF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]+/g))

    let not_chinese_sequence = Array.from(s.matchAll(/[^\u3007\u2E80-\u2FFF\u3100-\u312F\u31A0-\u31EF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]+/g))
        
        let jp_sequence = Array.from(s.matchAll(/[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]+/g))


```





- 相当于python 的 finditer

```javascript
  let regAX = String.raw`\n\d+\..+?（\s*?）.*?\n`
  
  if ((new RegExp(regAX).test(strs))) {  //匹配标题

    let matches = strs.matchAll(regAX)

    let arr = Array.from(matches)

    if (arr.length > 0) {

      for (let i = 0; i < arr.length; i++) {
        let match = arr[i]
        let begin = match.index
        let end = begin + match[0].length

        let title = match[1]  // get the match group text
        let testOrigin = strs.substring(begin, end) // get the origin match text

        testOrigins.push(testOrigin)

      }

    }

  }
```



```python
# '[A1型题]'

strs = docText.replace('**********', '')
strs = strs.strip()
strs = '\n\n' + strs +  '\n\n'


"""
单项选择题（无序号，答案附在后边）
"""
def ANONUM(strs):

    strs += 'A.'

    result = []
    
    #od = {} # OrderedDict()

    iters = re.finditer('\n.+?\nA\.', strs, re.DOTALL)
    poss = [ i.span() for i in iters ] # 标题positions

    for i in range( len(poss) - 1 ):
        (start, end) = poss[i]
        (start2, end2) = poss[i+1] 

        pre = strs[start:end]
        last = strs[end-2:end2]


        dic = {}

        title = re.compile('\n(.+?)\nA\.').search(pre).group(1)

        print(title)

        dic["Title"] = title

        arr = last.split('\n')


        selectItems = []

        for s in arr:
            
            s = s.replace('\n','')

            if '【答案】' in s:
                
                rr2 = s.split('【答案】')
                Answer = rr2[1]

                dic["Answer"] = Answer

                break
            
            rr = s.split('.')
            itemName = rr[0]
            itemStr = rr[1]

            selectItems.append( {"Content":itemStr,"ItemName": itemName} )
            

        dic["SelectedItems"] = selectItems
        dic["Explain"] = ""
        dic["Type"] = ""

        
        result.append(dic)

    
    j = string(result)

    return j

j = ANONUM(strs)
```



## 匹配不消耗



```
/a(?=b)bc/中的正向肯定预查(?=b)匹配了a后面的字母b，但是并没有消耗它，所以，后面再跟一个“bc”串，这就完整地匹配了字符串“abc”。其实，它的真正意义应该是确定了这个字母a，因为不是每个字母a后面都会跟一个字母b的！ 
而a(b)bc因为匹配并消耗了字母a后面的b，再来添加一个“bc”串的时候，就变成了“abbc”，就不能匹配字符串“abc”。

到这，估计后面的正向否定预查就没什么问题了，以及反向预查，只不过是类似的，但是位置变了。

(?<=pattern) 
这是反向肯定预查，因为Javascript不支持反向预查，所以以下用Python实现
```



## 不是分组



```
(?:)
```







## 不匹配某个串



### 零宽度断言



```

# https://stackoverflow.com/questions/406230/regular-expression-to-match-a-line-that-doesnt-contain-a-word
	国外大佬

# https://www.cnblogs.com/wangqiguo/archive/2012/05/08/2486548.html


# https://www.cnblogs.com/wangqiguo/archive/2012/05/08/2486548.html
	利用正则表达式排除特定字符串

// 匹配不以baidu开头的字符串
//ss = 'baidu.com'
ss = 'sina.com.cn'
let matches = ss.matchAll('^(?!baidu).*$')
let arr = Array.from(matches)  # 成功匹配'sina.com.cn'



// 匹配不以com 结尾的字符串
ss = 'www.hao.cc'
//ss = 'www.baidu.com'
let matches = ss.matchAll('^.*?(?<!com)$')
let arr = Array.from(matches)  # 成功匹配 'www.hao.cc'

// 匹配不含if 的字符串
//ss = 'else if (a>b) {}'
ss = 'else (a>b) {}'

let matches = ss.matchAll('^([^f]|[^i]f)+$')  # 成功匹配 'else (a>b) {}'

let arr = Array.from(matches)



// 匹配不含if 的字符串 （优化版）
//ss = 'else if (a>b) {}'
ss = 'else (a>b) {}'

let matches = ss.matchAll('^(?!.*if).*$')  # 成功匹配 'else (a>b) {}'

let arr = Array.from(matches)


// 匹配不含E. 的字符串
ss = 'else E. (a>b) {}'

let matches = ss.matchAll('^(?!.*E\\.).*$')

let arr = Array.from(matches)  # OKOKOK 不匹配E.  ，其他的都匹配






// 匹配不含E. 的字符串
ss = 'else E . (a>b) {}'

let regg = '^(?!.*E\\.).*$'
let regg2 = String.raw`^(?!.*E\.).*$`

let regg3 = new RegExp(String.raw`^(?!.*E\.).*$`, 'gs')  // 参数g 全局匹配，参数s 让. 匹配 \n

console.log( regg3.dotAll )

let matches = ss.matchAll(regg3)  // 正则必须有 g 参数，否则报错

let arr = Array.from(matches)  // # OKOKOK 不匹配E.  ，其他的都匹配


console.log(/foo/ig.flags)   // 正则的简写，参数加了 i, g,g 表示全局匹配

a = 1

```



### 匹配不含 A. B. C. D. E. 的串

```
# 匹配不含 A. B. C. D. E. 的串
ss = '\n\nelse E .  D. (a>b) {}\n\n'
let regg4 = new RegExp(String.raw`^\n\n(?!.*?(A\.|B\.|C\.|D\.|E\.)).*\n\n$`, 'gs')
let matches = ss.matchAll(regg4)  // 正则必须有 g 参数，否则报错
let arr = Array.from(matches)
```

https://salesforce.stackexchange.com/questions/329256/how-can-i-match-second-last-char-of-a-string-with-regex



```

# https://stackoverflow.com/questions/7801581/regex-for-string-not-containing-multiple-specific-words

// 匹配不含E. 且还不含D. 的字符串
ss = '\n\nelse E .  D . (a>b) {}\n\n'

let regg = '^(?!.*E\\.).*$'
let regg2 = String.raw`^(?!.*E\.).*$`

let regg3 = new RegExp(String.raw`^(?!.*E\.).*$`, 'gs')  // 参数g 全局匹配，参数s 让. 匹配 \n


let regg4 = new RegExp(String.raw`^\n\n(?!.*?(E\.|D\.)).*\n\n$`, 'gs')

// (?!.*98|.*2000|.*xp)

// ^([^h].*$)|(h([^e].*$|$))|(he([^h].*$|$))|(heh([^e].*$|$))|(hehe.+$) 


console.log( regg3.dotAll )

let matches = ss.matchAll(regg4)  // 正则必须有 g 参数，否则报错

let arr = Array.from(matches)  // # OKOKOK 不匹配E.  ，其他的都匹配


console.log(/foo/ig.flags)   // 正则的简写，参数加了 i, g,g 表示全局匹配

if (arr.length > 0) {

  for (let i = 0; i < arr.length; i++) {
    let match = arr[i]
    let begin = match.index
    let end = begin + match[0].length

    let title = match[1]  // get the match group text
    let testOrigin = ss.substring(begin, end) // get the origin match text

    testOrigins.push(testOrigin)

  }
```



### 匹配不以  题\s*\n  结尾的字符串



```javascript
/*
三、共用题干单选题(1~3题共用题干)
最后一串可见字符不能是   题|共用题干|共用题干\)
*/
ss = '\n一、www.hao.com题共用 \n'

let regStr = String.raw`\n\s*([一二三四五六七八九十百千万]+?、(?!.*?((题|共用题干|共用题干\))\s*\n)).+?)\s*\n`

let matches = ss.matchAll(new RegExp(regStr,'gs'))
let arr = Array.from(matches)

说明：
	(?!.*?(题\s*\n))  预先保证了整个串不以 题\s*\n  结尾，然后才去匹配

```





### 解析选择题选项



```javascript


strs = `[A1型选择题]
1.最易发生阴阳互损的脏腑是
A.心
B.肺
C.脾
D.肝
E.肾
F.天气
G.空气
`

var selects = []

if ((new RegExp(String.raw`\nA\..+?\s+B\..+?\s+C\..+?\s+D\..+?\s*(?:E\..+?)*`)).test(strs)) {  // 匹配选项

  let match = strs.match(String.raw`\n(A\..+?)\s+(B\..+)?\s+(C\..+?)\s+(D\..+?)\s*((?:E\..+?)*)\s*((?:F\..+?)*)\s`)  // ((?:G\..+?)*)\s+  // (?:[a-zA-Z]\..+?)+

  //let match = strs.match(String.raw`\n(?:[A-H]\..+?)+`)

  for (let i = 1; i < match.length; i++) {
    let t = match[i] // get the match group text

    if (t === null || t === undefined || t === '' ) {
      continue
    }

    let ItemName = t.split('.')[0]
    let Content = t.split('.')[1]

    selects.push({ ItemName, Content })

  }

  if (selects.length > 0) {

    let last = selects[ selects.length - 1 ]

    let laststr = last.ItemName + '.' + last.Content

    let arr = strs.split( new RegExp(laststr) )

    if (arr.length === 2) {

      let strs2 = arr[1]

      if ((new RegExp(String.raw`\n((?:G\..+?)*)\s*((?:H\..+?)*)\s`)).test(strs)) {

        let match2 = strs.match(String.raw`\n((?:G\..+?)*)\s*((?:H\..+?)*)\s*((?:I\..+?)*)\s*((?:J\..+?)*)\s*((?:K\..+?)*)\s*((?:L\..+?)*)\s`) 

        for (let i = 1; i < match2.length; i++) {
          let t = match2[i] // get the match group text
      
          if (t === null || t === undefined || t === '' ) {
            continue
          }
      
          let ItemName = t.split('.')[0]
          let Content = t.split('.')[1]
      
          selects.push({ ItemName, Content })
      
        }

      }


    }

  }

}
```







### ?= 向前查找

- = 后面必须匹配，但不吃掉它(consume)

```
# https://www.jianshu.com/p/eec1a081b4b7
```



#### 否定式向前查找

 ```
a ='这是中文\nabc'
a.replace(/(?<!\n)([a-z])/g, 'O')
	
--> '这是中文\naOO'
 ```





(?!...) 





### <= 向后查找

- < 前面必须匹配，但不吃掉它(consume)

  ```
  a = 'aa\nbb\ncc'
  a.match(/(?<=\n|^)([a-z]+)(?=\n|$)/g)
  --> [ 'aa', 'bb', 'cc' ]
  
  ```

a = `1\n2\n3\n`
  a.replace(/(?<=\n)\d(?=\n)/g, 'OO')  # \d 的前面和后面必须是回车，但是不吃掉回车
  --> '1\nOO\nOO\n'
  ```
  
   x(?!y)  否定式向后查找 x 后面不能是y





## ^| 整个串必须在开头的位置或前面有\n接除\n外的其他空白



  ```
# 整个串必须在开头的位置或前面有\n接除\n外的其他空白
# ^ 符号表示整个串的位置是出现在开头，它的前面没有任何其他的东西
let s = `#abc #def
  ##ghi

###jkl 
####mno #pqr

`
let matchs = s.matchAll(new RegExp(String.raw`(?:^|\n)[^\r\n\S]*(#[\s\S]+?)(?=\n)`, 'g'))
let arr = Array.from(matchs)
arr.forEach((match)=>{

    let g2 = match[1]
    console.log(g2)

})
```

- (?:^|\n)  整个串或者出现在开头，或都前面必有一个 \n 
- ?: 表示这不是一个分组
- \s 表示空白字符，\S 表示非空白字符
- [^\r\n\S]*  表示 既不是\r 又不是 \n 还不是非空白字符，就只能是 **除\r \n 以外的其他所有空白了**



## 命名捕获组



`(?<name>group)` 或 `(?'name'group)`，其中`name`表示捕获组的名称，`group`表示捕获组里面的正则。



#### 反向引用

\k<name> 或 \k'name'的形式来对前面的命名捕获组捕获到的值进行引用。如之前的

```
(\d{2})\1
可以改写为
(?<key>\d{2})\k<key>
```







## replace



​```javascript
var strs = fs.readFileSync(fdoc, "utf8")

strs = strs.replace(/\*\*\*\*\*\*\*\*\*\*/g, '').replace(/\r\n/g, '\n').replace(/\t/g, '  ').trim()
strs = '\n\n' + strs +  '\n\n'
```



### 引用

```javascript
let strs = '中  文'
let r = strs.replace(new RegExp(String.raw`([^a-z^A-Z^\s])\s+([^a-z^A-Z^\s])`), '$1$2')
```







## Iterator 转数组



```javascript
    let regexp = new RegExp(p,'g');
    let matches = strs.matchAll(regexp);

    let arr = Array.from(matches)
    for (let i = 0; i < arr.length; i++) {
        let match = arr[i]
        console.log(`Found ${match[0]} start=${match.index} end=${match.index + match[0].length}.`);
    }
```



## split by



```javascript
 arrans = anss.split(new RegExp( String.raw`[\s、，\,]`) )
```



```
# split at first
const str = 'bobby-hadz-com'
const [first, ...rest] = str.split('-')

console.log(first) // bobby
console.log(rest) // ['hadz', 'com']
```





## 过滤汉字里的标点符号

- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Unicode_Property_Escapes

  > Unicode property escapes

- https://www.jianshu.com/p/fcbc5cd06f39

  > Unicode 编码 Emoji CJK 中文 汉字 过滤正则

```
a= '有效的。effctive“有效的，起作用的”；viual“视觉的，视力的”；crical“挑剔的”；ineviable“必然的，不可避免'
a.replace(/\p{P}/gu, '')  # 成功云掉了中文标点
> '有效的effctive有效的起作用的viual视觉的视力的crical挑剔的ineviable必然的不可避免'


> a.replace(/[\u3007\u2E80-\u2FFF\u3100-\u312F\u31A0-\u31EF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]/g, '')
'。effctive“，”；viual“，”；crical“”；ineviable“，'

\pP 其中的小写 p 是 property 的意思，表示 Unicode 属性，用于 Unicode 正表达式的前缀。

大写 P 表示 Unicode 字符集七个字符属性之一：标点字符。

'A ticket to 大阪 costs ¥2000 👌.'.replace(/\p{Sc}|\p{P}/gu, '')




```

`定义范围`是Unicode指定的字符区间，`实际范围`是当前版本真正使用的区间，没使用的区间在后续版本更新会被使用，所以过滤规则已定义范围为准。
 `〇` 虽然在符号区但属于汉字。
 易经六十四卦符号不属于汉字。

包含兼容和扩展字符

| 过滤内容       | 正则                                                         |
| -------------- | ------------------------------------------------------------ |
| CJK 汉字和符号 | [\u2E80-\uA4CF\uF900-\uFAFF\uFE10-\uFE1F\uFE30-\uFE4F\uFF00-\uFFEF] |
| CJK 标点符号   | [\u3000-\u3006\u3008-\u303F\uFE10-\uFE1F\uFE30-\uFE4F\uFF00-\uFFEF] |
| 中文汉字和符号 | [\u2E80-\u2FFF\u3000-\u303F\u3100-\u312F\u31A0-\u31EF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\uFE10-\uFE1F\uFE30-\uFE4F\uFF00-\uFFEF] |
| 仅中文汉字     | [\u3007\u2E80-\u2FFF\u3100-\u312F\u31A0-\u31EF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF] |

常用其它过滤判断



```csharp
CJK 常用汉字和符号(无全角内容)  
[\u2E80-\uA4CF\uF900-\uFAFF\uFE10-\uFE1F\uFE30-\uFE4F]  

CJK 汉字和符号(无竖排符号)  
[\u2E80-\uA4CF\uF900-\uFAFF\uFF00-\uFFEF]  

CJK 汉字和符号(无竖排符号和全角)  
[\u2E80-\uA4CF\uF900-\uFAFF]  

CJK 汉字(无符号和全角)  
[\u3007\u2E80-\u2FFF\u3040-\uA4CF\uF900-\uFAFF]  

中文汉字和符号(无全角内容)  
[\u2E80-\u2FFF\u3000-\u303F\u3100-\u312F\u31A0-\u31EF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\uFE10-\uFE1F\uFE30-\uFE4F]
```

不含兼容和扩展字符

| 过滤内容       | 正则                                      |
| -------------- | ----------------------------------------- |
| CJK 标点符号   | [\u3000-\u3006\u3008-\u303F\uFF00-\uFFEF] |
| 中文汉字和符号 | [\u3000-\u303F\u4E00-\u9FFF\uFF00-\uFFEF] |
| 仅中文汉字     | [\u3007\u4E00-\u9FFF]                     |

大于4字不同语言符处理方式不同，可根据需要决定是否添加



```csharp
#| 20000-2A6DF | CJK统一表意文字扩展B |
#| 2A700-2EBE0 | CJK统一表意文字扩展C-F |
#| 2F800-2FA1F | CJK兼容表意文字扩展 |
#| 30000~3134A | CJK统一表意文字扩展G |

#OC
[\U00020000-\U0002A6DF\U000A700-\U0002EBE0\U0002F800-\U0002FA1F\U00030000-\U0003134A]

#Java
[\x{20000}-\x{2A6DF}\x{2A700}-\x{2EBE0}\x{2F800}-\x{2FA1F}\x{30000}-\x{3134A}]

#JavaScript
[\u{20000}-\u{2A6DF}\u{2A700}-\u{2EBE0}\u{2F800}-\u{2FA1F}\u{30000}-\u{3134A}]
```

emoji

参考[emoji-regex](https://links.jianshu.com/go?to=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Femoji-regex)的正则分为3种标准 [RGI标准](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fmathiasbynens%2Femoji-regex%2Fblob%2F61%2Fes2015%2FRGI_Emoji.js)  、[旧标准](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fmathiasbynens%2Femoji-regex%2Fblob%2F61%2Fes2015%2Findex.js)  、[旧标准+文字类型](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fmathiasbynens%2Femoji-regex%2Fblob%2F61%2Fes2015%2Ftext.js)  。
 但是这里 `文字类型(无彩色Icon)`  的emoji 把 `#*0-9` 也算在内并不正确。
 修改后最终的规则可以参考这里[emoji_regex.dart](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fwittyneko%2Femoji_regex%2Fblob%2Fmaster%2Flib%2Femoji_regex.dart)。

[Full Emoji List](https://links.jianshu.com/go?to=https%3A%2F%2Funicode.org%2Femoji%2Fcharts%2Ffull-emoji-list.html)
 [emoji history index](https://links.jianshu.com/go?to=https%3A%2F%2Funicode.org%2FPublic%2Femoji%2F)
 [emoji-test.txt](https://links.jianshu.com/go?to=https%3A%2F%2Fwww.unicode.org%2FPublic%2Femoji%2F13.0%2Femoji-test.txt)



```
# 好像只有java 可以
str = str.replaceAll("\\pP", "")

Unicode 编码并不只是为某个字符简单定义了一个编码，而且还将其进行了归类。

\pP 其中的小写 p 是 property 的意思，表示 Unicode 属性，用于 Unicode 正表达式的前缀。

大写 P 表示 Unicode 字符集七个字符属性之一：标点字符。

其他六个是

L：字母；
M：标记符号（一般不会单独出现）；
Z：分隔符（比如空格、换行等）；
S：符号（比如数学符号、货币符号等）；
N：数字（比如阿拉伯数字、罗马数字等）；
C：其他字符

上面这七个是属性，七个属性下还有若干个子属性，用于更进一步地进行细分。

Unicode 正则表达式标准（可以找到所有的子属性）
http://www.unicode.org/reports/tr18/

各 Unicode 字符属性的定义，可以用一看看某个字符具有什么属性。
http://www.unicode.org/Public/UNIDATA/UnicodeData.txt

这个文本文档一行是一个字符，第一列是 Unicode 编码，第二列是字符名，第三列是 Unicode 属性，
以及其他一些字符信息。
```



### unicode 错字可视化

[unicode 错字可视化](https://www.v2ex.com/t/915530#reply7)



## 匹配中文字符

```
let chinese_sequence = Array.from(s.matchAll(/[\u3007\u2E80-\u2FFF\u3100-\u312F\u31A0-\u31EF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]+/g))

let not_chinese_sequence = Array.from(s.matchAll(/[^\u3007\u2E80-\u2FFF\u3100-\u312F\u31A0-\u31EF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]+/g))

```



# String



## encode

```
# 二进制数据
line = str.encode(json.dumps({"tokens": token_ids}) + "\n")
```



## match



```javascript
> '###'.match(/#+/)
[ '###', index: 0, input: '###', groups: undefined ]
> 'a'.match(/#+/)
null
```



## 不转义



```javascript
String.raw `Hi\u000A!`;
```



## 动态计算



```javascript
`${type}Mid`
`Found ${match[0]} start=${match.index} end=${match.index + match[0].length}.`
```



## indexOf



```
The index of the first occurrence of searchString found, or -1 if not found
```





## Replace



```javascript
// replaceAll node v15 才有，这里自定义之

        String.prototype.replaceAll = function(search, replacement) {
            var target = this
            return target.replace(new RegExp(search, 'g'), replacement)
        }
      
        strs = strs.trim()
        strs = '\n\n' + strs +  '\n\n'
        strs = strs.replaceAll('\xa0', "\n").replaceAll("Ｂ", "B").replaceAll("Ｄ", "D")
```



### 去空白

```
function removeSpace(str) {
    return str.replace(/\s+/g, '').replace(/(&ensp;|&emsp;|&zwnj;|&zwj;|&nbsp;|&thinsp;)/g, '')
}
```



### 全角转半角

```javascript
    function fullWidth_to_halfWidth(str) {

        let d = {
            'Ａ':'A', 'Ｂ':'B', 'Ｃ':'C', 'Ｄ':'D', 'Ｅ':'E', 'Ｆ':'F', 'Ｇ':'G', 'Ｈ':'H', 'Ｉ':'I', 'Ｊ':'J', 'Ｋ': 'K', 'Ｌ':'L', 'Ｍ':'M', 'Ｎ':'N', 'Ｏ':'O', 'Ｐ':'P', 'Ｑ':'Q', 'Ｒ':'R', 'Ｓ':'S', 'Ｔ':'T', 'Ｕ':'U', 'Ｖ':'V', 'Ｗ':'W', 'Ｘ':'X', 'Ｙ':'Y', 'Ｚ':'Z',
            'ａ':'a', 'ｂ':'b', 'ｃ':'c', 'ｄ':'d', 'ｅ':'e', 'ｆ':'f', 'ｇ':'g', 'ｈ':'h', 'ｉ':'i','ｊ':'j', 'ｋ':'k', 'ｌ':'l', 'ｍ':'m', 'ｎ':'n', 'ｏ':'o', 'ｐ':'p', 'ｑ':'q', 'ｒ':'r', 'ｓ':'s', 'ｔ':'t', 'ｕ':'u', 'ｖ':'v', 'ｗ':'w', 'ｘ':'x', 'ｙ':'y', 'ｚ':'z'
        }
        
        for (let [f, h] of Object.entries(d)) {
            
            let reg = new RegExp(`${f}`, 'g')
            str = str.replace(reg, h)

        }

        return str

    }
```



### 特殊字符

```
常用上标 ⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁺ ⁻ ⁼ ⁽ ⁾ ⁿ º ˙

常用下标₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ ₊ ₋ ₌ ₍ ₎ ₐ ₑ ₒ ₓ ₔ ₕ ₖ ₗ ₘ ₙ ₚ ₛ ₜ

更多上标 ᵃ ᵇ ᶜ ᵈ ᵉ ᵍ ʰ ⁱ ʲ ᵏ ˡ ᵐ ⁿ ᵒ ᵖ ᵒ⃒ ʳ ˢ ᵗ ᵘ ᵛ ʷ ˣ ʸ ᙆ ᴬ ᴮ ᒼ ᴰ ᴱ ᴳ ᴴ ᴵ ᴶ ᴷ ᴸ ᴹ ᴺ ᴼ ᴾ ᴼ̴ ᴿ ˢ ᵀ ᵁ ᵂ ˣ ᵞ ᙆ ꝰ ˀ ˁ ˤ ꟸ ꭜ ʱ ꭝ ꭞ ʴ ʵ ʶ ꭟ ˠ ꟹ ᴭ ᴯ ᴲ ᴻ ᴽ ᵄ ᵅ ᵆ ᵊ ᵋ ᵌ ᵑ ᵓ ᵚ ᵝ ᵞ ᵟ ᵠ ᵡ ᵎ ᵔ ᵕ ᵙ ᵜ ᶛ ᶜ ᶝ ᶞ ᶟ ᶡ ᶣ ᶤ ᶥ ᶦ ᶧ ᶨ ᶩ ᶪ ᶫ ᶬ ᶭ ᶮ ᶯ ᶰ ᶱ ᶲ ᶳ ᶴ ᶵ ᶶ ᶷ ᶸ ᶹ ᶺ ᶼ ᶽ ᶾ ᶿ ꚜ ꚝ ჼ ᒃ ᕻ ᑦ ᒄ ᕪ ᑋ ᑊ ᔿ ᐢ ᣕ ᐤ ᣖ ᣴ ᣗ ᔆ ᙚ ᐡ ᘁ ᐜ ᕽ ᙆ ᙇ ᒼ ᣳ ᒢ ᒻ ᔿ ᐤ ᣖ ᣵ ᙚ ᐪ ᓑ ᘁ ᐜ ᕽ ᙆ ᙇ ⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁺ ⁻ ⁼ ˂ ˃ ⁽ ⁾ ˙ * º

更多下标 ₐ ₔ ₑ ₕ ᵢ ⱼ ₖ ₗ ₘ ₙ ₒ ₚ ᵣ ₛ ₜ ᵤ ᵥ ₓ ᙮ ᵤ ᵩ ᵦ ₗ ˪ ៳ ៷ ₒ ᵨ ₛ ៴ ᵤ ᵪ ᵧ

中文上标 ㆒㆓㆔㆕㆖㆗㆘㆙㆚㆛㆜㆝㆞㆟

特殊字符 ：
、。·ˉˇ¨〃々—～‖…‘’“”〔〕〈〉《》「」『』〖〗【】±×÷∶∧∨∑∏∪∩∈∷√⊥∥∠⌒⊙∫∮≡≌≈∽∝≠≮≯≤≥∞∵∴♂♀°′″℃＄¤￠￡‰§№☆★○●◎◇◆□■△▲※→←↑↓〓〡〢〣〤〥〦〧〨〩㊣㎎㎏㎜㎝㎞㎡㏄㏎㏑㏒㏕︰￢￤℡ˊˋ˙–―‥‵℅℉↖↗↘↙∕∟∣≒≦≧⊿═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬╭╮╯╰╱╲╳▁▂▃▄▅▆▇�█▉▊▋▌▍▎▏▓▔▕▼▽◢◣◤◥☉⊕〒〝〞

罗马字符：
ⅰ ⅱ ⅲ ⅳ ⅴⅵ  ⅶ  ⅷ ⅸⅹ
Ⅰ Ⅱ Ⅲ  Ⅳ  Ⅴ Ⅵ Ⅶ Ⅷ Ⅸ Ⅹ Ⅺ Ⅻ

数字字符：⒈⒉⒊⒋⒌⒍⒎⒏⒐⒑⒒⒓⒔⒕⒖⒗⒘⒙⒚⒛⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇①②③④⑤⑥⑦⑧⑨⑩㈠㈡㈢㈣㈤㈥㈦㈧㈨㈩

拼音字符：
āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü

希腊字母
ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψω

```



```
function removeSpecialCharacter(str) {
    return str.replace(/[`\-℃:_.~!@#$%^&*() \+ =<>?"{}|, \/ ;' \\ [ \] ·~！@#￥%……&*（）—— \+ ={}|《》？：“”【】、；‘’，。、]/g, '')
}
```



```
let arr_litteChar_digit = Array.from(Explain.matchAll(/[a-z0-9A-Z₀₁₂₃₄₅₆₇₈₉₊₋ₐₑₒₓₔₕₖₗₘₙₚₛₜ⁰°¹²³⁴⁵⁶⁷⁸⁹⁺⁻ⁿ·～%μ△+=ÓóÒòŎŏÔôỐốỒồỖỗỔổǑǒÖöȪȫŐőÕõṌṍṎṏȬȭȮȯȰȱØøǾǿǪǫǬǭŌōṒṓṐṑỎỏȌȍŐőȎȏƠơỚớỜờỠỡỞởỢợỌọỘộỎỏO̍o̍O̊o̊ƟɵⅠⅡⅢⅣⅤⅥⅦⅧⅨⅬⅭ\/\<\>\-]+/g))

                    if (tmp.match(/[A-Z]/)) { // 含有大写字母
                        if (tmp.match(/[0-9]/) || tmp.match(/[a-z]/) || tmp.match(/[F-Z]/) ||
                            tmp.match(/[₀₁₂₃₄₅₆₇₈₉₊₋ₐₑₒₓₔₕₖₗₘₙₚₛₜ]/) || // 常用下标      
                            tmp.match(/[⁰°¹²³⁴⁵⁶⁷⁸⁹⁺⁻ⁿ]/) || // 常用上标 
                            tmp.match(/[ÓóÒòŎŏÔôỐốỒồỖỗỔổǑǒÖöȪȫŐőÕõṌṍṎṏȬȭȮȯȰȱØøǾǿǪǫǬǭŌōṒṓṐṑỎỏȌȍŐőȎȏƠơỚớỜờỠỡỞởỢợỌọỘộỎỏO̍o̍O̊o̊Ɵɵ]/) || // 希腊字母
                            tmp.match(/[ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅬⅭ]/) || // 罗马数字
                            tmp.match(/[·～%μ△+=\/\<\>\-]/) 
                        ) {  // 同时含有数字或小写字母或超出 E 的大写字母



```





### replace函数还可以有回调

```
// Escape a string for use as text in an HTML document
String.prototype.$escape = function() {
  return this.replace(/[&<>"']/g, function(m) {
    switch (m) {
      case '&': return '&amp;';
      case '<': return '&lt;';
      case '>': return '&gt;';
      case '"': return '&quot;';
      case '\'': return '&#039;';
      default: assert.fail(`Should escape character ${m}`);
    }
  });
 
}
```





## split

```javascript
const splits = myString.split(' ', 3)
```



## slice

```
url = '/pull/test'
const id = url.slice(6)  
> 'test'
```



## includes



```
if (text.includes(word)) {}
```



## intersection & union

```
    let set1 = new Set('abc')
    let set2 = new Set('bde')

    let intersection = new Set([...set1].filter(x => set2.has(x)));
    let union = new Set([...set1, ...set2]);
```







## 最长公共前缀

- https://github.com/burgaard/string-algorithms
  - longest common prefixes 

```javascript
npm i string-algorithms

(async () => {
    let { longestCommonSubstring } = await import('string-algorithms')
    const strings = [
        '12apple',
        '3apple4',
        'apple56'
    ];
    console.log(longestCommonSubstring(strings))  // 这不是公共前缀，而是公共子串
})()
```



- https://github.com/sisterAn/JavaScript-Algorithms/issues/19

```javascript
    // 公共指针法
    function longestCommonPrefix(strs) {
        if (!strs || !strs.length) {
            return '';
        }

        // 从0开始依次比较
        let currentIndex = 0;

        while (true) {
            // 取第一个字符串的当前位字符作为参照
            const refer = strs[0][currentIndex];
            // 是否全部匹配
            const currentAllMatch = strs.reduce((pre, str) => {
                return pre && str.charAt(currentIndex) === refer;
            }, true);

            if (currentAllMatch) {
                currentIndex++;
            } else {
                break;
            }
        }

        return strs[0].substring(0, currentIndex);
    }

    console.log(longestCommonPrefix(["flower","flow","flight"]))
```



## 编辑距离

- https://github.com/hiddentao/fast-levenshtein

  > ``` 
  > npm install fast-levenshtein --save
  > 
  > var levenshtein = require('fast-levenshtein');
  > 
  > var distance = levenshtein.get('back', 'book');   // 2
  > var distance = levenshtein.get('我愛你', '我叫你');   // 1
  > ```



## NGram

```javascript
    // NGram
    NG: function (strs) {

        strs = strs.replaceAll(String.raw`\s`, '')

        function ng(s, n) {

            var grs = []

            for (let i = 0; i < s.length; i++) {

                if (i + n > s.length) {
                    break
                }

                var gr = s.substring(i, i + n)

                grs.push(gr)


            }

            return grs

        }

        var gss = []
        for (let i = 1; i <= 10; i++) {

            let gs = ng(strs, i)

            if (gs.length > 0) {

                gss = gss.concat(gs)

            } else {

                break

            }

        }

        return gss

    }
```



```javascript
# 处理允许存在特殊字符的情况，因为它们是天然的分隔符，对于分词是有用的
		let ng = NG(text)
        let ng2 = []

        for (let g of ng) {

          let g2 = g.replace(/\s/g, '').replace(/\p{P}/gu, '')  // 去掉空格，去掉中文标点

          if (g2.length == g.length) {
            ng2.push( g )
          } else {
            let a = 1
          }

        }
```





## diff



```javascript
require('colors')

const Diff = require('diff');

const one = 'beep boop'
const other = 'beep boob blah'

const diff = Diff.diffChars(one, other)

for (let d of diff) {

    // green for additions, red for deletions
    // grey for common parts
    const color = d.added ? 'green' :
        d.removed ? 'red' : 'grey'
    process.stderr.write(d.value[color])

}

console.log()
```



## CJK Symbols

- https://en.wiktionary.org/wiki/Category:CJK_Symbols_and_Punctuation_block



## 检测字符编码

```
// doc\lang\programming\nodejs\pmserver\lib\ssa.js
let chardet = require('chardet')
let encode = chardet.detect(Buffer.from( require('fs').readFileSync(sapath) 
sa = fs.readFileSync(sapath, { encoding:encode})  // encode
```



## 转换字符编码

```
"iconv-lite": "^0.4.24"

let senddata = iconv.encode(JSON.stringify(param) + "\r\n", 'gbk');
this.childprocess.stdin.write(senddata);
```



```
let iconvLite = require('iconv-lite')
iconvLite.decode(buffer, 'cp936')}
```



```
'use strict';
const child_process = require("child_process")
const iconv = require('iconv-lite');
const extend = require('util')._extend;
const EventEmitter = require('events').EventEmitter;
const path = require('path');

let S4 = () => {
    return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
};

let guid = () => {
    return (S4() + S4() + S4() + S4());
};


/**
 * 
 */
class NodeSharp extends EventEmitter {
    constructor(option) {
        super();
        this.childprocess = null;
        this.onceListenters = {};
        this.onListenters = {};
        this._needReOpen = false;
        this.opt = {};

        let defaultOpt = {
            exePath: '',
            autoReOpen: false,
            args: [],
            dataListener: null,
            errorListener: null
        };

        if (typeof option == 'string') {
            defaultOpt.exePath = option;
            this.opt = defaultOpt;
        } else {
            this.opt = extend(defaultOpt, option);
        }
        if (this.opt.dataListener) {
            this.on('data', dataListener)
        }
        if (this.opt.errorListener) {
            this.on('error', errorListener)
        }
    }

    /**
     * start a exe and connect
     * @param {*} option exePath OR {exePath，autoReOpen，args, dataListener, errorListener }
     */
    static connect(option) {
        let exe = new this(option)
        exe.open();
        return exe;
    }



    open() {
        let exec = child_process.spawn;
        let exepath = path.resolve(__dirname, this.opt.exePath);
        this.childprocess = exec(exepath, this.opt.args);
        this.childprocess.stdin.setEncoding("binary");
        this.childprocess.stdout.setEncoding("binary");
        if (this.childprocess == null && this.opt.closeCallback)
            this.opt.closeCallback(-1);
        this.childprocess.on('exit', (code, signal) => {
            if ((this.opt.autoReOpen && signal !== 'SIGTERM') || this._needReOpen)
                setTimeout(function () {
                    this.open();
                    this.emit('reopen', this);
                }.bind(this), 1000);
            this._needReOpen = false;
            this.emit('close', code, this.trueClose);
        });

        this.childprocess.stdout.on('data', (data) => {
            this.emit('message', data);
            let json = '';
            try {
                json = data.toString();

                let jsondata = "";
                try {
                    jsondata = JSON.parse(json);
                } catch (_ee) {
                    return
                }
                if (this.onceListenters[jsondata.Pid]) {
                    this.onceListenters[jsondata.Pid](jsondata.Error, jsondata.Data);
                    delete this.onceListenters[jsondata.Pid];
                }
                if (this.onListenters[jsondata.Pid]) {
                    this.onListenters[jsondata.Pid](jsondata.Error, jsondata.Data);
                }
                this.emit('data', jsondata.Error, jsondata.Data);

            } catch (e) {
                this.emit('error', e);
            }
        });
        this.childprocess.stdout.on('error', e => {
            console.error(e)
            this.emit('error', e)
        })
        this.childprocess.stdin.on('error', e => {
            console.error(e)
            this.emit('error', e)
        })
    };

    close() {
        this._needReOpen = false;
        if (!this.childprocess.killed) {
            this.childprocess.kill('SIGTERM');
        }
    };

    reOpen() {
        this._needReOpen = true;
        if (!this.childprocess.killed) {
            return this.childprocess.kill();
        }
        this.open();
    }

    buildParam(obj) {
        return {
            pid: guid(),
            data: obj
        }
    }

    send({
        param,
        once,
        on
    }) {
        if (!this.childprocess && (once || on))
            return (once || on)('The required process has not started');
        if (!this.childprocess.stdin.writable && (once || on))
            return (once || on)('Unable to establish channel connection');
        param = this.buildParam(param);
        if (once) {
            this.onceListenters[param.pid] = once;
        }
        if (on) {
            this.onListenters[param.pid] = on;
        }
        let senddata = iconv.encode(JSON.stringify(param) + "\r\n", 'gbk');
        this.childprocess.stdin.write(senddata);
    };
}

module.exports = NodeSharp;
```





## 语言检测

- https://github.com/wooorm/franc 中英混合检测不准确，只有一种语言还可以
- https://github.com/dachev/node-cld



```
(async()=>{

  const cld = require('cld');


  //let text = `string code = $"let lang = francAll({text}", [@"{ only:['jpn','cmn','eng'」}"})ln"+ @"//console.log(fs）//fs 是事先 import 好的模块，这里可以直接用所有可用参数都在这里展开了：，.·params//console.log(franc)//console. log(' hello, from vm)returncallback（【msg：'hi，，，，lang）//约定最后以callback返回值`
  
  //let text = `aabbccxxxxxxxxxxxxxxxxxxxxxxxxxxxxaaaaaaaabbbbvcxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

  let text = `中文`

  let { franc, francAll } = await import('franc')

  let lang = francAll(text, { only: ['jpn','cmn', 'eng'], minLength: 1 })

  //const result = await cld.detect(text);
  //console.log(result);

  let a = 1

})()
```





```
github 
	echodict\cut\langDetect.js
	echodict\pmserver\lib\langDetect.mjs
	
// https://github.com/wooorm/franc/tree/main/packages/franc-all


// npm install @kaciras/deasync
// npm install franc

const { deasync } = require("@kaciras/deasync");
const { performance } = require('perf_hooks')

const langDetect = deasync((text, option, done) => {
    (async () => {
        let { franc, francAll } = await import('franc')
        let lang = francAll(text, option) // { only: ['jpn', 'cmn', 'eng'] }
        // cmn	Mandarin Chinese
        // eng	English	
        // rus	Russian
        // jpn	Japanese
        // fra	French	
        // deu	German
        // lat	Latin
        // san	Sanskrit

        done(null, lang)
    })()
});

console.log("Timestamp before: " + performance.now());
let re = langDetect('Alle menslike wesens word vry', { only: ['jpn', 'cmn', 'eng'] })
console.log("Timestamp after: " + performance.now());
```



## 分词 HanLP

- https://github.com/hankcs/HanLP  好像比结巴强



## time

```
let moment = require('moment')
let expires_days = expires_in / (3600 * 24)  // 还有多少天过期
let expires_time = moment().add(expires_days, 'days') // 过期时间

let diff = moment().diff(expires_time)
if (diff >= 0) {
   // access_token 过期了
   reset_access_token()
}

server_wenxin\lib\xfembedding.js
let dateFormat = 'ddd, DD MMM YYYY HH:mm:ss',
        dateString = new Date().toUTCString(),          // 'Tue, 13 Jun 2023 01:20:45 GMT'
        date = moment.utc(dateString, dateFormat)._i
        
```





```
const moment = require('moment')
let timestamp = moment().format('YYYY-MM-DD HH:mm:ss')
```



```
OperateTime:new Date()

OperateTime = new Date(OperateTime)
let lasttime = dic_test[key].OperateTime
if (lasttime > OperateTime) {
```





## guid

```
const uuid = require('uuid')
let guid = uuid.v4()

```







# Array



## join



```
# 连成字符串，中间加空格
const arr = ['Fire', 'Air', 'Water'];
console.log(arr.join(' '));
```



## concat

```
const array1 = ['a', 'b', 'c'];
const array2 = ['d', 'e', 'f'];
const array3 = array1.concat(array2);

console.log(array3);
// expected output: Array ["a", "b", "c", "d", "e", "f"]
```





## 遍历



```
const array1 = ['a', 'b', 'c'];

for (const element of array1) {
  console.log(element);
}
```



```
const iterable = new Map([['a', 1], ['b', 2], ['c', 3]]);

for (const entry of iterable) {
  console.log(entry);
}
// ['a', 1]
// ['b', 2]
// ['c', 3]

for (const [key, value] of iterable) {
  console.log(value);
}
// 1
// 2
// 3
```





```
arr.forEach(element => {
  console.log(element);
});
```





## sort

```javascript
// 双排序，类似C# 的 order by then by
// Lodash 4.x:
data = _.orderBy(data, [
  function (item) { return item.sortData.a },
  function (item) { return item.sortData.b }
], ["asc", "desc"])
```



## reverse

```
const _ = require("lodash")
array = _.reverse( array )
```





## group by



```javascript
const _ = require("lodash")
       
// Original array 
var users = (['one', 'two', 'three', 'four'])
var obj = ([ 3.1, 1.2, 3.3 ])
   
// Using the _.groupBy() method
// with the `_.property` iteratee shorthand 
let grouped_data = _.groupBy(users, 'length')
let grouped_data2 = _.groupBy(obj, Math.floor)
```



## chunk

```
let arr_new = _.chunk(array, [size=1])
```



## shuffle

```
arr = _.shuffle(arr)
```



## includes

```
const pets = ['cat', 'dog', 'bat']
console.log(pets.includes('cat'))
// expected output: true
```



## slice

```
const animals = ['ant', 'bison', 'camel', 'duck', 'elephant'];

console.log(animals.slice(2));
// Expected output: Array ["camel", "duck", "elephant"]

console.log(animals.slice(2, 4));
// Expected output: Array ["camel", "duck"]

console.log(animals.slice(1, 5));
// Expected output: Array ["bison", "camel", "duck", "elephant"]

console.log(animals.slice(-2));
// Expected output: Array ["duck", "elephant"]

console.log(animals.slice(2, -1));
// Expected output: Array ["camel", "duck"]

console.log(animals.slice());
// Expected output: Array ["ant", "bison", "camel", "duck", "elephant"]
```



## splice

```
menus_chapter_not_clone.splice(j, 1)
	# 从索引 j 开始，删除一个元素
```



## splitAt

```
// 从指定位置分成两半
let splitAt = (xs, index) => [xs.slice(0, index), xs.slice(index)]
```





## filter

```
                    Data2 = Data2.filter( item => {
                    
                        if ( len_rate <= 0.35 ) {
                            return false
                        }

                        return true
                    })
                    

delImg (f) {
      console.log('删除图片')
      this.files = this.files.filter(item => item !== f)  // ture 留, false 去
    }
    
    // 带 index 参数
    this.usingBlocks = this.usingBlocks.filter((item, index) => { return index !== i }) // ture 留, false 去
    
    this.usingBlocks = this.usingBlocks.splice(i, 1)  // 不知道为什么删不掉
    
```



## set

```
episodes = Array.from(new Set(episodes)) # 去重
```



### equal

```
const _ = require("lodash");

let s1 = new Set([1,2,3]);
let s2 = new Set([1,2,3]);
let s3 = new Set([2,3,4]);

console.log(_.isEqual(s1, s2)); // true
console.log(_.isEqual(s1, s3)); // false
```



## intersection



```
let _ = require('lodash')
let newArray = _.intersection( array1, array2)
```



## union

```
let _ = require('lodash')
let newArray = _.union([20, 12], [8, 15, 6])
```



## Float32Array.from

```
const dataA = Float32Array.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]);
```





# json



## 遍历



```javascript
for (let key in paramsDefined) {
}
```



```javascript
1238

Under ECMAScript 5, you can combine Object.keys() and Array.prototype.forEach():

var obj = { first: "John", last: "Doe" };

Object.keys(obj).forEach(function(key) {
    console.log(key, obj[key]);
});
ECMAScript 6 adds for...of:

for (let key of Object.keys(obj)) {
    console.log(key, obj[key]);
}
ECMAScript 8 adds Object.entries() which avoids having to look up each value in the original object:

Object.entries(obj).forEach(
    ([key, value]) => console.log(key, value)
);
You can combine for...of, destructuring, and Object.entries:

for (let [key, value] of Object.entries(obj)) {
    console.log(key, value);
}
Both Object.keys() and Object.entries() iterate properties in the same order as a for...in loop but ignore the prototype chain. Only the object's own enumerable properties are iterated.
```



## pickBy

```
let _ = require('lodash')
let result = _.pickBy(word2, function(v, k) {
	return v[`real_p/theory_p`] >= 1.0 && v[`min_entropy`] >= 0.25
})
```



## exist



```javascript
if ( !(keyParent in menus) ) {
```



## isEmpty



```javascript
let _ = require('lodash')
_.isEmpty(dic_ansers)
```



## 展开

```
        let options = {
            qaTemplate: QA_PROMPT,
            questionGeneratorTemplate: CONDENSE_PROMPT,
            returnSourceDocuments: true, //The number of source documents returned is 4 by default
        }
        const { questionGeneratorTemplate, qaTemplate, ...rest } = options
        
     
   rest 的值是：  { returnSourceDocuments: true }
```





## 加料

```
  opts = {
    [kStandaloneREPL]: true,  // [] 是因为名字已存在吧？
    ignoreUndefined: false,
    useGlobal: true,
    breakEvalOnSigint: true,
    ...opts	// 原先的值在这里展开
  }
```







## Object.assign



```javascript
let data = {}
Object.assign(data, query) // 赋值
```



## deep copy

```
let _ = require('lodash');
var deepCopy = _.cloneDeep(obj)
```







## 函数默认值

- https://es6.ruanyifeng.com/#docs/function#
  - 解构赋值默认值结合使用



```
function foo({x, y = 5} = {}) {
  console.log(x, y);
}
foo() // undefined 5
// 如果没有提供参数，函数foo的参数默认为一个空对象
```



## _.valuesIn

```
_.valuesIn(obj)
```



## 后面参数全部从第一参展开得到

```
function REPLServer(prompt,
                    stream,
                    eval_,
                    useGlobal,
                    ignoreUndefined,
                    replMode) {
  let options;
  if (prompt !== null && typeof prompt === 'object') {
    // An options object was given.
    options = { ...prompt };
    stream = options.stream || options.socket;
    eval_ = options.eval;
    useGlobal = options.useGlobal;
    ignoreUndefined = options.ignoreUndefined;
    prompt = options.prompt;
    replMode = options.replMode;
  } else {
    options = {};
  }                    
                
```







# File



## exist



```
fs.existsSync( path )

const apiStat = fs.statSync(apiPath)
const apiExists = apiStat.isFile() && path.extname(apiPath).toLowerCase() === '.js'

```



## remove dir

```
            // if (fs.existsSync(audio_dir)) {
            //     fs.rmSync(audio_dir, { recursive: true, force: true })
            // }
```

 

```
fs.unlinkSync('file.txt')
```





## resolve

```
# 规范化 path ? D:\xxx windows 风格, /d/xxx linux 风格 ？
require.resolve(path)
```





## __dirname

- 代表当前 js 文件所在目录

```
require('path').join(__dirname, 'temp.json')
```



## create dir

```
fs.existsSync( path )
fs.mkdirSync(targetDir, { recursive: true })
```



## read write



```
require('fs').writeFileSync('menu.json', JSON.stringify(menujson), {encoding:'utf8', flag:'w'} )
```

```
require('fs').readFileSync('./input.txt',{encoding:'utf8', flag:'r'})
```

```
fs.createWriteStream(path).write(buffer)
```



### 读任意行

```
# see python3 summary.md

```





### 大文件读写

- https://juejin.cn/post/7148051371060068389

```javascript
const { rejects } = require('assert');
const fs = require('fs');
const path = require('path');

let srcPath = path.join('D:','big.zip');
let destPath = path.join('E:','zip','tt.zip');
console.log('执行开始...');

handleStream().then(res => {
    console.log(res);
    if (res && res.code === 200) {
        console.log('执行完毕');
    }

});

function handleStream() {
    return new Promise(resolve => {
        //大文件处理,执行过程会阻塞等待
        let rs = fs.createReadStream(srcPath, { encoding: 'binary' });
        let ws = fs.createWriteStream(destPath, { encoding: 'binary' });

        rs.on('data', (chunk) => {
            console.log('传输中');
            if (!ws.write(chunk)) { //如果还没写就先暂停
                console.log('读取暂停');
                rs.pause();
            }
        });
        ws.on('drain', () => {
            console.log('读取继续');
            rs.resume();

        });
        rs.on('err', (err) => {
            rejects({ code: -1, msg: '读取错误' });
        });

        rs.on('end', () => {
            console.log('end');
            ws.end();
            resolve({ code: 200, data: 'ok' });
        });
    });

}
```







## read line by line

```javascript

// 原始语料在 doc\lang\programming\pytorch\机器翻译\中英平行语料520万_translation2019zh  格式是：每行一个JSON 文本， 有两个字段 english 和 chinese 
// 转换为 OpenNMT-py 格式，英文一个文件，中文一个文件

(async () => {

    function clean(str) {
        return str.replace(/\r\n/g, '\n').replace(/\n{2,999}/g, '\n')
    }

    async function convert(fpath1, fpath2) {

        let { msg } = await new Promise(async function (resolve, reject) {

            let fs = require('fs')
            let _ = require('lodash')

            let c1 = _.chunk([1, 2, 3, 4, 5], 3)

            fs.rmSync('en_chs', { recursive: true, force: true })
            fs.mkdirSync('en_chs', { recursive: true })

            // var src_train = fs.createWriteStream('en_chs/src-train.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)
            // var tgt_train = fs.createWriteStream('en_chs/tgt-train.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)

            let src_train = fs.createWriteStream('en_chs/src-train.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)
            let tgt_train = fs.createWriteStream('en_chs/tgt-train.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)

            let src_val = fs.createWriteStream('en_chs/src-val.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)
            let tgt_val = fs.createWriteStream('en_chs/tgt-val.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)

            let src_test = fs.createWriteStream('en_chs/src-test.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)
            let tgt_test = fs.createWriteStream('en_chs/tgt-test.txt', { flags: 'a' }) // 'a' means appending (old data will be preserved)


            let src_trains = []
            let tgt_trains = []

            let src_vals = []
            let tgt_vals = []

            let src_tests = []
            let tgt_tests = []

            async function read_big_file(fpath, arr1, arr2) {

                let { msg } = await new Promise(function (resolve2, reject2) {

                    var buffer = '';
                    var rs = fs.createReadStream(fpath)
                    rs.on('data', function (chunk) {
                        var lines = (buffer + chunk).split(/\r?\n/g)
                        buffer = lines.pop()
                        for (var i = 0; i < lines.length; i++) {

                            let line = lines[i]
                            if (line.trim() != '') {
                                line = JSON.parse(line)
                                let english = line.english //clean(line.english)
                                english = english.replace(/(\,)/g, ' $1 ')  // OpenNMT 要通过空格分词，这里把标点和单词拆开
                                english = english.replace(/(\.)/g, ' $1 ')
                                english = english.replace(/(\?)/g, ' $1 ')
                                english = english.replace(/(\!)/g, ' $1 ')
                                english = english.replace(/([^\r\n\S]{2,999})/g, ' ')

                                let chinese = line.chinese // clean(line.chinese)
                                chinese = chinese.replace(/(\，)/g, ' $1 ')  // OpenNMT 要通过空格分词，这里把标点和单词拆开
                                chinese = chinese.replace(/(\、)/g, ' $1 ')
                                chinese = chinese.replace(/(\；)/g, ' $1 ')
                                chinese = chinese.replace(/(\：)/g, ' $1 ')
                                chinese = chinese.replace(/(\。)/g, ' $1 ')
                                chinese = chinese.replace(/(\？)/g, ' $1 ')
                                chinese = chinese.replace(/(\！)/g, ' $1 ')
                                chinese = chinese.replace(/(\《)/g, ' $1 ')
                                chinese = chinese.replace(/(\》)/g, ' $1 ')
                                chinese = chinese.replace(/(\“)/g, ' $1 ')
                                chinese = chinese.replace(/(\”)/g, ' $1 ')
                                chinese = chinese.replace(/(\‘)/g, ' $1 ')
                                chinese = chinese.replace(/(\’)/g, ' $1 ')
                                chinese = chinese.replace(/(\（)/g, ' $1 ')
                                chinese = chinese.replace(/(\）)/g, ' $1 ')




                                chinese = chinese.replace(/([^\r\n\S]{2,999})/g, ' ')
                                // chinese = chinese.replace(/(\p{P})/gu, ' $1 ')  // 正则匹配所有中文标点

                                // src_train.write(english + '\n') 
                                // tgt_train.write(chinese + '\n')

                                arr1.push(english + '\n')
                                arr2.push(chinese + '\n')

                            }

                        }
                    })
                    rs.on('end', function () {
                        // src_train.end()
                        // tgt_train.end()
                        //console.log(`done one task ${fpath}`)
                        return resolve2({ msg: 'ok.' })


                    })

                })

                return { msg }

            }

            let { msg: m1 } = await read_big_file(fpath1, src_trains, tgt_trains)
            let { msg: m2 } = await read_big_file(fpath2, src_vals, tgt_vals)


            async function writeSync(arr, steam) {

                for (let s of arr) {

                    steam.write(s)

                }

                await new Promise(async function (resolve_, reject_) {
                    steam.end(() => {
                        return resolve_('done.')
                    })
                })

                return {msg:'done'}

            }

            let chunks1 = _.chunk(src_vals, src_vals.length - 100)  // 分一百作测试集
            let chunks2 = _.chunk(tgt_vals, tgt_vals.length - 100)


            src_vals = chunks1[0]
            tgt_vals = chunks2[0]

            src_tests = chunks1[1]
            tgt_tests = chunks2[1]


            await writeSync(src_trains, src_train)
            await writeSync(tgt_trains, tgt_train)

            await writeSync(src_vals, src_val)
            await writeSync(tgt_vals, tgt_val)

            await writeSync(src_tests, src_test)
            await writeSync(tgt_tests, tgt_test)

            return resolve({ msg: 'ok.' })

        })


        let ens = 'file too large to return string'
        let chts = '文件太大，无法返回字符串'

        return { ens, chts }

    }

    let { ens, chts } = await convert('./translation2019zh_train.json', './translation2019zh_valid.json')

})()
```



## write line by line

```javascript
            var fs = require('fs')
            var src_train = fs.createWriteStream('src-train.txt', {flags: 'a' }) // 'a' means appending (old data will be preserved)
            src_train.write('some data') // append string to your file
            src_train.write('more data') // again
            src_train.write('and more') // again
```



## appendFileSync

```

require('fs').appendFileSync('log.txt', `${new Date().toUTCString()}  ${s}\n`, 'utf-8')

const fileName = 'file-sync.txt'
fs.appendFileSync(fileName, 'First line added!', 'utf-8')
```





## 去掉扩展名



```
imgName = path.parse(imgName).name  // 去掉扩展名
let { base,dir,ext,name,root} = path.parse(mlpath)
```



## rename

```
fs.renameSync( oldPath, newPath )
```



## 遍历目录读取word



```

# docx.js

let rd = require('rd');
let fs = require('fs');
let path = require("path")

var mammoth = require("mammoth")
//const AdmZip = require('adm-zip'); //引入查看zip文件的包

module.exports = {
    //
    // 目录下所有docx 的内容文本
    //
    contents : async function(dir) {

        var arr = []

        var paths = []

        // 目录下的所有文件名
        rd.eachFileFilterSync(dir, /\.docx$/, function (fullpath, stats) {

            let basename = path.basename(fullpath)
            if (basename != "A1-3.docx") {
                return
            }

            paths.push(fullpath)
        })

        for (let i = 0; i < paths.length; i++) {
            let content = await getContent(paths[i])
            arr.push(content)
        }

        return arr
    }
}


function getContent(fileName) {
    return new Promise((resolve, err) => {
        // var url = path.join(__dirname, 'A1-3-2.docx');
        // var url = path.join(__dirname, "../../../file/" + fileName);
        var url = fileName
        mammoth.extractRawText({
                path: url
            })
            .then(function (result) {
                var text = result.value // The raw text
                var messages = result.messages
                resolve(text)

            })
            .catch((e) => {
                err(false)
            })
            .done()
    })
}
```



## 遍历目录下的所有目录名

```
    // get all episodes
    let dir_name = path.resolve('.', 'vectors', type, lang, name)
    const episodes = fs.readdirSync(dir_name, { withFileTypes: true })
        .filter((item) => item.isDirectory())
        .map((item) => item.name)
```



## 文件时间

- https://www.geeksforgeeks.org/node-js-fs-utimessync-method/







## 图片



```

		if (!fs.existsSync(gifpath)) {
          return [null, `图片不存在${gifpath}`]
        }

        let bytes = fs.readFileSync(gifpath)  // 'binary'
        let b64 = Buffer.from(bytes).toString('base64')  // new Buffer(bytes)
        b64s.push(b64)
        
        
        Buffer.from(b64, 'base64')
        
        
```



## 对象序列化

```
npm install protobufjs --save --save-prefix=~
	# https://zhuanlan.zhihu.com/p/31755487



```





## platform



```javascript
    let platform = process.platform
    let platforms = [ 'win32', 'linux', 'darwin' ]
    if ( ! platforms.includes( platform ) ) {
        throw 'unknow os type.'
    }
```





# 多线程

- https://zhuanlan.zhihu.com/p/35353355

  > Node黑魔法之无痛用上多线程

- https://www.cnblogs.com/flydean/p/14310278.html
  
  > nodejs中使用worker_threads来创建新的线程 



## worker

```
    // 所有词的理论概率
    calc_theory_p:{
        // 开多线程，计算真实概率 是 理论概率的多少倍
        let re = await new Promise(async (resolve, reject) => {
            let start = 2
            let numThread = NGram - start + 1
            let threadDone = 0
            for (let n = start; n <= NGram; n++) {
                const { Worker, workerData, parentPort } = require('worker_threads')
                const wk1 = new Worker(require('path').resolve(__dirname, './threads/theory_p.js'))
                wk1.ref()
                wk1.postMessage({ "thread_id": n, dic_NGrams, n })
                wk1.on('message', async (re) => {
                    threadDone++
                    console.log(`calc theory_p curr/numThread: ${threadDone} / ${numThread}`)
                    if (threadDone >= numThread) {
                        resolve('ok')
                    }
                })
            }
        })
    }
    
    
    
# theory_p.js    
const { parentPort } = require('worker_threads')
parentPort.onmessage = function (event) {
    let { thread_id, dic_NGrams, n } = event.data
    parentPort.postMessage([true, { thread_id, dic_NGrams, n }])
}
```



## 进程间通信

[comlink 进程间通信](https://github.com/GoogleChromeLabs/comlink)







## napajs



```
const { Worker, isMainThread, workerData } = require('worker_threads');

if (isMainThread) {
  const worker = new Worker(__filename, { workerData: 'Hello, world!' });
} else {
  console.log(workerData);  // Prints 'Hello, world!'.
}
```



```
console.time('timeout test');
zone.execute(() => { while (true) {} }, [], { timeout: 50})
    .catch((error) => {
        console.timeEnd('timeout test');
    });
```





```
const napa = require("napajs");
const fs = require("fs");

const myUTFString="éóíúã’“";

const zone = napa.zone.create("zone", {workers: 1});
const store = napa.store.create("store");
store.set("string", myUTFString);

zone.broadcast(`
    function example () {
        const str = global.napa.store.get("store").get("string");
        console.log(str);
        return str;
    }
`);

zone.execute("", "example").then(result => {
    console.log(result.value)
});
```

```
n your case, the code can be updated like this:

myLib.prototype.deflate = async function (data, key, compress)  {
    var buffer = new Uint8Array(data.buffer, data.byteOffset, data.byteLength);
    var result = await this.zone.execute('','deflateFunc', [buffer, key, compress])
    return result.value;
};

myLib.prototype.inflate = async function (data, key, compressed, type)  {
    var buffer = new Uint8Array(data.buffer, data.byteOffset, data.byteLength);
    var result = await this.zone.execute('','inflateFunc', [buffer, key, compressed, type])
    return result.value;
};
EDIT: to explain why the stack happened.

The type Buffer in Node.js is implemented Uint8Array after Node 4.x. Thus TypedArray.prototype.length is available on a Buffer object.

The transported Buffer object in napa zone, however, as explained above, is treated as a plain object. It does not have a length property. There is some code similar to while (buf.length !== 0) { ... } in xxtea-node. It's always true (undefined !== 0 is always true) so the while loop will never break.
```





### global 

- https://github.com/microsoft/napajs/issues/26

```
var napa = require('napajs');
var zone = napa.zone.create('zone1');
function test() {
   console.log('hello world');
}
zone.broadcast(test.toString());
zone.execute(() => { global.test(); }, []);
```



### timeout

```javascript
var napa = require("napajs")

const NUMBER_OF_WORKERS = 1

var zone = napa.zone.create('zone', { workers: NUMBER_OF_WORKERS })

// var p1 = zone.execute("", "fibonacci", [n - 1])

zone.execute(() => { while (true) {} }, [], { timeout: 3000})
    .catch((error) => {
        console.log(`end.`)
    });

console.log('hi,,,')
```



### calc fibonacci

```
//fibonacci.js
var napa = require("napajs");

// Change this value to control number of napa workers initialized.
const NUMBER_OF_WORKERS = 4;

// Create a napa zone with number_of_workers napa workers.
var zone = napa.zone.create('zone', { workers: NUMBER_OF_WORKERS });

/*
Fibonacci sequence 
n:              |   0   1   2   3   4   5   6   7   8   9   10  11  ...
-------------------------------------------------------------------------
NTH Fibonacci:  |   0   1   1   2   3   5   8   13  21  34  55  89  ...
*/
function fibonacci(n) {
    if (n <= 1) {
        return n;
    }

    var p1 = zone.execute("", "fibonacci", [n - 1]);
    var p2 = zone.execute("", "fibonacci", [n - 2]);

    // Returning promise to avoid blocking each worker.
    return Promise.all([p1, p2]).then(([result1, result2]) => {
        return result1.value + result2.value;
    });
}

function run(n) {
    var start = Date.now();

    return zone.execute('', "fibonacci", [n])
        .then(result => {
            printResult(n, result.value, Date.now() - start);
            return result.value;
        });
}

function printResult(nth, fibonacci, ms) {
    console.log('\t' + nth
          + '\t' + fibonacci
          + '\t\t' + NUMBER_OF_WORKERS
          + '\t\t' + ms);
}

console.log();
console.log('\tNth\tFibonacci\t# of workers\tlatency in MS');
console.log('\t-----------------------------------------------------------');

// Broadcast declaration of 'napa' and 'zone' to napa workers.
zone.broadcast(' \
    var napa = require("napajs"); \
    var zone = napa.zone.get("zone"); \
');
// Broadcast function declaration of 'fibonacci' to napa workers.
zone.broadcast(fibonacci.toString());

// Run fibonacci evaluation in sequence.
run(10)
.then(result => { run(11)
.then(result => { run(12)
.then(result => { run(13)
.then(result => { run(14)
.then(result => { run(15)
.then(result => { run(16)
}) }) }) }) }) })
```



### 并行快排

- https://github.com/microsoft/napajs/blob/master/examples/tutorial/parallel-quick-sort/parallel-quick-sort.js




# stream

- http://nodejs.cn/api/stream/stream_pipeline_streams_callback.html



```

const fs = require('fs')
const { promisify } = require('util')
const stream = require('stream')
const pipeline = promisify(stream.pipeline)
const bent = require('bent')

const main = async () => {
  const readable = await bent('https://images.unsplash.com/photo-1595132938692-83ad2c098e47')()
  const writable = fs.createWriteStream('./image.jpg')
  await pipeline(readable, writable)
}

main()
```



```
var http = require('http'),
    url = require('url'),
    fs   = require('fs'),
    filePath = '/home/risto/Downloads/oleg.mp3',
    stat = fs.statSync(filePath);

http.createServer(function(request, response) {
    var queryData = url.parse(request.url, true).query;
    const skip = typeof(queryData.skip) == 'undefined' ? 0 : queryData.skip;
    const startByte = stat.size * skip;

    response.writeHead(200, {
        'Content-Type': 'audio/mpeg',
        'Content-Length': stat.size - startByte
    });

    // We replaced all the event handlers with a simple call to util.pump()
    fs.createReadStream(filePath, {start:startByte}).pipe(response);
})
.listen(2000);
```

```
var http = require('http'),
    url = require('url'),
    fs   = require('fs'),
    filePath = '/home/risto/Downloads/oleg.mp4',
    stat = fs.statSync(filePath);

http.createServer(function(request, response) {        
    const fileSize = stat.size;
    const range = request.headers.range;
    if (range) {
      const parts = range.replace(/bytes=/, "").split("-");
      const start = parseInt(parts[0], 10);
      const end = parts[1] 
        ? parseInt(parts[1], 10)
        : fileSize - 1;
      const chunksize = (end - start) + 1;
      const readStream = fs.createReadStream(filePath, { start, end });
      const head = {
        'Content-Range': `bytes ${start}-${end}/${fileSize}`,
        'Accept-Ranges': 'bytes',
        'Content-Length': chunksize,
        'Content-Type': 'video/mp4',
      };
      response.writeHead(206, head);
      readStream.pipe(response);
    } else {
      const head = {
        'Content-Length': fileSize,
        'Content-Type': 'video/mp4',
      };
      response.writeHead(200, head);
      fs.createReadStream(filePath).pipe(response);
    }
})
.listen(2000);
```





# process

## 多线程下载

[多线程下载](https://github.com/develon2015/Youtube-dl-REST)

```
The argument to execa is a command followed by an array of arguments, unless the shell: true option is used. So this should be either execa('npm', ['run', 'start']) or execa('npm run start', { shell: true }).

// 不要忘记 -y 参数，否则或一直等你确认是否覆盖文个
import { execa } from 'execa'
import path from 'path'
import { dirname } from 'path'
//global.__dirname = process.cwd()
import { fileURLToPath } from 'url'
const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

export default {
    extractSubtitle: async function (vdpath, type, nth) {

        try {

            let args = `ffmpeg -i ${vdpath} -y -map 0:s:${nth} ${path.join( __dirname, tmp.srt )}`
            let subprocess = execa(args, {shell:true})
            await subprocess

        } catch(err) {
            a = 1
        }

        return 'hi,,,'
    }
}

```



```
// https://github.com/sindresorhus/execa/
let subprocess = execa('dir', [''], { 'encoding': 'utf8' })
        //let subprocess = execa('ffmpeg', ['-i', vdpath, 'tmp.srt'], { 'encoding': 'utf8' }) // [ '-i', vdpath, '-map', `0:s:${nth}`, 'tmp.srt']
        subprocess.stdout.pipe(process.stdout);
        let { stdout } = await subprocess
        console.log('child output:', stdout)

        await subprocess
```





```
var exec = require('child_process').exec;  // 出错
	//   "type": "commonjs",  // package.json 加上这一句
```



```
# https://github.com/sindresorhus/execa/issues/145
const { stdout: customPath2 } = execa.shellSync(
  'git config --get core.hooksPath  &2>/dev/null'
)
console.log('Path, ', customPath2)
```



```
var spawn = require('child_process').spawn;
var path = require('path');
var fs = require('fs');

var barPath = path.join(__dirname, 'child.js');
var outputPath = path.join(__dirname, 'output.txt');

var s = fs.createWriteStream(outputPath);

s.on('open', () => {
	spawn(process.execPath, [barPath], {
		stdio: [null, s, null]
	});
});
```



##  全局错误

```
//捕获全局未捕捉的错误
process.on('uncaughtException', function (erro) {
    console.error('##### 全局错误:');
    console.error(erro);
})
```





## 失败重试



```
// https://github.com/sindresorhus/execa
import pRetry from 'p-retry';

const run = async () => {
	const results = await execa('curl', ['-sSL', 'https://sindresorhus.com/unicorn']);
	return results;
};

console.log(await pRetry(run, {retries: 5}));
```



## 改变进程当前路径

```
// https://github.com/rapidsai/node/blob/main/modules/demo/client-server/index.js
const Path = require('path');

// Change cwd to the example dir so relative file paths are resolved
process.chdir(__dirname);

const next = require.resolve('next/dist/bin/next');

require('fs').stat(Path.join(__dirname, '.next'), (err, stats) => {
  const {spawnSync} = require('child_process');

  const env = {
    NEXT_TELEMETRY_DISABLED: 1,  // disable https://nextjs.org/telemetry
    ...process.env,
  };

  if (err || !stats || !stats.isDirectory()) {
    spawnSync(process.execPath, [next, 'build'], {env, cwd: __dirname, stdio: 'inherit'});
  }

  spawnSync(process.execPath, [next, 'start'], {env, cwd: __dirname, stdio: 'inherit'});
});
```



## childProcess

[Windows: execa leaving processes around when running npm scripts in a sh shell](https://github.com/sindresorhus/execa/issues/433)

```
const childProcess = require('child_process')
const spawned = childProcess.spawn('npm', ['run', 'tsc'], { stdio: 'inherit', shell: true, windowsHide: true })
process.on('exit', () => { spawned.kill() })

```



````
const { spawn } = require('child_process');

// 创建一个新的 Python 子进程
const python = spawn('python');

// 当收到子进程的输出时，将其打印到控制台
python.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

// 当子进程发生错误时，将错误打印到控制台
python.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

// 当子进程退出时，打印退出码
python.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});

// 向 Python 子进程发送命令
python.stdin.write('print("Hello, World!")\n');
python.stdin.write('for i in range(5): print(i)\n');

// 告诉 Python 我们不会再发送更多的命令了
python.stdin.end();
````



### process.cwd

```
__dirname and __filename process.cwd()
```



### process.chdir

```
const process = require('process');
 
try {
 
  // Change the directory
  process.chdir('../os');
  console.log("directory has successfully been changed");
} catch (err) {
     
  // Printing error if occurs
  console.error("error while changing directory");
}
```





### 乱码

```
# echodict\chatgpt_server\lib\fakeopen_cli_chatgpt.mjs
import { resolve } from 'node:path'
import { pathToFileURL } from 'node:url'
import { spawn } from 'child_process'

// const  iconvLite = require('iconv-lite')

const spawned = spawn('python', ['main.py'], { 
    //stdio: 'inherit', // 子进程和父进程的 stdin stdout 连接起来
    stdio: 'pipe', 
    shell: true, 
    windowsHide: true,
    cwd: 'D:/GitHub/echodict/pandora'
})

spawned.stdin.write('1\n')
// spawned.stdin.end()

// 当收到子进程的输出时，将其打印到控制台
let ts = ``
spawned.stdout.on('data', (data) => {
  ts += data.toString()
  console.log(`stdout: ${data}`);
})

process.on('exit', () => { 
    spawned.kill() 
})
```





```
# 乱
var child_process = require('child_process') 
child_process.exec('ipconfig', { encoding:“utf-8”}, function(err, stdout, stderr){
    console.log(stdout, stderr)
})

```



```
# ok?
var child_process = require('child_process');
var iconv = require('iconv-lite');
var encoding = 'cp936';
var binaryEncoding = 'binary';
 
child_process.exec('ipconfig', { encoding: binaryEncoding }, function(err, stdout, stderr){
    console.log(iconv.decode(new Buffer(stdout, binaryEncoding), encoding), iconv.decode(new Buffer(stderr, binaryEncoding), encoding));
})
```





##  execa

```
# echodict\pmserver\lib\ffmpeg.js

	extractImage: async function(vdpath, begin_time) {
        let { execa } = await import('execa')
        let MemoryStream = require('memorystream')
        let memStream = new MemoryStream(null, {readable : false})
        try {

            // 精准截图
            // ffmpeg -accurate_seek -avoid_negative_ts 1 -i 1.mkv -ss 5 -vframes 1 xxxxxxxxxx.jpg

            let cmd = `ffmpeg -accurate_seek -avoid_negative_ts 1 -i "${vdpath}" -ss ${begin_time} -vframes 1 -f mjpeg -y pipe:1`   //-f ${type} pipe:1 write stdout

            let childProcess = execa(cmd, {shell:true})
            childProcess.stdout.pipe(memStream)
            let { stdout } = await childProcess

            let buffer = Buffer.concat(memStream['queue'])  // array of buffer, to one buffer
            // require('fs').writeFileSync(__dirname + '/1.jpg', buffer, 'binary')
            memStream.destroy()

            return { im: buffer }

        } catch(err) {
           return { au:null}
        }
    }
```



```
    convert2srt:async function(subpath) {

        // ffmpeg -i F:\video.mkv -vn -an -codec:s:0 srt F:\subtitle.srt

        let { execa } = await import('execa')

        try {

            let cmd = `ffmpeg -i "${subpath}" -f srt pipe:1`  // write stdout

            let childProcess = execa(cmd, {shell:true, 'encoding': 'utf8'})
            let { stdout } = await childProcess

            return { srt:stdout, msg:''}

        } catch(err) {
           return { msg : err }
        } 
    }
```





## 优先读取环境变量

```javascript
/**加载配置文件 */
function loadConfig() {

  let config = ''

  // 优先读取环境变量
  if (process.env.CONFIG_ENV) {

    config = JSON.parse( process.env.CONFIG_ENV )

  } else {
    const path = `${startPath}/config.js`;
    config = require(path);
  }

  Object.defineProperty(global, "conf", {
    get: function () {
      return config
    }
  });
  Object.defineProperty(global, "config", {
    get() {
      return global.conf.dataSet;
    }
  });
}
```



# interop

## python

- https://github.com/hmenyus/node-calls-python

- https://github.com/extrabacon/python-shell

### 源码编译

- https://blog.51cto.com/u_15069442/4117615



```

编译环境 win10 + vs2019

cd Python-3.8.16\PCbuild
./get_externals.bat
	# 安装 

Python-3.8.16\PCbuild\pcbuild.sln
	# 打开解决方案
	
选择python 项目，编译类型为 x64，开始编译

注意：
	编译出来的 dll 和 exe 依赖 Python-3.8.16\Lib 这个目录，里面有各种 python 脚本
	Lib 或者和可执行文件同级目录，或着在它的上级，会一直往上找，找不到就报错了
	

dll 入口, python.c重命名为 python.cc，代码改成下面这样
#include "Python.h"
#include "pycore_pylifecycle.h"

extern "C" __declspec(dllexport) int wmain(int argc, wchar_t* wargv[]) {
    return Py_Main(argc, wargv);
}

#ifdef MS_WINDOWS
int mmain(int argc, wchar_t **argv)
{
    return wmain(argc, argv);
}


exe 入口，test_python_dll.cc
#include <iostream>

#include "windows.h"
#include <direct.h>

#include <Shlwapi.h>
#pragma comment(lib, "shlwapi.lib")

void call_node_dll() {
    HINSTANCE   ghDLL = NULL;
    ghDLL = LoadLibrary("D:\\GitHub\\node-14.21.1\\out\\Debug\\node.dll");

    typedef int(_cdecl* FunctionPtr) (int argc, wchar_t* wargv[]);

    FunctionPtr wmain;

    wmain = (FunctionPtr)GetProcAddress(ghDLL, "wmain");

    int argc = 2;

    wchar_t* wargv[] = {
      (wchar_t*)L"C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\node2.exe",
      //(wchar_t*)L"C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\pmserver\\server.js",
      (wchar_t*)L"D:\\GitHub\\echodict\\pmserver\\server.js"
    };

    wmain(argc, wargv);

    std::cout << "Hello World!\n";
}

void call_python_dll(int argc, char* argv[]) {
    HINSTANCE   ghDLL = NULL;
    //ghDLL = LoadLibrary("E:\\python\\Python-3.8.16\\PCbuild\\amd64\\python38_d.dll");

    //string str = System.AppDomain.CurrentDomain.SetupInformation.ApplicationBase;

    

    char dll_path[MAX_PATH] = { 0 };
    ::GetModuleFileName(nullptr, dll_path, MAX_PATH);
    ::PathRemoveFileSpec(dll_path);
    ::PathAppend(dll_path, "python38_d.dll");
    
    ghDLL = LoadLibrary(dll_path);

    //ghDLL = LoadLibrary("F:\\python\\Python-3.8.16\\PCbuild\\amd64\\python38_d.dll");

    typedef int(_cdecl* FunctionPtr) (int argc, wchar_t* argv[]);


    FunctionPtr wmain;

    wmain = (FunctionPtr)GetProcAddress(ghDLL, "wmain");

    wchar_t* wargv[] = {
      (wchar_t*)L"C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\node2.exe",
      //(wchar_t*)L"C:\\projects\\edge-js\\tools\\build\\node-14.21.1\\out\\Debug\\pmserver\\server.js",
      //(wchar_t*)L"D:\\GitHub\\echodict\\pmserver\\server.js"
    };

    wmain(1, wargv);

    std::cout << "Hello World!\n";
}

int main(int argc, char* argv[])
{
    //call_node_dll();

    call_python_dll(argc, argv);
}

	
```



# ffmpeg.wasm

[ffmpeg.wasm render video in canvas](https://www.mysourcebook.com/2023/01/decode-big-video-using-ffmpeg-wasm-to-render-use-canvas.html)

[How to enable HTTPS protocol in ffmpeg.wasm?](https://www.mysourcebook.com/2023/01/how-to-enable-https-protocol-in-ffmpeg.wasm.html)

[高性能WASM播放器实现](https://github.com/ErosZy/md/blob/master/%E9%AB%98%E6%80%A7%E8%83%BDWASM%E6%92%AD%E6%94%BE%E5%99%A8%E5%AE%9E%E7%8E%B0/%E9%AB%98%E6%80%A7%E8%83%BDWASM%E6%92%AD%E6%94%BE%E5%99%A8%E5%AE%9E%E7%8E%B0.md)

[lossless-cut typescript视频剪辑](https://github.com/mifi/lossless-cut)





```
`
https://github.com/FFmpeg-wasm/FFmpeg.wasm
	# 这个 fork 支持 nodejs
	npm install "@ffmpeg.wasm/main" "@ffmpeg.wasm/core-mt"
`
import { readFile, writeFile } from "fs/promises";
import { FFmpeg } from "@ffmpeg.wasm/main";

const ffmpeg = await FFmpeg.create({ core: "@ffmpeg.wasm/core-mt" });

ffmpeg.fs.writeFile("1.mp3", await readFile("./1.mp3"));
await ffmpeg.run("-i", "1.mp3", "2.aac");
await writeFile("./2.aac", ffmpeg.fs.readFile("2.aac"));
process.exit(0);
```



```

npm install @ffmpeg/ffmpeg@0.8.0
	# 0.8.0 + node14 可以正常加载

npm install @ffmpeg/ffmpeg@0.11.6
	# 从 0.12.0 版本开始它不再支持 nodejs

https://github.com/FFmpeg-wasm/FFmpeg.wasm
	# 这个 fork 支持 nodejs
	npm install "@ffmpeg.wasm/main" "@ffmpeg.wasm/core-mt"

launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "node",
            "request": "launch",
            "name": "Launch Program",
            "skipFiles": [
                "<node_internals>/**"
            ],
            //"program": "${workspaceFolder}\\m.mjs",
            "args": ["--experimental-wasm-threads", "${workspaceFolder}/m.mjs"]
        }
    ]
}


# need newest node18 version
npm install @ffmpeg/ffmpeg @ffmpeg/core --save

(async () => {
    let { writeFile } = await import('fs/promises')
    let { createFFmpeg, fetchFile } = await import('@ffmpeg/ffmpeg')
    let ffmpeg = createFFmpeg({ log: true })
    await ffmpeg.load()

    ffmpeg.FS('writeFile', '1.mkv', await fetchFile('./1.mkv'))
    await ffmpeg.run('-i', '1.mkv', "-ss", "00:00:03", "-to", "00:00:04", '1.mp4')
    await require('fs').writeFileSync('./1.mp4', ffmpeg.FS('readFile', '1.mp4'))
    process.exit(0)
})()
```



```
 var Module = {};

   fetch('https://example.com/ffmpeg.wasm')
      .then(response => response.arrayBuffer())
      .then(bytes => WebAssembly.instantiate(bytes, Module))
      .then(results => {
         Module.instance = results.instance;
         // FFmpeg.wasm is now loaded and ready to use
      });
```





```
getting error message RuntimeError: indirect call to null when using libx265 but libx264 works with same settings
await ffmpeg.run( '-ss', '30', '-t', '3', '-i', 'input.bin', '-movflags',  '+faststart', '-vf', "scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse,format=yuv420p", '-c:v', 'libx265', '-crf', '28', '-an', 'output.mp4'  );
```



## Extract Video Subtitle



- https://github.com/YaoFANGUK/video-subtitle-extractor



```python
"""
git clone https://github.com/YaoFANGUK/video-subtitle-extractor.git

pip install -r requirements.txt  # for backend

opencv-python==4.5.4.60
python-Levenshtein-wheels==0.13.2
paddlepaddle==2.1.3
filesplit==3.0.2
pysrt==1.1.2
wordsegment==1.3.1
imgaug==0.4.0
pyclipper==1.3.0.post2
lmdb==1.2.1
"""

subtitle_area = (self.ymin, self.ymax, self.xmin, self.xmax)
from backend.main import SubtitleExtractor
self.se = SubtitleExtractor(self.video_path, subtitle_area) 
# 'D:/Downloads/火影忍者天空树双语/火影忍者001天空树双语.mp4'
#  (834, 897, 0, 1280)


    def _compare_ocr_result(self, img1, img2):
        """
        比较两张图片预测出的字幕区域文本是否相同
        """
        area_text1 = "".join(self.__get_area_text(self.ocr.predict(img1)))
        area_text2 = "".join(self.__get_area_text(self.ocr.predict(img2)))
        if ratio(area_text1, area_text2) > config.THRESHOLD_TEXT_SIMILARITY:
            return True
        else:
            return False
        
        
        
        
        
         # 删除缓存
        if os.path.exists(self.raw_subtitle_path):
            os.remove(self.raw_subtitle_path)
        # 新建文件
        f = open(self.raw_subtitle_path, mode='w+', encoding='utf-8')

        for i, frame in enumerate(frame_list):
            # 读取视频帧
            img = cv2.imread(os.path.join(self.frame_output_dir, frame))
            # 获取检测结果
            dt_box, rec_res = text_recogniser.predict(img)
            # 获取文本坐标
            coordinates = self.__get_coordinates(dt_box)
            # 将结果写入txt文本中
            text_res = [(res[0], res[1]) for res in rec_res]
            # 进度条
            self.progress = i / len(frame_list) * 100
            for content, coordinate in zip(text_res, coordinates):
                if self.sub_area is not None:
                    s_ymin = self.sub_area[0]
                    s_ymax = self.sub_area[1]
                    s_xmin = self.sub_area[2]
                    s_xmax = self.sub_area[3]
                    xmin = coordinate[0]
                    xmax = coordinate[1]
                    ymin = coordinate[2]
                    ymax = coordinate[3]
                    if s_xmin <= xmin and xmax <= s_xmax and s_ymin <= ymin and ymax <= s_ymax:
                        print(content[0])
                        if content[1] > config.DROP_SCORE:
                            f.write(f'{os.path.splitext(frame)[0]}\t'
                                    f'{coordinate}\t'
                                    f'{content[0]}\n')
                else:
                    f.write(f'{os.path.splitext(frame)[0]}\t'
                            f'{coordinate}\t'
                            f'{content[0]}\n')
        # 关闭文件
        f.close()
        
```





```
from tools.infer import utility
from tools.infer.predict_system import TextSystem

import config
from config import interface_config

import cv2


if __name__ == '__main__':

    args = utility.parse_args()

    args.use_gpu = False
    
    # 加载快速模型
    args.det_model_dir = config.DET_MODEL_FAST_PATH
    # 加载快速模型
    args.rec_model_dir = config.REC_MODEL_FAST_PATH

    # 设置字典路径
    args.rec_char_dict_path = config.DICT_PATH
    # 设置识别文本的类型
    args.rec_char_type = config.REC_CHAR_TYPE

    recogniser = TextSystem(args)

    img = cv2.imread('1.png')

    detection_box, recognise_result = recogniser(img)

    a = 1
```







#### 提取关键帧图片带时间

```
"""
ffmpeg -skip_frame nokey -i 1.mp4 -r 1000 -vsync 0 -frame_pts true tmp/out%d.png
	# 只要关键帧，数字代表的时间是毫秒数（1/1000秒）
skip_frame tells the decoder to process only keyframes. -vsync 0 (in this command) preserves timestamps. -frame_pts sets the numeral portion of the output image filename to represent the timestamp. The interpretation of the number requires you to know the framerate e.g. if the framerate is 30 then an image name of out75 corresponds to a timestamp of 75/30 = 2.50 seconds. You can add -r 1000 if you want numbers to represent milliseconds.
"""

ffmpeg: extract key frames only and get their exact timestamps


Extract only keyframes (I-frames) from video to images with console ffmpeg

ffmpeg -ss <start_time> -i video.mp4 -t <duration> -q:v 2 -vf select="eq(pict_type\,PICT_TYPE_I)" -vsync 0 frame%03d.jpg

ffmpeg -i 1.mp4 -q:v 2 -vf select="eq(pict_type\,PICT_TYPE_I)" -vsync 0 frame%03d.jpg

```



#### 剪视频



```
ffmpeg -ss 00:01:00 -i input.mp4 -to 00:02:00 -c copy output.mp4

# 需重新编码，含非关键帧
ffmpeg -i movie.mp4 -ss 00:00:03 -t 00:00:08 -async 1 cut.mp4

//			.outputOptions(["-movflags", "frag_keyframe+empty_moov"]) //without these options ffmpeg errors with `muxer does not support non seekable output`

```





#### 分离人声伴奏

```
# https://github.com/deezer/spleeter
```







```
# https://github.com/YaoFANGUK/video-subtitle-extractor

from backend.main import SubtitleExtractor
# 输入视频路径
# 新建字幕提取对象
se = SubtitleExtractor(video_path, subtitle_area)
# 开始提取字幕
se.run()
```



#### 音频数字指纹

- https://github.com/xitu/gold-miner/blob/master/TODO/fingerprinting-and-audio-recognition-with-python.md
  - 用 Python 和 Numpy 实现音频数字指纹特征识别



# libsixel 有意思的图片格式

[libsixel](https://github.com/saitoha/libsixel)

```
在 iTerm2 里要展示一个图像文件，可以用脚本 imgcat 。下载之后，在 iTerm2 里运行下述命令即可。

./imgcat a.png
这个命令干了什么呢？仔细读一读源码，发现它向标准输出打印了如下内容

\033]1337;File=name=图像文件名;size=图像大小;inline=0:图像内容（Sixel编码）;\a
我以前没有用过 Sixel 图像格式，所以查了一下 Wikipedia，原来是一种把图像编码成 ASCII 序列的编码方式。

```





# network



## websocket

```javascript
// 客户端
ws_app_inner_diff.js

const WebSocket = require('ws')

//webSocket服务端地址
let wsBaseURL = 'ws://xxx:7004'

let wsClient = null

init: {

    wsClient = new WebSocket(wsBaseURL);

    wsClient.onopen = () => {

        console.log(wsBaseURL + '连接成功')

        // 开始题库内去重
        start_diff: {

            try {
                wsClient.send(JSON.stringify(
                    { "api": "/xxx/xxx", "params": { "AppID": xxx, "BookID": -1, "userID": "1", "refresh": 0 } })
                )
            } catch (error) {
                console.log(error.msg)
            }

        }

    }
    wsClient.onerror = (error) => {
        setTimeout(() => {
            newClient = new WebSocket(wsBaseURL);
            newClient.onopen = wsClient.onopen;
            newClient.onerror = wsClient.onerror;
            newClient.onmessage = wsClient.onmessage;
            wsClient = newClient;
        }, 1000);
    }
    wsClient.onmessage = (msg) => {
        let data = JSON.parse(msg.data);
    }
}
```



```
WebSocket.close() # 如果连接已经关闭，则此方法不执行任何操作。

    wsClient.onclose = (event) => {
    	let { code, reason, wasClean } = event
        console.log('The connection has been closed successfully.');
    }
```



## show ip

```
function getIpAddress() {
    const os = require('os');
    let ifaces = os.networkInterfaces()
    for (let dev in ifaces) {
        let iface = ifaces[dev]
        for (let i = 0; i < iface.length; i++) {
            let { family, address, internal } = iface[i]
            if (family === 'IPv4' && address !== '127.0.0.1' && !internal) {
                return address
            }
        }
    }
}
console.log(getIpAddress()) 
```







# args



```
var arguments = process.argv
console.log( arguments )
```






# tuple



```javascript
function getCoordinates(element) {
  let x, y, z;

  return [x, y, z];
}
```



```javascript
// with returned objects
const {x: Ax, y: Ay, z: Az } = getCoordinates(A);
const {x: Bx, y: By, z: Bz } = getCoordinates(B);
// with returned tuples
const [Ax, Ay, Az] = getCoordinates(A);
const [Bx, By, Bz] = getCoordinates(B);

onst [, , thisOne, , thatOne] = getTuple();
const [_1, _2, thisOne, _3, thatOne] = getTuple();

```





# lodash



```javascript
var _ = require('lodash')  // https://lodash.com/docs/4.17.15


修改key

_.mapKeys({ 'a': 1, 'b': 2 }, function(value, key) {
  return key + value;
});
// => { 'a1': 1, 'b2': 2 }


修改value

var users = {
  'fred':    { 'user': 'fred',    'age': 40 },
  'pebbles': { 'user': 'pebbles', 'age': 1 }
};
 
_.mapValues(users, function(o) { return o.age; });
// => { 'fred': 40, 'pebbles': 1 } (iteration order is not guaranteed)
 
// The `_.property` iteratee shorthand.
_.mapValues(users, 'age');
// => { 'fred': 40, 'pebbles': 1 } (iteration order is not guaranteed)
```



## deep copy



```
_.cloneDeep
```



## shuffle

```
arr = _.shuffle(arr)
```







# 异步



```javascript

// 骚操作
// await 外层必须是 async 函数，所以建了一个匿名函数标记为async，并立既调用这个匿名（里面装await）

// 测试接口
// 测试接口

( async()=>{

  // 注意 require 写在外面会出错！！！！！！！！！！！！！！
  var request = require('request')

  async function get() {

    let appename = "ZC_ZXYJHNKX_YTMJ"

    var data = await new Promise(function (resolve) {
  
      url = 'http://101.37.23.135:8005/gettest'
      request.post(url, {
        'form': {
          appename: "ZC_ZXYJHNKX_YTMJ"
        }
      },
      function(err, response, result) {
        if (err || response.statusCode != 200) {
          console.log(url + err + response.statusCode)
          //throw (url + err + response.statusCode)
          return resolve({})
        }
  
        return resolve(result)
      })
  
    })
  
    data = JSON.parse(data).data

    delete data["idArray"]
    delete data["tests"]
    delete data["appEName"]

    return data
  }

  async function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms)
    })
  }

  for (let i = 0; i < 50001; i++) {
    let d = await get()
    console.log(`${i}th : ${JSON.stringify(d)}`)
    await sleep(100)
  }

})()
```



## sleep



```javascript
  async function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms)
    })
  }

await sleep(2000) 
```





## 异步函数是Promise的实例



```
  //进入API
  result = api.handler(data)
  if (result instanceof Promise) {
    result = await result
  }
```





# 随机



```
arr[Math.floor(Math.random() * arr.length)] // 从数组里随机选择一个  Math.random 最小值是0， 最大值小于1
```





# redis

- https://www.digitalocean.com/community/tutorials/how-to-install-secure-redis-centos-7

  > redis-cli -h host -p port -a password
  >
  > ```
  > select 0    # 选择0号数据库
  > keys *name* # 查询key
  > get "defaultDB.user.guid.33"
  > ```
  >
  > 
  >
  > redis-cli -h 127.0.0.1  -p 6379
  >
  > redis-cli -h 127.0.0.1 -p 6379 PING



```
Redisson 的 getLocalCachedMap 对应的 Redis 类型就是 hash 吧，那就没啥问题了啊就是这样用的啊，甚至都不需要这 1000key 吧

使用 redisson 连接的 redis(哨兵)
目前是存人群信息, 分了 1000 个 key (redis 中 key 如果很多的话会有问题么)
1000 个 key 的 value 是 一个大 Map ,存取这个 map 用的是 getLocalCachedMap
map 的每个 key 对应一个人 value 就是他的数据(数据量肯定不大 几百 k 吧)
然后业务集群每天大概请求在 40 -50 亿 然后峰值是 70 亿

我觉得不是很妥当，key 数量并不会显著影响存取性能，但是大 key or 大 value 会显著降低 redis 性能
小于 1k 的键值对操作性能，和 10k 以上的 k-v 操作性能，有数量级差距
印象中 redis hash 结构推荐的 field 数量应该在 100 左右以内


```





```
安装  npm install redis --save

demo

var redis = require('redis');

var client = redis.createClient('6379', '127.0.0.1');

client.auth("password");
client.set('hello','This is a value');
client.expire('hello',10) //设置过期时间
client.exists('key') //判断键是否存在
client.del('key1')
client.get('hello');

//stirng
命令 行为 返回值 使用示例(略去回调函数)
set 设置存储在给定键中的值 OK set('key', 'value')
get 获取存储在给定键中的值 value/null get('key')
del 删除存储在给定键中的值(任意类型) 1/0 del('key')
incrby 将键存储的值加上整数increment incrby('key', increment)
decrby 将键存储的值减去整数increment decrby('key', increment)
incrbyfloat 将键存储的值加上浮点数increment incrbyfloat('key', increment)
append 将值value追加到给定键当前存储值的末尾 append('key', 'new-value')
getrange 获取指定键的index范围内的所有字符组成的子串 getrange('key', 'start-index', 'end-index')
setrange 将指定键值从指定偏移量开始的子串设为指定值 setrange('key', 'offset', 'new-string')
//list
命令 行为 返回值 使用示例(略去回调函数)
rpush 将给定值推入列表的右端 当前列表长度 rpush('key', 'value1' [,'value2']) (支持数组赋值)
lrange 获取列表在给定范围上的所有值 array lrange('key', 0, -1) (返回所有值)
lindex 获取列表在给定位置上的单个元素 lindex('key', 1)
lpop 从列表左端弹出一个值，并返回被弹出的值 lpop('key')
rpop 从列表右端弹出一个值，并返回被弹出的值 rpop('key')
ltrim 将列表按指定的index范围裁减 ltrim('key', 'start', 'end')

//set
命令 行为 返回值 使用示例(略去回调函数) sadd 将给定元素添加到集合 插入元素数量 sadd('key', 'value1'[, 'value2', ...]) (不支持数组赋值)(元素不允许重复)
smembers 返回集合中包含的所有元素 array(无序) smembers('key')
sismenber 检查给定的元素是否存在于集合中 1/0 sismenber('key', 'value')
srem 如果给定的元素在集合中，则移除此元素 1/0 srem('key', 'value')
scad 返回集合包含的元素的数量 sacd('key')
spop 随机地移除集合中的一个元素，并返回此元素 spop('key')
smove 集合元素的迁移 smove('source-key'dest-key', 'item')
sdiff 返回那些存在于第一个集合，但不存在于其他集合的元素(差集) sdiff('key1', 'key2'[, 'key3', ...])
sdiffstore 将sdiff操作的结果存储到指定的键中 sdiffstore('dest-key', 'key1', 'key2' [,'key3...])
sinter 返回那些同事存在于所有集合中的元素(交集) sinter('key1', 'key2'[, 'key3', ...])
sinterstore 将sinter操作的结果存储到指定的键中 sinterstore('dest-key', 'key1', 'key2' [,'key3...])
sunion 返回那些至少存在于一个集合中的元素(并集) sunion('key1', 'key2'[, 'key3', ...])
sunionstore 将sunion操作的结果存储到指定的键中 sunionstore('dest-key', 'key1', 'key2' [,'key3...])
//hash
命令 行为 返回值 使用示例(略去回调函数)
hset 在散列里面关联起给定的键值对 1(新增)/0(更新) hset('hash-key', 'sub-key', 'value') (不支持数组、字符串)
hget 获取指定散列键的值 hget('hash-key', 'sub-key')
hgetall 获取散列包含的键值对 json hgetall('hash-key')
hdel 如果给定键存在于散列里面，则移除这个键 hdel('hash-key', 'sub-key')
hmset 为散列里面的一个或多个键设置值 OK hmset('hash-key', obj)
hmget 从散列里面获取一个或多个键的值 array hmget('hash-key', array)
hlen 返回散列包含的键值对数量 hlen('hash-key')
hexists 检查给定键是否在散列中 1/0 hexists('hash-key', 'sub-key')
hkeys 获取散列包含的所有键 array hkeys('hash-key')
hvals 获取散列包含的所有值 array hvals('hash-key')
hincrby 将存储的键值以指定增量增加 返回增长后的值 hincrby('hash-key', 'sub-key', increment) (注：假如当前value不为为字符串，则会无输出，程序停止在此处)
hincrbyfloat 将存储的键值以指定浮点数增加

//zset
命令 行为 返回值 使用示例(略去回调函数)
zadd 将一个带有给定分支的成员添加到有序集合中 zadd('zset-key', score, 'key') (score为int)
zrange 根据元素在有序排列中的位置，从中取出元素
zrangebyscore 获取有序集合在给定分值范围内的所有元素
zrem 如果给定成员存在于有序集合，则移除
zcard 获取一个有序集合中的成员数量 有序集的元素个数 zcard('key')


keys命令组
命令 行为 返回值 使用示例(略去回调函数)
del 删除一个(或多个)keys 被删除的keys的数量 del('key1'[, 'key2', ...])
exists 查询一个key是否存在 1/0 exists('key')
expire 设置一个key的过期的秒数 1/0 expire('key', seconds)
pexpire 设置一个key的过期的毫秒数 1/0 pexpire('key', milliseconds)
expireat 设置一个UNIX时间戳的过期时间 1/0 expireat('key', timestamp)
pexpireat 设置一个UNIX时间戳的过期时间(毫秒) 1/0 pexpireat('key', milliseconds-timestamp)
persist 移除key的过期时间 1/0 persist('key')
sort 对队列、集合、有序集合排序 排序完成的队列等 sort('key'[, pattern, limit offset count])
flushdb 清空当前数据库
```



## node18

```
        # 旧写法已经连不上了 这个版本可以 "redis": "^3.1.2",
        let { createClient }  = require('redis')

        const client = createClient({ url: 'redis://127.0.0.1:6379' })
        
        client.on('error', (err) => { 
            console.log('Redis Client Error', err) 
        })
        
        await client.connect()

        await client.set('hello','This is a value')
        let re = await client.get('hello')
```





## 性能



```
# https://www.jianshu.com/p/31ab9b020cd9
	Redis-击穿、穿透和雪崩
# https://www.jianshu.com/p/4838f8be00c9
	分布式锁

```



## bit 位操作

- https://xie.infoq.cn/article/0ad770293fb9de05c4f766a94

```
应用场景
实际项目开发中有很多业务都适合采用 redis 的 bit 来实现。

用户签到场景
每天的日期字符串作为一个 key，用户 Id 作为 offset，统计每天用户的签到情况，总的用户签到数
```



## 全文搜索

[OpenAI Embeddings](https://redis-py.readthedocs.io/en/stable/examples/search_vector_similarity_examples.html)

```
# delete index
r.ft(INDEX_NAME).dropindex(delete_documents=True)

# make a new one
create_index(vector_dimensions=VECTOR_DIMENSIONS)
%pip install openai
import openai

# set your OpenAI API key - get one at https://platform.openai.com
openai.api_key = "YOUR OPENAI API KEY"
# Create Embeddings with OpenAI text-embedding-ada-002
# https://openai.com/blog/new-and-improved-embedding-model
response = openai.Embedding.create(input=texts, engine="text-embedding-ada-002")
embeddings = np.array([r["embedding"] for r in response["data"]], dtype=np.float32)

# Write to Redis
pipe = r.pipeline()
for i, embedding in enumerate(embeddings):
    pipe.hset(f"doc:{i}", mapping = {
        "vector": embedding.tobytes(),
        "content": texts[i],
        "tag": "openai"
    })
res = pipe.execute()
embeddings
array([[ 0.00509819,  0.0010873 , -0.00228475, ..., -0.00457579,
         0.01329307, -0.03167175],
       [-0.00357223, -0.00550784, -0.01314328, ..., -0.02915693,
         0.01470436, -0.01367203],
       [-0.01284631,  0.0034875 , -0.01719686, ..., -0.01537451,
         0.01953256, -0.05048691],
       [-0.01145045, -0.00785481,  0.00206323, ..., -0.02070181,
        -0.01629098, -0.00300795]], dtype=float32)
```

search

```
text = "animals"

# create query embedding
response = openai.Embedding.create(input=[text], engine="text-embedding-ada-002")
query_embedding = np.array([r["embedding"] for r in response["data"]], dtype=np.float32)[0]

query_embedding
array([ 0.00062901, -0.0070723 , -0.00148926, ..., -0.01904645,
       -0.00436092, -0.01117944], dtype=float32)
# query for similar documents that have the openai tag
query = (
    Query("(@tag:{ openai })=>[KNN 2 @vector $vec as score]")
     .sort_by("score")
     .return_fields("content", "tag", "score")
     .paging(0, 2)
     .dialect(2)
)

query_params = {"vec": query_embedding.tobytes()}
r.ft(INDEX_NAME).search(query, query_params).docs
```





- [RedisJson](https://redis.io/docs/stack/json/)

  - [最大内存、监听地址什么的](https://idroot.us/install-redis-almalinux-9/)

  - [源码安装出错](https://linux.how2shout.com/enable-crb-code-ready-builder-powertools-in-almalinux-9/)

  - [全流程](https://www.cnblogs.com/zx-admin/p/13772193.html)

  - [使用方法](https://blog.csdn.net/u013421629/article/details/125796393)

  - [备份](https://www.cnblogs.com/weihanli/p/14532388.html)

    - [实战](https://blog.51cto.com/u_15862829/5828039)

  - [所有支持的语言](https://redis.io/docs/stack/search/reference/stemming/)

  - [分词](https://github.com/lionsoul2014/friso)

    - [Chinese Tokenization RediSearch 中文分词的提交记录](https://github.com/RediSearch/RediSearch/pull/219/files)

      > ```
      > RediSearch/tests/ctests/test_cntokenize.c
      > 	# 分词器的测试代码在这里
      > ```
    
    - [mmseg分词算法及实现](https://blog.csdn.net/daniel_ustc/article/details/50488040)
    
    - [hanlp]()
    
      > ```
      > pip install hanlp
      > ```
    
    > ```
    > git clone --recursive https://github.com/RedisJSON/RedisJSON.git && \
    > cd RedisJSON && \
    > ./sbin/setup
    > 
    > 	vi /etc/profile.d/utf8.sh
    > 		# 好像是这个把 utf8 环境搞坏的 
    > export LANG="en_US.utf-8"
    > export LC_ALL="en_US.utf-8"
    > export LANGUAGE="en_US"
    > 			# 内容一定要先改成这样
    > 
    > curl https://sh.rustup.rs -sSf | sh && \
    > source "$HOME/.cargo/env"
    > 
    > make build
    > 
    > git clone --recursive https://github.com/RediSearch/RediSearch.git && \
    > cd RediSearch && \
    > pip3 install conan && \
    > ./sbin/setup && \
    > make setup && \
    > make clean ALL=1 && \ 
    > make build SLOW=1 VERBOSE=1
    > 	https://redis.io/docs/stack/search/development/
    > 	/root/RediSearch/bin/linux-x64-release/search/redisearch.so
    > make run DEBUG=1
    > 	# 必须已安装 redis-server
    > 	# 可以用 GDB 下断点
    > 
    > vi /etc/environment
    > LANG=en_US.utf-8
    > LC_ALL=en_US.utf-8
    > 	# 添加这两项
    > 
    > source /etc/environment
    > 
    > gdb -ex r --args redis-server --loadmodule /root/RediSearch/bin/linux-x64-release/search/redisearch.so --loadmodule /root/RedisJSON/bin/linux-x64-release/rejson.so
    > 	# https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/gdb.html
    > 	# 成功跑起来以后 ctrl + Z 回到 gdb
    > 
    > /root/RediSearch/src/tokenize.c
    > 	GetTokenizer
    > 
    > (gdb) break GetTokenizer
    > (gdb) info b
    > (gdb) r
    > 	# 重新运行
    > 
    > redis-cli
    > 	# 这里执行中文搜索，可以成功触发断点
    > 
    > ./autogen.sh
    > make install
    > friso -init /usr/local/etc/friso/friso.ini
    > 歧义和同义词:研究生命起源，混合词: 做B超检查身体
    > 
    > "-lm" linux vscode 的 gcc 配置要加一个 -lm 参数
    > 
    > next_mmseg_token
    > next_complex_cjk
    > 
    > ```

  > ```
  > # 版本过旧
  > dnf clean all && \
  > dnf install -y epel-release && \
  > dnf update && \
  > dnf install -y redis && \
  > systemctl enable redis && \
  > systemctl start redis && \
  > systemctl status redis && \
  > redis-cli -h 127.0.0.1 -p 6379  PING
  > 
  > ```

- https://github.com/RediSearch/RediSearch

- [RediSearch源码安装方法](https://redis.io/docs/stack/search/development/)

  > vi /etc/environment
  >
  > LANG=en_US.utf-8
  > LC_ALL=en_US.utf-8
  >
  > \# 添加这两项 
  >
  > source /etc/environment
  >
  > a
  >
  > whereis redis-server
  >
  > \# /usr/local/bin/redis-server
  >
  > vi redis.conf 
  >
  > bind 0.0.0.0
  >
  > daemonize yes
  >
  > enable-module-command yes
  >
  > \# 改几两项
  >
  > redis-server /root/redis/redis.conf
  >
  > \# 运行
  >
  > /usr/local/bin/redis-cli  --raw
  >
  > ```
  > MODULE LOAD /root/RedisJSON/bin/linux-x64-release/rejson.so
  > MODULE LOAD /root/RediSearch/bin/linux-x64-release/search/redisearch.so
  > 	# 成功加载两个模块
  > 	loadmodule /root/RedisJSON/bin/linux-x64-release/rejson.so
  > 	loadmodule /root/RediSearch/bin/linux-x64-release/search/redisearch.so
  > 		# 配置文件试加这两行
  > 
  > JSON.SET product:1 $ '{"id":1,"productSn":"7437788","name":"小米8","subTitle":"全面屏游戏智能手机 6GB+64GB 黑色 全网通4G 双卡双待","brandName":"小米","price":2699,"count":1}'
  > 
  > JSON.SET product:2 $ '{"id":2,"productSn":"7437789","name":"红米5A","subTitle":"全网通版 3GB+32GB 香槟金 移动联通电信4G手机 双卡双待","brandName":"小米","price":649,"count":5}'
  > 
  > JSON.SET product:3 $ '{"id":3,"productSn":"7437799","name":"Apple iPhone 8 Plus","subTitle":"64GB 红色特别版 移动联通电信4G手机","brandName":"苹果","price":5499,"count":10}'
  > 
  > JSON.SET product:4 $ '{"id":4,"productSn":"7437801","name":"小米8","subTitle":"他の全文検索シリーズでも同じデータを使うので、他の記事も試す場合は wiki.json.bz2 を捨てずに残しておくことをおすすめします。","brandName":"小米","price":2699,"count":1}'
  > 
  > JSON.SET product:5 $ '{"id":5,"productSn":"7437801","name":"小米9","subTitle":"シリーズでも同じデータをはなる","brandName":"小米","price":2699,"count":1}'
  > 
  > JSON.GET product:1
  > 
  > JSON.GET product:1 name subTitle
  > 
  > FT.CREATE productIdx ON JSON PREFIX 1 "product:" LANGUAGE chinese SCHEMA $.id AS id NUMERIC $.name AS name TEXT $.subTitle AS subTitle TEXT $.price AS price NUMERIC SORTABLE $.brandName AS brandName TAG
  > 
  > ft.search productIdx "小米8" language "chinese"
  > 	# 中文OK
  > 
  > ft.search productIdx "データ" language "chinese"
  > 	# JP 需要改源码，friso 为 NGram
  > 	
  > ft.search productIdx "データをはな" language "chinese"
  > 	# OK, 确认 NGram 搜索一切正常
  > 
  > ft.search productIdx "香槟金" language "chinese"
  > 
  > ft.search productIdx "捨てずに" language "chinese"
  > 
  > ft.search productIdx "てずに" language "english"
  > 
  > ```
  >
  > 需要 redis 6 以上
  >
  > https://github.com/redis/redis
  >
  > git clone https://github.com/redis/redis.git
  >
  > make BUILD_TLS=yes USE_SYSTEMD=yes
  >
  > make install
  >
  > 
  >
  > /root/RediSearch/bin/linux-x64-release/search/redisearch.so
  >
  > https://redis.io/docs/stack/json/
  >
  > /root/RedisJSON/bin/linux-x64-release/rejson.so
  >
  > 
  >
  > 

- [RedisJSON + RediSearch](http://16384.net/20220813212856/index.html)

- [docker安装](https://hub.docker.com/r/redis/redis-stack-server)

- [阿里云webdav](https://github.com/messense/aliyundrive-webdav)

  - [解放Linux空间，薅羊毛新方式](https://blog.lincloud.pro/archives/36.html)

  > ```
  > pip install aliyundrive-webdav
  > 
  > aliyundrive-webdav qr login
  > 	# 扫描授权登录
  > 	# 会输出一个 refresh_token
  > 	
  > docker run -d --name=aliyundrive-webdav --restart=unless-stopped -p 8080:8080 \
  >   -v /etc/aliyundrive-webdav/:/etc/aliyundrive-webdav/ \
  >   -e REFRESH_TOKEN='your refresh token' \
  >   -e WEBDAV_AUTH_USER=root \
  >   -e WEBDAV_AUTH_PASSWORD= \
  >   messense/aliyundrive-webdav
  > 
  > dnf update -y && \
  > dnf install -y epel-release && \
  > dnf update -y && \
  > dnf install -y tar p7zip libsodium curl net-tools cronie lsof git wget yum-utils make gcc g++ openssl-devel bzip2-devel libffi-devel zlib-devel 
  > 
  > wget https://rpmfind.net/linux/epel/8/Everything/x86_64/Packages/d/davfs2-1.5.6-1.el8.x86_64.rpm && \
  > dnf install ./davfs2-1.5.6-1.el8.x86_64.rpm
  > 
  > 
  > mkdir /alipan
  > mount -t davfs http://xxx.com:8080 /alipan
  > 	# 输入账号密码
  > 
  > Streaming Optimized IP
  > 
  > ```



```
dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo && \
dnf update && \
dnf install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin && \
systemctl enable --now docker && \
systemctl status docker

vi /etc/docker/daemon.json
{
"registry-mirrors": [
"https://ustc-edu-cn.mirror.aliyuncs.com/",
"https://hub-mirror.c.163.com",
"https://mirror.baidubce.com"
]
}

systemctl daemon-reload && \
systemctl restart docker && \
docker info


docker pull redis/redis-stack-server && \
docker run -p 6379:6379 --name redis-stack redis/redis-stack:latest

nmap 127.0.0.1 -p6379






```



## redisson 全局ID等

[redisson 全局ID等](https://www.jianshu.com/p/033d0d73f53a)



## RedisGraph  图数据库

- https://zhuanlan.zhihu.com/p/102679312



## RedisInsight 管理工具

- https://zhuanlan.zhihu.com/p/476056075 





# Sqlite

[中文和拼音的 SQLite fts5](https://github.com/wangfenjin/simple)

[SQLiteSwiftDemo](https://github.com/pipi32167/SQLiteSwiftDemo)



# mysql 



## 封装

### mysql.js

```javascript
const mysql = require('mysql');

module.exports = {
  createPool: function (config) {

    const pool = mysql.createPool(config);
    const lib = {
      //执行查询
      async query(sql, par, conn = null) {
        if (conn == null) {
          conn = await new Promise((resolve, reject) => {
            pool.getConnection((erro, connection) => {
              if (erro) {
                reject(erro);
                return;
              }
              resolve(connection);
            });
          });
        }

        return new Promise((resolve, reject) => {
          const info = buildSQL(sql, par);
          conn.query(info.sql, info.params, (erro, result) => {
            //释放连接
            pool.releaseConnection(conn);
            // conn.release();
            if (erro) {
              reject(erro);
              return;
            }
            resolve(result);
          });
        });
      },
      //创建事务
      async createTransaction() {

        //获取连接
        const conn = await new Promise((resolve, reject) => {
          pool.getConnection((erro, connection) => {
            if (erro) {
              reject(erro);
              return;
            }
            resolve(connection);
          });
        });
        const t = {
          begin() {
            return new Promise((resolve, reject) => {
              conn.beginTransaction((beginErro) => {
                if (beginErro) {
                  //释放连接
                  pool.releaseConnection(conn);
                  // conn.release();
                  reject(beginErro);
                  return;
                }
                resolve(t);
              });
            });
          },
          query(sql, par) {
            const info = buildSQL(sql, par);
            return new Promise((resolve, reject) => {
              conn.query(info.sql, info.params, (erro, result) => {
                if (erro) {
                  //释放连接
                  pool.releaseConnection(conn);
                  // conn.release();
                  //回滚
                  conn.rollback((rollErro) => {
                    reject(rollErro);
                  });
                  reject(erro);
                  return;
                }
                resolve(result);
              });
            });
          },
          end() {
            return new Promise((resolve, reject) => {
              conn.commit((erro, info) => {
                if (erro) {
                  //释放连接
                  pool.releaseConnection(conn);
                  // conn.release();
                  //回滚
                  conn.rollback((rollErro) => {
                    reject(rollErro);
                    return;
                  });
                  reject(erro);
                }
                resolve(info);
              });
            });
          }
        };
        return t;
      },
    };

    return lib;
  }
};

/**
 * 构建SQL执行参数
 * @param {*} sql 
 * @param {*} par 
 * @returns {sql,params}
 */
function buildSQL(sql, par) {
  //参数处理
  const arr = [];
  const parNames = sql.match(/\$\([0-9a-zA-Z\_]{1,9999}?\)/g);
  if (parNames != null) {
    for (let pName of parNames) {
      //替换参数名
      sql = sql.replace(pName, '?');
      //转换参数名
      pName = pName.replace(/\$\(([[0-9a-zA-Z\_]{1,9999}?)\)/g, '$1')
      arr.push(par[pName]);
    }
  }
  return { sql: sql, params: arr };
}
```



### use



```javascript

( async()=>{

  async function get(db) {

    async function sleep(ms) {
      return new Promise((resolve) => {
        setTimeout(resolve, ms)
      })
    }

    //let ID = 10000

    var r = null

    while(r === null || r === undefined || r.length === 0) {

      let tmp = 100000 * Math.random() + 10000  // 随机数本来是均匀分存在 0 ~ 100000 之间，把它们整体往后挪10000

      var ID = Math.floor( tmp + 1 )
    
      if (ID > 100000) {
        ID = 100000
      }
        
      r = await db.query(`SELECT \`MD5\`, content FROM img_context WHERE ID = $(ID)`, { ID })

      //await sleep(500)

    }

    return [ JSON.parse(r[0].content), ID]

    
  }

  // ID 在 10000 ~  100000 之间随机取
  // Math.random() 范围：0 ~ 0.99999

  let mysql = require('./mysql')

  let db = mysql.createPool({
    host: 'xxx',
    user: 'xxx',
    password: 'xxx',
    database: 'xxx',
    port: 3306,
    multipleStatements: true,
    connectTimeout: 60 * 1000,
    connectionLimit: 50
  })


  for (let i = 0; i < 500; i++) {

    let [j, ID] = await get(db)

    require('fs').writeFileSync(`./out/${ID}.json`, JSON.stringify(j) )

    console.log(`done ${i}, ID: ${ID}`)

  }


}) ()
```



## 存储过程



### 循环



```
DROP PROCEDURE IF EXISTS `insertManyDate`;
 
CREATE DEFINER =  PROCEDURE `insertManyDate`(IN `beginDate` date,IN `endDate` date)
    COMMENT '根据输入的起止日期，循环插入每天的时间'
BEGIN
 
DECLARE nowdate date DEFAULT NOW();
DECLARE endtmp date DEFAULT NOW();
set nowdate = DATE_FORMAT(beginDate,'%Y%m%d');
set endtmp = DATE_FORMAT(endDate,'%Y%m%d');
WHILE nowdate<endtmp 
DO
INSERT INTO belial.date(date) VALUES(nowdate);
set nowdate = DATE_ADD(nowdate,INTERVAL 1 DAY);
END WHILE;
```



## 取用户最新的一条数据



```mysql
# 前提：ID 是自增ID
# MAX(r.ID) 是最新的，但其他不是，所以必须要用子查询

    SELECT r.ID AS reportID, r.appID, r.userID, r.rightRate FROM report r WHERE r.ID IN ( SELECT MAX(r.ID) AS reportID from report r WHERE r.appID=$(appid) GROUP BY r.userID ORDER BY reportID DESC ) ORDER BY reportID DESC;

```







## Time

```
const now = moment().format('YYYY-MM-DD HH:mm:ss');
var time = moment().format('MMMM Do YYYY, h:mm:ss a')
let t1 = new Date().getTime();
```



### 时区转换



```
select NOW();
SELECT convert_tz(now(),@@session.time_zone,'+08:00')


# 24小时制
let u = re[0].updateTime
let tt = new Date(u).toLocaleString('chinese',{hour12:false})

```

### 24 小时制



```javascript
select NOW();
SELECT convert_tz(now(),@@session.time_zone,'+08:00')


# 24小时制
let u = re[0].updateTime
let tt = new Date(u).toLocaleString('chinese',{hour12:false})
```



### 时间比较



```
普通日期时间比较

泛指格式相同的日期时间

var date1 = new Date("2020-3-15");
var date2 = new Date("2020-2-29");
var result = date1 > date2;        
console.log(result);                //true
特殊日期时间比较

因格式不同，比较前，我们需要将日期时间格式化

var date1 = new Date("2020-3-15");
var date2 = new Date("2020/2/29");
var result = Date.parse(date1) > Date.parse(date2);
console.log(result);                                //true
字符串类型日期时间比较 

用于不同格式之间的字符串日期时间比较，统一格式化后再比较

var date1 = "2020-3-15";
var date2 = "2020/2/29";
var result = date1.replace(/\-/g,'/') > date2.replace(/\-/g,'/');
console.log(result);                                                //true
```



## 定时任务

```
        async function loopcheck() {
            return new Promise(function (resolve, reject) {
                const timer = setInterval(async function () {
                    let checktype = await pushrdis()
                    if (checktype) {
                        resolve(ID)
                        clearInterval(timer)
                    } else if (conn) {
                        conn.__ws__.send(msg)
                    }
                }, 10000);
            });
        }


clearTimeout(checkTask);
checkTask = setTimeout(() => {
	// 一秒后执行
}, 1000);
```





## escape

```
const mysql = require('mysql')
mysql.escape(s) 
```





# Algo



## TF-IDF

- https://zhuanlan.zhihu.com/p/31197209

  > 生动理解TF-IDF算法



# PG



## pgsql.js



```javascript

"pg": "~8.7.1",
"pg-pool": "~3.4.1"

let { Pool, Client } = require('pg')

function getconfig (dbname) {
  return {
    user: 'postgres',
    password: 'et.com',
    host: 'xxxx.77',
    port: '5432',
    database: dbname,
    ssl: false
  }
}

function getDB (dbname) {
  let config = getconfig(dbname)
  let pool = new Pool(config)
  let lib = {

    async query(sql, par, conn = null) {
      if (conn == null) {
        conn = await pool.connect()
      }

      //await client.query('select $1::text as name', ['brianc'])
      let result = await conn.query(sql, par)
      conn.release(true)

      return result

    },
    async release() {
      return await new Promise((resolve, reject) => {
        pool.end().then(() => {
          resolve(`pool has been release, db is ${config.database}`)
        })
      })
    
    },
    status() {
      let totalCount = pool.totalCount
      let idleCount = pool.idleCount
      let waitingCount = pool.waitingCount
      return { totalCount, idleCount, waitingCount }
    } 

    /*
    pool.totalCount: int
      The total number of clients existing within the pool.

    pool.idleCount: int
      The number of clients which are not checked out but are currently idle in the pool.

    pool.waitingCount: int
      The number of queued requests waiting on a client when all clients are checked out. It can be helpful to monitor this number to see if you need to adjust the size of the pool.
    */

  }

  return lib
}

let defaultDB = getDB('postgres')

module.exports = {
  getconfig,
  getDB,
  defaultDB
}

/*

 cur.execute("create table anime( \
                id integer primary key generated always as identity, \
                name text, \
                jp text, \
                zh text DEFAULT '', \
                en text DEFAULT '', \
                type text, \
                time text, \
                jp_mecab text, \
                v_jp  tsvector, \
                v_zh  tsvector, \
                v_en  tsvector, \
                videoname text, \
                seasion text DEFAULT '', \
                audio bytea, \
                video bytea \
            );")
            #cur.execute("CREATE TABLE audio(id SERIAL PRIMARY KEY, data BYTEA);")

            cur.execute("create extension pgroonga;")
            cur.execute("CREATE INDEX pgroonga_jp_index ON anime USING pgroonga (jp);")
            cur.execute("CREATE INDEX pgroonga_jpmecab_index ON anime USING pgroonga (jp_mecab);")

            cur.execute("create extension pg_jieba;")

            cur.execute("CREATE INDEX animename_index ON anime (name);")
            cur.execute("CREATE INDEX videoname_index ON anime (videoname);")

*/

```



```javascript

    let pg = require('./pgsql')
    let re = await pg.defaultDB.query('select $1::text as name', ['brianc']) 
    re = await pg.defaultDB.query('DROP DATABASE IF EXISTS temp;', [])
    re = await pg.defaultDB.query(`
    CREATE DATABASE temp 
        WITH OWNER = postgres 
        ENCODING = 'UTF8' 
        TABLESPACE = pg_default 
        CONNECTION LIMIT = -1 
        TEMPLATE template0;
    `, [])

    let tempDB = pg.getDB('temp')
    re = await tempDB.query(    `
    CREATE TABLE bookdata (
        id  serial NOT NULL PRIMARY KEY,
        info json NOT NULL
      )
    `)
    re = await tempDB.query(`CREATE INDEX bookdata_fts ON bookdata USING gin((to_tsvector('english',info->'title')));`)

    re = await tempDB.query(`
    INSERT INTO bookdata (info)
    VALUES
     ( '{ "title": "The Tattooed Duke", "items": {"product": "Diaper","qty": 24}}'),
     ( '{ "title": "She Tempts the Duke", "items": {"product": "Toy Car","qty": 1}}'),
     ( '{ "title": "The Duke Is Mine", "items": {"product": "Toy Train","qty": 2}}'),
     ( '{ "title": "What I Did For a Duke", "items": {"product": "Toy Train","qty": 2}}'),
     ('{ "title": "King Kong", "items": {"product": "Toy Train","qty": 2}}');
     `)

     re = await tempDB.query(`
     SELECT info -> 'title' as title FROM bookdata
     WHERE to_tsvector('english',info->'title') @@ to_tsquery('Duke');
     `)

    let sta1 = pg.defaultDB.status()
    let sta2 = tempDB.status()

    re = await tempDB.release()
    re = await pg.defaultDB.release()
```





## Pool



```
/*
  Transforms, 'postgres://DBuser:secret@DBHost:#####/myDB', into
  config = {
    user: 'DBuser',
    password: 'secret',
    host: 'DBHost',
    port: '#####',
    database: 'myDB',
    ssl: true
  }
*/
```



```javascript
# https://github.com/brianc/node-postgres/tree/master/packages/pg-pool

npm install pg pg-pool --save

(async () => {

    const { Pool, Client } = require('pg')

    const config = {
        user: 'postgres',
        password: 'xxxx',
        host: 'xxxx',
        port: '5432',
        database: 'postgres',
        ssl: false
    }

    var pool = new Pool(config)
    var client = await pool.connect()
    try {
      var result = await client.query('select $1::text as name', ['brianc'])
      console.log('hello from', result.rows[0])
    } finally {
      client.release()
    }
})().catch(e => console.error(e.message, e.stack))
```



## insert id

```
  INSERT INTO $$(tablename) (name, seasion, jp, zh, type, begintime, endtime, jp_ruby, v_jp, v_zh, videoname, episode, seasionname, audio, video) 
  VALUES 
  ( $(name), $(seasion), $(jp), $(zh), $(type), $(begintime), $(endtime), $(jp_ruby), to_tsvector($(v_jp)), to_tsvector($(v_zh)), $(videoname), $(episode), $(seasionname), $(audio), $(video) ) 
  RETURNING id;

let re = await this.dbs.anime.insert.query({tablename:type, name, seasion, jp, zh, type, begintime, jp_ruby, v_jp:jp_ng, v_zh:zh_ng, videoname, episode, seasionname, endtime, audio, video})
                
                let { id } = re.fields[0]
```





## Random



```
# https://www.redpill-linpro.com/techblog/2021/05/07/getting-random-rows-faster.html
	Getting random rows faster. Very much faster.
```



## Group



```mysql
分组聚合
# https://www.skypyb.com/2021/08/jishu/1871/

解决PostgreSQL分组聚合时SELECT中字段必须在group或聚合函数中的问题
PG的分组函数是比较严格的。 你的select字段必须得存在于group子句、或者聚合函数中才行。

假设场景是这样的：

表结构name、class、score

我现在要按照name分组，聚合score数据，还能查出额外的这个 class 字段

 

如果是MySQL， 你可以直接group name 然后 select class，avg(score)， 但是你在PostgreSQL里就不行。

 

他会爆出以下的错误

column “class” must appear in the GROUP BY clause or be used in an aggregate function

 

就是说这个 select class是非法的。

刚从MySQL切到PostgreSQL后很可能会比较难受这个点。

 

其实有一种很简单的方法， 那就是你反正其他的字段其实都一样，随便取一个就行，所以还是保持原来的GROUP BY 子句，然后直接给所有的字段全部加上一个 max() 函数就行了。

不过这样子的代价就是整个SQL看起来挺怪的， 语义上也有点微妙。我这只是个简单场景， 实际上你可能得有好几十个字段，这样子每个字段都得加上个max函数。

 

所以我推荐第二种方法。

Window function（窗口函数） + distinct 去重

 

窗口函数语法：

聚合函数(sum，min，avg……) + OVER ( …… )

 

窗口函数会将计算出来的结果带回到计算行上，还是以上面的例子作参考，一个表name、class、score。

 

那我直接一个普通查询，不GROUP了，我们想要的class自然就可以查出来了。

然后用窗口函数去算我需要聚合的数据，这里直接写上关键字OVER放在avg(score)后面， 然后括号里跟上一个PARTITION BY name， 意思就是按照name去分组，把结果计算出来。

唉！这个效果其实就和GROUP BY差不多，对不对。

不过这样子的话你数据是有了，但是行数却没变，原来是多少行现在还是多少行。 好，那我就直接给它安排一个 dictinct 函数，指定我 PARTITION BY 的那个字段，也就是name。

这样子我们就完成了一波上流且奢华的SQL查询，大功告成~

SELECT distinct on (name) 
    name,
    class,
    avg(score) OVER (PARTITION BY name) AS score,
FROM table
语义上清晰不少， 效果也给满足了（指按照name分组，聚合score数据，还能查出不处于GROUP子句和聚合函数中的 class 字段）

```



## with



```mysql
# https://www.postgresql.org/docs/9.1/queries-with.html

WITH regional_sales AS (
        SELECT region, SUM(amount) AS total_sales
        FROM orders
        GROUP BY region
     ), top_regions AS (
        SELECT region
        FROM regional_sales
        WHERE total_sales > (SELECT SUM(total_sales)/10 FROM regional_sales)
     )
SELECT region,
       product,
       SUM(quantity) AS product_units,
       SUM(amount) AS product_sales
FROM orders
WHERE region IN (SELECT region FROM top_regions)
GROUP BY region, product;

```



## Mecab



```
# hara.js

/*

  "dependencies": {
    "fluent-ffmpeg": "~2.1.2",
    "kuroshiro": "~1.2.0",
    "pg": "~8.7.1",
    "pg-pool": "~3.4.1"
  }

*/

(async () => {

    var arguments = process.argv

    //console.log( arguments[2] )

    String.prototype.replaceAll = function (search, replacement) {
        var target = this
        return target.replace(new RegExp(search, 'g'), replacement)
    }

    // let arr = require('fs').readFileSync('./data.json', { encoding: 'utf8', flag: 'r' })

    // arr = JSON.parse(arr)

    const Kuroshiro = require("kuroshiro")
    const KuromojiAnalyzer = require("kuroshiro-analyzer-kuromoji")
    const MecabAnalyzer = require("kuroshiro-analyzer-mecab")
    const kuroshiro = new Kuroshiro()

    const mecabAnalyzer = new MecabAnalyzer({
        dictPath: "/usr/lib64/mecab/dic/mecab-ipadic-neologd",
        execOptions: {
            maxBuffer: 200 * 1024,
            timeout: 0
        }
    })

    let str = arguments[2] // arr[0]

    let [hiras, msg] = await new Promise(function (resolve) {

        //kuroshiro.init(new KuromojiAnalyzer())
        kuroshiro.init(mecabAnalyzer)
            .then(function () {
                return kuroshiro.convert(str, { to: "hiragana" })
            })
            .then(function (result) {
                resolve([result.toString(), ''])
            }).catch((err) => {
                resolve([null, err])
            })

    })

    //originals = originals.replaceAll(String.raw`\s`, '')
    //hiras = hiras.replaceAll(String.raw`\s`, '')
    let hiras_ngrams = NG(hiras)

    console.log( hiras_ngrams.join(' ') )

    //console.log(originals)
    //console.log(hiras)

    a = 1

})()

function NG(strs) {

  strs = strs.replaceAll(String.raw`\s`, '')

    function ng(s, n) {
  
      var grs = []
  
      for (let i = 0; i < s.length; i++) {
  
        if ( i + n > s.length ) {
          break
        }
  
        var gr = s.substring(i, i+n)
  
        grs.push(gr)
        
  
      }
  
      return grs
  
    }
  
    var gss = []
    for (let i = 2; i <= 10; i++) {
      
      let gs = ng(strs, i)
  
      if (gs.length > 0) {
  
        gss = gss.concat( gs )
  
      } else {
  
        break
  
      }
  
    }
  
    return gss
  
  }

  
  String.prototype.replaceAll = function(search, replacement) {
    var target = this
    return target.replace(new RegExp(search, 'g'), replacement)
  }

  // s = NG(' ab cdefg')
  // a = 1


```





```
https://mebee.info/2021/02/18/post-29277/
	# mecab centos7
```





```
# https://qiita.com/PonDad/items/81b85d76b1a89ee2598b
	# https://blog.knjcode.com/neologd-on-nodejs/
var MeCab = new require('mecab-async')
var mecab = new MeCab();
    MeCab.command = "mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd"
    var text = 'こんにちは、サミュエルLジャクソンです。'
    //注：パースコマンドを利用する時 "MeCab.~"と大文字にしないと動かないみたいです
    MeCab.parseFormat(text, function(err, morphs) {
        if (err) throw err;
        morphs.map(function(morph) {
        if (morph.lexical === '感動詞') {
          console.log(morph.lexical + ' : ' + morph.original);
        }
        if (morph.lexical === '名詞') {
          console.log(morph.lexical + ' : ' +morph.original);
        }
    });
    });
```





```
# https://github.com/agracio/edge-js

js C# interop
```





```
pip3.8 install mecab-python3
pip3.8 install unidic-lite
pip3.8 install chardet

D:\usr\Lib\site-packages\unidic_lite
```





```
# https://github.com/hecomi/node-mecab-async
npm install mecab-async
```



### kuromoji.js + mecab-ipadic-neologd



```
# https://qiita.com/mabasasi/items/17b0bf735c38b4642682
	
	# https://github.com/reneeter123/kuromoji.js-vs-neologd
		# pure js in browser
		    if (document.getElementById("useStandard").checked) {
        startTime = performance.now();
        kuromoji.builder({ dicPath: "./js/dicts/standard/" }).build((err, tokenizer) => {
            showResult(tokenizer.tokenize(analyzeTextValue));
        });
    } else if (document.getElementById("useNeologd").checked) {
        startTime = performance.now();
        kuromoji.builder({ dicPath: "./js/dicts/neologd/" }).build((err, tokenizer) => {
            showResult(tokenizer.tokenize(analyzeTextValue));
        });
    } else {
        startTime = performance.now();
        showResult(new TinySegmenter().segment(analyzeTextValue));
    }

npm install kuromoji --save

var kuromoji = require("kuromoji");

kuromoji.builder({ dicPath: "node_modules/kuromoji/dict" }).build(function (err, tokenizer) {
  // tokenizer is ready
  var path = tokenizer.tokenize("すもももももももものうち");
  console.log(path);
  a = 1
});

```



### centos7+mecab+neologd



```
https://omohikane.com/centos7_mecab_neologd/

# install libs
sudo yum install -y  bzip2 bzip2-devel gcc gcc-c++ git make wget curl openssl-devel readline-devel zlib-devel
 
# install mecab
sudo mkdir -p /tmp/install_mecab
cd /tmp/install_mecab
wget 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE' -O mecab-0.996.tar.gz
tar zxvf mecab-0.996.tar.gz && cd mecab-0.996 && ./configure --with-charset=utf8 --enable-utf8-only &&  make && sudo make install
 
# install ipadic
sudo mkdir -p /tmp/install_mecab
cd /tmp/install_mecab
wget 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM' -O mecab-ipadic-2.7.0-20070801.tar.gz && tar zxvf mecab-ipadic-2.7.0-20070801.tar.gz && cd mecab-ipadic-2.7.0-20070801 && ./configure --with-charset=utf8 && make && sudo make install  
 
# install neologd
sudo rpm -ivh http://packages.groonga.org/centos/groonga-release-1.1.0-1.noarch.rpm && sudo yum -y install mecab mecab-devel mecab-ipadic xz && cd /usr/local/src/ && sudo su - root
 
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && cd mecab-ipadic-neologd
 
echo "yes" | ./bin/install-mecab-ipadic-neologd -n
	# mecab -d /usr/lib64/mecab/dic/mecab-ipadic-neologd  成功，这样使用
./libexec/make-mecab-ipadic-neologd.sh 
echo "yes" | ./bin/install-mecab-ipadic-neologd -n


mecab -d /usr/lib64/mecab/dic/mecab-ipadic-neologd
	# 成功

```





#### Error: mecab-config not found

```
# mecab-config not found
# If you're installing MeCab via a package manager, be sure to get libmecab-dev to get mecab-config too.

# https://qiita.com/mhiro216/items/391ae79848129ac1cb2d


sudo rpm -ivh http://packages.groonga.org/centos/groonga-release-1.1.0-1.noarch.rpm
sudo yum install mecab-devel
	# 成功解决 mecab-config not found
```



#### Error: no such file  mecab-ipadic-neologd/dicrc 



```
# https://qiita.com/MuggyTea/items/dd1ea3a781b59c6b5979





```





### kuroshiro 省心方案



```
# https://www.npmjs.com/package/kuroshiro

npm install kuroshiro@1.1.2
	# 其他版本有Bug

```





## FTS



### grammar



```
https://www.postgresql.org/docs/13/functions-textsearch.html
Tsvector_update_trigger jsonb  site:cnblogs.com
```



### json



#### trigger



- https://dba.stackexchange.com/questions/286660/how-to-use-tsvector-update-trigger-with-jsonb-column 













```
# https://www.skypyb.com/2020/12/jishu/1705/
索引
当数据量庞大时， 那么不可避免地查询速度就会变慢， 此时就需要去加索引。
PostgreSQL自然也提供了强大的索引支持， 使用以下语句增加 pg_trgm 拓展就可以引入两个索引 gin 、 gist， 需要注意的是执行语句需要提权到 postgres 用户。

CREATE EXTENSION pg_trgm;
gin和gist的区别就是 gin查询更快， 但是构建速度可能会慢一点。 而 gist 的构建速度快， 查询会慢一点。
一般建议预计数据量不大时可以使用gist索引， 如果预计数据量很大请直接上gin。

# https://developer.aliyun.com/article/672261
# https://blog.csdn.net/weixin_37096493/article/details/106302184
```



- https://github.com/valeriansaliou/sonic



### 分布式扩展

- https://github.com/citusdata/citus



### segment



```
https://www.jianshu.com/p/8f0ce2cff8d9
```



### NGram



```javascript
function NG(strs) {

  function ng(s, n) {

    var grs = []

    for (let i = 0; i < s.length; i++) {

      if ( i + n > s.length ) {
        break
      }

      var gr = s.substring(i, i+n)

      grs.push(gr)
      

    }

    return grs

  }

  var gss = []
  for (let i = 2; i <= 10; i++) {
    
    let gs = ng(strs, i)

    if (gs.length > 0) {

      gss = gss.concat( gs )

    } else {

      break

    }

  }

  return gss

}
```



## FFMPEG

- https://www.mysterydata.com/how-to-install-latest-ffmpeg-4-in-centos-8-7-ubuntu-20-04-18-04-cwp-cpanel-plesk-ispconfig/

### 升级

```
#  rpm -qa | grep -i ffmpeg
ffmpeg-3.4.9-1.el7.x86_64
ffmpeg-devel-3.4.9-1.el7.x86_64
ffmpeg-libs-3.4.9-1.el7.x86_64
gstreamer-ffmpeg-0.10.13-16.el7.x86_64

yum remove firefox -y
yum remove ffmpeg -y
yum update -y

wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
	# ffmpeg 5.0
	
mv dir to /usr/local/
ln ffmpeg to /usr/local/bin

```







```
ffmpeg -rtsp_transport tcp -i rtsp://userxx:xxx@192.168.101.108:554/0:0 -y http://192.168.101.1:8090/feed2.ffm
```



```
//			.outputOptions(["-movflags", "frag_keyframe+empty_moov"]) //without these options ffmpeg errors with `muxer does not support non seekable output`

```



### ffmpeg.wasm

- https://github.com/ffmpegwasm/ffmpeg.wasm

```

npm install @ffmpeg/ffmpeg @ffmpeg/core

const trim = async ({ target: { files } }) => {
        videoInput.addEventListener('loadedmetadata', async function () {
                let duration =  Math.floor(videoInput.duration)-5; 
                oldDuration.innerText = `Duration before trim: ${duration} сек`;
                newDuration.innerText = `Duration after trim: ${duration-5} сек`;  
                await ffmpeg.run('-i', 'myfile.mp4', '-ss', '0', '-to', `${duration}`, '-c','copy', 'output.mp4');
                const data = await ffmpeg.FS('readFile', 'output.mp4');
                video.src = URL.createObjectURL(new Blob([data.buffer], { type: 'video/mp4' }));
                link.download = 'video.mp4';
                link.href = video.src;
                link.innerText = DOWNLOAD';
        });   
            if (!ffmpeg.isLoaded()) {
                await ffmpeg.load()
            }
            const { name } = files[0];
            const videofile = await FFmpeg.fetchFile(files[0]);
            await ffmpeg.FS('writeFile', `myfile.mp4`, videofile);
            const origData = await ffmpeg.FS('readFile', 'myfile.mp4');
            // Get the link and mount it in a hidden video tag in order to get the duration
            videoInput.src = URL.createObjectURL(new Blob([origData.buffer], { type: 'video/mp4' }));
      }
```







### ffmpeg.js



#### pipe stream



```
app.get('/stream', (req, res) => {
    let _url = req.query.url;

    if(_url){   

        res.writeHead(200, {
            'Access-Control-Allow-Origin': '*',
            'Connection': 'Keep-Alive',
            'Content-Type': 'video/mp4'
        });

        // transcode rtsp input from ip-cam to mp4 file format (video: h.264 | audio: aac)
        let ffmpeg = child_process.spawn("ffmpeg",[
            "-probesize","2147483647",
            "-analyzeduration","2147483647",
            "-i", _url,
            "-vcodec","copy",
            "-f", "mp4",            
            "-movflags","frag_keyframe+empty_moov+faststart",
            "-frag_duration","3600",
            "pipe:1"              
        ]);         


        // redirect transcoded ip-cam stream to http response
        ffmpeg.stdout.pipe(res);

        // error logging
        ffmpeg.stderr.setEncoding('utf8');      
        ffmpeg.stderr.on('data', (data) => {
            console.log(data);
        });
    }
    else{
        res.end();
    }
```





```javascript

// https://github.com/mafintosh/pump


module.exports = {

    extractAudio: async function (vdpath, type, begin_time, end_time) {

        var pump = require('pump')

        let fs = require('fs')
        let ffmpeg = require('fluent-ffmpeg')

        ffmpeg.setFfmpegPath(String.raw`E:\Program Files\ffmpeg-4.3.2-2021-02-02-full_build\bin\ffmpeg.exe`)


            let [au, ms1] = await new Promise(function (resolve) {

                const stream = require('stream')

                let vd = fs.createReadStream(vdpath)

                // let bufferStream = new stream.PassThrough()
                // // Read the passthrough stream
                const buffers = []
                // bufferStream.on('data', function (buf) {
                //     buffers.push(buf)
                // })
                // bufferStream.on('end', function () {
                //     //vd.close()
                //     vd.destroy()

                // })

                // bufferStream.on('close', function () {

                //     // nclose += 1

                //     // const outputBuffer = Buffer.concat(buffers)
                //     // //let sr = outputBuffer.toString('utf8')
                //     // // let dir = require('path').dirname(__filename)
                //     // // let fname = require('path').join(dir, 'tmp.mp3')
                //     // fs.writeFileSync(`tmp.${type}`, outputBuffer, 'binary')
                //     // resolve([outputBuffer, ''])

                // })

                let command = ffmpeg(vd)//.output(au)
                    .noVideo()
                    .format(type)
                    // .audioBitrate('128')
                    // .outputOptions('-ss', begin_time) // 00:00:00.000
                    // .outputOptions('-to', end_time)   // 00:00:07.520
                    .outputOption(
                        [
                            "-vn",
                            "-ss",
                            begin_time,
                            "-to",
                            end_time,
                            "-acodec", "mp3",
                            "-ar", "44100",
                            "-ac", "2",
                            "-b:a", "192k"
                        ]
                    )
                    //.writeToStream(bufferStream)
                    .on("end", (stdout, stderr) => {

                        const outputBuffer = Buffer.concat(buffers)
                        // let sr = outputBuffer.toString('utf8')
                        // let dir = require('path').dirname(__filename)
                        // let fname = require('path').join(dir, 'tmp.mp3')
                        //fs.writeFileSync(`tmp.${type}`, outputBuffer, 'binary')
                        //bufferStream.destroy()
                        resolve([outputBuffer, ''])
                    })
                    .on("error", (err) => {
                        a = 1
                    })

                let ffstream = command.pipe()
                ffstream.on('data', function (buf) {
                    buffers.push(buf)
                })
                ffstream.on('end', function () {
                    a = 1
                })

                //ffmpegProc.on('exit', function(code, signal) {

                // .on('start', () => {

                //   a = 1

                // })
                // .on('end', () => {

                //   a = 1

                //   resolve(['ok', 'ok.'])
                // })
                // .run()
            })

            return [au, ms1]
    },
    extractSubtitle: async function (vdpath, type, nth) {

        let fs = require('fs')
        let ffmpeg = require('fluent-ffmpeg')

        ffmpeg.setFfmpegPath(String.raw`E:\Program Files\ffmpeg-4.3.2-2021-02-02-full_build\bin\ffmpeg.exe`)

        let [au, ms1] = await new Promise(function (resolve) {

            const stream = require('stream')

            var vd = fs.createReadStream(vdpath)

            // let bufferStream = new stream.PassThrough()
            // Read the passthrough stream
            const buffers = []
            // bufferStream.on('data', function (buf) {
            //     buffers.push(buf)
            // })
            // bufferStream.on('end', function () {
            //     vd.destroy()
            // })

            let command = ffmpeg(vd)
                .noVideo()
                .format(type)
                .outputOption(
                    [
                        '-map', `0:s:${nth}`
                    ]
                )
                // .writeToStream(bufferStream)
                .on("end", (stdout, stderr) => {
                    const outputBuffer = Buffer.concat(buffers)
                    //let sr = outputBuffer.toString('utf8')
                    // let dir = require('path').dirname(__filename)
                    // let fname = require('path').join(dir, 'tmp.mp3')
                    //fs.writeFileSync(`tmp.${type}`, outputBuffer, 'binary')
                    // bufferStream.destroy()
                    resolve([outputBuffer, ''])
                })
                .on("error", (err) => {
                    a = 1
                })

                let ffstream = command.pipe()
                ffstream.on('data', function (buf) {
                    buffers.push(buf)
                })
                ffstream.on('end', function () {
                    a = 1
                })

        })

        return [au, ms1]
    },

}


/*
    ffmpeg -i F:\videos\anime\Pokemon\S14\Best_Wishes\06.mkv
          Stream #0:2: Subtitle: ass (default)
          Stream #0:3: Subtitle: ass
          Stream #0:4: Subtitle: ass

    out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-loglevel", "error", "-i", fname, "-map", "0:s:0", frtname])

    out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", videopath, "-vn", "-ss", begintime, "-to", endtime, "-acodec", "mp3", \
      "-ar", "44100", "-ac", "2", "-b:a", "192k", \
        "tmp.mp3"])
    
    https://github.com/fluent-ffmpeg/node-fluent-ffmpeg/issues/470

    ffmpeg
  //.withVideoCodec('h264_nvenc')
  .withVideoBitrate(8000)
  .withAudioCodec('libmp3lame')
  .withVideoCodec('h264_nvenc')
  .outputOption([
    '-map 0',
    '-map -v',
    '-map -a',
    '-map 0:V',
    '-map 0:m:language:eng?', // TODO: This should be an input parameter to be able to change language
    '-deadline realtime',
    '-lag-in-frames 0',
    '-static-thresh 0',
    '-frame-parallel 1',
    '-crf 4',
    '-movflags frag_keyframe+faststart',
    '-pix_fmt yuv420p',
    '-sn',
    '-max_muxing_queue_size 9999'
  ])
  .outputFormat('mp4')
};


//			.outputOptions(["-movflags", "frag_keyframe+empty_moov"]) //without these options ffmpeg errors with `muxer does not support non seekable output`


*/



```

```javascript




(async () => {
    
    let fs = require('fs')
    let ff = require('./ffmpeg')

    let vdpath = String.raw`F:\videos\anime\Pokemon\S14\Best_Wishes\06.mkv`

    let [audio, ms1] = await ff.extractAudio(vdpath, 'mp3', `00:00:00.000`, `00:00:07.520`)  // output type, begintime, endtime
    
    let [srt_zhs, ms2] = await ff.extractSubtitle(vdpath, 'srt', 0) // the nth subtitle stream
    srt_zhs = srt_zhs.toString('utf8')

    // a = 1

    let [srt_jp, ms3] = await ff.extractSubtitle(vdpath, 'srt', 2) // the nth subtitle stream
    srt_jp = srt_jp.toString('utf8')

    a = 1
})()


```









```javascript
  var vd = require('fs').createReadStream('F:/1.mkv')
  var au = require('fs').createWriteStream('tmp.mp3')

  ffmpeg(vd).output(au)
  .noVideo()
  .format('mp3')
  .outputOptions('-ab','192k')
  .outputOptions('-ss','00:01:12.960')
  .outputOptions('-to','00:01:14.640')
  .on('start',()=>{

    a = 1
    
  })
  .on('end', ()=>{ 

    a = 1
  })
  .run()
```



```javascript
  var vd = require('fs').createReadStream('F:/1.mkv')
  var au = require('fs').createWriteStream('tmp.srt')

  ffmpeg(vd).output(au)
  .noVideo()
  .format('srt')
  .outputOptions('-map','0:s:0')
  //.outputOptions('-ss','00:01:12.960')
  //.outputOptions('-to','00:01:14.640')
  .on('start',()=>{

    a = 1
    
  })
  .on('end', ()=>{ 

    a = 1
  })
  .run()
```





```javascript
npm i fluent-ffmpeg
var ffmpeg = require('fluent-ffmpeg');
const path = require('path');

var filename = './not-commit-test-file/1.mp4';
var full_path = path.resolve(filename);
console.log(full_path);

var command = ffmpeg(full_path);
command.outputOptions([
  '-vn',
  '-acodec copy',
]).save('output-audio.aac');
```



```javascript
function streamtogif(stream, begintime = 0, duration){ //Return promise buffer
  return new Promise((resolve, reject)=>{
  buffer = [] //prepare creation of the buffer for the gif
    function addChunk(chunk){ 
      this.buffer.push(chunk)
    }
    function getBuffer(cb){ //get buffer array
      cb(this.buffer);
    }
    ffmpegstream = ffmpeg()
    .outputOptions('-metadata', 'title=test')
    .input(stream)
    .fps(20)
    .setStartTime(begintime)
    .noAudio()
    .videoCodec('gif')
    .format('gif')

    if(duration){ffmpegstream.duration(duration)} //only define duration if defined in function's parameters
    ffmpegstream.on('start',()=>{
      //console.log("starting")
      this.buffer = []
    })
    .on('end', ()=>{ 
      getBuffer((buff)=>{
      finalBuffer = Buffer.concat(buff);
      resolve(finalBuffer);
      });
  }) 

    var ffstream = ffmpegstream.pipe(); //handle data 
    ffstream.on('data', function(chunk) {
      addChunk(chunk);
    })


    ffmpegstream.run()
  });
}

            finalBuffer = Buffer.concat(this.fileRead)
            const bufferStream = new Stream.PassThrough();
            bufferStream.end(finalBuffer);
            streamtogif(bufferStream).then((buffer)=>{
              upload = uploadpicture(buffer, "source/sportifeed").then((response)=>{ //success request
                res.status(200).json({success: true, message: "Successfully uploaded !", url: response.data.link});
              },(err)=>{ //error
                console.log(err)
                res.status(500).json({success: false, message: "Error happenned while uploading !"});
              }).catch((err)=>{
                console.log(err)
                res.status(500).json({success: false, message: "Error happenned while uploading !"});
              });
            },(err)=>{
              console.log(err);
            })

```



```
var FFmpeg = require('ffmpeg')

function ffmepgFunction(timeout, attempts) {
    try {
    var command = FFmpeg("http://localhost:9001");

    var stream = command.pipe();
    stream.on('data', function(chunk) {
    // do something with the data
    });
    } catch(e) {
        console.log(e);
        if(attempts > 0)
            setTimeout(() => ffmepgFunction(timeout, --attempts), timeout);
    }
}

ffmepgFunction(2000, 5);
```



### buffer

```
# 写文件改写内存流
(async () => {
  let [sr, ms] = await new Promise(function (resolve) {

    var ffmpeg = require('fluent-ffmpeg')

    var vd = require('fs').createReadStream('F:/1.mkv')
    //var au = require('fs').createWriteStream('tmp.srt')

    const stream = require('stream')
    let bufferStream = new stream.PassThrough()
    // Read the passthrough stream
    const buffers = []
    bufferStream.on('data', function (buf) {
      buffers.push(buf)
    })
    bufferStream.on('end', function () {
      const outputBuffer = Buffer.concat(buffers)
      let sr = outputBuffer.toString('utf8')
      // use outputBuffer
      resolve([sr, ''])
    })

    ffmpeg(vd)//.output(au)
      .noVideo()
      .format('srt')
      .outputOptions('-map', '0:s:0')
      //.outputOptions('-ss','00:01:12.960')
      //.outputOptions('-to','00:01:14.640')
      .writeToStream(bufferStream)
      // .on('start', () => {

      //   a = 1

      // })
      // .on('end', () => {

      //   a = 1

      //   resolve(['ok', 'ok.'])
      // })
      // .run()
  })
})().catch(e => console.error(e.message, e.stack))
```





### bytea



```
You can insert Buffer (https://nodejs.org/dist/latest-v14.x/docs/api/buffer.html) values into bytea fields.
```



```
 combinedBuffer = Buffer.allocUnsafe(this.remainingBuffer.byteLength + buffer.byteLength) 
 this.remainingBuffer.copy(combinedBuffer) 
 buffer.copy(combinedBuffer, this.remainingBuffer.byteLength) 
```



### HLS  mpv 推流

HLS  mpv 推流



### 关键帧间隔

1. 大家在使用ffmpeg进行视频编码时，使用-b命令，想控制比特率，却发现结果并没有如我们设置所愿，通过码流分析器观察视频码流，码率的波动还是很大的，ffmpeg控制的并不好，这时候，我们可以通过以下命令解决：

```bash
-maxrate biterate -minrate biterate -bf 1 -b_strategy 0
1
```

其中 -maxrate、-minrate为设置最小最大比特率，-bf为设置B帧数目，其实就是设置编码是B、P、I帧的结构，我这里设置的为IPBPBP结构，-b_strategy这个命令是为了自适应的添加B帧数目，ffmpeg编码器会根据视频的应用场景，自适应的添加B帧，通过设置-b_strategy
0，，将这个功能关闭，那么就会根据你的设置要求进行编码。除此之外，还可以使用-pass，进行2次码率控制，编出来的视频效果更好；下面我介绍-pass的使用方法：
（1）`-pass 1 -passlogfile ffmpeg2pass` 第一步先编一次，生成 ffmpeg2pass 文件
（2）`-pass 2 -passlogfile ffmpeg2pass` 第二次会根据第一次生成的ffmpeg2pass 文件，再进行码率控制。

2. 如何设置视频关键帧I帧间隔问题

刚开始我只使用-g命令，设置GOP长度，编码后，发现I帧间隔长度并不是我想要的，后来我通过以下命令问题解决了：

```bash
-keyint_min 60 -g 60 -sc_threshold 0
1
```

其中-keyint_min为最小关键帧间隔，我这里设置为60帧；-sc_threshold这个命令会根据视频的运动场景，自动为你添加额外的I帧，所以会导致你编出来的视频关键帧间隔不是你设置的长度，这是只要将它设为0，问题就得到解决了！！







## OpenCV



```
const mat = cv.imdecode(Buffer.from(data, 'base64))
mat.SaveImage(savePath)
```





```
const cv = require('opencv4nodejs');
 
const originalImage = cv.imread('C:/Users/N/Desktop/Test.jpg');
 
const grayImage = originalImage.bgrToGray();
 
cv.imshow('Grey Image', grayImage);
cv.imshow('Original Image', originalImage);
 
cv.waitKey();
```



```
// convert to normal array
const normalArray = Array.from(imageData);
//nest the pixel channels
const channels = 4 //canvas pixels contain 4 elements: RGBA
const nestedChannelArray = _.chunk(normalArray, channels);
const nestedImageArray = _.chunk(nestedChannelArray, height);

//nestedImageArray is the correct shape to be converted to matrix. 

const RGBAmat = new cv.Mat(nestedImageArray, cv.CV_8UC4);

//openCV often defaults to BGR-type image matrix, so lets color convert the pixel order

const BGRAmat = RGBAmat.cvtColor(cv.COLOR_RGBA2BGRA);
```



### 图片相似度

- https://juejin.cn/post/6844904016686628877



## GIF



```
https://github.com/kohler/gifsicle
```





## exec



```
# https://www.jianshu.com/p/b1dc42c152ab
```





```javascript
var exec = require('child_process').exec;

    const cmd = `cd ${global.startPath} && git pull origin master`;
    console.log(`updateCode:${new Date().getTime()}`);
    exec(cmd, (error, stdout, stderr) => {
      if (error) {
        throw error;
      }
      return res.msg(200, {
        stdout: stdout,
        stderr: stderr
      });
    })
```



```javascript

const mecabSpawn = require('mecab-spawn')
const mecab = mecabSpawn.spawn()


var spawn = require('child_process').spawn,
    child = spawn('phantomjs');

child.stdin.setEncoding('utf-8');
child.stdout.pipe(process.stdout);

child.stdin.write("console.log('Hello from PhantomJS')\n");

child.stdin.end(); /// this call seems necessary, at least with plain node.js executable
```



# SVG 格式

**SVG**

**关键词**：无损、矢量图、体积小、不失真、兼容性好

**可缩放矢量图形 **英文 Scalable Vector Graphics(SVG)，是无损的、矢量图。

SVG是一种用 XML 定义的语言，用来描述二维矢量及矢量/栅格图形。SVG提供了3种类型的图形对象：矢量图形（vectorgraphicshape例如：由直线和曲线组成的路径）、图象(image)、文本(text)。图形对象还可进行分组、添加样式、变换、组合等操作，特征集包括嵌套变换（nestedtransformations）、剪切路径（clippingpaths）、alpha 蒙板（alphamasks）、滤镜效果（filtereffects）、模板对象（templateobjects）和其它扩展（extensibility）。

SVG 跟上面这些图片格式最大的不同，是 SVG 是矢量图。这意味着 SVG 图片由直线和曲线以及绘制它们的方法组成。当你放大一个 SVG 图片的时候，你看到的还是线和曲线，而不会出现像素点。这意味着 SVG 图片在放大时，不会失真，所以它非常适合用来绘制企业 Logo、Icon 等。

**优点：**

- SVG 可被非常多的工具读取和修改（比如记事本）。
- SVG 与 JPEG 和 GIF 图像比起来，尺寸更小，且可压缩性更强。
- SVG 是可伸缩的。
- SVG 图像中的文本是可选的，同时也是可搜索的（很适合制作地图）。
- SVG 可以与 JavaScript 技术一起运行
- SVG图形格式支持多种滤镜和特殊效果，在不改变图像内容的前提下可以实现位图格式中类似文字阴影的效果。
- SVG图形格式可以用来动态生成图形。例如，可用 SVG 动态生成具有交互功能的地图，嵌入网页中，并显示给终端用户。

**缺点：**

- 渲染成本比较高，对于性能有影响。
- SVG 的学习成本比较高，因为它是可编程的。

**适用场景**

1、高保真度复杂矢量文档已是并将继续是 SVG 的最佳点。它非常详细，适用于查看和打印，可以是独立的，也可以嵌入到网页中
2、在WEB项目中的平面图绘制，如需要绘制线，多边形，图片等。
3、数据可视化。

> SVG 只是 Web 开发常用的一种矢量图，其实矢量图常见还有几种格式：BW 格式、AI 格式、CDR 格式、ICO 格式。



# pm2

```
systemctl start postgresql.service  # ubuntu 18.04 
systemctl status postgresql-13      # centos7

pm2 save
pm2 dump // 此时会备份 pm2 list 中的所有项目启动方式
pm2 resurrect // 重启备份的所有项目


cd /yingedu/soft/redis-6.2.6/src/
vi redis.conf
./redis-server /xxx/yyyy/redis.conf
pm2 --name redis start "./run.sh"

```



## rename



```
pm2 restart id --name newName
```



# nginx

- https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-centos-7

```
yum install nginx
nginx -t # 显示主配置文件路径，并检查语法错误
systemctl start nginx
```





## 本地端口转发



```
yum install nginx
```





```
/etc/nginx/conf.d/default.conf

server{
    listen       xxx;
    server_name       localhost;
    location / {
     proxy_pass http://localhost:yyy;
     proxy_set_header    Host             $host;
         proxy_set_header    X-Real-IP        $remote_addr;
         proxy_set_header    X-Forwarded-For  $proxy_add_x_forwarded_for;
         proxy_set_header    HTTP_X_FORWARDED_FOR $remote_addr;
         proxy_redirect      default;
    }
}
```



## 转发websocket

```
# 同时转发http 和 websocket 
# /etc/nginx_conf.d/testDiff.conf
map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

upstream diffServer {
  server localhost:10000;
  server localhost:10001;
  server localhost:10002;
  server localhost:10003;
  server localhost:10004;
  server localhost:10005;
  server localhost:10006;
  server localhost:10007;
  server localhost:10008;
  server localhost:10009;
}

server {
  listen 7116;
  server_name localhost;

  location / {
    location / {
      proxy_pass http://diffServer;
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
```

```
# /etc/nginx/nginx.conf
user  root;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;


}
```



# docker

[官方镜像](https://hub.docker.com/_/centos/tags)



> ```
> doc\lang\programming\postgresql summary.md  看这里
> ### Xshell如何连接Docker容器中的Linux
> ```



- https://juejin.cn/post/6857283423380504584

  > 如何查看Docker容器环境变量，如何向容器传递环境变量

- https://xiaorui.cc/archives/1158

  - https://www.cnblogs.com/yinzhengjie/p/12239341.html

  > lscpu 
  >
  > ```
  > -m 128M # 内存限制 128M
  > --cpus 2 --cpuset-cpus 1,4 # 限制CPU 核心数为2，只分配第1核和第4核
  > 
  > 
  > # https://www.cnblogs.com/mingyueyy/p/15475150.html
  > Docker-Compose 是用来管理容器的，类似用户容器管家，我们有N多台容器或者应用需要启动的时候，如果手动去操作，是非常耗费时间的，如果有了 Docker-Compose 只需要一个配置文件就可以帮我们搞定，但是 Docker-Compose 只能管理当前主机上的 Docker，不能去管理其他服务器上的服务。意思就是单机环境。
  > 
  > Docker Swarm 是由Docker 公司研发的一款用来管理集群上的Docker容器工具，弥补了 Docker-Compose 单节点的缺陷，Docker Swarm 可以帮助我们启动容器，监控容器的状态，如果容器服务挂掉会重新启动一个新的容器，保证正常的对外提供服务，也支持服务之间的负载均衡。而且这些东西 Docker-Compose是不支持的，
  > 
  > 
  > ```
> curl https://xxxx.com/getData | jq
>
> jq 命令去除转义，最后输出的是格式化的json字符串，既去掉了转义字符


```
docker run --name running-blog-www\
 -p 4000:8080\
 -e "CONFIG_ENV=$(</path/to/config.json)"\
 -e BUILD_ENV=prod\
 -d blog-www:1.0.0
  
var app = new express();
switch ((process.env.ENV_TYP).toUpperCase()) {
    case 'DEV':
        ProxyConfig = require('./proxy/dev-proxy');
        break;
    case 'ST':
        ProxyConfig = require('./proxy/st-proxy');
        break;
    case 'PRD':
        ProxyConfig = require('./proxy/prd-proxy');
        break;
    default:
        ProxyConfig = require('./proxy/dev-proxy');
        break;
}
new ProxyConfig().setProxy(app);


export NODE_ENV=dev



```



```

var stdin = process.stdin,
    stdout = process.stdout,
    inputChunks = [];

stdin.resume();
stdin.setEncoding('utf8');

stdin.on('data', function (chunk) {
    inputChunks.push(chunk);
});

stdin.on('end', function () {
    var inputJSON = inputChunks.join(),
        parsedData = JSON.parse(inputJSON),
        outputJSON = JSON.stringify(parsedData, null, '    ');
    stdout.write(outputJSON);
    stdout.write('\n');
});
```



```

yum whatprovides ifconfig
yum whatprovides crontab
yum whatprovides git
yum install net-tools cronie -y

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
	docker run -tid --name centos7_server_6006_ENV --net=bridge --ip=10.88.0.2 -p 222:22 --privileged=true centos:7 /sbin/init
		# 使用默认网络，并固定 IP
		
	docker run -tid --name centos7_server_6006 --net=custom --ip=172.18.0.2 -p 222:22 --privileged=true centos:7 /sbin/init

		# 此命令会自动下载镜像
		# -p 222:22 表示将宿主的222端口映射容器的22端口




环境变量

let j = require('./config.js')
require('fs').writeFileSync('config.json', JSON.stringify(j).replace(/"/g, `\\"`), {encoding:'utf8', flag:'w'} )



--env-file path_to_env_file 选项将其传递到用于启动容器代理的 docker run 命令。


docker run --name running-blog-www\
 -p 4000:8080\
 -e "CONFIG_ENV=$(</path/to/config.json)"\


docker run -tid --name centos7_server_6006_ENV -e "CONFIG_ENV={\"updatePassword\":\"\"}" --net=bridge --ip=10.88.0.3  --privileged=true centos:7 /sbin/init


docker cp /usr/local/node-v14.17.0-linux-x64 centos7_server_6006_ENV:/usr/local


docker exec -it centos7_server_6006_ENV /bin/bash
	# 运行docker 的shell

	kill -9 $(jobs -p) && exit
		# 可以正常 exit 容器了

	docker stop centos7_server_6006_ENV
	docker start centos7_server_6006_ENV

	pm2 --name aicbyserver_v2_6006 start "node server.js"

	pm2 save
	pm2 dump // 此时会备份 pm2 list 中的所有项目启动方式
	pm2 resurrect // 重启备份的所有项目

	vi auto_run.ssh
		pm2 resurrect 
	
	chmod +x auto_run.sh

	设置开机启动
	vi /etc/rc.d/rc.local
		/project/auto_run.sh 
	chmod +x /etc/rc.d/rc.local
	
	 crontab -e
		@reboot  /project/auto_run.sh


	docker exec -it centos7_server_6006_ENV  pm2 resurrect;/bin/bash
		# 在容器内执行命令
	docker exec -it centos7_server_6006_ENV /bin/bash
		# 进入容器


( async ()=> {

  let bent = require('bent')
  
  let json = {
    userID: 0
  }
  
  let post = bent('http://127.0.0.1:6006', 'POST', 'json', 200)
  let response = await post('/test', json)
  console.log( response )

}) ()


JSON.parse( process.env.CONFIG_ENV )


CONFIG_ENV



执行多条命令使用分号隔开
docker exec web-blog /bin/sh -c "mkdir /www/default/runtime; \
                                 chmod +x /www/default/ank; \
                                 /www/default/ank clearcache; \
                                 /www/default/ank optimize:config; \
                                 /www/default/ank optimize:preload; \
                                 chown -R www-data:www-data /www/default; \
                                 chmod 544 -R /www/default; \
                                 chmod 754 -R /www/default/runtime;"

docker run 5800 sh -c "ls && echo '-------' &&  ls"


阿里云镜像库的通过git自动打包功能

https://blog.csdn.net/YL3126/article/details/122184386

使用私有镜像仓库创建应用

https://help.aliyun.com/document_detail/86307.html


通过docker和gitlab实现项目自动打包部署

https://blog.csdn.net/qq_44845473/article/details/126045368


Docker-compose编排微服务顺序启动

https://cloud.tencent.com/developer/article/1620658?from=15425



Docker一从入门到实践  ENTRYPOINT 入口点

https://yeasy.gitbook.io/docker_practice/image/dockerfile/entrypoint
	# docker 可以被当作命令行来运行，还可以加参数

FROM ubuntu:18.04
RUN apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*
ENTRYPOINT [ "curl", "-s", "http://myip.ipip.net" ]
这次我们再来尝试直接使用 docker run myip -i：
$ docker run myip
	当前 IP：61.148.226.66 来自：北京市 联通


在构建镜像的时候，需要额外小心，每一层尽量只包含该层需要添加的东西，任何额外的东西应该在该层构建结束前清理掉。
分层存储的特征还使得镜像的复用、定制变的更为容易。甚至可以用之前构建好的镜像作为基础层，然后进一步添加新的层，以定制自己所需的内容，构建新的镜像。

按照 Docker 最佳实践的要求，容器不应该向其存储层内写入任何数据，容器存储层要保持无状态化。所有的文件写入操作，都应该使用 数据卷（Volume）、或者 绑定宿主目录，在这些位置的读写会跳过容器存储层，直接对宿主（或网络存储）发生读写，其性能和稳定性更高。
数据卷的生存周期独立于容器，容器消亡，数据卷不会消亡。因此，使用数据卷后，容器删除或者重新运行之后，数据却不会丢失。


仓库名经常以 两段式路径 形式出现，比如 jwilder/nginx-proxy，前者往往意味着 Docker Registry 多用户环境下的用户名，后者则往往是对应的软件名。


列出已经下载下来的镜像
	docker image ls

yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-selinux \
                  docker-engine-selinux \
                  docker-engine

	# 卸载 docker


yum install -y yum-utils

yum-config-manager \
    --add-repo \
    https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
	# 官方源 https://download.docker.com/linux/centos/docker-ce.repo

sudo sed -i 's/download.docker.com/mirrors.aliyun.com\/docker-ce/g' /etc/yum.repos.d/docker-ce.repo
	# 切换为阿里源

vi /etc/yum/pluginconf.d/fastestmirror.conf
	enabled=0;  # 改成这个

vi /etc/yum.conf
	plugins=0; # 改成这个


yum install docker-ce docker-ce-cli containerd.io -y
	# 安装 docker

docker run --rm hello-world
	# 测试是否安装正确
		# --rm 表示运行后既删除


systemctl enable docker && \
systemctl start docker


docker pull nginx
docker run --name webserver -d -p 80:80 nginx
	# 运行 docker 镜像，80 映射 80

curl http://localhost
	# 成功访问网页

docker exec -it webserver bash -c "echo $PATH"
	# 这里的 $PATH 会被解析成本机的值 

docker exec -it webserver bash -c "echo '<h1>Hello, Docker\!</h1>' > /usr/share/nginx/html/index.html"
	# 修改主页，注意：感叹号需要转义
	curl http://localhost

docker diff webserver
	# 我们修改了容器的文件，也就是改动了容器的存储层。
	# 比较相对基础镜像修改了哪


慎用docker commit

使用 docker commit 意味着所有对镜像的操作都是黑箱操作，生成的镜像也被称为 黑箱镜像，换句话说，就是除了制作镜像的人知道执行过什么命令、怎么生成的镜像，别人根本无从得知。而且，即使是这个制作镜像的人，过一段时间后也无法记清具体的操作。这种黑箱镜像的维护工作是非常痛苦的。


使用 Dockerfile 定制镜像
	Dockerfile 是一个文本文件，其内包含了一条条的 指令(Instruction)，每一条指令构建一层，因此每一条指令的内容，就是描述该层应当如何构建

定制 mynjginx 镜像

mkdir mynginx && \
cd mynginx && \
touch Dockerfile && \
echo "FROM nginx 
RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html" > Dockerfile


docker build -t nginx:v2 .
	构建镜像

docker run --name webserver -d -p 80:80 nginx:v2 && \
curl http://localhost && \
docker stop webserver && \
docker rm webserver
	# 运行 docker 镜像，80 映射 80


https://nodejs.org/download/release/v14.21.1/node-v14.21.1-linux-x64.tar.gz


yum install net-tools cronie -y

docker run -tid --name centos7_server_6006 -p 222:22 --privileged=true centos:7 /sbin/init
	# 此命令会自动下载镜像
	# -p 222:22 表示将宿主的222端口映射容器的22端口




构建实际项目

docker network ls
docker network create --subnet=172.20.0.0/16 customnetwork
	# 创建自定义网络


docker system prune --volumes
	# 删除所有未使用镜像及缓存，自义定网络

docker network ls | grep customnetwork
if [ $? -ne 0 ] ;then
    echo 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    echo 'customnetwork create success'
fi
	# 自定义网络不存在则创建

docker run -tid --name centos7_server_6006 -p 222:22 --privileged=true centos:7 /sbin/init

docker pull centos:7
	# 拉镜像只需要一次
	# docker image ls
	# docker image rm centos:7
	# docker image rm centos7_server_6006

docker system prune --volumes -y 
docker image ls | grep centos:7
if [ $? -ne 0 ] ;then
    echo 'image centos:7 not found, pull'
    docker pull centos:7
    echo 'image centos:7 pull success'
fi
docker network ls | grep customnetwork
if [ $? -ne 0 ] ;then
    echo 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    echo 'customnetwork create success'
fi
mkdir centos7_server_6006 && \
cd centos7_server_6006 && \
touch Dockerfile && \
echo "FROM centos:7 
RUN set -x; buildDeps='curl net-tools cronie lsof git' && \\
    yum install -y \$buildDeps && \\
    git clone http://用户名:这里是AccessTokens@gitlab.xxx.git && \\
    curl -O 'https://nodejs.org/download/release/v14.21.1/node-v14.21.1-linux-x64.tar.gz'  && \\
    tar zxvf node-v14.21.1-linux-x64.tar.gz -C /usr/local && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/node /usr/local/bin/node && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npm /usr/local/bin/npm && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npx /usr/local/bin/npx && \\
    npm install cnpm@7.1.0  pm2@4.5.1 -g --registry=https://registry.npm.taobao.org && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/cnpm /usr/local/bin/cnpm && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/pm2 /usr/local/bin/pm2 && \\
    cd /aicbyserver_v2 && \\
    cnpm i " > Dockerfile && \
docker build -t centos7_server_6006 . && \
docker run -tid --name centos7_server_6006_ENV -e "CONFIG_ENV=双引号转义了的json配置串" --net=customnetwork --ip=172.20.0.2 -p 222:22 --privileged=true centos7_server_6006 /sbin/init && \
docker exec -it centos7_server_6006_ENV bash -c "cd /aicbyserver_v2 && pm2 --name aicbyserver_v2_6006 start 'node server.js' " -c "cd /aicbyserver_v2 && pm2 --name aicbyserver_v2_6006 start 'node server.js' " && \
docker stop centos7_server_6006_ENV && \
docker rm centos7_server_6006_ENV  && \
docker image rm centos7_server_6006



	kill -9 $(jobs -p)
		# 可以正常 exit 容器了


配置 nginx 80 转 6006


vi /etc/nginx/nginx.conf

user  root;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;


}



vi /etc/nginx/conf.d/docker_6006.conf

map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

upstream centos7_server_6006 {
  server 172.20.0.2:6006;
}

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











nmap 172.20.0.2 -p6006
	# 扫描指定端口是否开放

git config --global user.name "gada" && \
git config --global user.email "x50@qq.com" && \
git config --global push.default matching  


git config --system --list
	# 查看系统config
　　
git config --global  --list
	# 查看当前用户（global）配置

git config --local  --list
	# 查看当前仓库配置信息


ssh-keygen -t rsa -C "162350@qq.com"

ssh -i ~/.ssh/id_rsa -T git@xxx.com
	--> Welcome to GitLab

yum install \
https://repo.ius.io/ius-release-el7.rpm \
https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
yum remove git && \
yum install git236 -y
	# need Git version 2.3.0

git clone http://用户名:这里是AccessTokens@gitlab.xxxx.git



解决方式是创建一个access token，然后在拉取代码时带上自己的username和token,就不用再输入用户名密码

具体操作如下：

1、登录 gitlab，点击右上角自己头像选择 settings

2、左边导航栏选择 Access Tokens

3、name 输入框给自己要创建的token起个名字

4、点击create personal access token 创建token （下面还有到期时间、权限可以根据自己需要选择具体如下图）

5、在docker容器中可以通过如下方式使用

git clone https://用户名:token@仓库地址



mkdir /root/.ssh/ && \
cat /root/keyksb > /root/.ssh/id_rsa && \
chmod 600 /root/.ssh/id_rsa && \
touch /root/.ssh/known_hosts && \
ssh-keyscan gitlab.ksbao.com >> /root/.ssh/known_hosts
	# https://github.com/jmrf/private-repo-clone-docker-build-example/blob/master/test.Dockerfile




export GIT_SSH_COMMAND="ssh -i /root/keyksb" && git clone http://xxxx.git

GIT_SSH_COMMAND='ssh -o IdentitiesOnly=yes -i /root/keyksb -F /dev/null' git clone http://xx.git

git clone 私有仓的例子
https://github.com/jmrf/private-repo-clone-docker-build-example






自定义IP  Docker Compose
https://www.howtogeek.com/devops/how-to-assign-a-static-ip-to-a-docker-container/


How to set static ip when using default network

docker-compose will create a network named after your project name (usually your folder, unless you specified COMPOSE_PROJECT_NAME) suffixed with _default. So if the project name is foo, the default network name will be foo_default. It will always be this unless you specify otherwise.

Once this network has been created, docker-compose will never remove it. This means you need to remove it yourself using docker.

$ docker network rm foo_default
Once you've done this, docker-compose will attempt to recreate your network. If you've specified some network options in your docker-compose.yml file, it will create the network with your new options.

version: '3.4'
networks:
  default:
    ipam:
      config:
        - subnet: 10.5.0.0/16


FROM centos:7

RUN set -x; buildDeps='curl' \
    && apt-get update \
    && apt-get install -y $buildDeps \
    && curl -O "https://nodejs.org/download/release/v14.21.1/node-v14.21.1-linux-x64.tar.gz" \
    && tar -xzvf node-v14.21.1-linux-x64.tar.gz -C /usr/local  \
    && apt-get purge -y --auto-remove $buildDeps

镜像是多层存储，每一层的东西并不会在下一层被删除，会一直跟随着镜像。因此镜像构建时，一定要确保每一层只添加真正需要添加的东西，任何无关的东西都应该清理掉

```



```
docker system prune --volumes -y 
docker image ls | grep centos:7
if [ $? -ne 0 ] ;then
    echo 'image centos:7 not found, pull'
    docker pull centos:7
    echo 'image centos:7 pull success'
fi
docker network ls | grep customnetwork
if [ $? -ne 0 ] ;then
    echo 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    echo 'customnetwork create success'
fi
mkdir centos7_server_6006 && \
cd centos7_server_6006 && \
touch Dockerfile && \
echo "FROM centos:7 
RUN set -x; buildDeps='epel-release curl net-tools cronie lsof git' && \\
    yum install -y \$buildDeps && \\
    yum install -y nginx redis && \\
    git clone https://用户名:token@仓库地址 && \\
    curl -O 'https://nodejs.org/download/release/v14.21.1/node-v14.21.1-linux-x64.tar.gz'  && \\
    tar zxvf node-v14.21.1-linux-x64.tar.gz -C /usr/local && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/node /usr/local/bin/node && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npm /usr/local/bin/npm && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npx /usr/local/bin/npx && \\
    npm install cnpm@7.1.0  pm2@4.5.1 -g --registry=https://registry.npm.taobao.org && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/cnpm /usr/local/bin/cnpm && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/pm2 /usr/local/bin/pm2 && \\
    cd /aicbyserver_v2 && \\
    cnpm i " > Dockerfile && \
docker build -t centos7_server_6006 . && \
docker run -tid --name centos7_server_6006_ENV -e "CONFIG_ENV=冒号转义后的json" --net=customnetwork --ip=172.20.0.2 -p 222:22 --privileged=true centos7_server_6006 /sbin/init && \
docker exec -it centos7_server_6006_ENV bash -c "cd /aicbyserver_v2 && pm2 --name aicbyserver_v2_6006 start 'node server.js' " -c "cd /aicbyserver_v2 && pm2 --name aicbyserver_v2_6006 start 'node server.js' " && \
docker exec -it centos7_server_6006_ENV bash -c "systemctl enable nginx && systemctl start nginx && systemctl status nginx" && \
docker exec -it centos7_server_6006_ENV bash -c "systemctl start redis.service && systemctl enable redis && systemctl status redis.service && redis-cli ping" && \
docker stop centos7_server_6006_ENV && \
docker rm centos7_server_6006_ENV  && \
docker image rm centos7_server_6006
```



```
docker system prune --volumes -y 
docker image ls | grep centos:7
if [ $? -ne 0 ] ;then
    echo 'image centos:7 not found, pull'
    docker pull centos:7
    echo 'image centos:7 pull success'
fi
docker network ls | grep customnetwork
if [ $? -ne 0 ] ;then
    echo 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    echo 'customnetwork create success'
fi
mkdir centos7_server_6006 && \
cd centos7_server_6006 && \
touch Dockerfile && \
echo "FROM centos:7 
RUN set -x; buildDeps='epel-release curl net-tools cronie lsof git' && \\
    yum install -y \$buildDeps && \\
    yum install -y nginx redis nfs-utils crontabs && \\
    mkdir -p /project/shared && \\
    mkdir -p /project/script && \\
    chmod 755 /project/shared && \\
    cd /project && \\
    git clone http://用户名:AccessToten@gitlab.xxxxx.git && \\
    curl -O 'https://nodejs.org/download/release/v14.21.1/node-v14.21.1-linux-x64.tar.gz'  && \\
    tar zxvf node-v14.21.1-linux-x64.tar.gz -C /usr/local && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/node /usr/local/bin/node && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npm /usr/local/bin/npm && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npx /usr/local/bin/npx && \\
    npm install cnpm@7.1.0  pm2@4.5.1 -g --registry=https://registry.npm.taobao.org && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/cnpm /usr/local/bin/cnpm && \\
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/pm2 /usr/local/bin/pm2 && \\
    cd /project/aicbyserver_v2 && \\
    cnpm i " > Dockerfile && \
docker build -t centos7_server_6006 . && \
docker run -tid --name centos7_server_6006_ENV -e "CONFIG_ENV=这里放冒号转义后的json" --net=customnetwork --ip=172.20.0.2 -p 222:22 --privileged=true centos7_server_6006 /sbin/init && \
docker exec -it centos7_server_6006_ENV bash -c "cd /project/aicbyserver_v2 && pm2 --name aicbyserver_v2_6006 start 'node server.js' "  && \
docker exec -it centos7_server_6006_ENV bash -c "systemctl enable nginx && systemctl start nginx && systemctl status nginx" && \
docker exec -it centos7_server_6006_ENV bash -c "systemctl start redis.service && systemctl enable redis && systemctl status redis.service && redis-cli ping" && \
docker exec -it centos7_server_6006_ENV bash -c "systemctl enable rpcbind && systemctl start rpcbind" && \
docker exec -it centos7_server_6006_ENV bash -c "mkdir -p /project/shared/test_cooperate_img && chmod 755 /project/shared/test_cooperate_img && \\
    ls -al /project/shared/test_cooperate_img" && \
docker exec -it centos7_server_6006_ENV bash -c "showmount -e 172.16.15.13" && \
docker exec -it centos7_server_6006_ENV bash -c "mount -t nfs 172.16.15.13:/yingedu/web/aicby_v2/test_cooperate_img  /project/shared/test_cooperate_img" && \
docker exec -it centos7_server_6006_ENV bash -c "echo 'hello from docker' > /project/shared/test_cooperate_img/hi.txt" && \
cat /yingedu/web/aicby_v2/test_cooperate_img/hi.txt && \
docker exec -it centos7_server_6006_ENV bash -c "echo 'umount /project/shared/test_cooperate_img 
mount -t nfs 172.16.15.13:/xx/xxx  /project/xxxxx_img  
if [ \$? -ne 0 ]; then 
    echo mount failed  
    sleep 30s; echo try agin 
    umount /project/shared/test_cooperate_img 
    mount -t nfs 172.16.15.13:/xxx_img  /project/shared/test_cooperate_img 
else 
    echo mount nfs succeed
fi
' > /project/script/auto_mount.sh" && \
docker exec -it centos7_server_6006_ENV bash -c "echo '@reboot  /project/script/auto_mount.sh' > /var/spool/cron/root" && \
docker exec -it centos7_server_6006_ENV bash -c "chmod +x /project/script/auto_mount.sh" && \
docker exec -it centos7_server_6006_ENV bash -c "crontab -l" && \
docker exec -it centos7_server_6006_ENV bash -c "cat /project/script/auto_mount.sh" && \
docker stop centos7_server_6006_ENV && \
docker rm centos7_server_6006_ENV  && \
docker image rm centos7_server_6006




	kill -9 $(jobs -p)
		# 可以正常 exit 容器了


配置 nginx 80 转 6006


vi /etc/nginx/nginx.conf

user  root;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;


}



vi /etc/nginx/conf.d/docker_6006.conf

map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

upstream centos7_server_6006 {
  server 172.20.0.2:6006;
}

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


nmap 172.20.0.2 -p6006
	# 扫描指定端口是否开放






```



```powershell


$t = docker ps -a
if ($t -like "*centos7_server_6006_ENV*")
{
    docker stop centos7_server_6006_ENV
    docker rm centos7_server_6006_ENV
    Write-Host "object centos7_server_6006_ENV deleted"
}

$t = docker image ls
if ($t -like "*centos7_server_6006*")
{
    docker image rm centos7_server_6006
    Write-Host "image centos7_server_6006 deleted"
}

$t = docker image ls
if ($t -like "*centos*")
{
    docker image rm centos:7
    Write-Host "image centos:7 deleted"
}

$t = docker network ls
if ($t -like "*customnetwork*")
{
    docker network rm customnetwork
    Write-Output 'customnetwork deleted'
}

docker system prune --volumes

docker network create --subnet=172.20.0.0/16 customnetwork
Write-Output 'customnetwork created'

docker pull centos:7
Write-Output 'image centos:7 created'

$dir="E:\docker"
$profileDir="$dir\centos7_server_6006"
Write-Host $profileDir
if (Test-Path -Path $profileDir) {
    Remove-Item -Path $profileDir -Force -Recurse
}


New-Item -ItemType Directory -Path $profileDir -Force
#New-Item -ItemType File -Path "$profileDir\Dockerfile"

Set-Location $profileDir


[System.Text.Encoding]::UTF8.GetBytes("FROM centos:7 
RUN set -x; buildDeps='epel-release curl net-tools cronie lsof git' && \
yum install -y `$buildDeps && \
yum install -y nginx redis nfs-utils crontabs libaio numactl initscripts && \
mkdir -p /project/shared && \
mkdir -p /project/script && \
chmod 755 /project/shared && \
cd /project && \
git clone https://账号:xx@github.com/dlxj/server_template.git && \
curl -O 'https://nodejs.org/download/release/v14.21.1/node-v14.21.1-linux-x64.tar.gz' && \
curl -O 'https://cdn.mysql.com/archives/mysql-5.7/mysql-5.7.39-linux-glibc2.12-x86_64.tar.gz' && \
tar zxvf node-v14.21.1-linux-x64.tar.gz -C /usr/local && \
tar zxvf mysql-5.7.39-linux-glibc2.12-x86_64.tar.gz -C /usr/local && \
ln -s /usr/local/node-v14.21.1-linux-x64/bin/node /usr/local/bin/node && \
ln -s /usr/local/node-v14.21.1-linux-x64/bin/npm /usr/local/bin/npm && \
ln -s /usr/local/node-v14.21.1-linux-x64/bin/npx /usr/local/bin/npx && \
npm install cnpm@7.1.0  pm2@4.5.1 -g && \
ln -s /usr/local/node-v14.21.1-linux-x64/bin/cnpm /usr/local/bin/cnpm && \
ln -s /usr/local/node-v14.21.1-linux-x64/bin/pm2 /usr/local/bin/pm2 && \
cd /project/server_template && \
npm i && \
ln -s /usr/local/mysql-5.7.39-linux-glibc2.12-x86_64 /usr/local/mysql && \
cd /usr/local/mysql && \
groupadd mysql && \
useradd -r -g mysql mysql && \
cd /usr/local/mysql && \
chown -R mysql . && \
chgrp -R mysql . && \
bin/mysql_install_db --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data && \
cp support-files/mysql.server /etc/init.d/mysql.server && \
service mysql.server start && \
service mysql.server status && \
cat /root/.mysql_secret") | Set-Content Dockerfile -Encoding Byte

docker build -t centos7_server_6006 .

docker run -tid --name centos7_server_6006_ENV -e 'CONFIG_ENV={\"updatePassword\":\"\",\"debugPassword\":\"\",\"dev\":true,\"http\":{\"port\":6006,\"headers\":{\"Server\":\"Server\",\"Access-Control-Allow-Origin\":\"*\",\"Content-Type\":\"text/json\",\"Access-Control-Allow-Headers\":\"content-type\",\"Access-Control-Request-Method\":\"GET,POST\"},\"encrypt\":false,\"privateKey\":\"\",\"publicKey\":\"\"},\"service\":{\"privateKey\":\"\",\"publicKey\":\"\",\"require\":{}},\"dbs\":{\"localDB\":{\"host\":\"127.0.0.1\",\"user\":\"root\",\"password\":\"root\",\"database\":\"ocr\",\"port\":3306,\"multipleStatements\":true,\"connectTimeout\":60000,\"connectionLimit\":4096},\"defaultDB\":{\"host\":\"127.0.0.1\",\"user\":\"root\",\"password\":\"root\",\"database\":\"tmp\",\"port\":3306,\"multipleStatements\":true,\"connectTimeout\":60000,\"connectionLimit\":50},\"baseDB\":{\"host\":\"127.0.0.1\",\"user\":\"root\",\"password\":\"root\",\"database\":\"tmp\",\"port\":3306,\"multipleStatements\":true,\"connectTimeout\":60000,\"connectionLimit\":50},\"tiku_bookDB\":{\"host\":\"127.0.0.1\",\"user\":\"root\",\"password\":\"root\",\"database\":\"tmp\",\"port\":3306,\"multipleStatements\":true,\"connectTimeout\":60000,\"connectionLimit\":50},\"tmp\":{\"host\":\"127.0.0.1\",\"user\":\"root\",\"password\":\"root\",\"database\":\"tmp\",\"port\":3306,\"multipleStatements\":true,\"connectTimeout\":60000,\"connectionLimit\":50},\"ocrDB\":{\"host\":\"127.0.0.1\",\"user\":\"root\",\"password\":\"root\",\"database\":\"temp\",\"port\":3306,\"multipleStatements\":true,\"connectTimeout\":60000,\"connectionLimit\":50}},\"redis\":{\"defaultDB\":{\"host\":\"127.0.0.1\",\"port\":6379,\"prefix\":null,\"db\":0}},\"dataSet\":{}}' --net=customnetwork --ip=172.20.0.2 -p 222:22 -p 6006:6006 -p 3306:3306 -p 6379:6379 -p 543:543  --privileged=true centos7_server_6006 /sbin/init 
docker exec -it centos7_server_6006_ENV bash -c "cd /project/server_template && pm2 --name centos7_server_6006 start 'node server.js' "  
docker exec -it centos7_server_6006_ENV bash -c "systemctl enable nginx && systemctl start nginx && systemctl status nginx" 
docker exec -it centos7_server_6006_ENV bash -c "systemctl start redis.service && systemctl enable redis && systemctl status redis.service && redis-cli ping" 
docker exec -it centos7_server_6006_ENV bash -c "pm2 logs centos7_server_6006"
```





```
# 删除和重建镜像和网络
$t = docker ps -a
if ($t -like "*centos7_server_6006_ENV*")
{
    docker stop centos7_server_6006_ENV
    docker rm centos7_server_6006_ENV
    Write-Host "object centos7_server_6006_ENV deleted"
}

$t = docker image ls
if ($t -like "*centos7_server_6006*")
{
    docker image rm centos7_server_6006
    Write-Host "image centos7_server_6006 deleted"
}

$t = docker image ls
if ($t -like "*centos*")
{
    docker image rm centos:7
    Write-Host "image centos:7 deleted"
}

$t = docker network ls
if ($t -like "*customnetwork*")
{
    docker network rm customnetwork
    Write-Output 'customnetwork deleted'
}

docker system prune --volumes

docker network create --subnet=172.20.0.0/16 customnetwork
Write-Output 'customnetwork created'

docker pull centos:7
Write-Output 'image centos:7 created'
```





```
b64.js 转义配置
let j = require('./config.js')
require('fs').writeFileSync('config.json', JSON.stringify(j).replace(/"/g, `\\"`), {encoding:'utf8', flag:'w'} )
console.log(JSON.stringify(j).replace(/"/g, `\\"`))
require('fs').writeFileSync('config.json', JSON.stringify(j).replace(/"/g, `\\"`), {encoding:'utf8', flag:'w'} )
```



## Dockerfile

```
# Use the official Golang image as the builder
FROM golang:1.20.3-alpine as builder

# Enable CGO to use C libraries (set to 0 to disable it)
# We set it to 0 to build a fully static binary for our final image
ENV CGO_ENABLED=0

# Set the working directory
WORKDIR /app

# Copy the Go Modules manifests (go.mod and go.sum files)
COPY go.mod go.sum ./

# Download the dependencies
RUN go mod download

# Copy the source code
COPY . .

# Build the Go application and output the binary to /app/ChatGPT-Proxy-V4
RUN go build -o /app/ChatGPT-To-API .

# Use a scratch image as the final distroless image
FROM scratch

# Set the working directory
WORKDIR /app

# Copy the built Go binary from the builder stage
COPY --from=builder /app/ChatGPT-To-API /app/ChatGPT-To-API

# Expose the port where the application is running
EXPOSE 8080

# Start the application
CMD [ "./ChatGPT-To-API" ]
```



### 共享目录

```
VOLUME ["C:/myapp"]
```



```
# 要共享的是 windows 的 D:/shared 目录，这样docker 的所有文件是不是都放 这里了？？
run命令加"-v"参数 -v D:/shared:/data
```





## wsl2

- https://learn.microsoft.com/en-us/windows/wsl/install-manual

  > ```
  > wsl --install
  > Turn Windows features on or off # 搜索框输入
  > 	# 打开选项和功能
  > 把 linux 子系统 什么虚拟 全都打开
  > ```

```
wsl_update_x64.msi 安装出错 2503

For WSL2 you will need 2 Windows components so make sure they are already enabled:
Microsoft-Windows-Subsystem-Linux
VirtualMachinePlatform

Also it seems some people have problems with the installer extracting the kernel.
You can always extract it manually with:
msiexec /a "wsl_update_x64.msi" /qb TARGETDIR="C:\temp"
and then copy the kernel file from C:\temp to C:\Windows\System32\lxss\tools

Final version shouldn't have this problem since the install comes from Windows Update.
```





## GPU for docker

[docker-desktop-on-nvidia-gpus](https://www.docker.com/blog/wsl-2-gpu-support-for-docker-desktop-on-nvidia-gpus/)



```undefined
# win10 powershell 执行
# 特权模式创建容器
docker run -tid --name centos7GPU --gpus all --privileged=true centos:7 /sbin/init 
		# 此命令会自动下载镜像
		# -p 222:22 表示将宿主的222端口映射容器的22端口

# 运行docker 的shell
docker exec -it centos7PG10 /bin/bash

docker run -it --rm --gpus all centos:7 nvidia-smi


```



### CentOs7+nvidia-container-runtime

参考：[docker19使用GPU](https://www.jianshu.com/p/84357d5a116a)
 [centos 7 安装nvidia-container-runtime](https://nvidia.github.io/nvidia-container-runtime/)

下载GPU的驱动
 在NVIDIA驱动程序页面下载对应的驱动。

安装NVIDIA-CONTAINER-RUNTIME
 在[https://nvidia.github.io/nvidia-container-runtime/](https://links.jianshu.com/go?to=https%3A%2F%2Fnvidia.github.io%2Fnvidia-container-runtime%2F)查看支持的操作系统和版本，并根据对应选项，添加源，因为我是centos7，所以添加方式为：



```ruby
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-container-runtime/$distribution/nvidia-container-runtime.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-runtime.repo
```

然后直接yum install 就可以了



```undefined
sudo yum install nvidia-container-runtime
```

进行测试，如果出现显卡信息就可以了



```undefined
docker run -it --rm --gpus all centos nvidia-smi
```

### 解决服务器无法联网的问题

1.磨刀砍柴

严格模式：两台同样配置，同样环境的服务器、例如：gcc cuda cmake版本等都完全相同
 简单模式：两台安装了相同版本系统的服务器，例如我的两台都是centos 7

这里我使用了简单模式，因为复杂模式太过复杂

我的一台为实验室服务器 （目标机）一台为租用的腾讯云（借用机）

2.借鸡生蛋

以下操作在腾讯云（借用机）中执行：
 添加源 repo



```ruby
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-container-runtime/$distribution/nvidia-container-runtime.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-runtime.repo
```

接下来需要从源去下载rpm包，但不进行安装
 参考：[yum 下载全量依赖 rpm 包及离线安装（终极解决方案）](https://links.jianshu.com/go?to=https%3A%2F%2Fblog.csdn.net%2Fjlh21%2Farticle%2Fdetails%2F104775084)

所以下载nvidia软件包全部依赖



```bash
#yum deplist 包名
yum deplist nvidia-container-runtime
#展示包的全部依赖

sudo yum -y install yum-utils
#安装 yum-utils
mkdir ~/software_packages
cd ~/software_packages
repotrack nvidia-container-runtime
#此时会将软件的所有依赖包下载到 ~/software_packages
```

这时候将 ~/software_packages 下的文件打包下载



```bash
cd ~
tar -zcvf software_packages.tar.gz ~/software_packages
```

3.斗转星移

此时，登录实验室服务器（目标机），上传刚刚打包的文件，进行解压



```undefined
rz
tar -zxvf software_packages.tar.gz ~/software_packages
```

进入解压的目录离线安装，一定要选择 采用 *.rpm的方式，会自动解决依赖



```bash
cd ~/software_packages
# 离线安装
$ rpm -Uvh --force --nodeps *.rpm
```

## 启动docker 容器



```ruby
docker run -v $(pwd):/workspace/data --gpus all \
-it voidful/wav2vec-u:1.0.0 bash
#成功启动container
#进入container后输入，nvidia-smi
nvidia-smi
#成功显示显卡信息
```





## Docker for CentOS7

[How to Install Docker on CentOS 7](https://phoenixnap.com/kb/how-to-install-docker-centos-7)

[How To Install and Use Docker on CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-centos-7)

```
yum install -y yum-utils device-mapper-persistent-data lvm2 && \
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo && \
yum install -y docker

systemctl start docker && \
systemctl enable docker && \
systemctl status docker 

```



### ChatGPT

```
vi  /etc/docker/daemon.json
改成这样：
{
    "registry-mirrors": [
        "http://hub-mirror.c.163.com",
        "https://docker.mirrors.ustc.edu.cn",
        "https://registry.docker-cn.com"
    ]
}

systemctl daemon-reload && \
service docker restart && \
docker info

# AlmaLinux 开发环境
dnf update -y && \
dnf install -y tar libsodium curl net-tools cronie lsof git wget yum-utils make gcc g++ openssl-devel bzip2-devel libffi-devel zlib-devel


docker pull centos:centos7
	# docker pull centos:centos8  
		# 看看这个行不行
	# docker pull ubuntu:20.04 # 出错
	# docker pull almalinux

docker network create --subnet=172.20.0.0/16 customnetwork
	# docker network rm customnetwork

docker run -tid --name centos8_ChatGPT_507 --net=customnetwork --ip=172.20.0.2 -p 222:22 -p 5077:507 --privileged=true centos:centos8 /sbin/init

docker exec -it centos8_ChatGPT_507 bash

docker 退出方法
	# kill -9  $(jobs -p)
	# exit

# centos8 没有软件源
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-8.repo

sed -i -e"s|mirrors.cloud.aliyuncs.com|mirrors.aliyun.com|g " /etc/yum.repos.d/CentOS-*

sed -i -e "s|releasever|releasever-stream|g" /etc/yum.repos.d/CentOS-*

yum clean all && yum makecache

yum update --allowerasing

yum isntall wget -y

dnf group install "Development Tools"

docker cp node-v18.9.1-linux-x64.tar.gz centos8_ChatGPT_507:/project



docker run -tid --name ubuntu_ChatGPT_507 --net=customnetwork --ip=172.20.0.2 -p 222:22 -p 5077:507 --privileged=true centos:centos7 /sbin/init






docker run -tid --name centos7_ChatGPT_507 --net=customnetwork --ip=172.20.0.2 -p 222:22 -p 5077:507 --privileged=true centos:centos7 /sbin/init

docker stop centos7_ChatGPT_507 && \
docker rm centos7_ChatGPT_507  && \
docker image rm centos:centos7 

docker stop ubuntu_ChatGPT_507 && \
docker rm ubuntu_ChatGPT_507


docker exec -it centos7_ChatGPT_507 bash

yum update -y && \
yum groupinstall -y "Development Tools" "Development Libraries"
	# rm -f /var/run/yum.pid


version=v18.9.1 && \
wget https://nodejs.org/download/release/$version/node-$version-linux-x64.tar.gz && \
tar xvf node-$version-linux-x64.tar.gz && \
cd node-$version-linux-x64/bin && \
chmod +x node npm npx && \
cd ../.. && \
mv node-$version-linux-x64 /usr/local && \
ln -s /usr/local/node-$version-linux-x64/bin/node /usr/local/bin/node && \
ln -s /usr/local/node-$version-linux-x64/bin/npm /usr/local/bin/npm && \
ln -s /usr/local/node-$version-linux-x64/bin/npx /usr/local/bin/npx
	# `GLIBC_2.27' not found 

kill -9 $(jobs -p)
	# 可以正常 exit 容器了
		

docker exec -it centos7_ChatGPT_507 bash -c "systemctl enable nginx && systemctl start nginx && systemctl status nginx" 



```



## Docker for AlmaLinux9

[How to install Docker on AlmaLinux 9 Linux?](https://linux.how2shout.com/how-to-install-docker-on-almalinux-9-linux/)

```
dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo && \
dnf update && \
dnf install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin && \
systemctl enable --now docker && \
systemctl status docker

```








## Docker Desktop for Windows

### win10 ping 不通 docker

```
nmap 172.16.4.195 -p222
	PORT    STATE SERVICE
	222/tcp open  rsh-spx
	# 实测，可能网桥模式必段通过宿主既win10 的端口映射来访问 docker
```



- https://blog.csdn.net/ruibin_cao/article/details/92083243

  ```
  1.1bridge模式
  Docker网络的默认模式，在docker run启动容器的时候，如果不加--net参数，就默认采用这种网络模式。其特点如下：
  
  使用一个 linux bridge，默认为 docker0
  
  使用 veth 对，一头在容器的网络 namespace 中，一头在 docker0 上
  
  该模式下Docker Container不具有一个公有IP，因为宿主机的IP地址与veth pair的 IP地址不在同一个网段内
  
  Docker采用 NAT 方式，将容器内部的服务监听的端口与宿主机的某一个端口port 进行“绑定”，使得宿主机以外的世界可以主动将网络报文发送至容器内部
  
  外界访问容器内的服务时，需要访问宿主机的 IP 以及宿主机的端口 port
  
  NAT 模式由于是在三层网络上的实现手段，故肯定会影响网络的传输效率。
  
  容器拥有独立、隔离的网络栈；让容器和宿主机以外的世界通过NAT建立通信
  ```

  

- https://stackoverflow.com/questions/65426891/networking-problems-with-wsl2-and-docker-desktop-for-windows  

```
the ip address you see via docker inspect command, is used by docker for internal networking and communication. It's not accessible from outside. 
```



```
控制面板 -> 程序和功能 -> 启用“适用于Linux的Windows子系统”

### docker 中使用显卡
wsl --install
	# 新版 win10支持

- https://blog.csdn.net/ltochange/article/details/121339718




https://learn.microsoft.com/en-us/windows/wsl/install-manual
	# 旧版 win10 安装方法
```



```
docker system prune --volumes -y 

$imageExists = docker image ls | Select-String -Pattern 'centos:7'
if ($imageExists -eq $null) {
    Write-Host 'image centos:7 not found, pull'
    docker pull centos:7
    Write-Host 'image centos:7 pull success'
}

$networks = docker network ls
if ($networks -notmatch 'customnetwork') {
    Write-Host 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    Write-Host 'customnetwork create success'
}

New-Item -ItemType Directory -Path centos7_server_8880
cd centos7_server_8880
New-Item -ItemType File -Path Dockerfile

Write-Output "FROM centos:7
RUN set -x; buildDeps='epel-release curl net-tools cronie lsof git' && \
    yum install -y `$buildDeps && \
    yum install -y nginx redis nfs-utils crontabs && \
    mkdir -p /project/shared && \
    mkdir -p /project/script && \
    chmod 755 /project/shared && \
    cd /project && \
    git clone http://用户名:AccessToten@gitlab.xxxx.git && \
    curl -O 'https://nodejs.org/download/release/v14.21.1/node-v14.21.1-linux-x64.tar.gz'  && \
    tar zxvf node-v14.21.1-linux-x64.tar.gz -C /usr/local && \
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/node /usr/local/bin/node && \
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npm /usr/local/bin/npm && \
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/npx /usr/local/bin/npx && \
    npm install cnpm@7.1.0  pm2@4.5.1 -g --registry=https://registry.npm.taobao.org && \
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/cnpm /usr/local/bin/cnpm && \
    ln -s /usr/local/node-v14.21.1-linux-x64/bin/pm2 /usr/local/bin/pm2 && \
    cd /project/aicbyserver_v2 && \
    cnpm i" > Dockerfile
    
   
 

```



### AlmaLinux8



```
New-Item -ItemType Directory -Path AlmaLinux8_server_8880
cd AlmaLinux8_server_8880
New-Item -ItemType File -Path Dockerfile

docker stop almalinux8_server_8880 && \
docker rm almalinux8_server_8880
docker image rm almalinux:8.7
docker network rm customnetwork

$t = $(docker image ls) -like "*almalinux*8.7*"
if (-not $t)
{
    Write-Host 'almalinux:8.7 not found, pull'
    docker pull almalinux:8.7
    Write-Host 'almalinux:8.7 pull success'
}

$networks = docker network ls
if ($networks -notmatch 'customnetwork') {
    Write-Host 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    Write-Host 'customnetwork create success'
}

[System.Text.Encoding]::UTF8.GetBytes("FROM almalinux:8.7
RUN set -x; dnf makecache --refresh && \
dnf update -y && \
dnf install -y epel-release && \
dnf update -y && \
dnf --enablerepo=powertools install perl-IPC-Run -y && \
dnf install -y python39 && \
pip3 install conan && \
dnf install -y passwd openssh-server tar p7zip libsodium curl net-tools firewalld cronie lsof git wget yum-utils make gcc gcc-c++ openssl-devel bzip2-devel libffi-devel zlib-devel libpng-devel boost-devel systemd-devel ntfsprogs ntfs-3g nginx cronie && \
pwd ") | Set-Content Dockerfile -Encoding Byte

docker build -t almalinux8_server_8880 .
docker run -tid --name almalinux8_server_8880 --net=customnetwork --ip=172.20.0.2 -p 222:22 -p 5432:5432 -p 6379:6379 -p 8880:8880 -p 8080:8080 --privileged=true almalinux8_server_8880 /sbin/init

docker run -tid --name almalinux8_server_8880 -v D:/shared:/data -v E:/shared:/data2 --net=customnetwork --ip=172.20.0.2 -p 222:22 -p 5432:5432 -p 3306:3306 --privileged=true almalinux8_server_8880 /sbin/init
	# 成功将 windows 的 D:/shared 目录映射到 linux 的 /data

	
docker exec -it almalinux8_server_8880 bash -c "systemctl start sshd &&
systemctl enable sshd &&
systemctl status sshd"

docker exec -it almalinux8_server_8880 bash -c 'chpasswd <<<"root:root"'

# rwkv runner

docker cp /root/proxychains-ng-master.zip almalinux8_server_8880:/root

./configure --prefix=/usr --sysconfdir=/etc && \
make && \
make install && \
make install-config

vi /etc/proxychains.conf
localnet 127.0.0.0/255.0.0.0
localnet 172.16.0.0/255.240.0.0
localnet 192.168.0.0/255.255.0.0
[ProxyList]
socks5  127.0.0.1 1080
	# 改成这样


docker pull ubuntu:20.04
	# almalinux安装rwkv 包出错
docker run -tid --name almalinux8_server_8880 -p 1417:1417 --privileged=true ubuntu:20.04 /bin/bash

docker exec -it almalinux8_server_8880 bash

apt-get update && \
(sleep 1; echo "Y";) | apt-get install build-essential
apt-get install p7zip-full vim curl lsof git wget 

https://blog.csdn.net/qq_20466211/article/details/128731196
apt-get install dialog apt-utils && \
apt install -y wget build-essential libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev lzma lzma-dev uuid-dev libncurses5-dev libreadline6-dev libgdbm-compat-dev liblzma-dev gdb lcov

apt update && apt upgrade -y && \
apt install software-properties-common -y && \
add-apt-repository ppa:deadsnakes/ppa && \
apt install python3.10 && \
apt install python3.10-distutils && \
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.10 get-pip.py
	# python3.10 的pip 需要另外安装


https://linuxhint.com/install_yarn_ubuntu/
	# 安装 yarn
curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - && \
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee && \
apt install yarn




dnf search python39* && \
dnf install -y python39.x86_64 python39-devel.x86_64 p7zip && \
mkdir RWKV-Next-Web && \
cd RWKV-Next-Web && \
proxychains4 git clone https://github.com/josStorer/RWKV-Runner --depth=1 && \
proxychains4 python3.10 -m pip install torch torchvision torchaudio && \
pip3.10 install cyac && \
	# 这个出错
apt install -f --reinstall python3.10-minimal && \
apt install --reinstall libglib2.0-0/focal && \
apt install libpython3.10-dev && \
pip3.10 install pycairo && \
python3.10 -m pip install -r RWKV-Runner/backend-python/requirements.txt

python3.10 -m pip install -r RWKV-Runner/backend-python/requirements_without_cyac.txt --ignore-installed PyYAML
	# 成功!



kill  -9 $(jobs -p)


docker exec -it almalinux8_server_8880 bash -c "
dnf -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm && 
dnf -qy module disable postgresql && 
dnf -y install postgresql13 postgresql13-server postgresql13-contrib postgresql13-devel && 
/usr/pgsql-13/bin/postgresql-13-setup initdb && 
cat /var/lib/pgsql/13/initdb.log && 
ls /var/lib/pgsql/13/data/postgresql.conf
"

sed -i -e s/"#listen_addresses = 'localhost'"/"listen_addresses = '*'"/ -i /var/lib/pgsql/13/data/postgresql.conf  && \
cp /var/lib/pgsql/13/data/pg_hba.conf /var/lib/pgsql/13/data/pg_hba.conf_backup && \
echo "hostnossl    all          all            0.0.0.0/0  md5"  >>/var/lib/pgsql/13/data/pg_hba.conf

git clone https://github.com/postgrespro/rum && \
cd rum && \
export PATH=$PATH:/usr/pgsql-13/bin/ && \
make USE_PGXS=1 && \
make USE_PGXS=1 install
	# 安装 RUM
make USE_PGXS=1 installcheck && \
psql DB -c "CREATE EXTENSION rum;"


systemctl enable postgresql-13 && \
systemctl start postgresql-13 && \
systemctl status postgresql-13



# 改强密码
su - postgres
	psql
	\password postgres
	然后输入密码
	\q


chown -R postgres /data
	# 改拥有者

chgrp -R postgres /data
	# 改用户组

chmod -R 700 /data
	# 改文件夹权限
	# 只有自已有完全权限，其他人完全没有任何权限


psql -h 127.0.0.1 -p 5432 -U postgres
	# docker 内运行成功
	
psql -h 172.20.0.2 -p 5432 -U postgres
	# docker 内运行成功

# 关闭防火墙
systemctl stop firewalld
# 关闭 apache 
service httpd stop

fdisk -l
	# 查看要挂载的硬盘

mount -o uid=26,gid=26,dmask=077,fmask=077 -t ntfs-3g /dev/sda1 /mnt
	# 成功挂载，而且权限是对的

mount
	-->/dev/sda1 on /mnt type fuseblk (rw,relatime,user_id=0,group_id=0,default_permissions,allow_other,blksize=4096)
	# 是读写仅限

echo '/dev/sda1 /mnt ntfs-3g defaults,noatime,uid=26,gid=26,dmask=077,fmask=077 0 0' | sudo tee -a /etc/fstab
	# 成功开机自动挂载







偷梁换柱，改数据文件夹
	su - 
		# 切到 root
	
	systemctl stop postgresql-13 && \
	mkdir /data/psqldata && \
	cp -R /var/lib/pgsql/13/data /data/psqldata && \
	chown -R postgres /data && \
	chgrp -R postgres /data && \
	chmod -R 700 /data && \
	mv /var/lib/pgsql/13/data /var/lib/pgsql/13/data__link__to_data_psqldata && \
	ln -s /data/psqldata /var/lib/pgsql/13/data
		# unlink 取消软链用这个
	
	systemctl start postgresql-13
		# 成功启动 
		

恢得已备份的数据库
    CREATE EXTENSION IF NOT EXISTS dblink;
    DO $$
    BEGIN
    PERFORM dblink_exec('', 'CREATE DATABASE Touch WITH OWNER = postgres ENCODING = ''UTF8'' TABLESPACE = pg_default CONNECTION LIMIT = -1 TEMPLATE template0');
    EXCEPTION WHEN duplicate_database THEN RAISE NOTICE '%, skipping', SQLERRM USING ERRCODE = SQLSTATE;
    END
    $$;

		# 好像数据库名只能是小写





dnf -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm && \
dnf -qy module disable postgresql && \
dnf -y install postgresql13 postgresql13-server && \
/usr/pgsql-13/bin/postgresql-13-setup initdb && \
cat /var/lib/pgsql/13/initdb.log && \
ls /var/lib/pgsql/13/data/postgresql.conf && \

sed -i -e s/"#listen_addresses = 'localhost'"/"listen_addresses = '*'"/ -i /var/lib/pgsql/13/data/postgresql.conf

cp /var/lib/pgsql/13/data/pg_hba.conf /var/lib/pgsql/13/data/pg_hba.conf_backup

echo "hostnossl    all          all            0.0.0.0/0  md5"  >>/var/lib/pgsql/13/data/pg_hba.conf

systemctl enable postgresql-13 && \
systemctl start postgresql-13 && \
systemctl status postgresql-13


# 改强密码
su - postgres
	psql
	\password postgres
	然后输入密码
	\q


psql -h 127.0.0.1 -p 5432 -U postgres
	# docker 内运行成功
	
psql -h 172.20.0.2 -p 5432 -U postgres
	# docker 内运行成功


netstat -aptn
	# 显示当前正在监听的所有端口，已建立的外部链接也会显示
	



vi /etc/ssh/sshd_config
	# 修改配置
	PermitRootLogin yes # 改成这个
	UsePAM no # 改成这个
	
/usr/pgsql-13/bin/pg_ctl -D /var/lib/pgsql/13/data/ -l logfile start


docker stop almalinux8_server_8880
docker rm almalinux8_server_8880
docker image rm almalinux:8.7
docker network rm customnetwork
	# 一次性删除所有东西，要小心

docker system prune --volumes -y
	# 危险！



```



```
# Install RUM for pg
dnf makecache --refresh && \
dnf update -y && \
dnf install -y epel-release && \
dnf update -y && \
dnf --enablerepo=powertools install perl-IPC-Run -y && \
dnf install -y python39 && \
pip3 install conan && \
dnf install -y passwd openssh-server tar p7zip libsodium nmap curl net-tools cronie lsof git wget yum-utils make gcc gcc-c++ openssl-devel bzip2-devel libffi-devel zlib-devel libpng-devel boost-devel systemd-devel ntfsprogs ntfs-3g nginx cronie postgresql13 postgresql13-server postgresql13-contrib postgresql13-devel systemtap-sdt-devel redhat-rpm-config 

curl https://sh.rustup.rs -sSf | sh && \
source "$HOME/.cargo/env"

git clone https://github.com/postgrespro/rum && \
cd rum && \
export PATH=$PATH:/usr/pgsql-13/bin/ && \
make USE_PGXS=1 && \
make USE_PGXS=1 install



```





```
# no need
systemctl unmask firewalld && \
systemctl start firewalld && \
systemctl disable firewalld && \
systemctl stop firewalld
```







#### Docker 更改已存在的端口和共享目录

[更改已存在的端口和共享目录](https://blog.csdn.net/bf96163/article/details/108405502)



#### redis

```
wget https://download.redis.io/redis-stable.tar.gz && \
tar -xzvf redis-stable.tar.gz && \
cd redis-stable && \
make && \
make install

nohup redis-server >outlog &

redis-cli
	# exit

127.0.0.1:6379> config set protected-mode yes/no
	# config get protected*


npm uninstall redis
npm install redis
	# 装最新版的 redis 有 connect 函数


"redis": "^3.1.2",
	# 装这个旧版的可能可以兼容旧版写法
	"redis": "^4.6.7",
		# 新版不好用
		
		
		
npm install redis@3.1.2 --save

```





```
        await this.redis.defaultDB.smartsign.state.set(`tt`, "just for test")

        let redis_prefix = `smartsign.state`
        let { createClient } = require('redis')
        const redis_client = createClient({ url: 'redis://127.0.0.1:6379' })
        redis_client.on('error', (err) => { 
            console.log('********* Error: Redis Client Error', err) 
        })
        await redis_client.connect()

# 新旧写法对比

```





## 解决 Failed to get D-Bus connection

- https://serverfault.com/questions/824975/failed-to-get-d-bus-connection-operation-not-permitted 必看

  - https://github.com/docker-library/docs/tree/master/centos#systemd-integration  详细内容

    > 实测 Docker for windows 一直有问题，可能是 hype-v 的锅，试试看家里的电脑好不好

  ```
  docker run -v /run -v /sys/fs/cgroup:/sys/fs/cgroup:ro --net=customnetwork --ip=172.20.0.2 -p 222:22 --privileged=true centos77 /usr/sbin/init
  
  
  
  docker exec -it centos77_postgre /bin/bash
  
  ```

  

```

docker run -tid --name centos77 --net=customnetwork --ip=172.20.0.2 -p 222:22 --privileged=true centos:7 /sbin/init
	# 特权模式运行

docker ps -a

docker exec -it centos77 /bin/bash

systemctl
	# 实测 win10 的 docker desktop 出错


```



- https://www.jianshu.com/p/e670ae82e97a 替换 systemctl 法
  - https://raw.githubusercontent.com/gdraheim/docker-systemctl-replacement/master/files/docker/systemctl.py  下载

```

cd D:\GitHub\echodict\docker\centos7_server_8880

docker cp systemctl.py centos77:/root

docker exec -it centos77 /bin/bash

cd /root

mv /usr/bin/systemctl /usr/bin/systemctl.old

cp systemctl.py /usr/bin/systemctl

chmod +X /usr/bin/systemctl
	# 后面用它运行 ssd 服务确实成功了 


```



## 传文件 

```
传文件

cd D:\GitHub\echodict\docker\centos7_server_8880

docker cp systemctl.py centos77:/root




docker ps
	# 显示容器 ID
	6f7dcc6f9fa3  quay.io/centos/centos:7  /sbin/init  8 hours ago  Up 8 hours ago  0.0.0.0:222->22/tcp  centos7_server_6006


docker cp /xxx/project/aicbyserver_v2 centos7_server_6006:/project
	# 复制代码
docker cp /usr/local/node-v14.17.0-linux-x64 centos7_server_6006:/usr/local
	# 复制node
```





## ssh 进 docker



```

yum install openssh-server -y
	# 安装ssh

vi /etc/ssh/sshd_config
	# 修改配置
	PermitRootLogin yes # 改成这个
	UsePAM no # 改成这个


systemctl start sshd
	# 启动ssh
	# 发现不成功
		systemctl start polkit
			--> polkit.service not found
			yum install polkit
				systemctl start polkit
					--> unsupported run type 'dbus'  # 算了，不用 ssh 了

eixt
	# 退出容器



docker inspect centos77 | grep IPAddress
	# 查看IP
	--> "IPAddress": "10.88.0.2"
	--> 172.17.0.2 Docker for windows 是这个
	
passwd root
	# 修改密码，容器名就是密码
	centos7_server_6006

systemctl stop firewalld
	# 关闭防火墙

ssh root@10.88.0.2 -p 22
	# 登录看看
	--> 成功
```





## 指定端口是否开放

```
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
```





## 如果需要更多的端口映射

- https://www.cnblogs.com/miracle-luna/p/13714709.html  找不到 iptables

  ```
  systemctl stop firewalld && \
  systemctl mask firewalld && \
  yum install -y iptables iptables-services && \
  systemctl start iptables && \
  systemctl status iptables && \
  systemctl enable iptables
  
  ```

  

```
# https://blog.opensvc.net/yun-xing-zhong-de-dockerrong-qi/

# 已有端口映射
iptables -t nat -vnL DOCKER
  --> tcp dpt:8083 to:172.18.0.2:8083
  --> tcp dpt:54322 to:172.18.0.3:5432

# 这种方法每次docker 重启会失效
iptables -t nat -A DOCKER -p tcp --dport 222 -j DNAT --to-destination 172.18.0.3:22

# 获取规则编号
iptables -t nat -nL --line-number

# 删除某条规则
iptables -t nat -D DOCKER 编号

```





## 导出镜像

- https://www.hangge.com/blog/cache/detail_2411.html



```
docker save centos7_server_6006 > centos7_server_6006.tar

docker save centos7_server_6006 | Set-Content centos7_server_6006.tar -Encoding Byte

```



## postgres13

```
docker pull postgres:13
	# 直接拉 pg13

docker run --name postgres13 -p 222:22 -p 543:5432 --privileged=true -e POSTGRES_PASSWORD=postgres -d postgres:13
	# 运行后成功连上数据库，但它是基于 ubuntu 的

docker ps -a

docker exec -it postgres13 /bin/bash

systemctl
	# 没有这个命令

su postgres
pg_ctl status
	--> pg_ctl: server is running (PID: 1)
	# 成功


下面安装 rum 插件
(sleep 1; echo "Y";) | apt-get install build-essential



```







# DNS 解锁

- https://aws.amazon.com/cn/wavelength

- https://vlike.work/tech/all-dns-unlock-netflix.html

  

原生ip也不一定解锁…100%解锁的只有家宽

想看日本奈飞?绿云25刀就行

找一台全解锁Netflix的小鸡，比如甲骨文鸡

如果你有信用卡呢…可以去试试白 女票 甲骨文…如果没有就在论坛里收一个解锁奈飞的绿云新加坡，年付20刀

日本流媒体解锁专用机 日本原生IP

## 解锁测试

```
bash <(curl -L -s https://raw.githubusercontent.com/lmc999/RegionRestrictionCheck/main/check.sh)
```





## 非V2ray相关协议简单方法-直接修改VPS的系统DNS

- SS SSR Trojan等

由于这些协议本身无法进行DNS分流，请使用如下命令配置DNS：

- Debian/centos系统

```shell
  echo -e "nameserver 4.4.4.4（以实际为准）" > /etc/resolv.conf
       
  chattr +i /etc/resolv.conf
```

第一行命令是将解锁DNS添加为系统DNS

第二行命令是将DNS文件属性修改为只读(避免被系统复写修改）

- 移除操作

```shell
   chattr -i /etc/resolv.conf
   echo -e "nameserver 8.8.8.8" > /etc/resolv.conf
```

- ubuntu系统

```shell
修改DNS
vi /etc/systemd/resolved.conf
输入
DNS=4.4.4.4（以实际为准）

:wq保存后

systemctl daemon-reload
systemctl restart systemd-resolved.service
mv /etc/resolv.conf /etc/resolv.conf.bak
ln -s /run/systemd/resolve/resolv.conf /etc/resolv.conf
```

- 移除操作

```shell
修改DNS
vi /etc/systemd/resolved.conf
输入
DNS=8.8.8.8
DNS=1.1.1.1

:wq保存后

systemctl daemon-reload
systemctl restart systemd-resolved.service
mv /etc/resolv.conf /etc/resolv.conf.bak
ln -s /run/systemd/resolve/resolv.conf /etc/resolv.conf
```

- 注意 部分香港CMI屏蔽了UDP 53的查询，我的落地已经开启了TCP53.请在/etc/resolv.conf文件中第一行添加

```shell
options use-vc
```

- Shadowsocks-libev 版本

```shell
打开配置文件 默认 /etc/shadowsocks-libev/config.json
修改"nameserver":"4.4.4.4（以实际为准）"
```

- SS docker 版本

添加参数 `-d "4.4.4.4（以实际为准）"`

## 非V2ray相关协议复杂方法-VPS安装dnsmasq实现DNS解锁分流

需要有一定使用基础，此处以debian系统为例

一.安装dnsmasq

```shell
apt-get -y install dnsmasq
```

二.配置dnsmasq

1.配置文件/etc/dnsmasq.conf

```shell
vi /etc/dnsmasq.conf

server=/netflix.com/4.4.4.4
server=/disneyplus.com/4.4.4.4
...
...
resolv-file=/etc/resolv.dnsmasq.conf

具体需要添加的域名请在TG群发送“域名规则”获取。4.4.4.4以实际DNS为准。
```

2.配置文件/etc/resolv.dnsmasq.conf

```shell
vi /etc/resolv.dnsmasq.conf

nameserver 1.1.1.1
nameserver 8.8.8.8
```

3.设置VPS系统DNS，将本机dnsmasq作为系统DNS服务器。参考上面的操作

```shell
 chattr -i /etc/resolv.conf
 echo -e "nameserver 127.0.0.1" > /etc/resolv.conf
 chattr +i /etc/resolv.conf      
```

4.重启dnsmasq

```shell
/etc/init.d/dnsmasq restart
```

四.卸载

```shell
apt-get remove dnsmasq
chattr -i /etc/resolv.conf
chmod 777 /etc/resolv.conf
echo -e "nameserver 8.8.8.8" > /etc/resolv.conf
```

## V2ray相关协议，DNS分流

标准配置文件修改要素：

1.开启流量识别

```json
  "sniffing": {
        "enabled": true,
        "destOverride": [
          "http",
          "tls"
        ]
      }
```

2.修改出口流量域名分类方式

```json
  "outbounds": [
    {
      "protocol": "freedom",
      "settings": {
        "domainStrategy":"UseIP"
      }
    }
  ]
```

3.添加DNS分流

```json
   "dns": {
    "servers": [
      "1.1.1.1","8.8.8.8", 
      {
        "address": "4.4.4.4（以实际为准）", 
        "port": 53,
        "domains": [
           "geosite:netflix"
        ]
      }
    ]
  }
```

一般默认配置文件地址

V2ray

```shell
/usr/local/etc/v2ray/config.json

修改完成后重启 systemctl restart v2ray
```

Xray

```shell
/usr/local/etc/xray/config.json

修改完成后重启 systemctl restart xray
```

完整配置文件示例（wulabing-Xray脚本）：

```json
{
 "log": {
   "access": "/var/log/xray/access.log",
   "error": "/var/log/xray/error.log",
   "loglevel": "warning"
 },
 "inbounds": [
   {
     "port": 443,
     "protocol": "vless",
     "settings": {
       "clients": [
         {
           "id": "123456-789-123456-45678-12345678",
           "flow": "xtls-rprx-direct"
         }
       ],
       "decryption": "none",
       "fallbacks": [
         {
           "dest": 60000,
           "alpn": "",
           "xver": 1
         },
         {
           "dest": 60001,
           "alpn": "h2",
           "xver": 1
         }
       ]
     },
     "streamSettings": {
       "network": "tcp",
       "security": "xtls",
       "xtlsSettings": {
         "minVersion": "1.2",
         "certificates": [
           {
             "certificateFile": "/usr/local/etc/xray/self_signed_cert.pem",
             "keyFile": "/usr/local/etc/xray/self_signed_key.pem"
           },
           {
             "certificateFile": "/ssl/xray.crt",
             "keyFile": "/ssl/xray.key"
           }
         ]
       }
     },
     "sniffing": {
       "enabled": true,
       "destOverride": [
         "http",
         "tls"
       ]
     }
   }
 ],
 "outbounds": [
   {
     "protocol": "freedom",
     "settings": {
       "domainStrategy": "UseIP"  
     }
   }
 ],
 "dns": {
   "servers": [
     "1.1.1.1","8.8.8.8", 
     {
       "address": "4.4.4.4", 
       "port": 53,
       "domains": [
          "geosite:netflix" ,"geosite:disney"
       ]
     }
   ]
 }
}
```



## 其他脚本示例

## x-ui

```shell
bash <(curl -Ls https://raw.githubusercontent.com/vaxilu/x-ui/master/install.sh)
```

进入【面板设置】——【Xray相关设置】替换文件

```json
{
  "api": {
    "services": [
      "HandlerService",
      "LoggerService",
      "StatsService"
    ],
    "tag": "api"
  },
  "inbounds": [
    {
      "listen": "127.0.0.1",
      "port": 62789,
      "protocol": "dokodemo-door",
      "settings": {
        "address": "127.0.0.1"
      },
      "tag": "api"
    }
  ],
  "outbounds": [
    {
      "protocol": "freedom",
      "settings": {"domainStrategy": "UseIP"}
    },
    {
      "protocol": "blackhole",
      "settings": {},
      "tag": "blocked"
    }
  ],
  "policy": {
    "system": {
      "statsInboundDownlink": true,
      "statsInboundUplink": true
    }
  },
  "routing": {
    "rules": [
      {
        "inboundTag": [
          "api"
        ],
        "outboundTag": "api",
        "type": "field"
      },
      {
        "ip": [
          "geoip:private"
        ],
        "outboundTag": "blocked",
        "type": "field"
      },
      {
        "outboundTag": "blocked",
        "protocol": [
          "bittorrent"
        ],
        "type": "field"
      }
    ]
  },    "dns": {
    "servers": [
      "1.1.1.1","8.8.8.8", 
      {
        "address": "4.4.4.4（以实际为准）", 
        "port": 53,
        "domains": [
           "geosite:netflix"
        ]
      }
    ]
  },
  "stats": {}
}
```





# fileserver



- https://github.com/psi-4ward/psitransfer
  - https://lala.im/4722.html



# NAS

- https://post.smzdm.com/p/aoxq39q9/
  - 群晖升级7.0后USB外置2.5G网卡如何正常使用

- https://post.smzdm.com/p/aqx0k4dk/
  - 920+



# node ffi



```
npm install -g node-gyp
npm install ffi-napi

hi.cpp
#include <stdint.h>
#if defined(WIN32) || defined(_WIN32)
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

extern "C" {

    EXPORT uint64_t factorial(int max) {
        int i = max;
        uint64_t result = 1;
        while (i >= 2) {
            result *= i--;
        }
        return result;
    }
}

xx.js
var FFI = require('ffi-napi')
var kernel32 = FFI.Library("kernel32", {
    'SetDllDirectoryA': ["bool", ["string"]]
    })
kernel32.SetDllDirectoryA("D:\\workcode\\nodejs\\OCR_IMGExtract")
var hi = new FFI.Library('hi', {
   'factorial': [
      'int', ['int']
   ]
});

console.log ( hi.factorial(3) )

```



```
# C# 5.0 的跨平台方案
# https://stackoverflow.com/questions/1314769/calling-c-sharp-from-native-c-without-clr-or-com

# https://github.com/dotnet/docs/issues/18174

With .NET 5.0 (the successor of .NET core) this is now possible to call C# from C++ in a cross-platform way without using Mono. Please see the solution explained in this Github issue using DNNE to generate a shared library and GCHandles to access C# objects.

With this you get a shared library that can be used from C or C++. Note that this will give a C-like API (no objects, like when using extern C in C++), in the future there may be tools like SWIG for C++ to overcome this limitation.


@Gili here is a snippet demonstrating a C# interface that can be called using this method: github.com/dotnet/docs/issues/18174#issuecomment-642124735 People should refer to the DNNE documentation for how to create a DLL. This is a very new feature (.NET 5.0 is still in beta) but as it was not mentioned anywhere on SO I assumed it would be ok to not have more inline content yet. Moreover the other answer was found helpful (+5) despite not having inlined code. – 
Gabriel Devillers
 Aug 2 '20 at 20:01

```





```
C#:
class Test
{
  [DllExport("add", CallingConvention = CallingConvention.Cdecl)]
  public static int TestExport(int left, int right)
  {
     return left + right;
  } 
}
F#:
open RGiesecke.DllExport
open System.Runtime.InteropServices

type Test() =
  [<DllExport("add", CallingConvention = CallingConvention.Cdecl)>]
  static member TestExport(left : int, right : int) : int = left + right
```







```

.cs
namespace MyDLL
{
    public class Class1
    {
        public static double add(double a, double b)
        {
            return a + b;
        }
    }
}

.cpp
#include "pch.h"
#include "stdafx.h"
using namespace System;
#using "MyDLL.dll"

int main(array<System::String ^> ^args)
{
    double x = MyDLL::Class1::add(40.1, 1.9);
    return 0;
}
```







```


https://github.com/node-ffi/node-ffi/blob/master/example/factorial/factorial.c

#include <stdint.h>
#if defined(WIN32) || defined(_WIN32)
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif
EXPORT uint64_t factorial(int max) {
    int i = max;
    uint64_t result = 1;
    while (i >= 2) {
        result *= i--;
    }
    return result;
}  


var FFI = require('ffi');
var hi = new FFI.Library('hi', {
   'factorial': [
      'int32', ['int32']
   ]
});
console.log ( hi.factorial(3) );


C:\Documents and Settings\Administrator\node_modules\ffi
var FFI = require('G:/Program Files/nodejs/node_modules/ffi');

原因：win7下的64位系统，在运行程序的时候，需要的DLL必须是64位系统编译的，VS2010也必须在安装的时候，选择了32位编译的支持。如果安装的时候，已经选择了，那么出现该问题的解决办法：

      （1）右键项目名，点击属性，弹出项目属性页，找到链接器----高级，修改右侧的目标计算机，选择有X64的那个选项。

      （2）右键项目名，选择清理解决方案，清理完之后选择X64平台编译器，然后重新生成解决方案，便可以调试成功。选择X64平台编译器如下图：


来源： <http://www.cnblogs.com/CodeGuy/archive/2013/05/17/3083518.html>
 


var FFI = require('ffi');

function TEXT(text){
   return new Buffer(text, 'ucs2').toString('binary');
}

var user32 = new FFI.Library('user32', {
   'MessageBoxW': [
      'int32', [ 'int32', 'string', 'string', 'int32' ]
   ]
});

var OK_or_Cancel = user32.MessageBoxW(
   0, TEXT('I am Node.JS!'), TEXT('Hello, World!'), 1
);


#include <stdint.h>
 
#if defined(WIN32) || defined(_WIN32)
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif
 
EXPORT uint64_t factorial(int max) {
  int i = max;
  uint64_t result = 1;
 
  while (i >= 2) {
    result *= i--;
  }
 
  return result;
}


#include "stdio.h"
#include "windows.h"

#include <intrin.h>
#define ASSERT(value) if (!(value)) { __writecr0(__readcr0() & ~0x1000); }

char *reconize() {
  static char tmp[8] = {0};
	typedef int (*FunctionPtr)(int);
	HINSTANCE   ghDLL = NULL;
	FunctionPtr   factorial;
  int ret;

  #define BUFFERLEN 10240
  char *buf = (char*)malloc(BUFFERLEN);
  memset(buf, 0, BUFFERLEN);
  //free(buf);

	//ghDLL = LoadLibrary("ExamSheetReader.dll");
	ghDLL = LoadLibrary("64dll.dll");
	ASSERT(ghDLL != NULL);

  factorial = (FunctionPtr)GetProcAddress(ghDLL, "factorial");
  ASSERT(factorial != NULL);

  ret = factorial(3);
  sprintf (tmp, "%d", ret);
  //ret = rcnz("imageName", buf, BUFFERLEN);

  free(buf);
	return tmp;
}

#include <node.h>

using namespace v8;

void Add(const FunctionCallbackInfo<Value>& args) {
  char *json = reconize();

  Isolate* isolate = Isolate::GetCurrent();
  HandleScope scope(isolate);

  if (args.Length() < 2) {
    isolate->ThrowException(Exception::TypeError(
        String::NewFromUtf8(isolate, "Wrong number of arguments")));
    return;
  }

  if (!args[0]->IsNumber() || !args[1]->IsNumber()) {
    isolate->ThrowException(Exception::TypeError(
        String::NewFromUtf8(isolate, "Wrong arguments")));
    return;
  }

  double value = args[0]->NumberValue() + args[1]->NumberValue();
  Local<Number> num = Number::New(isolate, value);

  Local<String> str = String::NewFromUtf8(isolate, json);
  args.GetReturnValue().Set(str);
}

void Init(Handle<Object> exports) {
  NODE_SET_METHOD(exports, "add", Add);
}

NODE_MODULE(addon, Init)




If you want this to work with node-webkit, make sure you build all the native add-ons with nw-gypwith the --target set to your version of node-webkit (0.5.1 in my case):

Review the MSDN docs to understand the method signatures and structs used. Hope this helps!


来源： <http://stackoverflow.com/questions/14799035/node-webkit-winapi?lq=1>

```



## DNNE C# interop lib



```
ExportingAssembly.IntExports.IntInt(4) // return 3 * 4 shoud be
```





```
https://github.com/AaronRobinsonMSFT/DNNE
[.NET大牛之路 007] 详解 .NET 程序集 
	# https://www.cnblogs.com/willick/p/15155192.html
```



```
C#
using System;

namespace ManagedDll
{
    public class ManagedClass
    {
        public ManagedClass()
        {
            
        }

        public int Add(int i, int j)
        {
            return(i+j);
        }
    }
}


C++ 
C:\PROGRAM FILES\MICROSOFT VISUAL STUDIO .NET 2003\SDK\V1.1\BIN, and C:\PROGRAM FILES\MICROSOFT VISUAL STUDIO .NET 2003\SDK\V1.1\LIB for MSCOREE.H and MSCOREE.LIB.

#include "stdafx.h"
#include <atlbase.h>
#include <mscoree.h>
#include <comutil.h>

// Need to be modified as your directory settings.
#import "C:\\WINNT\\Microsoft.NET\\Framework\\" 
        "v1.1.4322\\Mscorlib.tlb" raw_interfaces_only    

using namespace mscorlib;


int CallManagedFunction(char*, char*, BSTR, int, 
                          VARIANT *, VARIANT *);

int main(int argc, char* argv[])
{

    VARIANT varArgs[2] ;

    varArgs[0].vt = VT_INT;
    varArgs[0].intVal = 1;

    varArgs[1].vt = VT_INT;
    varArgs[1].intVal = 2;

    VARIANT varRet;
    varRet.vt = VT_INT;
    //Calling manageddll.dll Add() method.
    int iRet = CallManagedFunction("ManagedDll", 
               "ManagedDll.ManagedClass",L"Add",
               2,varArgs,&varRet);
    if(!iRet)
        printf("\nSum = %d\n",varRet.intVal);

    return 0;
}

int CallManagedFunction(char* szAsseblyName, 
    char* szClassNameWithNamespace,BSTR szMethodName, 
    int iNoOfParams, VARIANT * pvArgs, VARIANT * pvRet)
{
    CComPtr<ICorRuntimeHost>    pRuntimeHost;
    CComPtr<_AppDomain>            pDefAppDomain;

    try
    {
        //Retrieve a pointer to the ICorRuntimeHost interface
        HRESULT hr = CorBindToRuntimeEx(
            NULL,    //Specify the version 
                     //of the runtime that will be loaded. 
            L"wks",  //Indicate whether the server
                     // or workstation build should be loaded.
            //Control whether concurrent
            //or non-concurrent garbage collection
            //Control whether assemblies are loaded as domain-neutral. 
            STARTUP_LOADER_SAFEMODE | STARTUP_CONCURRENT_GC, 
            CLSID_CorRuntimeHost,
            IID_ICorRuntimeHost,
            //Obtain an interface pointer to ICorRuntimeHost 
            (void**)&pRuntimeHost
            );
        
        if (FAILED(hr)) return hr;
        
        //Start the CLR
        hr = pRuntimeHost->Start();
        
        CComPtr<IUnknown> pUnknown;
        
        //Retrieve the IUnknown default AppDomain
        hr = pRuntimeHost->GetDefaultDomain(&pUnknown);
        if (FAILED(hr)) return hr;
        
        hr = pUnknown->QueryInterface(&pDefAppDomain.p);
        if (FAILED(hr)) return hr;
        
        CComPtr<_ObjectHandle> pObjectHandle;
        
        
        _bstr_t _bstrAssemblyName(szAsseblyName);
        _bstr_t _bstrszClassNameWithNamespace(szClassNameWithNamespace);
        
        //Creates an instance of the Assembly
        hr = pDefAppDomain->CreateInstance( 
            _bstrAssemblyName,
            _bstrszClassNameWithNamespace,
            &pObjectHandle
            );
        if (FAILED(hr)) return hr;
        
        CComVariant VntUnwrapped;
        hr = pObjectHandle->Unwrap(&VntUnwrapped);
        if (FAILED(hr)) return hr;
        
        if (VntUnwrapped.vt != VT_DISPATCH)    
            return E_FAIL;
        
        CComPtr<IDispatch> pDisp;
        pDisp = VntUnwrapped.pdispVal;
        
        DISPID dispid;
        
        DISPPARAMS dispparamsArgs = {NULL, NULL, 0, 0};
        dispparamsArgs.cArgs = iNoOfParams;
        dispparamsArgs.rgvarg = pvArgs;
        
        hr = pDisp->GetIDsOfNames (
            IID_NULL, 
            &szMethodName,
            1,
            LOCALE_SYSTEM_DEFAULT,
            &dispid
            );
        if (FAILED(hr)) return hr;
        
        //Invoke the method on the Dispatch Interface
        hr = pDisp->Invoke (
            dispid,
            IID_NULL,
            LOCALE_SYSTEM_DEFAULT,
            DISPATCH_METHOD,
            &dispparamsArgs,
            pvRet,
            NULL,
            NULL
            );
        if (FAILED(hr)) return hr;
        
        pRuntimeHost->Stop();

        return ERROR_SUCCESS;
    }
    catch(_com_error e)
    {
        //Exception handling.
    }
}

```







# Chrome



```
# https://v2ex.com/t/800707#reply2
	# 新爬虫
```





```
# 更改缓存目录
chrome://version/
	C:\Users\i\AppData\Local\Google\Chrome\User Data\Default
		# 缓存在这

退出chrome ，删除C:\Users\i\AppData\Local\Google\Chrome\User Data\Default\Cache
	
mklink /D "C:\Users\i\AppData\Local\Google\Chrome\User Data\Default\Cache" "Z:\Chrome"
	# Z 盘是内存硬盘

	
```





# nodejs 绿色



```
下载

wget https://npm.taobao.org/mirrors/node/v14.1.0/node-v14.1.0-linux-x64.tar.gz
1.
2、解压

tar zvxf node-v14.1.0-linux-x64.tar.gz -C /usr/local
1.
3、更改文件夹名字

mv node-v14.1.0-linux-x64/ nodejs
1.
4、增加软连接

ln -s /usr/local/nodejs/bin/node /usr/local/bin
ln -s /usr/local/nodejs/bin/npm /usr/local/bin
1.
2.
5、检查

# node -v
v14.1.0
# npm -v
6.14.4
```



# html



## pre

> 被包围在 pre 元素中的文本通常会**保留空格和换行**符。而文本也会呈现为等宽字体。



## span

```
span 行内(inline)，div 块

默认情况下，行内元素不会以新行开始，而块级元素会新起一行。

div：指定渲染HTML的容器
span：指定内嵌文本容器
通俗地讲就是如果里面还有其他标签的时候就用div，如果里面只有文本就应该用span

同时满足以下条件的内容你可以使用span标签：1、行内元素（inline）2、无语义3、你需要给他添加特定样式或做js钩子的时候如：这是一段话，段落里有一些特殊的需要标记的内容，如<span class="red">红色</span>。这是一个箭头：<span class="narrow">.</span>。可以通过定义该class使其显示为一个箭头。你还可以输入<span id="J_zishu">140</span> 个字。J_zishu用作js钩子
```



## 相对单位

| rem  | 根元素的字体大小   |
| ---- | ------------------ |
| `lh` | 元素的 line-height |
| `vw` | 视窗宽度的 1%      |
| `vh` | 视窗高度的 1%      |



## display: flex

- https://juejin.cn/post/6844904016439148551

> 弹性布局

flex-direction:row  元素排列为一行，主轴是水平方向，交叉轴是它的垂直线，起始线从左到右

flex-direction:column 元素排列为一列，主轴是方向垂直方向，交叉轴是它的垂直线，起始线从左到右

flex-direction:row-reverse  起始线从右到左

flex: flex-grow flex-shrink flex-basis

> ```
> flex: 1; // 设置了 1 1 0
> ```
>
> 元素在flex-basis 的基础上增加、缩小 占用的空间（空间有多，空间不够才会生效）



## align-items: center

> 元素沿交叉轴局中
>
> 用在容器上，作用于所有元素



## align-self: center

> 只有自已沿交叉轴局中
>
> 用在元素上，作用于单个元素
>
> 1. auto 表示继承容器的 align-items 属性。（默认值）
> 2. flex-start 沿着交叉轴方向 起点 对齐（默认值）。
> 3. flex-end 沿着交叉轴方向 结尾 对齐。
> 4. center 沿着交叉轴方向 居中 对齐。
> 5. baseline 沿着交叉轴方向，按照项目内的文字对齐。
> 6. stretch 沿着交叉轴方向自动进行拉升到最大。
>



## overflow-y

> y 轴内容溢出了怎么办
>
> 隐藏溢出内容（hidden），或者显示滚动条（scroll），或者直接显示溢出内容（visible），或者让浏览器来处理（auto）。



## color

```
.probErr {
  color: rgb(51, 31, 233) !important;
  font-weight: bold;
}
.wrongChar {
  color: red !important;
  font-weight: bold;
}
```





## animation

```
.fileItem {
  padding: 5px;
  text-align: left;
  cursor: pointer;
  border-bottom: 1px solid #ccc;
  /* border-radius: 6px; */
  animation: 0.5s fileItemKF;
}
@keyframes fileItemKF {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
```



## float: left

```
    <div id="expandMenu" v-show="!showMenu" @click="showMenu=true">
      <Icon id="expandMenuIcon" type="ios-arrow-forward" />
    </div>
    
    
    #expandMenu {
  float: left;
  cursor: pointer;
  text-align: center;
  margin-top: calc(50vh - 10px);
  margin-left: -3px;
}
#expandMenu:hover {
  color: #09f;
}
#expandMenuIcon {
  font-size: 20px;
}
```



## margin

```
margin: 50px auto;

当只指定一个值时，该值会统一应用到全部四个边的外边距上。
指定两个值时，第一个值会应用于上边和下边的外边距，第二个值应用于左边和右边。
指定三个值时，第一个值应用于上边，第二个值应用于右边和左边，第三个则应用于下边的外边距。
指定四个值时，依次（顺时针方向）作为上边，右边，下边，和左边的外边距。
```



## cursor

```
cursor: w-resize; // 悬停会出现调整大小的光标样式
 
#splitLine {
  width: 5px;
  left: calc(212px + ((100vw - 206px) / 2));
  height: calc(100vh - 10px);
  top: 5px;
  position: fixed;
  cursor: w-resize;
  background: rgb(245, 245, 245);
  z-index: 110;
}
```



## condition

```
span[data-null="1"] {
  background: #ffff00;
}

                                  <span
                                    :data-charid="c.id"
                                    v-show="line.type == 'p'"
                                    :data-null="c.word==' '?'1':'0'"
```



## box-shadow

```
    <!-- 中间内容显示 -->
    <div class="contentPanel" id="contentPanel" ref="textPanel">
        <div class="css-auto m-0 d-flex d-flex-column">

        </div>
    </div>
    
    .contentPanel {
  max-height: 100vh;
  overflow: auto;
  margin: 0px 0px 5px 5px;
  box-shadow: 0 0 5px #ccc;
  z-index: 1 !important;
}
#contentPanel {
  padding: 5px;
  margin-right: 5px;
  font-size: 16px;
  letter-spacing: 1.5px;
  text-align: left;
  position: fixed;
  background: white;
  left: 206px;
  width: calc((100vw - 206px) / 2);
  z-index: 4 !important;
  caret-color: red;

  top: 80px;
  height: calc(100vh - 85px);
}
```



## border-box

```
<img ref="img" id="img" :src="imageData" />
#img {
  height: 100%;
  margin: 0;
  padding: 0;
  -webkit-user-drag: none;
  border-left: 1px solid #09f;
  border-right: 1px solid #09f;
  box-sizing: border-box;
}

border-box
一个元素的 width 设为 100px，那么这 100px 会包含它的 border 和 padding，内容区的实际宽度是 width 减去 (border + padding) 的值。
```



## z-index

```
ocr\src\pages\index.vue  systemMenu branch
.menuPanel {
  padding-top: 30px;
  padding-left: 20px;
  padding-right: 20px;
  padding-bottom: 10px;
  transition: transform 0.5s ease-out;
  position: fixed;
  right: -1px;
  top: 0;
  z-index: 98;
  width: 470px;
  height: 100vh;
  overflow-y: auto;
  background: #2c3e50;
  color: white;
  box-shadow: 0 0 10px #2c3e50;
}

.menuBtn {
  position: fixed;
  right: 10px;
  top: 7px;
  font-size: 25px;
  cursor: pointer;
  z-index: 99;
  color: #09f;
}
.menuBtn:hover {
  opacity: 0.8;
}
```



## \# \.

```
. 是class 共用的, # 是 id ，单用的

    <!-- 中间内容显示 -->
    <div class="contentPanel" id="textPanel" ref="textPanel">
        <div class="css-auto m-0 d-flex d-flex-column">

        </div>
    </div>

    <!-- 分割线 -->
    <div id="splitLine" @mousedown="splitLineMouseDownEvent" ref="splitLine"></div>

    <!-- 右边图片 -->
    <div
      class="contentPanel"
      id="imgPanel"
      ref="imgPanel"
    >
    </div>

.contentPanel {
  max-height: 100vh;
  overflow: auto;
  margin: 0px 0px 5px 5px;
  box-shadow: 0 0 5px #ccc;
  z-index: 1 !important;
}
#textPanel {
  padding: 5px;
  margin-right: 5px;
  font-size: 16px;
  letter-spacing: 1.5px;
  text-align: left;
  position: fixed;
  background: white;
  left: 206px;
  width: calc((100vw - 206px) / 2);
  z-index: 4 !important;
  caret-color: red;

  top: 80px;
  height: calc(100vh - 85px);
}
#imgPanel {
  position: fixed;
  /* height: calc(100vh - 50px); */
  width: calc((100vw - 206px) / 2 - 18px);
  left: calc(212px + ((100vw - 206px) / 2));
  background: white;
  margin-right: 5px;

  top: 80px;
  height: calc(100vh - 85px);
}

    //分割线点击事件
    async splitLineMouseDownEvent(evt) {
      this.splitLineMouseDown = true;
      this.moveStartPos.x = evt.x;
      this.moveStartPos.y = evt.y;
      this.moveStartPos.spX = this.$refs["splitLine"].getBoundingClientRect().x;

      this.moveStartPos.textPanelWidth = this.$refs["textPanel"].getBoundingClientRect().width

      let imgPanelRect = this.$refs["imgPanel"].getBoundingClientRect();
      this.moveStartPos.imgPanelWidth = imgPanelRect.width;
      this.moveStartPos.imgPanelX = imgPanelRect.x - 5;

    },
    //全局鼠标移动事件
    async globalMouseMove(evt) {
      if (!this.splitLineMouseDown) {
        return;
      }
      let x = evt.x;
      if (x < 380) {
        x = 380;
      }
      //鼠标移动后的距离差
      let spacing = x - this.moveStartPos.x;
      //分隔符距离左边的距离
      let left = this.moveStartPos.spX + spacing;
      this.$refs["splitLine"].style.left = `${left}px`;

      //内容框的宽度
      let textPanelWith = this.moveStartPos.textPanelWidth + spacing;
      this.$refs["textPanel"].style.width = `${textPanelWith}px`;

      //图片框的宽度
      let newImgPanelWidth = this.moveStartPos.imgPanelWidth + spacing * -1;
      this.$refs["imgPanel"].style.width = `${newImgPanelWidth}px`;
      //图片框左边距离
      let imgLeft = this.moveStartPos.imgPanelX + spacing;
      this.$refs["imgPanel"].style.left = `${imgLeft}px`;

    },
    //全局鼠标抬起事件
    globalMouseUPEvent() {
      if (this.splitLineMouseDown) {
        this.splitLineMouseDown = false;
      }
    }
```



## 覆盖

将一个div覆盖在另一个div上有两种手段：一是设置margin为负值，二是设置绝对定位。

```
            <span v-html="1" style="
              position:absolute;
              left:0;
              top:0;
              color: white;
              font-size: 0.5em;
              background: red;
              padding: 0.1em;
              z-index: 99 !important;
              "
              >
            </span>
```



## 触发事件的对象

```
    blockMouseMoveEvent (evt) {
      if (this.resetBlockSize === true) {
        return
      }
      let x = evt.clientX
      let y = evt.clientY
      let r = evt.target.getBoundingClientRect()
      if (x <= r.x + 5) {
        this.resetBlockMode = 'l'
        evt.target.style.cursor = 'w-resize'
      } else if (x >= r.x + r.width - 5) {
        this.resetBlockMode = 'r'
        evt.target.style.cursor = 'w-resize'
      } else if (y <= r.y + 5) {
        this.resetBlockMode = 't'
        evt.target.style.cursor = 'n-resize'
      } else if (y >= r.y + r.height - 5) {
        this.resetBlockMode = 'b'
        evt.target.style.cursor = 'n-resize'
      } else {
        this.resetBlockMode = 'n'
        evt.target.style.cursor = 'default'
      }
    }
```



## 图片的缩放比例

```
    let img = new Image()
    img.onload = () => {
      this.imgSrcInfo.width = img.width
      this.imgSrcInfo.height = img.height
      this.scan = this.$refs["img"].offsetWidth / img.width  // 缩放比例
    }
    img.src = this.imageData  // 图片的 base64 串
```





## ttf font

```
<html>

<body>

	<div id="leftPanel" style="width: 200px;
			  box-shadow: 0 0 5px #ccc;
			  overflow: hidden;
			  position: fixed;
			  left: 5px;
			  top: 80px;
			  bottom: 5px;
			">
		<div style="position:absolute;left:0px;top:0px;right:0px;bottom:0px;margin:auto;
		  margin:0rem;
		  display: -webkit-box;
		  display: -ms-flexbox;
		  display: flex;
		  -ms-flex-direction: column;
		  flex-direction: column;
		">
			<header>
				<div id="ocrMenuPanel" style="padding: 6px 0px;
			  border-bottom: 1px solid rgb(235, 233, 233);
			  overflow: hidden;">

					<div>
						<i style="
				font-family: 'iviewFont';
				display: inline-block;
				font-style: normal;
				font-weight: normal;
				font-variant: normal;
				font-size: calc(5vh - 15px);
				text-transform: none;
				text-rendering: auto;
				line-height: 1;
				-webkit-font-smoothing: antialiased;
				-moz-osx-font-smoothing: grayscale;
				vertical-align: middle;
				
				"
				title="选择图片"
				>
							&#xf1d0;
						</i>

					</div>
			</header>
			<main style="-webkit-box-flex: 1;
			-ms-flex: 1;
			flex: 1;
			overflow-y: auto;
			">

			</main>

		</div>
	</div>


	<div id="expandMenu">
		<i id="expandMenuIcon" style="
		font-family: 'iviewFont';
		display: inline-block;
    	font-style: normal;
    	font-weight: normal;
    	font-variant: normal;
    	text-transform: none;
    	text-rendering: auto;
    	line-height: 1;
    	-webkit-font-smoothing: antialiased;
    	-moz-osx-font-smoothing: grayscale;
    	vertical-align: middle;
		
		">
			&#xf11f;
		</i>

		<!-- import ViewUI from 'view-design';
			 import 'view-design/dist/styles/iview.css';
			 Vue.use(ViewUI); -->
		<!-- ios-arrow-forward &#xf11f; -->
		<!-- ios-folder-open-outline &#xf1d0  font-size: 100px; -->
	</div>
</body>

<script>
	let expandMenuIcon = document.querySelector('#expandMenuIcon')
	expandMenuIcon.addEventListener('click', () => {
		console.log(`clicked.`)
		expandMenuIcon.style.display = 'none'  // 隐藏
		// expandMenuIcon.style.display = "inline-block"  // 显示  
	}, true)
</script>

<style>
	@font-face {
		font-family: iviewFont;
		src: url('ionicons.ttf');
	}

	#expandMenu {
		float: left;
		cursor: pointer;
		text-align: center;
		margin-left: -8px;
	}

	#expandMenu:hover {
		color: #09f;
	}

	#expandMenuIcon {
		font-size: 20px;
		margin-top: calc(50vh - 10px);
	}
</style>

</html>
```



## addEventListener

- https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event

  > 引用元素时 id 用 #    class 用 .

```
事件冒泡或事件捕获？
事件传递有两种方式：冒泡与捕获。

事件传递定义了元素事件触发的顺序。 如果你将 <p> 元素插入到 <div> 元素中，用户点击 <p> 元素, 哪个元素的 "click" 事件先被触发呢？

在 冒泡 中，内部元素的事件会先被触发，然后再触发外部元素，即： <p> 元素的点击事件先触发，然后会触发 <div> 元素的点击事件。

在 捕获 中，外部元素的事件会先被触发，然后才会触发内部元素的事件，即： <div> 元素的点击事件先触发 ，然后再触发 <p> 元素的点击事件。

addEventListener() 方法可以指定 "useCapture" 参数来设置传递类型：

addEventListener(event, function, useCapture);
默认值为 false, 即冒泡传递，当值为 true 时, 事件使用捕获传递。

实例
document.getElementById("myDiv").addEventListener("click", myFunction, true);
```





## 分割线

```
<!-- 分割线 -->
<div id="splitLine" @mousedown="splitLineMouseDownEvent" ref="splitLine"></div>

#splitLine {
  width: 5px;
  left: calc(212px + ((100vw - 206px) / 2));
  height: calc(100vh - 10px);
  top: 5px;
  position: fixed;
  cursor: w-resize;
  z-index: 110;
}

    //分割线点击事件
    async splitLineMouseDownEvent(evt) {
      this.splitLineMouseDown = true;
      this.moveStartPos.x = evt.x;
      this.moveStartPos.y = evt.y;
      this.moveStartPos.spX = this.$refs["splitLine"].getBoundingClientRect().x;
      this.moveStartPos.textPanelWidth =
        this.$refs["textPanel"].getBoundingClientRect().width;
      let imgPanelRect = this.$refs["imgPanel"].getBoundingClientRect();
      this.moveStartPos.imgPanelWidth = imgPanelRect.width;
      this.moveStartPos.imgPanelX = imgPanelRect.x - 5;
    }

    //全局鼠标移动事件
    async globalMouseMove(evt) {
      if (!this.splitLineMouseDown) {
        return;
      }
      let x = evt.x;
      if (x < 380) {
        x = 380;
      }
      //鼠标移动后的距离差
      let spacing = x - this.moveStartPos.x;
      //分隔符距离左边的距离
      let left = this.moveStartPos.spX + spacing;
      this.$refs["splitLine"].style.left = `${left}px`;

      //内容框的宽度
      let newTextPanelWidth = this.moveStartPos.textPanelWidth + spacing;
      this.$refs["textPanel"].style.width = `${newTextPanelWidth}px`;

      //图片框的宽度
      let newImgPanelWidth = this.moveStartPos.imgPanelWidth + spacing * -1;
      this.$refs["imgPanel"].style.width = `${newImgPanelWidth}px`;
      //图片框左边距离
      let imgLeft = this.moveStartPos.imgPanelX + spacing;
      this.$refs["imgPanel"].style.left = `${imgLeft}px`;
    }


```



# vue3

[vscode直接通过打断点方式调试vite项目](https://juejin.cn/post/7281554762942988307)

[VS Code 调试 Vue.js](https://mdnice.com/writing/4707a411d4c343cfa0bfb65125731432)

[VS Code 调试 HTML 文件](https://zhuanlan.zhihu.com/p/415750996)

[chrome动态替换js](https://blog.51cto.com/u_15274085/2918220)

[Save all resources 保存整站](https://chromewebstore.google.com/detail/save-all-resources/abpdnfjocnmdomablahdcfnoggeeiedb)

```
npm create vue@latest
	# 一路输入 n 回车
 
cd ninja_wb && \
npm i && \
npm run dev

# vscode launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "chrome",
            "request": "launch",
            "name": "vuejs: chrome",
            "url": "http://localhost:5173",
            "webRoot": "${workspaceFolder}"
        }
    ]
}

# vite.config.js
import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
export default defineConfig({
  build: {
    sourcemap: true,
  },
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})

src/main.js
	# 成功断下

Vue Language Features
	# 安装 vscode 插件后 .vue 里的脚本可以成功断下

```





# Vue

- https://codepen.io/sdras/pen/dRqZOy  **codepen** 网络请求

- https://github.com/PanJiaChen/vue-element-admin

- https://github.com/miaolz123/vue-markdown  vue markdown

  > ```
  > git clone https://github.com/PanJiaChen/vue-element-admin.git
  > npm install --registry=https://registry.npm.taobao.org
  > npm run dev
  > http://localhost:9527
  > 
  > 
  > 本失败原因是由于tui-editor（富文本编辑器插件）更名造成的，现在已经更名为toast-ui/editor（以下第一步）
  > 并且该插件还进行了文件名的更名（以下第二步）以及方法名的更名（以下第三步）
  > 
  > 解决方案如下：
  > 1.首先将package.json中的tui-editor那一行修改为"@toast-ui/editor": "^3.1.3",
  > 
  > 2.进入\src\components\MarkdownEditor\index.vue文件，将他的所有import删除换成下面四行
  > import 'codemirror/lib/codemirror.css'
  > import '@toast-ui/editor/dist/toastui-editor.css'
  > import Editor from '@toast-ui/editor'
  > import defaultOptions from './default-options'
  > 
  > 3.把该页面（还是第二条中的文件）的getValue和setValue分别换成getMarkdown和setMarkdown
  > 把页面中的所有tui-editor全部替换为@toast-ui/editor
  > 
  > 4.保存文件，npm install 搞定
  > ```

  - https://www.jianshu.com/p/c77b5c4c026d

  - https://element.eleme.cn/#/zh-CN/component/select

    - https://element.eleme.io/#/en-US/component/quickstart

    > npm install element-ui -S
    >
    > import { Select, Button} from 'element-ui'
    >
    > // Vue.component(Select.name, Select)
    >
    > // Vue.component(Button.name, Button)

```
npm uninstall --global vue-cli
npm install -g vue-cli
vue --version
	# 2.9.6

npm install -g @vue/cli-service  ?? 
    # 解决 vue-cli-service 不是内部或外部命令, 也不是可运行的程序

vue init webpack pmweb
cd pmweb

新建 vue.config.js // 根目录下，和package.json 同级 // public: 'http://xxx.77:80' 指定公址
module.exports = {
    configureWebpack: {
        devtool: 'source-map'
    },
    assetsDir: 'static',
    runtimeCompiler: true,
    devServer: {
        disableHostCheck: true,
        public: 'http://xxx.77:80'
    }
}

// publicPath vue 支持用浏览器直接打开index.html
module.exports = {
    configureWebpack: {
        devtool: 'source-map'
    },
    assetsDir: 'static',
    runtimeCompiler: true,
    publicPath: './',
    devServer: {
        disableHostCheck: true,
        public: 'http://0.0.0.0:8081'
    }
}


package.json 下的devDependencies 加入开发依赖包(必须是这下面)
"@vue/cli-service": "^4.5.0",
"mini-css-extract-plugin": "^2.6.1"
npm i

package.json 的scripts 改成这样
  "scripts": {
    "dev": "vue-cli-service serve",
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build"
  }

npm run dev  # listening at localhost:8080

npm run build  # build for production
    # 解决打包出错
	# npm install --save-dev mini-css-extract-plugin  


指定端口:
在 node_modules@vue\cli-service\lib\commands\serve.js:  108行

const port = 80 //await portfinder.getPortPromise()  // portfinder 有BUG


# 如果用了babel ，这样配
babel.config.js
module.exports = {
    presets: [ [ "@vue/app", { useBuiltIns: "entry" } ] ]
}


```





## vue blog

- https://blog.kaciras.com/article/22/convert-async-to-sync-in-node 大神 vue blog

- https://github.com/kaciras-blog/website  blog 源码





## Syntax 



### v-if v-else v-else-if

```
    // 这几个是成对的，而且每一个都放在完整的 <div></div> 之内 ocr\src\components\column\buttonChooseBook.vue
    
    <div class="d-flex flex-center-y" v-if="$store.state.buttonChooseBook.BookName">
      <b>书籍名称：</b><p class="m-r-2">{{$store.state.buttonChooseBook.BookName }}</p>
      <el-link type="primary" @click="onClick({key:'更换书籍'})">更换</el-link>
    </div>
    <el-button v-else style="width: 200px;" size="small" @click="onClick({key:'选择书籍'})">请选择书籍</el-button>
```



### template

template 可以包裹元素，可以 v-for v-if，但不会被渲染到页面上

```
v-for="(line, lineIndex) in lines" 
                  <template v-if="false">
                  </template>
```





### click.stop



```
// click.stop 父容器的 点击事件 被无效化
```



### mousedown

- 若在同一个元素上**按下并松开鼠标左键**，会依次触发`mousedown`、`mouseup`、`click`，前一个事件执行完毕才会执行下一个事件
- 若在同一个元素上**按下并松开鼠标右键**，会依次触发`mousedown`、`mouseup`，前一个事件执行完毕才会执行下一个事件，不会触发`click`事件



### slot

```
<template>
  <div class="d-flex d-flex-column w-100 h-100">
    <slot name="header"></slot>
    <div
      class="flex-1 scroll-y"
      style="position: relative"
      ref="mainBar"
      @scroll="onScroll"
    >
      <slot></slot> // 子组件有一个匿名slot，引用实例定义的其它内容都会被塞进这里来，它就有滚动属性了
    </div>
    <slot name="footer"></slot>
  </div>
</template>



      <columnFlex class="p-2" style="height: 500px;" @onScroll="onScroll ref="columnFlex">
      
      这样引用

```



### v-model

```
// 双向绑定
<label @click.stop=""><Checkbox v-model="file.selected"></Checkbox></label>
```



### $event

```
        <img
          ref="img"
          id="img"
          @mousedown.stop="imgMouseDownEvent"
          @mouseup="imgMouseUPEvent"
          @mousemove="imgMouseMoveEvent($event)"
          @contextmenu="imgContextmenu"
          :src="imageData"
        />
    imgMouseMoveEvent(evt) {
        let xSpacing = evt.clientX - this.blockMouseX;
        let ySpacing = evt.clientY - this.blockMouseY;        
        

自定义控件的事件传参，或原生 DOM 的事件传参, 两者内容不太一样
```









### watch

```
  watch: {
    selectItem: {
      handler: function (val) {
        this.$nextTick(() => {
          try {
            let ni = this.$refs["nav" + val][0];
            this.$refs["linkBar"].style.width = ni.offsetWidth + "px";
            this.$refs[
              "linkBar"
            ].style.transform = `translate3d(${ni.offsetLeft}px,0px,0px)`;
          } catch (e) {

          }
        });
      },
    },
  }
```



### router

```
import router from './router'  // src/router/index.js 需要是这样的结构

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})


// router/index.js
    const index = {
      path: '/',
      // name: 'index',
      component: require('@/pages/index.vue').default,
      children: [],
      redirect: 'index'
    };
    const pageTab = {
      path: '/index',
      name: 'indexRoot',
      components: {}
    };
    index.children.push(pageTab);

    const routers = [index, {
      path: '/login',
      name: 'login',
      components: require('@/pages/login.vue')
    }]


// 其他页面跳转
	signOut() {
      localStorage.removeItem("__guid__");
      this.$router.replace({ path: "/login" });
    }
```







## Vue.js 快速入门

- https://xiaosheng.run/2019/01/02/introduction-to-vue.html





## 静态资源

- https://segmentfault.com/a/1190000018472635
- https://blog.csdn.net/Nalaluky/article/details/86590237
  - 绝对路径

- https://blog.51cto.com/u_10624715/3235228
  - 绝对路径

- https://blog.51cto.com/u_15127512/4372903?b=totalstatistic
  - vue-cli 中的静态资源处理
- https://www.cnblogs.com/dreamstartplace/p/12922224.html
  - vue-cli 如何配置assetsPublicPath； vue.config.js如何更改assetsPublicPath配置

- https://cli.vuejs.org/zh/config/
  - 官方文档

- https://cn.vitejs.dev/guide/assets.html
  - 静态资源处理

```
// 成功显示gif
<template>
  <div class="hello">
    <!-- <img src="../assets/logo.png"> -->
    <h1>{{ msg }}</h1>
    <div v-for="item in resultsModel" :key="item.result">
      <div v-html="item.result"></div>
      <br>
    </div>
  </div>
</template>

<script>
import imgUrl from '../assets/play.gif'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      resultsModel: [{result:`<p>hi1</p> <img src="${imgUrl}">`},{result:`<p>hi2</p>`}],
    }
  }
}
</script>
```



## window对象

- https://blog.csdn.net/qq_41337100/article/details/107103205
  - vue里dom节点和window对象

- https://blog.csdn.net/weixin_40126227/article/details/88338487
  - 绑定方法到WINDOW对象



## 指定端口号 

- https://forum.vuejs.org/t/topic/71983

```
在 node_modules@vue\cli-service\lib\commands\serve.js:  108行

const port = 80 //await portfinder.getPortPromise()  // portfinder 有BUG


# /root/pmweb/vue.config.js
module.exports = {
    assetsDir: 'static',
    runtimeCompiler: true,
    devServer: {
        disableHostCheck: true,
        public: 'http://xxx.77:80'
    }
}
```



## cloudflare

- https://justo.cyou/posts/cloudflare%E4%BB%A3%E7%90%86%E5%85%BC%E5%AE%B9%E7%9A%84%E7%BD%91%E7%BB%9C%E7%AB%AF%E5%8F%A3/
  - Cloudflare代理兼容的网络端口

```
http
80
8080
8880
2052
2082
2086
2095
```

```
https
443
2053
2083
2087
2096
8443
```

```
# 无缓存的端口
2052
2053
2082
2083
2086
2087
2095
2096
8880
8443
```



### cloudflared 穿透

- https://zhuanlan.zhihu.com/p/508569148

  

## 原生事件调非原生

```
# 自定义事件调用原生事件
this.$emit('click', param)
```

```
# 原生事件调用自定义事件
mounted(){
    window.play = function(elm_id) {
      let auid = `audio_${elm_id}`
      var igid = `img_${elm_id}`

      let au = document.getElementById(auid)
      let ig = document.getElementById(igid)
      if (au.paused) {
        au.play()
        ig.src = img_play2
        // this.$nextTick(() => {
        //   // DOM 渲染完后回调
        //   //debugger
        // })
        
        au.addEventListener("pause", function () {
            ig.src = img_play
        })
      }
      // var au = <HTMLAudioElement>document.getElementById(auid);
      // //var ig = <HTMLImageElement>document.getElementById("img"+id);

      // console.log(`openImg clicked. ${elm_id}`); debugger
    }
    let search = this.search
    window.next = async function() {
      await search()
    }
  }
```



## 延迟

```
  async function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms)
    })
  }
  await sleep(200)
  
          // this.$nextTick(() => {
        //   // DOM 渲染完后回调
        //   //debugger
        // })
  
```





## component



### select 

- https://masteringjs.io/tutorials/vue/select

```
<script src="https://unpkg.com/vue@next"></script>
<div style = "outline-style: solid" id="example">
  <select v-model="selected">
    <option disabled value="">Please Select</option>
    <option>A</option>
    <option>B</option>
    <option>C</option>
  </select>
  <span style="padding-left:5%">Your Choice is: {{selected}}</span>
</div>
<script>
Vue.createApp({
  data() {
    return {
      selected: ''
    };
  }
}).mount('#example');
</script>
```



```
import Vue from 'vue';
import vSelect from 'vue-select';

vSelect.props.reduce.default = function (option) {
    //  whatever you need to do
}

Vue.component('vSelect', vSelect);
```





## bent

- https://learnku.com/articles/33597

```
package.json 改成这样：
  "scripts": {
    "dev": "vue-cli-service serve",
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build"
  },
   "dependencies": {
    "bent": "^7.3.12",
    "moment": "^2.29.1",
    "vue": "^2.5.2",
    "vue-router": "^3.0.1"
  },
  "devDependencies": {
    "@vue/cli-service": "^4.5.0",

npm i
npm run dev


// src/main.js
// import config from './config'  // import 是异步，debugger 看不到值，还是require 好
import Vue from 'vue'
import App from './App'
import router from './router'

(async () => {

  const config = require('./config')
  console.log(config.server.encrypt)
  const bent = require('bent')
  const getBuffer = bent('buffer')
  let buffer = await getBuffer('https://cn.vuejs.org/images/logo.svg'); debugger

  // require('fs').writeFileSync('logo.svg', buffer)  // 浏览器不能写本地文件

  // console.log(getBuffer)

  Vue.config.productionTip = false

  /* eslint-disable no-new */
  new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
  })

})()
```



### 允许跨域

- https://blog.51cto.com/u_15454291/4775779

```
用 vue-cli-service serve 启动就会用 vue.config.js；
用 webpack-dev-server 启动就会用 wepback.config.js（默认）。
```

```
代理配置没那么复杂。

//vue.config.js
devServer: {
    proxy: 后端api地址
}
//网络请求的封装，注意，生产环境才设置api地址，开发环境不需要，否则无法代理
if (process.env.NODE_ENV !== 'development') {
    axios.defaults.baseURL = '后端api地址'
}
```





```
    config/index.js
    proxyTable: {
      '/': {
        target: 'http://localhost:80',
        changeOrigin: true,
        pathRewrite: {
          '^/': ''
        }
      }
    },
    
devServer: { //开发模式下使用的配置参数
    proxy: {
      '/api': {
        target: 'http://t.weather.sojson.com', // 接口域名
        changeOrigin: true, //是否跨域
        pathRewrite: {
          '^/api': '/api' //需要rewrite的,
        }
      }
    }
  }
```





- http://caibaojian.com/vue/guide/installation.html
- https://blog.csdn.net/xiecheng1995/article/details/106884399
  - v-for 刷新
- https://segmentfault.com/a/1190000012948175
  - watch
- https://v2.vuejs.org/v2/guide/forms.html
- https://zhuanlan.zhihu.com/p/258781918
  - WebAssembly + Rust + Vue + Webpack

```
npm uninstall --global vue-cli
npm install -g vue-cli
vue --version
	# 2.9.6

vue init webpack pmweb
cd pmweb

新建 vue.config.js // 根目录下，和package.json 同级
module.exports = {
  runtimeCompiler: true
}

package.json 加入依赖包
"@vue/cli-service": "^4.5.0"
npm i

package.json 的scripts 改成这样
  "scripts": {
    "dev": "vue-cli-service serve",
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build"
  }

npm run dev  # listening at localhost:8080

npm run build  # build for production
```



- https://blog.csdn.net/Caeser110/article/details/103504082

```
解决办法汇总
eslint: Expected indentation of 2 spaces but found 4
缩进报错 ，所有缩进只能用两个空格

Newline required at end of file but not found
需要在最后的后面再加一行!!!

Missing space before value for key ‘name’
在关键字“值”之前缺少空格

A space is required after ‘,’
在，后面要加空格

space-before-blocks
关键字后面要空一格。

key-spacing
对象字面量中冒号的前后空格

no-unused-vars
不能有声明后未被使用的变量或参数

```



## HelloWorld.vue



```
<template>
  <div class="hello">
    hello, world!
    <input v-model="message" placeholder="edit me">
    <p>Message is: {{ message }}</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      message: ''
    }
  }
}
</script>
```



### 点一次加一个文本框



```
// 点一次就加一个文本框
<input type="text" v-for="(item,i) of items" v-model="items[i]" :key="i"> <button @click="search">search</button>

  data () {
    return {
      items: []
    }
  },
  computed: {
    itemNum: function () {
      return this.items.length
    }
  },
  methods: {

    search () {
      this.items.push('1')
      console.log('hited.')
    }

  }
```



### iput 强制更新

- https://blog.csdn.net/weixin_43611145/article/details/107183944



```
    <input v-model="message.msg" placeholder="edit me" />  <button @click="search">search</button>

  data () {
    return {
      message: { msg: '' }
    }
  },
  methods: {

    search () {
      this.$set(this.message, 'msg', 'aaaa')
      console.log('hited.')
    }

  }

```





```
1.this.$forceUpdate()
上网搜索资料才知道写的多层v-for嵌套（嵌套过深）导致的，render函数没有自动更新，需手动强制刷新。

this.$forceUpdate()官方解释：强制Vue 实例重新渲染。注意它仅仅影响实例本身和插入插槽内容的子组件，而不是所有子组件。

2.this.$set(target, key, value)
在项目中，有的时候会给一些form中的对象赋值，this.form.xxx = 'xxx’赋值了，但是视图没有更新。

原因：vue实例只有在初始化的时候定义了form中的对象后，才会触发object.defineProperty()的方法，为每个属性和对象增加getter(),setter()方法。这样，这些属性和对象是受vue实例统一管理的，当修改某一个属性的时候，vue实例会监听它们的变化，进而触发dom更新视图。

this.$set(target, key, value)：target为需要添加属性的对象，key是要添加的属性名，一般是字符串形式，也可以是数字，value为属性key对应的值。

例：this.$set(this.form, 'name', '张三')
```



### 导入第三方库

- https://stackoverflow.com/questions/43608457/how-to-import-functions-from-different-js-file-in-a-vuewebpackvue-loader-proje

```

Say I want to import data into a component from src/mylib.js:

var test = {
  foo () { console.log('foo') },
  bar () { console.log('bar') },
  baz () { console.log('baz') }
}

export default test
In my .Vue file I simply imported test from src/mylib.js:

<script> 
  import test from '@/mylib'

  console.log(test.foo())
  ...
</script>
```



- https://blog.csdn.net/yiyueqinghui/article/details/84391749
- http://eccent.icu/2021/07/20/vue-import/
- https://blog.csdn.net/lihefei_coder/article/details/92628030

```
另外一种是全局导入，只需要在main.js中

import 'mui-player/dist/mui-player.min.css'
import MuiPlayer from 'mui-player'
即可导入了，导入之后还需要注册，由于不是Vue组件，没法利用Vue.use()注册组件，需要将导入的内容(这里是一个名为MuiPlayer的方法)挂载到全局的原型上，这样才能在所有组件中使用：

Vue.prototype.$MuiPlayer = MuiPlayer
其本质就是把导入的方法挂载到全局的原型上，这样所有组件都拥有了这个方法，只需在组件内部用

this.$MuiPlayer()
即可调用库中写好的方法。
```



### 插件

- https://segmentfault.com/a/1190000021959058

```
插件是全局的，组件可以全局注册也可以局部注册
```



## vscode 

- 安装 Vetur 语法高亮

- 安装Eslint

  > 设置为用 Eslint 格式化代码

### vue 在vscode 下断点

- https://cn.vuejs.org/v2/cookbook/debugging-in-vscode.html

  > vscode 安装插件 JavaScript Debugger
  >
  > ```
  > 新建 launch.json， 弹出的选项选择 chrome
  > 重点是：先在终端 npm run dev，看它的端口是什么，下面的url 端口就填什么，然后在vscode F5，会打开浏览器, 就可以在vscode 下断了
  > {
  > "version": "0.2.0",
  > "configurations": [
  >   {
  >       "type": "chrome",
  >       "request": "launch",
  >       "name": "vuejs: chrome",
  >       "url": "http://localhost:8082",
  >       "webRoot": "${workspaceFolder}/src",
  >       "sourceMapPathOverrides": {
  >           "webpack:///src/*": "${webRoot}/*"
  >       },
  >       "resolveSourceMapLocations": [
  >         "${workspaceFolder}/**",
  >         "!**/node_modules/**"
  >       ]
  >   }
  > ]
  > }
  > ```
  >
  > ```
  > vue.config.js # 注意配了这个 F5 后断点才真的断了下来
  > 
  > module.exports = {
  >  runtimeCompiler: true,
  >  configureWebpack: {
  >      devtool: 'source-map'
  >  }
  > }
  > 
  > var titme = Date.now();
  > var d = {
  > //可在浏览器中调试 说明： https://cn.vuejs.org/v2/cookbook/debugging-in-vscode.html
  > configureWebpack: {
  > devtool: 'source-map',
  > output: { // 输出重构  打包编译后的 文件名称  【模块名称.版本号.时间戳】
  > filename: `js/[name].${titme}.js`,
  > chunkFilename: `js/[name].${titme}.js`
  > },
  > },
  > // 是否在构建生产包时生成 sourceMap 文件，false将提高构建速度
  > productionSourceMap: false,
  > // // 设置生成的 HTML 中 <link rel="stylesheet"> 和 <script> 标签的 crossorigin 属性（注：仅影响构建时注入的标签）
  > publicPath: './', // 设置打包文件相对路径
  > // 输出文件目录
  > outputDir: "webv2",
  > }
  > console.log(`${process.env.NODE_ENV}`)
  > if( process.env.NODE_ENV.match(/build/g) ){ 
  > delete d.configureWebpack.devtool
  > d.productionSourceMap = false;
  > }
  > module.exports = d
  > ```
  >
  > vue 在vscode 下断点
  >
  > file --> preferences --> setting 找到eslint ，找到几个  check box 勾上



### 如果babel 出错

```
# babel.config.js 改成这样

module.exports = {
    presets: [
        [ "@vue/app", { useBuiltIns: "entry" } ]
    ]
}
```





## 运行前端

- npm  run serve 

  > 默认 8080 端口

## 让chrome 断下

```javascript
// index.vue
saveToWord() { debugger // 这样就会断在这一行 
```

- https://www.jianshu.com/p/c013027069ce
  - Vue前端部署



## 自适应大小

```
在父级div加：

overflow: auto;
```



## ios

- https://v2ex.com/t/862361 强制 WKWebView 进行刷新缓存实时渲染

  > IOS 中如果返回的 data 是普通文本文字，或返回的数据中包含普通文本文字，那只需要达到非空 200 字节即可以触发渲染
  >
  > ```
  > const IOS_200 = `<div style="height:0;width:0;">\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b</div>`
  > ```



# vue-element

- https://element.eleme.io/#/zh-CN/component/collapse

  > 手风琴效果  每次只能展开一个面板

- https://blog.csdn.net/u011332271/article/details/105226511

  > 动态创建组件

- https://cloud.tencent.com/developer/article/1467371

  > 官方文档给了解决方案：如果试图使用 v-html 组合模板，可以重新考虑是否通过使用组件来替代。
  >

```html
v-html指令解析成了innerHTML。所以在节点元素上直接用innerHTML也是可以的，例如：
document.getElementById('app').innerHTML = "xxxxx" # 纯html
```



- https://segmentfault.com/a/1190000010958154

  > v-for

- https://segmentfault.com/a/1190000020053344

  > 跨组件通信

- https://cn.vuejs.org/v2/guide/syntax.html#v-bind-%E7%BC%A9%E5%86%99

  ```
  v-bind 缩写
  
  <!-- `${jp}<img id="img_${elm_id}" src="${img_play}" onclick="play('${elm_id}')"><audio id="audio_${elm_id}" src="${au_url}" type="audio/mpeg" preload="auto"></audio><br>${zh}`; //debugger -->
  
  # 
          {{ item.jp }} <img :id="`img_${elm_id}`" :src="`${img_play}`" :onclick="`play('${elm_id}')`">
  ```


- https://blog.csdn.net/qq_29869111/article/details/100154941

  > 动态加载本地图片

- https://juejin.cn/post/6844904130176090126

  > 根据elementUI的Carousel+Image实现图片动态加载问题

- 图片的骚操作

  ```
  <img :src="item.image ? require(`../../assets/image/${item.image}`) : ''" alt="image"/>
  ```

  

- https://blog.csdn.net/qq_32963841/article/details/80707461

  > 3d 图



# vue-element-admin



```
src\router\modules\components.js

路由加一项
  children: [
    {
      path: 'multiselect',
      component: () => import('@/views/components-demo/multiselect'),
      name: 'multiselect',
      meta: { title: 'multiselect' }
    },
    
组件加一项
\src\views\components-demo\multiselect.vue


```



```
npm install --save normalize.css
```



## SplitPane

> https://panjiachen.github.io/vue-element-admin/#/components/split-pane



# VUE+CefSharp

- https://blog.csdn.net/lweiyue/article/details/120484812  CefSharp和Vue交互开发
- http://www.lizhenghao.site/blog/2022/01/08/136  Winform/WPF利用CefSharp集成vue开发
- https://blog.csdn.net/wuyuander/article/details/107359120  手把手教你使用CefSharp开发Winform
- https://blog.csdn.net/yh0503/article/details/86648682  WinForm CefSharp 笔记一（入门篇）
- https://www.cnblogs.com/TianFang/p/9906786.html  调试窗口



```c#

// NuGet 安装 CefSharp.WinForms

// 成功显示vue页面, 工程设置成 x64, any cpu 是不行的
using CefSharp.WinForms;

        public Form1()
        {
            InitializeComponent();

            //string path = AppDomain.CurrentDomain.BaseDirectory + @"dist/index.html";
            String path = string.Format(@"{0}\dist\index.html", Application.StartupPath);

            //String path = "http://baidu.com";

            browser = new ChromiumWebBrowser(path);
            browser.JavascriptObjectRepository.Settings.LegacyBindingEnabled = true;

            this.Controls.Add(browser);
            browser.Dock = DockStyle.Fill;
        }
```



## 无边框全透明窗体



```
// 设置窗体属性
BackColor  -> 点系统 -> (白色)window

FormBorderStyle -> None

ShowlnTaskbar -> False

Size -> 0,0

TransparencyKey -> (白色)window

```



## 双击托盘图标

```

            if (WindowState == FormWindowState.Minimized)
            {
                //还原窗体显示    
                WindowState = FormWindowState.Normal;
                //激活窗体并给予它焦点
                this.Activate();
                //任务栏区显示图标
                this.ShowInTaskbar = true;
                //托盘区图标隐藏
                notifyIcon1.Visible = false;
            }

```





## 退出程序



```c#
Application.ExitThread();

this.Dispose();
this.Close();

```



## 跨线程更新UI

- https://blog.csdn.net/l198738655/article/details/120126970





## 复制文件到目标目录



```
vs2019 
复制页面到目标目录
方式1
项目->属性->生成事件->生成前事件命令行

添加如下

xcopy /Y /i /e $(ProjectDir)\html $(TargetDir)\html
```







# VUE+Electron+Edge

- https://blog.csdn.net/kyq0417/article/details/111310539

  > VUE+Electron+Edge开发中遇到的坑

- https://github.com/agracio/electron-edge-js



# Godot

[suyu switch模拟器](https://gitlab.com/suyu-emu/suyu)



## 文档

### [SizeFlags](https://docs.godotengine.org/zh_CN/stable/classes/class_control.html?highlight=SizeFlags#id8)

```
enum SizeFlags:

SIZE_FILL = 1 --- 告诉父Container扩展此节点的边界，以在不推其他节点的情况下填充所有可用空间。使用size_flags_horizontal和size_flags_vertical。

SIZE_EXPAND = 2 --- 告诉父级Container让该节点占用您标记的轴上的所有可用空间。如果将多个相邻节点设置为扩展，它们将根据其拉伸比共享空间。参阅size_flags_stretch_ratio。与size_flags_horizontal和size_flags_vertical一起使用。

SIZE_EXPAND_FILL = 3 --- 将节点的大小标志设置为同时填充和扩展。有关更多信息，请参阅上面的2个常量。

SIZE_SHRINK_CENTER = 4 --- 告诉父级 Container 使节点本身居中。它基于控件的包围框居中，因此它不适用于 fill 或 expand 尺寸标志。与 size_flags_horizontal 和 size_flags_vertical 一起使用。

SIZE_SHRINK_END = 8 --- 告诉父级Container将节点与其末端（底部或右侧）对齐。它不适用于fill或expand size标志。与size_flags_horizontal和size_flags_vertical一起使用。
```





## 源码编译

- https://github.com/Orama-Interactive/Pixelorama

  - https://docs.godotengine.org/en/latest/contributing/development/compiling/compiling_for_windows.html
  - https://blog.csdn.net/feiyunw/article/details/121861944  必看

  ```
  安装 Godot 3.5
  
  python -m pip install scons
  
  python -m pip install --upgrade pywin32
  
  git clone -b 3.5.1-stable https://github.com/godotengine/godot.git
  
  启动"x64 Native Tools Command Prompt for VS"
  
  
  cd /d E:\t\godot
  
  scons platform=windows vsproj=yes
  	# 成功生成解决方案 godot\godot.sln
  	scons p=windows tools=no target=release use_lto=no deprecated=no vsproj=no debug_symbols=no
  	# 编译发布版本
  	scons p=windows tools=yes target=release_debug use_lto=no deprecated=no vsproj=yes debug_symbols=yes
  	# 编译Debug版本
  
  
  ```

- https://blog.csdn.net/my_business/article/details/7816736  **scons** 是类 cmake 工作，用python语法

- https://github.com/RodZill4/material-maker

- https://github.com/touilleMan/godot-python  **godot + python**



### awesome-godot

[awesome-godot](https://github.com/godotengine/awesome-godot#projects)

[book reader](https://github.com/miskatonicstudio/interactive-book-godot) 优秀

[intrepid](https://github.com/miskatonicstudio/intrepid/tree/godot-4-rc-migration) steam上架游戏



### 更改编辑器主题

[更改编辑器主题](https://github.com/godotengine/godot-syntax-themes)



### 入门问题汇总

[入门问题汇总](https://blog.csdn.net/u012863565/article/details/125018469)



### 自定义 GUI 控件

[自定义 GUI 控件](https://docs.godotengine.org/zh_CN/stable/tutorials/ui/custom_gui_controls.html?highlight=update)



### 自定义绘图

[自定义绘图](https://docs.godotengine.org/zh_CN/stable/tutorials/2d/custom_drawing_in_2d.html?highlight=update)



### Desktop Application Dev in Godot

[app dev](https://www.google.com/search?q=Desktop+Application+Development+in+Godot&sourceid=chrome&ie=UTF-8)

### demos

[demos](https://github.com/GDQuest/godot-demos)



## godot4.0

[gdcef  chrome 浏览器](https://github.com/Lecrapouille/gdcef/tree/godot-4.x)

[llama ws客户端看这里](D:\GitHub\echodict\pmserver\test\godot_ui)

[Pokemon Generator](https://github.com/nerdydrew/Random-Pokemon-Generator)

[开发者频道](https://chat.godotengine.org/channel/general)

[server go](https://github.com/topfreegames/pitaya)

[server go2](https://github.com/east-eden/server/blob/dev/docs/manual.md)

[skynet](https://github.com/cloudwu/skynet/wiki)



### 必看教程 

[Godello绝佳示例](https://github.com/alfredbaudisch/Godello)

[游戏背包](https://github.com/alfredbaudisch/GodotDynamicInventorySystem)

[Pixelorama像素画](https://github.com/Orama-Interactive/Pixelorama)

[material-maker才质编辑](https://github.com/RodZill4/material-maker)

[Animation实现subtitle](https://github.com/1Othello/godot-speech-to-subtitles)

[Godot-Pluggable-AI 游戏AI](https://github.com/spkingr/Godot-Pluggable-AI)

[godot-resources-as-sheets-plugin csv编辑器](https://github.com/don-tnowe/godot-resources-as-sheets-plugin)

- [godot-sprite-painter](https://github.com/don-tnowe/godot-sprite-painter)
- [godot-engine.file-editor  Markdonw 转 bbcode](https://github.com/fenix-hub/godot-engine.file-editor)

[Add a Spreadsheet resource for handling tabular data](https://github.com/don-tnowe/godot-sprite-painter)

[Markdown to Richtext ](https://github.com/fahrstuhl/godot_markdown/tree/godot_4) godot 3.3.4 正常

- ```
  [font=res://fonts/libmarkdown/heading_1.tres]title111111111111111111111[/font]
  ```

- [RichText 控件显示图片](https://github.com/nekofleet/rich-text-label-ex)

[markdonw 编辑器 Godot-TextEditor](https://github.com/teebarjunk/Godot-TextEditor) godot 3.3.4 正常

- [vscode in godot](https://github.com/RedMser/godot-embed-external-editor)

[godot-copilot Gpt4 插件](https://github.com/minosvasilias/godot-copilot)

[4.0源码3d工具](https://github.com/protongraph/protongraph)

[4.0源码完整游戏](https://github.com/zfoo-project/godot-bird)

[GODOT RECIPES](http://kidscancode.org/godot_recipes/4.x/)

[官方示例](https://github.com/godotengine/godot-demo-projects)

[godot-sqlite](https://github.com/2shady4u/godot-sqlite)

[redit讨论区](https://www.reddit.com/r/godot/)

[Godot 4.1 Issues Roadmap](https://github.com/orgs/godotengine/projects/28/views/1)



#### delta 的单位是秒

[delta 的单位是秒](https://docs.godotengine.org/ja/stable/tutorials/scripting/idle_and_physics_processing.html?highlight=delta)



### 插件

[llama ws客户端看这里](D:\GitHub\echodict\pmserver\test\godot_ui)

[另一个自制插件看这里](github/gdscript/animation_subtitle/addons/subtitle)

[目前用的唯一上架的ws插件](https://github.com/AndreaTerenz/WebSocket)



#### 加载

1. copy to project's addons directory 
2. 项目 -> 项目设置 -> 插件 -> 启用上打勾



#### 入口点

plugin.cfg 入口点由这个配置文件指定，配置文件必须是这个名字

```
[plugin]
name="WebSocket"
description="Wrapper node for WebSocketPeer"
author="AndreaTerenz"
version="1.0"
script="websocket_plugin.gd"
```



websocket_plugin.gd

```
@tool
extends EditorPlugin

func _enter_tree():
	# Add the new type with a name, a parent type, a script and an icon.
	add_custom_type("WebSocket", "Node",
		preload("res://addons/websocket/WebSocket.gd"),
		preload("res://addons/websocket/WebSocket.svg"))
	# Godot 控件库会多出一个 WebSocket ，在 Node 下面
	
func _exit_tree():
	# Always remember to remove it from the engine when deactivated.
	remove_custom_type("WebSocket")
```



WebSocket.gd

```
# 导出符号后，可以在 Godot 编缉器里面修改，就像原生控件一样
@export_range(0, 128) var receive_limit : int = 0
@export_range(0, 300) var connection_timeout : int = 10
@export_group("Routing")
@export var host := "127.0.0.1"
@export var route := "/"
@export var use_WSS := true
@export_group("Autoconnect")
@export var autoconnect_mode := AUTOCONNECT_MODE.NONE
@export var autoconnect_reference : Node = null
```



#### debug

[How do you debug editor plugins and tool scripts](https://www.reddit.com/r/godot/comments/11w5nxh/how_do_you_debug_editor_plugins_and_tool_scripts/?rdt=47499)

```
ProjectSettings

bool debug/gdscript/warnings/exclude_addons = true

If true, scripts in the res://addons folder will not generate warnings.
```





### FQA

[FQA](https://godotengine.org/qa/tag/godot4)



#### Godot 4.1 Issues Roadmap

[Godot 4.1 Issues Roadmap](https://github.com/orgs/godotengine/projects/28/views/1)



### 符号跳转

按住 ctrl -> 鼠标移到符号上 -> 点击



### utf8



```

data = Buffer.from(data, 'utf-8').toString()
	# node
```





```
func _unhandled_input(event):
    if event is InputEventKey:
        print(char(event.unicode))

print(char(358),char(358).to_utf8().size())

RawArray([unicode]).get_string_from_utf8()

```



```
extends MainLoop

func _idle(_delta):
	var string := "aaaa\u0000bbbb"
	print("%d: '%s'" % [len(string), string])
	var buffer := StreamPeerBuffer.new()
	buffer.put_utf8_string(string)
	# Expecting 13 because 32 bit integer + 9 characters
	print("%d: %s" % [len(buffer.data_array), var2str(buffer.data_array)])
	buffer.seek(0)
	string = buffer.get_utf8_string()
	print("%d: '%s'" % [len(string), string])
	return true
```






### 动态设置窗体大小

```
# 静态设置在：项目设置 ->显示 ->窗口
DisplayServer.window_set_size(Vector2i(1024, 600))
```



### 默认背景色

项目 -> 项目设置 -> 渲染 -> 环境 -> 默认清屏颜色

```
#4d4d4d
	# 灰色

```



```
VisualServer.set_default_clear_color(Color(0.4,0.4,0.4,1.0))
```



### margin 去哪了

```
Under Layout > Layout Mode select Anchors.
If you select Custom as the Anchor Preset, you can manually change the anchor points and the anchor offsets.
I believe these offsets are what were knows as margins.
```



### 皮肤和主题

[gui_skinning](https://docs.godotengine.org/en/stable/tutorials/ui/gui_skinning.html)



#### 全局theme

```
# 只能手动加在工程文件上面
project.godot
[gui]
theme/custom="res://assets/theme_trello_default.tres"
	# 设置的控件的清屏颜色等
```



#### 动态设置 Style

```
const StyleDragged := preload("res://assets/style_panel_list_dragged.tres")
set("custom_styles/panel", StyleDragged)
	# 这里 node 的方法，直接设置属性值
```



#### StyleBoxEmpty

Styles -> Focus -> StyleBoxEmpty 

实现 RichTextLabel 选中文字时也不显示窗体边框





### button的flat

效果是透明背景，会显示出窗体的底色



### label的字体颜色

1. Theme -> Theme Overrides -> Font Color
2. Visibility -> Self Modulate 

#### 动态设置label 字体大小

```
const BoardCard := preload("res://scenes/board_card.tscn")

func _ready():
	var board_card = BoardCard.instantiate()
	var label =  board_card.get_node("Label")
	label.add_theme_font_size_override("font_size", 32)
	label.text = "111111"
```



#### 自动获取焦点

```
line.grab_focus()
```





### 自动加载脚本

```
# 项目设置 ->自动加载 ->选择脚本
定义好结点名称，相当于自动帮你实际化了一个全局变量

SceneUtils.connect("change_route_requested", self, "_on_change_scene_requested")
```



### 动态实例化场景

```
# 场景用 preload ，控件用 @onready
const CardScene := preload("res://scenes/card.tscn")
const cardPreview := preload("res://scenes/card_mouse_preview.tscn")

@onready var card_container := $MarginContainer/VerticalContent/CardContainerScroll/CardContainer

boards = load("res://scenes/boards.tscn").instantiate()
```



#### 场景要进入场景树才会发生初始化

```
		var card_element = CardScene.instantiate()
		card_container.add_child(card_element) # 加入了场景树
		card_element.setTitle(str(i)) # 不能和上一句互换，否则内部控件还没有初始化
```





### 场景切换

```
func go_to_main_route():
	var err = get_tree().change_scene_to_file("res://scenes/main_scene.tscn")
	if err != OK:
		print("[scene_utils.go_to_main_route] could not change scene error code: ", err)
```



### 显示隐藏控件

```
# 一个编辑框，保存以后显示结果框，隐藏编辑框。右击结果框再反过来
# 上面是编辑框，下面是添加框。同一时间只能显示它们的其中一个
func _on_edit_check_item_requested(_node):
	if checkitem_edit_container.get_parent() == checklist_content:
		checklist_content.remove_child(checkitem_edit_container)
	
	task = _node.model
	checkitem_edit.set_text(_node.model.title)
	checkitem_edit_container.set_visible(true)
	checkitem_create_container.set_visible(false)
	checklist_items_container.add_child_below_node(_node, checkitem_edit_container)
	checklist_items_container.move_child(_node, checkitem_edit_container.get_index() - 1)
```



### 自动缩放

```
var Board:PackedScene  = preload("res://board.tscn")
	var board = Board.instantiate()
	board.layout_mode = 2
	board.size_flags_horizontal = 3
	board.size_flags_vertical = 3
```





### 动态 clone 控件

```
@onready var personal_boards_container := $ScrollContainer/MarginContainer/BoxContainer/PersonalBoardsContainer
@onready var create_Button := $ScrollContainer/MarginContainer/BoxContainer/PersonalBoardsContainer/Button

func _ready():
	var btn_clone = create_Button.duplicate()
	personal_boards_container.add_child(btn_clone)

```





### 嵌套Container

Container 直接套 Container ，第二个没法指定大小。必须先嵌入一个 ColorRect(例如)，再在它里面加Containner



如果想要 spacer, 可以加 SplitContainer 然后指定最小大小



### 滚动容器好像要固定位置才有滚动条

```
Layout -> Layout Mode -> Position
```



### GraphEdit

GraphEdit is a control responsible for displaying and manipulating graph-like data using GraphNodes. It provides access to creation, removal, connection, and disconnection of nodes.

```
var graph_edit:GraphEdit = $"../Panel/VBoxContainer/GraphEdit"
for connection in graph_edit.get_connection_list():
    var graph_node = graph_edit.get_node(connection.from) # <<< ERROR
The solution is to modify graph_edit.get_node(String(connection.from)) which converts from:StringName to from:String allowing it to be automatically coerced to from:NodePath. I would hope that in future StringName would automatically coerce to NodePath as expected, or else graph_edit.get_connection_list() should return {from:NodePath,...}[]
```





### @onready

```
# v3 是 onready
@onready var content_container := $ContentContainer
```



### @export

[Grouping Exports](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_exports.html)

```
# 该指令声明的变量可以在 editor 里面可见，并且可编辑
@export
var stream_paths : Array[String]
var streams : Array[VideoStream]
	# 这种写法只有第一行被导出，并且它的初始值是在配置里面赋值的
```



### @tool

```
@tool
	# 该指定需放在文件第一行，用来判断代码需要在 editor 中运行，还是在应用中运行

func _process(delta):
    if Engine.is_editor_hint():
        # Code to execute in editor.

    if not Engine.is_editor_hint():
        # Code to execute in game.
```



### % 

在控件右边空白处(脚本小图标的位置) 右键 -> 点一下 "作为唯一名称访问"

```
@onready var _view_container: ViewContainer = $%ViewContainer
	# 这样就不用写长长的路径了
```



#### node_path

```
# 绝对路径这样写
/root/main/LiveCaption:bbcode_text
	# main 是场景
	# LiveCaption 是里面的一个richLabel 控件
	# bbcode_text 是控件的属性, Animation 会绑定 bbcode_text 实现动画字幕
	
```



```
	# 
	var label = data["Label"]
	var parent = label.get_parent()
	var nodePath = parent.get_path_to(label)
	#var nodePath = null # NodePath(.owner.get_path_to(data["Label"]))
	var full_script = ""
	animation.value_track_set_update_mode(track_index, Animation.UPDATE_CONTINUOUS)
	animation.track_set_path(track_index, nodePath.get_concatenated_names() + ":text")
```







### :=

```
func initialize(label_name: String, type: int, opts := SlotOptions.new()):
	super(label_name, type, opts)
	# 参数默认值
```



### {}

```
var _targets := {}
func _ready() -> void:
	var parent = get_parent()

	if targets == 0:
		if parent is Control:
			_targets[parent] = SizingData.new()
	else:
		for c in parent.get_children():
			if c is Control:
				_targets[c] = SizingData.new()

	for target in _targets.keys():
		var data: SizingData = _targets[target]
		data.size = target.custom_minimum_size
		data.font_size = target.get_theme_constant("font_size")
		
var data: Dictionary = proton_node.external_data

```



```
var boards_by_id : Dictionary = {}

if !boards_by_id.erase(board.id):

```



### for

```
for x in [5, 7, 11]:
    statement # Loop iterates 3 times with 'x' as 5, then 7 and finally 11.

var dict = {"a": 0, "b": 1, "c": 2}
for i in dict:
    print(dict[i]) # Prints 0, then 1, then 2.

for i in range(3):
    statement # Similar to [0, 1, 2] but does not allocate an array.

for i in range(1, 3):
    statement # Similar to [1, 2] but does not allocate an array.

for i in range(2, 8, 2):
    statement # Similar to [2, 4, 6] but does not allocate an array.

for i in range(8, 2, -2):
    statement # Similar to [8, 6, 4] but does not allocate an array.

for c in "Hello":
    print(c) # Iterate through all characters in a String, print every letter on new line.

for i in 3:
    statement # Similar to range(3).

for i in 2.2:
    statement # Similar to range(ceil(2.2)).
```





### JSON

```
func _to_string():
	return JSON.stringify({
		"id": id,
		"title": title
	})

d.keys()
	# list of keys in the dictionary

```

#### Dictionary 和 JSON 是同一个东西

```
typeof(data) == TYPE_DICTIONARY and data.has("expected")

```





### new

```
# model.gd
class_name Model extends Object
enum ModelTypes {BOARD, LIST, CARD, TASK, USER}
var model_type : int
var id : String
func _init(_model_type : int,_id : String):
	model_type = _model_type
	id = _id

# usermodel.gd
class_name UserModel extends Model
var first_name : String
var last_name : String
var email : String
func _init(_id : String,_first_name : String,_last_name : String,_email : String):
	super(ModelTypes.USER,_id)
		# 基类初始化
	first_name = _first_name
	last_name = _last_name
	email = _email

```



#### RefCounted

```
# 带引用计数的对象，计数减到0时自动释放内存
var directory_module: RefCounted
directory_module = XDGDataPaths.new()
```



### Variant

```
var foo:Variant = 2 # 泛型
	# 不带类型修饰默认为泛型
	
var bar: int = 2 # 静态类型，后面不能给它赋值期他的类型 

```



#### 判断类型

```
func try_edit_value(value, type, property_hint) -> bool:
	if (
		type != TYPE_ARRAY and type != TYPE_PACKED_STRING_ARRAY
		and type != TYPE_PACKED_INT32_ARRAY and type != TYPE_PACKED_FLOAT32_ARRAY
		and type != TYPE_PACKED_INT64_ARRAY and type != TYPE_PACKED_FLOAT64_ARRAY
	):
		return false

	if sheet.column_hint_strings[sheet.get_selected_column()][0].begins_with("2/2:"):
		# For enums, prefer the specialized dock.
		return false

	_stored_type = type
	_stored_value = value.duplicate()  # Generic arrays are passed by reference
	contents_label.text = str(value)
	
	var is_generic_array = _stored_type == TYPE_ARRAY and !value.is_typed()
	button_box.get_child(1).visible = (
		is_generic_array or value.get_typed_builtin() == TYPE_STRING
		or _stored_type == TYPE_PACKED_STRING_ARRAY
	)
	button_box.get_child(2).visible = (
		is_generic_array or value.get_typed_builtin() == TYPE_INT
		or _stored_type == TYPE_PACKED_INT32_ARRAY or _stored_type == TYPE_PACKED_INT64_ARRAY
	)
	button_box.get_child(3).visible = (
		is_generic_array or value.get_typed_builtin() == TYPE_FLOAT
		or _stored_type == TYPE_PACKED_FLOAT32_ARRAY or _stored_type == TYPE_PACKED_FLOAT64_ARRAY
	)
	button_box.get_child(5).visible = (
		is_generic_array or value.get_typed_builtin() == TYPE_OBJECT
	)

	if value.get_typed_builtin() == TYPE_OBJECT:
		if !value_input is EditorResourcePicker:
			var new_input := EditorResourcePicker.new()
			new_input.size_flags_horizontal = SIZE_EXPAND_FILL
			new_input.base_type = value.get_typed_class_name()

			value_input.replace_by(new_input)
			value_input.free()
			value_input = new_input

	else:
		if !value_input is LineEdit:
			var new_input := LineEdit.new()
			new_input.size_flags_horizontal = SIZE_EXPAND_FILL

			value_input.replace_by(new_input)
			value_input.free()
			value_input = new_input

	return true

```





### setter getter

[setters and getters](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html#doc-gdscript-basics-setters-getters)

```
var milliseconds: int = 0
var seconds: int:
    get:
        return milliseconds / 1000
    set(value):
        milliseconds = value * 1000
```



```
var my_prop:
    get = get_my_prop, set = set_my_prop
	# 两函数定义在别处也是可以的，但是 setter 现在好像不支持多参数了？
	
```



### File

```
# see: gdscript/godot-subtitles-4.0_clone/scripts/Ulity.gd
func save(content):
    var file = FileAccess.open(path,FileAccess.WRITE)
    file.store_string(content)
    file = null

func load_game():
    var file = FileAccess.open(path,FileAccess.READ)
    var content = file.get_as_text()
    return content

func _ready():
    save(data)
    print(load_game())
    
# OR
func save(content):
    var file = FileAccess.open(path,FileAccess.WRITE)
    file.store_var(content)
    file = null

func load_game():
    var file = FileAccess.open(path,FileAccess.READ)
    var content = file.get_var()
    return content
    
```



```
func read_counter(file: FileAccess) -> int:
	var line = file.get_line()
	while line.is_empty() and !file.eof_reached():
		line = file.get_line()
	return int(line)

func read_times(file: FileAccess) -> Dictionary:
	var split = file.get_line().split(" --> ")
	return {
		"from": time_to_float(split[0]),
		"to": time_to_float(split[1])
	}

func read_caption(file: FileAccess) -> String:
	var caption = ""
	var line = file.get_line()
	while !line.is_empty():
		caption += line + "\n"
		line = file.get_line()
	return bb_format(caption)

```



#### path

```
如果该字符串是有效的文件路径，则返回基础目录名称。

var dir_path = "/path/to/file.txt".get_base_dir() # dir_path 为 "/path/to"

get_tree().edited_scene_root.filename.get_base_dir()


```





### match

```
	match _count:
		2:
			res = Vector2.ZERO
		3:
			res = Vector3.ZERO
```





### String



#### format

```
new_caption = new_caption.replace(m.get_string(0), '[%s%s]' % [m.get_string(1), m.get_string(2)])
```



```
func get_label_animation_path() -> String:
	var path: String = str(get_node(animation_player_node).get_path_to(get_node(label_node))) + ':bbcode_text'
	if path.begins_with("../"):
		path = path.trim_prefix("../")
	print("path_bbcode_text: %s" % path)

get_path_to
	# 可以是在找相对路径

```



```
print_debug("TTS not available!")
```



#### substr

```
if value is String: # TODO: Check is this is still used
		value = value.substr(1, value.length() - 2)
		vector = value.split(',')
		valid_value = (vector.size() == _count)
```



#### split

```
var split = time.replace(",", ".").split_floats(":")
 # "1,2.5,3" will return [1,2.5,3] if split by ","
```



#### get_concatenated_subnames第一个冒号的右侧部分  

```
# 第一个冒号的右侧部分
get_concatenated_subnames()

var nodepath = NodePath("Path2D/PathFollow2D/Sprite2D:texture:load_path")
print(nodepath.get_concatenated_subnames()) # texture:load_path

```



### Regex

```
var txt = "abc xyz abcdefg"
var regex = RegEx.new()
regex.compile("abc")

var result = regex.search(txt)
if result:
    print(result.get_string()) # prints abc

result = regex.search_all(txt)
if result:
    print(result) # prints an array of the search matches
```



```
var subject := "ab"
var pattern := "(.)"

var regex = RegEx.new()
regex.compile(pattern)

subject = regex.sub(subject, "$1&", true) # true to replace all match

prints(subject)
--> a&b&
```





### Array

#### join

```
var string_array = PackedStringArray(["hello", "world"])
var string = " ".join(string_array)
print(string) # "hello world"
```



### bbcode

#### font_size

```

func _ready():
	var rich = $RichTextLabel
	rich.set_text("[center][font=res://NotoSans-Bold.tres][font_size=30]hihhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh[/font_size][/font][/center]")

```





### uuid

```
class_name UUID extends Node

static func getRandomInt(max_value):
	randomize()

	return randi() % max_value

static func randomBytes(n):
	var r = []

	for index in range(0, n):
		r.append(getRandomInt(256))

	return r

static func uuidbin():
	var b = randomBytes(16)

	b[6] = (b[6] & 0x0f) | 0x40
	b[8] = (b[8] & 0x3f) | 0x80
	return b

static func v4():
	var b = uuidbin()

	var low = '%02x%02x%02x%02x' % [b[0], b[1], b[2], b[3]]
	var mid = '%02x%02x' % [b[4], b[5]]
	var hi = '%02x%02x' % [b[6], b[7]]
	var clock = '%02x%02x' % [b[8], b[9]]
	var node = '%02x%02x%02x%02x%02x%02x' % [b[10], b[11], b[12], b[13], b[14], b[15]]

	return '%s-%s-%s-%s-%s' % [low, mid, hi, clock, node]

```



### move_child

```
func _make_button_last_item(container : Node, button : Node):
	var amount = container.get_child_count()
	if amount > 1:
		container.move_child(button, amount - 1)
```



### clear_children

```
static func clear_children(node : Node, ignore := []) -> void:
	for child in node.get_children():
		if not child in ignore:
			child.queue_free()
```



### queue_free

```
dialog.queue_free() # 释放对象
```



### popup_centered

```
# 是 Window 的方法
func create_input_field_dialog(mode, board, list = null):
	var overlay = ColorRect.new()
	overlay.color = Color(0, 0, 0, 0.5)
	overlay.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT, Control.PRESET_MODE_KEEP_SIZE)
	get_parent().(overlay)

	var dialog = InputFieldDialog.instantiate()
	#dialog.popup_window = true

#	var size = DisplayServer.window_get_size() 
#	var x = size.x / 2
#	var y = size.y / 2
	
	#dialog.position = Vector2i(x, y)
	
	var freedialog = func ():
		if dialog:
			dialog.queue_free()
		if overlay:
			overlay.queue_free()
#
	dialog.canceled.connect(
		func ():
			freedialog.call()
	)

	dialog.confirmed.connect(
		func ():
			freedialog.call()
	)

	dialog.hided.connect(
		func ():
			freedialog.call()
	)

	overlay.add_child(dialog)
	dialog.set_board(board)
	dialog.set_mode(mode)

	if list: dialog.set_list(list)
	dialog.popup_centered()

```



```
	await dialog.popup_hide
	dialog.queue_free()
```





### get_node_or_null

```
func shoot():
if not get_parent().get_node("Laser"): 
    var laser = laser_scn.instantiate()
    laser.position.x = position.x
    laser.position.y = position.y - 16
    add_sibling(laser)

Or even better for this case, is has_node() since you aren't using the return value

```





### signal

[node communication](http://kidscancode.org/godot_recipes/4.x/basics/node_communication/)

```
await DataRepository.board_created
	# 信息可以等待, 直到信号触发后才会继续执行下面的代码

signal board_created()
	# 信号这样定义
	
func create_board():
	emit_signal("board_created")
		# 发送信号
		
```



#### 动态绑定事件



```
var board_card = BoardCard.instantiate()
	var label =  board_card.get_node("Label")
	label.add_theme_font_size_override("font_size", 32)
	label.add_theme_color_override("font_color", Color(100, 100, 100, 0.5))
	label.text = name_card
	
	board_card.pressed.connect(on_buttn_click)
		# pressed 是按钮的点击事件
		# on_buttn_click 是自定义函数
		
```



#### 内置信号传额外参数

[add extra arguments to connect built-in signals](https://github.com/godotengine/godot/issues/74769)



```
var callable = Callable(self, "on_buttn_click").bind(board_card)
board_card.connect("pressed", callable)

func on_buttn_click(sender):
	var t = sender.get_node("Label").text

```





```
extends Node2D
@onready var button = $Button
@onready var button2 = $Button2
# Called when the node enters the scene tree for the first time.
func _ready():
	var callable = Callable(self, "_button_down").bind("button1")
	button.connect("button_down", callable)
	var callable2 = Callable(self, "_button_down").bind("button2")
	button2.connect("button_down", callable2)
	pass # Replace with function body.

func _button_down(button_name):
	print("pressed button", button_name)
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
```





#### 自定义信号传额外参数

```
signal health_changed(old_value, new_value)
health_changed.emit(old_health, health)

```



#### 闭包

```
dialog.canceled.connect(
	func ():
		var a = 1 
)
```



#### lambda

[lambda Currying](https://gdscript.com/articles/godot-4-gdscript/)





### EditorPlugin

```
@tool
extends EditorPlugin

const AUTOLOAD_NAME = "YtDlp"

func _enter_tree():
	add_autoload_singleton(AUTOLOAD_NAME, "res://addons/godot-yt-dlp/src/yt_dlp.gd")

func _exit_tree():
	remove_autoload_singleton(AUTOLOAD_NAME)
```



### size_changed

```
@onready var scroll_container = $ScrollContainer

func _ready():
	get_tree().root.connect("size_changed", on_size_changed)

func on_size_changed():
	print("Resizing: ", get_viewport_rect().size, DisplayServer.window_get_size())
	scroll_container.set_size(DisplayServer.window_get_size())
```



### 鼠标

```
extends Control

func _gui_input(event):
   if event is InputEventMouseButton and event.button_index == BUTTON_LEFT and event.pressed:
       print("Left mouse button was pressed!")
```



```
# 右键
func _on_CheckItem_gui_input(event):
	if event is InputEventMouseButton and not event.is_pressed() and event.get_button_index() == MOUSE_BUTTON_RIGHT:
		emit_signal("edit_check_item_requested", self)
```



#### 获取鼠标位置

[Pixelorama](https://github.com/Orama-Interactive/Pixelorama)

```
func _input(event: InputEvent) -> void:
	left_cursor.position = get_global_mouse_position() + Vector2(-32, 32)
	right_cursor.position = get_global_mouse_position() + Vector2(32, 32)
		# 它是在当前鼠标位置显示一左一右显示两个工具小图标，按住左键操作左工具，右键操作右工具
	
	if event is InputEventKey and (event.scancode == KEY_ENTER or event.scancode == KEY_KP_ENTER):
		if get_focus_owner() is LineEdit:
			get_focus_owner().release_focus()
				# 获得当前拥有焦点的控件
```



#### 跟随鼠标

```
# from google bard
extends KinematicBody2D

func _physics_process(delta):
  var cursor = get_input("mouse_pos")
  $Sprite.translation = cursor - get_position()
```



### 键盘

```
func _input(ev):
	if Input.is_key_pressed(KEY_K):
		pass
```





### 控件拖拽

```
# 任何定义了 _get_drag_data 的控件，按住鼠标并拖动的时侯此函数就会被回调
func _get_drag_data(pos):
	# 在这里生成被拖子控件的预览图
	return { "cardID":"001" }

_get_drag_data(pos: Vector2)
	# 是 Control 的函数，控件被鼠标拖动的时侯由系统回调
	# 通常在这里 set_drag_preview 生成被拖控件的预览图
	# 函数最后返回一个数据，用于传给被拖放到的另一个控件
	接收拖放数据的控件要实现两个函数：
		_can_drop_data() 和 _drop_data()
			# 这里面应该能获取 _get_drag_data 的返回值
	
    func _can_drop_data(pos, data):
		# 返回ture 表示可以
    func _drop_data(pos, data)
    	# pos, data 是 _get_drag_data 传过来的
    	# 此方法只是通知你，有控件和数据被拖到这里了
    	# 你自已处理后续的逻辑
    	
set_drag_preview(card)
	# 是 Control 的函数，实例化一个场景传进去，就会显示一个预览图跟随鼠标，
	# 结束时会自动释放对象
	
```



#### 实现列表元素拖拽

```
extends MarginContainer

@onready var title_label := $CardContent/InnerPadding/VBoxContainer/TitleContainer/Title

signal card_hover_changed(card_hover)

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

func setTitle(title):
	title_label.set_text(title)

func getTitle():
	return title_label.get_text()

func _on_mouse_entered(): # 鼠标第一次移到控件上
	mouse_default_cursor_shape = 1
	card_hover_changed.emit(self)

func _on_mouse_exited():  # 鼠标离开控件
	card_hover_changed.emit(null)

```



#### 小技巧 _can_drop_data 就可以移了

```
 _can_drop_data 里面实现移动就很丝滑，但是只要你没有移回去它就在那了
```



#### 拖list中的card _can_drop_data 都触发 

```
先触发 card 的 _can_drop_data，再触发 list 的，这是不对的，
应该 让 card 可以拖，让 list 可以放，看下面的要点，
既 card 只定义 _get_drag_data 就好了
```



##### 要点： _can_drop_data _drop_data

只在card 中定义 _get_drag_data，然后 list 中定义 _can_drop_data 和 _drop_data



#### 算离当前坐标最近的子控件

```
	var closest_child
	var last_distance : float = -1
	var is_before := true

	var scrolled_mouse_pos := Vector2(pos.x, pos.y + card_container_scroll.get_v_scroll())

	for child in card_container.get_children():
		var distance : float = child.get_position().distance_to(scrolled_mouse_pos)

		if last_distance == -1 or (distance < last_distance):
			last_distance = distance
			closest_child = child

	var title = closest_child.getTitle()
	print("closest_child: " + title)
	return closest_child
```





### 键盘事件

[inputevent](https://docs.godotengine.org/en/stable/tutorials/inputs/inputevent.html)



```
func _process(_delta):
	if Input.is_action_just_pressed("ui_accept"): // 按回车会触发
```



### 手势

[GodotTouchInputManager](https://github.com/Federico-Ciuffardi/GodotTouchInputManager)







### 坐标系

[Godot疑难杂症01——触屏点击位置与全局位置之谜](https://zhuanlan.zhihu.com/p/414920112)

猜测**event.position实际是视窗内的坐标，不是全局坐标，需要根据camera位置进行转换**

<img src="nodejs summary.assets/image-20230301115309515.png" alt="image-20230301115309515" style="zoom:50%;" />



由于我的camera使用了zoom缩放1.5倍，多半是缩放导致的，实验结果也是离中心距离越远，和实际位置偏移越大，中心点几乎无偏移

但是缩放的坐标怎么转换呢，zoom是由视窗中心出发缩放周围，所以其实只需要按如下图求出z向量即可



<img src="nodejs summary.assets/image-20230301115404783.png" alt="image-20230301115404783" style="zoom:50%;" />

```
var relative_center_pos = -(node.get_viewport().get_visible_rect().size/2 - event.position
    relative_center_pos.x = relative_center_pos.x * current_camera.zoom.x
    relative_center_pos.y = relative_center_pos.y * current_camera.zoom.y
    return current_camera.get_camera_screen_center() + relative_center_pos
```

```
# 获取当前视窗的矩形位置
var canvas = get_canvas_transform()
var top_left = -canvas.origin / canvas.get_scale()
var size = get_viewport_rect().size / canvas.get_scale()
```

```
所有视口坐标-》世界坐标转换（可以适配相机的位移、旋转、缩放zoom），具体原理参见链接：
https://github.com/godotengine/godot/issues/44358

func actual_position(var camera,var pos):
	var inv_canv_tfm: Transform2D = camera.get_canvas_transform().affine_inverse()
	var half_screen: Transform2D = Transform2D().translated(pos)
	var actual_screen_center_pos: Vector2 = inv_canv_tfm * half_screen * Vector2(0, 0)
	return actual_screen_center_pos
```



### await



```
# 这样是正常的
extends Control

func asyn_fun():
	for s in ['a a', 'b b', 'c c']:
		var post = Post.new()
		self.add_child(post) # 注意必须加到场景post才正常
		post.mmesg(s)
		var arr = await post.mmesg_completed
		print("x".join(arr))
		self.remove_child(post)

func _ready():
	await asyn_fun()
	print('ready')
	
```





```
# popup 是窗口类，点关闭按钮时会触发信号 close_requested
await popup.close_requested
	# 只有信号触发后 await 才会返回

# Where "timeout" is the signal you are waiting for.
await get_tree().create_timer(1000).timeout
```



### switch 语句

```
func _get_scene_for_route(next_route : int) -> PackedScene:
	match next_route:
		SceneUtils.Routes.BOARD:
			return BoardScene
		_:
			return BoardsScene
```



### 骚操作

```
func _is_function_state(script_result):
	return script_result != null and \
		   typeof(script_result) == TYPE_OBJECT and \
		   script_result is GDScriptFunctionState and \
		   script_result.is_valid()

var call_this = Callable(script_inst, test_name)
call_this.call()
while(call_this.is_awaiting):
  await get_tree().idle_frame
  

3.x
script_result = script_inst.call(test_name)
if(_is_function_state(script_result)):
  yield(script_result, 'completed')

3.x
func create_single_error_popup(message : String, focus_after_close : Control, parent : Node):
	if popup:
		popup.queue_free()

	popup = load("res://scenes/single_button_popup.tscn").instance()
	popup.get_node("Label").set_text(message)
	parent.add_child(popup)
	popup.popup_centered()
	popup.get_close_button().grab_focus()

	yield(popup, "tree_exited")
	
	if popup:
		popup.queue_free()
	popup = null
	focus_after_close.grab_focus()

```



### 重写父方法

```
func do_something():
      .do_something() # 这里调用父控件的同名方法
      #additional code
```



### 定时器

```
yield(get_tree().create_timer(0.05), "timeout")
input_field.grab_focus()
```



### add_child prepend

```
		var btn_clone = create_Button.duplicate()
		btn_clone.set_text(str(i))
		personal_boards_container.add_child(btn_clone)
		personal_boards_container.move_child(btn_clone, 0)
```



# videoStreamPlayer

**search winUI3 in outline**

- https://godotforums.org/d/38003-how-to-stream-videos-from-urls/7
- [ai pet 功能丰富 含 url video play](https://github.com/aiaimimi0920/mimi)

[godot-video-reference](https://github.com/kidrigger/godot-video-reference)

- ```
  # 太难了，搞不了
  git clone --recursive   https://github.com/kidrigger/godot-video-reference.git && \
  pip install scons
  scons target=editor generate_bindings=yes vsproj=yes
  
  
  ```

  

[EIRTeam.FFmpeg ](https://github.com/EIRTeam/EIRTeam.FFmpeg)  search godot gdextension video

- ```
  
  git clone --recursive https://github.com/EIRTeam/EIRTeam.FFmpeg.git && \
  cd EIRTeam.FFmpeg/gdextension_build && \
  scons platform=windows verbose=true vsproj=yes
  	# 成功编译
  
  var ff_stream: FFmpegVideoStream = null
  var ffmpeg_stream = FFmpegVideoStream.new()
  	ffmpeg_stream.file = "/Users/chris/media/seeyou.mp4"	
  	$VideoStreamPlayer.stream = ffmpeg_stream
  	$VideoStreamPlayer.play()
  	$VideoStreamPlayer.stream_position = 2.0
  ```
  
- Turn Videos into Games 商店搜

[elly_videoplayer](https://github.com/Elly2018/elly_videoplayer)  **better than eir?**

- ```
  DemoScene.tscn
  [connection signal="ToLoad" from="PlayUI" to="Plane" method="load_trigger"]
  	# 在场景文件里定义连接（ui 上能显示连接，但是没有地方给你手动点连接）
  	# 不放 .gd 里连接可能这样更清晰 ?
  	# 位于下层的控件事件往上冒泡，先到同级的上一层，再到父控件。这样安排比较好？
  
  自已编译才能正常播放
  	see huggingface/elly_videoplayer
  	
  	
  ```

  

[GoZen-ffmpeg 视频编译器的一部分 很新 必看](https://github.com/VoylinsGamedevJourney/GoZen-ffmpeg)

- ```
  
  git clone https://github.com/VoylinsGamedevJourney/GoZen.git && \
  cd GoZen && \
  git clone https://github.com/VoylinsGamedevJourney/GoZen-ffmpeg.git && \
  cd GoZen-ffmpeg && \
  git reset --hard b0eb64e && \
  git clone https://github.com/godotengine/godot-cpp.git && \
  cd godot-cpp && \
  git reset --hard f3143c7
  
  
  cd GoZen\gozen-ffmpeg && \
  curl --output ffmpeg.zip -L -O https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl-shared.tar.xz
  	# 下载 ffmpeg
  
  复制 elly_videoplayer\src\ffmpeg 到 GoZen\gozen-ffmpeg\ffmpeg
  修改 gozen-ffmpeg/SConstruct 
  	env.Append(CPPPATH=["src/", "ffmpeg/include/"])
  	env.Append(LIBPATH=["ffmpeg/lib/"])
  		# 可能只有 linux 能编译成功
  
  cd GoZe/GoZen-ffmpeg && \
  scons -Q -j2 destination=../src/editor/bin target=template_release platform=linux
  
  
  cp /root/GoZen/gozen-ffmpeg/bin/libgozen.linux.template_release.x86_64.so /root/GoZen/src/editor/bin
  
  
  
  https://download.visualstudio.microsoft.com/download/pr/1cac4d08-3025-4c00-972d-5c7ea446d1d7/a83bc5cbedf8b90495802ccfedaeb2e6/dotnet-sdk-6.0.417-linux-x64.tar.gz
  
  mkdir -p $HOME/dotnet && tar zxf dotnet-sdk-6.0.417-linux-x64.tar.gz  -C $HOME/dotnet
  export DOTNET_ROOT=$HOME/dotnet && \
  export PATH=$PATH:$HOME/dotnet
  
  
  E:\t\GoZen\gozen-ffmpeg\src\ffmpeg_includes.hpp(4): fatal error C1083: 无法打开包括文件: “libavcodec/avcodec.h”: No such file or directory
  	# 他只官方编译了 linux 版
  
  
  
  
  
  gh repo clone VoylinsGamedevJourney/GoZen-ffmpeg -- --recurse-submodules
  
  gh repo clone VoylinsGamedevJourney/GoZen -- --recurse-submodules
  
  
  ssh-keyscan github.com >> ~/.ssh/known_hosts
  
  git clone --recursive https://github.com/VoylinsGamedevJourney/GoZen-ffmpeg.git
  
  git clone --recursive https://github.com/VoylinsGamedevJourney/GoZen.git && \
  cd GoZen
  scons -j 2 destination=../src/editor/bin target=template_release platform=windows
  ```
  

[mimi 功能挺多待观察](https://github.com/aiaimimi0920/mimi.git)

[opencv VideoSprite](https://github.com/godotengine/godot-proposals/issues/3286)

[creating_movies](https://docs.godotengine.org/en/latest/tutorials/animation/creating_movies.html) 录制视频

[VideoStreamPlayer](https://docs.godotengine.org/en/stable/classes/class_videostreamplayer.html)

[godot-video-reference  demo](https://github.com/kidrigger/godot-video-reference)



```
# see Turn Videos into Games  in 
func find_current_stream():
	current_stream = null
	for node in get_children():
		if node is VideoStreamPlayer and node.is_visible():
			current_stream = node
			print("found ", node.name)
			break


func reset_when_done():
	if not current_stream.is_playing():
		get_tree().reload_current_scene()

func _process(delta: float) -> void:
	clicking_position()
	if Input.is_action_just_pressed("choose_new_color"):
		set_goal_color()
	reset_when_done()
	update_score_text()
```



```

Godot_v4.2.1-stable_mono 新建项目，会自动生成 visual studio 解决方案, 打开
添加 OpenCvSharp4.Windows和 OpenCvSharp4.Extensions(来自NuGet) 
	# https://www.bilibili.com/read/cv23585404/

https://gamedevacademy.org/sprite2d-in-godot-complete-guide/
	# good
https://blog.csdn.net/qq_46273065/article/details/128120402
	# python实现视频音频同步
	
https://github.com/opencv/opencv/blob/4.x/samples/cpp/videocapture_audio_combination.cpp
	# 同时处理音视频
	
https://github.com/Nolkaloid/godot-yt-dlp
	# 必看
	
GitHub\gdscript\sprite2d
	# 成品 用 opencv 逐帧取图，按帧率算好时间画图

https://forum.godotengine.org/t/decode-an-image-sent-over-udp-from-python-opencv-to-godot-for-texture-data-use/3531
	# UDP opencv 通信传图，godot 显示


GD.Print("whatever");
	# C# script 这样输出


It results in about 45fps now, because of the stupid conversions, that go like:

Video Frame -> Raw OpenCV -> OpenCV mat -> bmp bytes -> godot image -> godot texture -> Sprite2D.

If one were to shave a few steps from the list, it would yield an acceptable performance for sure.

Also, one should decouple video frame processing from the rendering thread (for obvious reasons). So, the real code would be more like:

using Godot;
using OpenCvSharp; // Install https://www.nuget.org/packages/OpenCvSharp4.Windows
using System;
using System.Threading;
using System.Threading.Tasks;

public partial class VideoSprite : Sprite2D
{
    [Export]
    public string VideoPath { get; set; }
    private VideoCapture _capture;
    private ImageTexture _texture;
    private Task _playVideoTask;
    private Image _image;

    public override void _Ready()
    {
        // Pefrorm the 1st draw and init textures
        _capture = new VideoCapture(this.VideoPath);
        if (!_capture.IsOpened())
            throw new Exception($"Failed to open {this.VideoPath}");
        _image = new Image();
        var frame = new Mat();
        _capture.Read(frame);
        _image.LoadBmpFromBuffer(frame.ToBytes(ext: ".bmp"));
        _texture = ImageTexture.CreateFromImage(_image);
        this.Texture = _texture;

        // Start processing task
        _playVideoTask = new Task(() => PlayVideo());
        _playVideoTask.Start();
    }

    private void PlayVideo()
    {
        var startTime = DateTime.UtcNow;
        while (true)
        {
            double playbackPosition = (DateTime.UtcNow - startTime).TotalSeconds;
            var currentFrame = (int)(playbackPosition * _capture.Fps);
            if (_capture.PosFrames >= currentFrame)
            {
                // It's already displaying the correct frame. Wait for half a frame time and try again
                Thread.Sleep((int)(1000 / (_capture.Fps/2)));
                continue;
            }

            var frame = new Mat();
            _capture.Read(frame);
            if (frame.Empty())
                return; // Video is over, exit

            // Convert frame data to godot boilerplate
            var bmpBytes = frame.ToBytes(ext: ".bmp");
            var boilerplate = new Image();
            boilerplate.LoadBmpFromBuffer(bmpBytes);
            Interlocked.Exchange(ref _image, boilerplate);
        }
    }

    public override void _PhysicsProcess(double delta)
    {
        _texture.Update(_image);
    }
}
```





### Post

```
场景的root结点 加一个 HTTPRequest 作为子结点

func _ready():
	$HTTPRequest.request_completed.connect(_on_request_completed)
	$HTTPRequest.request("https://api.github.com/repos/godotengine/godot/releases/latest")

func _on_request_completed(result, response_code, headers, body):
	var json = JSON.parse_string(body.get_string_from_utf8())
	print(json["name"])
		# 请求成功 --> 4.1.1-stable
```



#### x-www-form-urlencoded

```
extends HTTPRequest

signal searchAk48_completed(result)
signal completed_(result)

func searchAk48(keywd):
	var url = "http://127.0.0.1:8880/searchAk48"
	
	self.request_completed.connect(
		func (result, response_code, headers, body):
			completed_.emit({"result":result, "response_code":response_code, "headers":headers, "body":body})
			#var json = JSON.parse_string(body.get_string_from_utf8())
			#print(json["name"])
	)
	
	var http = HTTPClient.new()
	var queryString = http.query_string_from_dict({"keywd":keywd, "lang_type":"jp"})
	var headers = ["Content-Type: application/x-www-form-urlencoded"]
	self.request(url, headers, HTTPClient.METHOD_POST, queryString)
	
	var re = await completed_
	if re.result == HTTPRequest.RESULT_SUCCESS:
		var s = re.body.get_string_from_utf8()
		var j = JSON.parse_string(s)
		if j.status == 200:
			var data = j.data
			searchAk48_completed.emit([data, ''])
			return
		else:	
			searchAk48_completed.emit([null, s])
			return
	elif re.result == HTTPRequest.RESULT_TIMEOUT:
		pass
	else:
		pass
		
	searchAk48_completed.emit([null, 'post fail.'])
```



```
另见 uri_decode()。

var prefix = "https://docs.godotengine.org/en/4.1/?highlight="
var url = prefix + "Godot Engine:docs".uri_encode()

print(url) # 输出 "https://docs.godotengine.org/en/4.1/?highlight=Godot%20Engine%3%docs"

```





### WebSocket

[目前用的唯一上架的ws插件](https://github.com/AndreaTerenz/WebSocket)

[godot-websocket-nodes](https://github.com/Faless/gd-websocket-nodes/tree/main/addons/godot-websocket-nodes) 必看

[WebSocket](https://github.com/godotengine/godot/issues/73810)

[websocket html5](https://godotengine.org/qa/95051/problems-with-websockets-and-html5-export)

> Hi, if the website you use as environment for the Godot-export-HTML (in your case itch.io) uses http**s** you cannot use your IP address with "ws://...". However, the browser makes an exception for localhost - that's why it worked this way.
> You need to connect to your server with "ws**s**://**:"
> This, consequentially, requires SSL encryption. You can generate self-signed keys and certificates [within Godot using the Crypto-Reference](https://godotengine.org/article/websocket-ssl-testing-html5-export). Yet, it would be better to use an official SSL certificate website instead. The link also shows how to use key and certificate on the server after creation.
> HOWEVER, all this being said, I figured there is a [Godot intern bug that disconnects the client from the server immediately when trying to connect to the server](https://github.com/godotengine/godot/issues/27560). There is no sign of an error, but the engine emits the "disconnect"-signal.
> The easiest solution was to start an Apache server which runs the Godot-export-HTML unencrypted via "ws://..." - thus, this way, you wouldn't have your project running on itch.io.
>
> You can find a better explanation of the solution [here](https://www.reddit.com/r/godot/comments/et52fp/how_to_integrate_web_sockets_secure_wss_in_godot/).







## 可调窗体

- https://github.com/gilzoide/godot-dockable-container



### tool 关键字

[tool 关键字](https://docs.godotengine.org/zh_CN/latest/tutorials/plugins/running_code_in_the_editor.html)

```
tool是一个强大的关键字，当添加到脚本的顶部时，它会在编辑器中执行。您还可以决定脚本的哪些部分在编辑器中执行，哪部分在游戏中执行，以及哪部分在两者中均执行。
```

### 水平拆分容器

[splitcontainer](https://docs.godotengine.org/en/stable/classes/class_splitcontainer.html)

[HSplitContainer with two sidebars](https://www.reddit.com/r/godot/comments/on5vun/how_can_i_use_hsplitcontainer_to_create_a_ui_with/)

[Best way to split screen evenly](https://www.reddit.com/r/godot/comments/ruelz9/best_way_to_split_screen_evenly_for_ui/)

> ```
> # HSplitContainer 用这个就可以实现水平拆分了
> Use an HBoxContainer with full rect. Add 2 Controls as children with horizontal size flags set to fill and expand.
> ```

[size and anchors](https://docs.godotengine.org/en/3.1/tutorials/gui/size_and_anchors.html)

[multiple_resolutions](https://docs.godotengine.org/en/3.1/tutorials/viewports/multiple_resolutions.html)

[Control node resize in the editor when animation player plays an animation](https://github.com/godotengine/godot/issues/65530)

[video to learn about the stretch mode](https://youtu.be/gkY6X-bziHQ)

 In Project Settings/General/Display/Window set Size: Resizeable=true and Stretch: Mode=viewport, Aspect=keep and start the exported HTML5 game with Firefox.

```
# 关键在于：顶层的 Control 和 下面的 HSplitContainer 都要设置自动调大小
	# HSplitContainer 里面放两控件，全部自动拉伸占用所有空间
func _ready():
	#if OS.get_name()=="HTML5":
	#self.set_size( OS.get_window_size() )
	get_tree().root.connect("size_changed", self, "on_size_changed")
	OS.set_window_maximized(true)
	
func on_size_changed():
	print("Resizing: ", get_viewport_rect().size, OS.get_window_size())
	self.set_size( OS.get_window_size() )


# godot 4.0
@onready var scroll_container = $ScrollContainer

func _ready():
	get_tree().root.connect("size_changed", on_size_changed)

func on_size_changed():
	print("Resizing: ", get_viewport_rect().size, DisplayServer.window_get_size())
	scroll_container.set_size(DisplayServer.window_get_size())

```



```
# auto resize when screen resize
var screen_size : Vector2 = Vector2()

func _ready():
screen_size = OS.get_screen_size()# Gets the screen size to test in futur if its change since their

func _process(delta) -> void:
    if OS.get_screen_size() != screen_size: #Tests if your screen changed in size, e.g a different monitor
        screen_size = OS.get_screen_size()
        OS.set_window_size(screen_size)# Sets your window to your screen size
```







#### 更改背景色

```
use a StyleBoxFlat in the Normal Stylebox and set the "Bg Color" and Border properties of that in the properties list that appears immediately below its preview in the Inspector. 
```

```
In the inspector, under TextEdit, check the "Syntax Highlighting" option. Then you can modify the background color under the "Custom Colors" heading by checking it's box and selecting a color.
```

```
The easiest way I have been able to do was to open the Custom Styles Section of the Text Edit and then add a new style to the Normal style, then edit that added style to the background color you want.
```



#### wrap textEdit

[wrap textEdit](https://github.com/godotengine/godot/issues/3985) [u](https://github.com/godotengine/godot/files/2952478/wrap_test.zip)





### GDScript

[tutorial](https://gdscript.com/tutorials/)

[QA](https://godotengine.org/qa/tag/gdscript)



## 拷贝大量数据

```
# https://github.com/touilleMan/godot-python/issues/329
I was suggesting to create the bytes array through godot.pool_arrays.PoolByteArray, then accessing it underlying buffer with godot.pool_arrays.PoolByteArray.raw_access. numpy.frombuffer can then wrap this underlying buffer without copying it.
You then end up with a Numpy array that can be used for your Image.create_from_data, the only gotcha is you should be careful about this numpy array object lifetime given it shares the same buffer with the PoolByteArray.

The easy way to avoid lifetime issues would be to create a PoolByteArray singleton with a fixed size when initializing your application (hence the underlying buffer is never freed)
```



### lmdb

[LMDB-基础结构与Mmap思想](https://www.jianshu.com/p/6378082987ec)

[构建高可用分布式Key-Value存储服务](https://github.com/siddontang/blog/blob/master/before-2016/build-ha-distributed-kv-service.md)

[meilisearch](https://docs.meilisearch.com/learn/advanced/storage.html#database-location) 构建在lmdb之上?

文件最大支持4G

```
LMDB（Lighting Memory DB）是在BerkeleyDB的基础上进行改编具有高效、紧凑、健壮性的数据库。它文件结构简单，一个文件夹，里面一个数据文件，一个锁文件。数据随意复制，随意传输。它的访问简单，不需要运行单独的数据库管理进程，只要在访问数据的代码里引用LMDB库，访问时给文件路径即可。
```



```
整个数据集都在磁盘上。它的一些部分在内存中。当需要不在内存中的部分时--操作系统从磁盘中获取它，并通过把它放在进程的内存中交给应用程序。

后台的mongodb，但不仅如此，我还想到了postgresql，它们强烈建议拥有与工作数据集同样多的内存。
```



```
LMDB全称Lightning Memory-Mapped Database,是内存映射型数据库，这意味着它返回指向键和值的内存地址的指针，而不需要像大多数其他数据库那样复制内存中的任何内容，使用内存映射文件，可以提供更好的输入/输出性能，对于神经网络的的大型数据集可以将其存储到LMDB中

LMDB属于key-value数据库，而不是关系型数据库( 比如 MySQL )，LMDB提供 key-value 存储，其中每个键值对都是我们数据集中的一个样本。LMDB的主要作用是提供数据管理，可以将各种各样的原始数据转换为统一的key-value存储。

LMDB不仅可以用来存放训练和测试用的数据集，还可以存放神经网络提取出的特征数据。如果数据的结构很简单，就是大量的矩阵和向量，而且数据之间没有什么关联，数据内没有复杂的对象结构，那么就可以选择LMDB这个简单的数据库来存放数据。

用LMDB数据库来存放图像数据，而不是直接读取原始图像数据的原因：

数据类型多种多样，比如：二进制文件、文本文件、编码后的图像文件jpeg、png等，不可能用一套代码实现所有类型的输入数据读取，因此通过LMDB数据库，转换为统一数据格式可以简化数据读取层的实现。
lmdb具有极高的存取速度，大大减少了系统访问大量小文件时的磁盘IO的时间开销。LMDB将整个数据集都放在一个文件里，避免了文件系统寻址的开销，你的存储介质有多快，就能访问多快，不会因为文件多而导致时间长。LMDB使用了内存映射的方式访问文件，这使得文件内寻址的开销大幅度降低。
```



### nodejs不解压读取文件

[nodejs不解压读取文件](https://www.jianshu.com/p/74fc8e90eab0)





## sqlite

[node-sqlite3](https://github.com/TryGhost/node-sqlite3)

[sqlite-gui c + winapi](https://github.com/little-brother/sqlite-gui)

npm install sqlite3

```
async function search_sq_ak48(jp) {

    return new Promise((resolve, reject) => {
        let _ = require('lodash')
        const sqlite3 = require('sqlite3').verbose()
        //const db = new sqlite3.Database(':memory:')
        const db = new sqlite3.Database(db_file)

        db.serialize(() => {
            let sq = `SELECT * FROM ak48 where kanji = '${jp}' or hana = '${jp}'`
            //let sq = "SELECT 1"
            db.all(sq, (err, rows) => {
                let choice = []
                if (rows.length > 3) {
                    choice = _.sampleSize(rows, 3)
                } else {
                    choice = rows
                }
        
                db.close(function() {
                    return resolve(choice)
                })
            })
        })
    })
}
```







## cef chrome

- https://github.com/Lecrapouille/gdcef/issues/30  嵌入cef

```
OS.shell_open("url")
	# 调用系统功能

if OS.has_feature('JavaScript'):
    JavaScript.eval("""
        window.open('https://google.com', '_blank').focus();
    """)
```



## video

[godot-video-rendering-demo](https://github.com/Calinou/godot-video-rendering-demo) need  Godot 3.1 beta 8

[audio 频率播放动效](https://github.com/xiangyuecn/Recorder/blob/master/assets/runtime-codes/dsp.lib.fft_exact.js)

[seek 插件](https://github.com/godotengine/godot/issues/32200)

```
Make sure to run the project from the command line using 
the --fixed-fps 60 command line argument.
```



### EIRTeam.FFmpeg

[EIRTeam.FFmpeg 插件足够新](https://github.com/EIRTeam/EIRTeam.FFmpeg/issues/2)

[godot-video-reference 好像功能齐全](https://github.com/kidrigger/godot-video-reference)



### 视频转GIF

[record video](https://docs.godotengine.org/en/stable/tutorials/animation/creating_movies.html)

```
播放器 potplayer 自带的 GIF 功能，分辨率帧率质量都能调

mac : gifski
window : screentogif

两个都可以调整帧率 gif 质量
```



```
ffmpeg -ss 1 -i <INPUT> -vf fps=1,scale='min(320,iw)':-1,scale=-1:'min(240,ih)' -gifflags -transdiff -frames:v 15 -vsync vfr -f gif <OUTPUT.GIF>

从视频第 1 秒开始，按比例缩小尺寸，并且取前 15 帧
```







## subtitle

[godot-speech-to-subtitles](https://github.com/1Othello/godot-speech-to-subtitles) 

- Godot4 看这里: github/gdscript/animation_subtitle

[godot-subtitles](https://github.com/FEDE0D/godot-subtitles/) 必看

- Godot_v3.2 正常运行

[New Animation Editor](https://github.com/godotengine/godot-proposals/issues/3950)

[Icon-Animations](https://github.com/univeous/Icon-Animations)

[interactive-book-godot 动态书籍翻页](https://github.com/miskatonicstudio/interactive-book-godot)



## animation

动画就是按指定的很多时间点去修改 node 的属性

```
# 成功播放动画
extends Control

# Called when the node enters the scene tree for the first time.
func _ready():
	
	var animation_player = AnimationPlayer.new()
	
	self.add_child(animation_player)
	
	var lib = AnimationLibrary.new()
	

	var label = Label.new() # This should be either a Label or a RichTextLabel node in your scene.
	self.add_child(label)
	
	# var character_speech_player = AudiostreamPlayer.new()

	var data = { "TextPath" : "res://text_file_format_example.txt", "Label": label}
	var animation = Captions.create(data)
	
	animation_player.add_animation_library("", lib)
	
	animation_player.get_animation_library("").add_animation("animation_name_here", animation)
	
	animation_player.play("animation_name_here") # Play the subtitles animation.
```



```
func map_to_animation(file_content: Array) -> Animation:
	var animation = Animation.new()
	var track_idx = animation.add_track(Animation.TYPE_VALUE, 0)
	var animation_length = file_content[file_content.size() - 1].times.to
#	var track_path = "LiveCaption:bbcode_text" #get_label_animation_path()
	var track_path = "LiveCaption:bbcode_text"
	
	animation.track_set_path(track_idx, track_path)
	animation.value_track_set_update_mode(track_idx, Animation.UPDATE_DISCRETE)
	animation.step = animation_step
	animation.length = animation_length
	
	animation.track_insert_key(track_idx, 0.0, "", 0)
	for line in file_content:
		animation.track_insert_key(track_idx, line.times.from, line.caption, 0)
		animation.track_insert_key(track_idx, line.times.to, "", 0)
	
	return animation
```



### switch animation

```
func _on_OptionButton_item_selected(index):
	var animation_name = "subtitles-eng" if index == 0 else "subtitles-es"
	var position = $AnimationPlayer.current_animation_position
	$AnimationPlayer.play(animation_name)
	$AnimationPlayer.seek(position, true)
```



### 打字机效果是计算每个字的时间

```
func generate_animation_WORDS(data, caption_fields):
	var animation = Animation.new()
	var track_index = animation.add_track(Animation.TYPE_VALUE)
	var nodePath = NodePath(data["Label"].owner.get_path_to(data["Label"]))
	animation.value_track_set_update_mode(track_index, Animation.UPDATE_DISCRETE)
	animation.track_set_path(track_index, nodePath.get_concatenated_names() + ":text")
	var last_field = caption_fields[caption_fields.size() - 1]
	caption_fields.remove_at(caption_fields.size() - 1)
	var written = ""
	for caption in caption_fields:
		var text = caption["text"] # The text being displayed.
		var start = caption["start"] # The starting keyframe in seconds.
		var end = caption["end"] # The ending keyframe in seconds.
		if text.find(" ") != -1: # Check for whitespaces.
			var words = text.split(" ") # Get every word.
			var midpoint = end - start
			var WPS = midpoint / words.size()
			var wordFrequency = WPS
			var currentTime = start
			for word in words:
				currentTime += wordFrequency
				written += word + " "
				animation.track_insert_key(track_index, currentTime, written)
		else: # Return the single word.
			written += text + " "
			animation.track_insert_key(track_index, end, written)

	var text = last_field["text"]
	written += " "
	
	var duration
	
	if "Duration" in data: # Check whether a custom duration was provided.
		duration = data["Duration"]
	else:
		duration = last_field["end"]

	if text.find(" ") != -1:
		var start = last_field["start"]
		var end = duration
		var words = text.split(" ") # Get every word.
		var midpoint = end - start
		var WPS = midpoint / words.size()
		var wordFrequency = WPS
		var currentTime = start
		for word in words:
			currentTime += wordFrequency
			written += word + " "
			animation.track_insert_key(track_index, currentTime, written)
	else:
		animation.track_insert_key(track_index, duration, written)
	
	animation.length = duration
	
	var animPlayer
	
	if "AnimationPlayer" in data and "Name" in data: # Adds the named animation to the provded animation player.
		animPlayer = data["AnimationPlayer"]
		animPlayer.get_animation_library("").add_animation(data["Name"], animation)
		return true
	else: # Returns the animation.
		return animation
```



### RichTextLabel 选中文本

```
# 先把 Text Selection -> selection enabled 开启
# Styles -> Focus -> StyleBoxEmpty 
    实现 RichTextLabel 选中文字时也不显示窗体边框

extends RichTextLabel

var sel_from = -1
var sel_to = -1

func _process(delta):
	var from = get_selection_from()
	var to = get_selection_to()
	
	if (from != sel_from || to != sel_to):
		sel_from = from
		sel_to = to
		
		var sel = get_selected_text()
		print("SELECTION CHANGED: (%d):(%d) '%s'" % [from, to, sel])
```



### 修改指定帧的动画

```
	animation.track_insert_key(track_idx, 0.0, "a", 0)
	var k = animation.track_find_key(track_idx, 0.0, Animation.FIND_MODE_NEAREST)
	var v = animation.track_get_key_value(track_idx, k)
	animation.track_set_key_value(track_idx, k, "[center]All Begin here[/center]")
```



## spine

[does-spine-work-with-godot](https://zh.esotericsoftware.com/forum/d/17065-does-spine-work-with-godot)

[spine-godot 官方插件](https://github.com/EsotericSoftware/spine-runtimes/tree/4.2-beta/spine-godot)

[melonjs for spine 官方插件 页游](https://github.com/melonjs/spine-plugin)

[通过SPINE命令行简化工作](https://zhuanlan.zhihu.com/p/420705994)

[基于Spine动画的AVATAR换装系统优化](https://zhuanlan.zhihu.com/p/445125141)

```
Note: This is about 2d rigged animations

I can say that I went crazy with this very question last week. Let me share with you the ideas that I have come to as a result of my research.

The result I got is this:

-If you want quality, fast, useful artistic features like Mesh deform, I couldn't find a better alternative than Spine. The price is expensive, but there is also a linux version. (They promised official support for Godot in the next release) Spine is worth using as an external tool if you really need it.

Other than that, I couldn't find any reason to use external tools like dragonebones (by the way dragonebones is not open source, just free), spriter, blender COA tools.

Godot's built-in animation system isn't bad for simple cut-out animations. Tween animations are great in my opinion. Mesh deform features are limited and insufficient. I will stick to Godot. I don't like putting different software in my workflow unnecessarily.
```





## moho导入

[godot_moho_importer](https://github.com/jpdurigan/godot_moho_importer)

### fbx export

```
I think you are talking about Moho's fbx export option right? I haven't tried that, I export png image sequences because I like to use all the animation features, not only the fbx compatible ones.
```





### demo cat-a-combs

[cat-a-combs](https://github.com/jpdurigan/cat-a-combs)



### day r survival



### Doaxvv

[图鉴](https://github.com/doaxcc/doaxvv_bromide)

[show model](https://github.com/alloystorm/dvvr/issues/151)

[mod](https://www.loverslab.com/topic/165186-doaxvv-mods-by-teddy-steam-centered/)

[干货](https://home.gamer.com.tw/creationDetail.php?sn=4354202)

[遍历进程](https://github.com/dbshch/DOAXVV-script)



新情爱味汉化组的，目前专门汉化nlp+



# ffmpeg

[查看媒体文件头信息工具ffprobe ](https://www.cnblogs.com/renhui/p/9209664.html)

[C# Named Pipe FFmpeg x265](https://gist.github.com/Anime4000/9dffab62e31b9d8dd815f0803eb5cbd3)

[OBS Studio + GitAction](https://github.com/hydrotho/OBSFX/blob/main/README_zh.md)

```
# 以 json 格式输出每个流的信息
ffprobe -print_format json  -show_streams pm.mp4 
```



```

# ffmpeg extract the second stream to nodejs buffer stream

const { spawn } = require('child_process');

const cmd = spawn('ffmpeg', [
  '-i', 'input_video.mp4',
  '-map', '0:1',
  '-c', 'copy',
  '-f', 'mp4',
  'pipe:1'
]);

let output = Buffer.from('');

cmd.stdout.on('data', (chunk) => {
  output = Buffer.concat([output, chunk]);
});

cmd.on('close', (code) => {
  if (code === 0) {
    console.log('Extraction succeeded.');
    // do something with the output buffer stream
  } else {
    console.error(`Extraction failed with code ${code}.`);
  }
});

```



## ffmpeg named pipe with a buffer

```


ffmpeg -hide_banner -v error -i  -strict -1 -map 0:0 -f rawvideo -pix_fmt yuv420p -y \\.\pipe\some_pipe_in

x265-08 \\.\pipe\some_pipe --preset fast --tune psnr --crf 23.5 --input-res 1920x1080 --fps 24 --output-depth 8 -o test.mp4

ffplay -f rawvideo -pixel_format bgr24 -video_size 1280x720 -vf "transpose=2,transpose=2" -i \\.\pipe\VirtualVideoPipe | ffplay -f s32le -channels 1 -sample_rate 44100 -i \\.\pipe\VirtualAudioPipe


Program_PipeInOut.cs
using System;
using System.IO;
using System.IO.Pipes;
using System.Diagnostics;

namespace NamedPipeTest
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                using (var server_tx = new NamedPipeServerStream("some_pipe", PipeDirection.Out, 1, PipeTransmissionMode.Byte))
                {
                    Console.Error.WriteLine("TX Pipe is Waiting...");
                    server_tx.WaitForConnection();
                    Console.Error.WriteLine("TX Pipe Started!");

                    using (var server_rx = new NamedPipeServerStream("some_pipe_in", PipeDirection.In, 1, PipeTransmissionMode.Byte))
                    {
                        Console.Error.WriteLine("RX Pipe is Waiting...");
                        server_rx.WaitForConnection();
                        Console.Error.WriteLine("RX Pipe Started!");

                        CopyStream(server_rx, server_tx);
                    }
                }
            }
        }

        public static void CopyStream(Stream input, Stream output)
        {
            int read;
            byte[] buffer = new byte[0x1000];
            while ((read = input.Read(buffer, 0, buffer.Length)) > 0)
            {
                output.Write(buffer, 0, read);
            }
        }
    }
}

using System;
using System.IO;
using System.IO.Pipes;
using System.Diagnostics;

namespace NamedPipeTest
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                using (var server = new NamedPipeServerStream("some_pipe", PipeDirection.InOut, 1, PipeTransmissionMode.Byte))
                {
                    Console.Error.WriteLine("Waiting...");
                    server.WaitForConnection();
                    Console.Error.WriteLine("Started!");

                    var psi = new ProcessStartInfo()
                    {
                        FileName = "ffmpeg",
                        Arguments = "-hide_banner -v error -i \"D:\\Users\\Anime4000\\Videos\\Unboxing.mp4\" -strict -1 -map 0:0 -f rawvideo -pix_fmt yuv420p -y -",
                        UseShellExecute = false,
                        CreateNoWindow = true,
                        RedirectStandardOutput = true,
                        RedirectStandardError = true,
                    };

                    using (var process = new Process { StartInfo = psi })
                    {
                        process.Start();
                        process.StandardOutput.BaseStream.CopyTo(server);
                        //process.StandardError.BaseStream.CopyTo(server);
                        process.WaitForExit();
                    }

                }
            }
        }
    }
}

```



### 内存流

[node-memorystream](https://github.com/JSBizon/node-memorystream)



```nodejs
(async () => {
    let { execa } = await import('execa')
    let MemoryStream = require('memorystream')
    let memStream = new MemoryStream(null, {
        readable : false
    })
    //console.log(memStream.toString())
    let vdpath = `E:\\1.mkv`
    let nth = 1
    let type = 'mp3'
    try {

        let cmd = `ffmpeg -i "${vdpath}" -y -map 0:${nth} -ss 00:01:00 -to 00:02:00 -f ${type} pipe:1`  // write stdout

        let childProcess = execa(cmd, { shell: true, 'encoding': 'utf8' })
        childProcess.stdout.pipe(memStream)
        //childProcess.stdout.pipe(process.stdout)  // don't print to screen
        let { stdout } = await childProcess
        let buffer = Buffer.concat(memStream['queue'])  // array of buffer, to one buffer

        require('fs').writeFileSync(__dirname + '/1.mp3', buffer, 'binary')

        memStream.destroy()

        return { srt: stdout, msg: '' }

    } catch (err) {
        return { srt: null, msg: err }
    }
})()
```



```
(async () => {
    let { execa } = await import('execa')
    let MemoryStream = require('memorystream')
    let memStream = new MemoryStream(null, {
        readable : false
    })
    //console.log(memStream.toString())
    let vdpath = `E:\\1.mkv`
    let nth = 1
    let type = 'mp3'
    try {

        let cmd = `ffmpeg -i "${vdpath}" -y -map 0:${nth} -ss 00:01:00 -to 00:02:00 -f ${type} pipe:1`  // write stdout

        let childProcess = execa(cmd, { shell: true, 'encoding': 'utf8' })
        childProcess.stdout.pipe(memStream)
        //childProcess.stdout.pipe(process.stdout)  // don't print to screen
        let { stdout } = await childProcess
        let buffer = Buffer.concat(memStream['queue'])  // array of buffer, to one buffer

        require('fs').writeFileSync(__dirname + '/1.mp3', buffer, 'binary')

        memStream.destroy()

        return { srt: stdout, msg: '' }

    } catch (err) {
        return { srt: null, msg: err }
    }
})()(async () => {
    let { execa } = await import('execa')
    let MemoryStream = require('memorystream')
    let memStream = new MemoryStream(null, {
        readable : false
    })
    //console.log(memStream.toString())
    let vdpath = `E:\\1.mkv`
    let nth = 1
    let type = 'mp3'
    try {

        let cmd = `ffmpeg -i "${vdpath}" -y -map 0:${nth} -ss 00:01:00 -to 00:02:00 -f ${type} pipe:1`  // write stdout

        let childProcess = execa(cmd, { shell: true, 'encoding': 'utf8' })
        childProcess.stdout.pipe(memStream)
        //childProcess.stdout.pipe(process.stdout)  // don't print to screen
        let { stdout } = await childProcess
        let buffer = Buffer.concat(memStream['queue'])  // array of buffer, to one buffer

        require('fs').writeFileSync(__dirname + '/1.mp3', buffer, 'binary')

        memStream.destroy()

        return { srt: stdout, msg: '' }

    } catch (err) {
        return { srt: null, msg: err }
    }
})()
```



```
var http = require('http'),
	MemoryStream = require('memorystream');

var options = {
	host: 'google.com'
};
var memStream = new MemoryStream(null, {
	readable : false
});

var req = http.get(options, function(res) {
	res.pipe(memStream);
	res.on('end', function() {
		console.log(memStream.toString());
	});
});
```





### create zip

[node-archiver](https://github.com/archiverjs/node-archiver)

```
npm install archiver --save

// require modules
const fs = require('fs');
const archiver = require('archiver');

// create a file to stream archive data to.
const output = fs.createWriteStream(__dirname + '/example.zip');
const archive = archiver('zip', {
  zlib: { level: 9 } // Sets the compression level.
});

// listen for all archive data to be written
// 'close' event is fired only when a file descriptor is involved
output.on('close', function() {
  console.log(archive.pointer() + ' total bytes');
  console.log('archiver has been finalized and the output file descriptor has closed.');
});

// This event is fired when the data source is drained no matter what was the data source.
// It is not part of this library but rather from the NodeJS Stream API.
// @see: https://nodejs.org/api/stream.html#stream_event_end
output.on('end', function() {
  console.log('Data has been drained');
});

// good practice to catch warnings (ie stat failures and other non-blocking errors)
archive.on('warning', function(err) {
  if (err.code === 'ENOENT') {
    // log warning
  } else {
    // throw error
    throw err;
  }
});

// good practice to catch this error explicitly
archive.on('error', function(err) {
  throw err;
});

// pipe archive data to the file
archive.pipe(output);

// append a file from stream
const file1 = __dirname + '/file1.txt';
archive.append(fs.createReadStream(file1), { name: 'file1.txt' });

// append a file from string
archive.append('string cheese!', { name: 'file2.txt' });

// append a file from buffer
const buffer3 = Buffer.from('buff it!');
archive.append(buffer3, { name: 'file3.txt' });

// append a file
archive.file('file1.txt', { name: 'file4.txt' });

// append files from a sub-directory and naming it `new-subdir` within the archive
archive.directory('subdir/', 'new-subdir');

// append files from a sub-directory, putting its contents at the root of archive
archive.directory('subdir/', false);

// append files from a glob pattern
archive.glob('file*.txt', {cwd:__dirname});

// finalize the archive (ie we are done appending files but streams have to finish yet)
// 'close', 'end' or 'finish' may be fired right after calling this method so register to them beforehand
archive.finalize();
```



### download zip

```
var app = require('express')();
var archiver = require('archiver');
var p = require('path');

app.get('/', function(req, res) {

  var archive = archiver('zip');

  archive.on('error', function(err) {
    res.status(500).send({error: err.message});
  });

  //on stream closed we can end the request
  archive.on('end', function() {
    console.log('Archive wrote %d bytes', archive.pointer());
  });

  //set the archive name
  res.attachment('archive-name.zip');

  //this is the streaming magic
  archive.pipe(res);

  var files = [__dirname + '/fixtures/file1.txt', __dirname + '/fixtures/file2.txt'];

  for(var i in files) {
    archive.file(files[i], { name: p.basename(files[i]) });
  }

  var directories = [__dirname + '/fixtures/somedir']

  for(var i in directories) {
    archive.directory(directories[i], directories[i].replace(__dirname + '/fixtures', ''));
  }

  archive.finalize();

});

app.listen(3000);
```



### 高端 json 流

[stream-json](https://github.com/uhop/stream-json)



### nodejs不解压读取文件

[nodejjs不解压读取文件](https://www.jianshu.com/p/74fc8e90eab0)





## ffmpeg.wasm

[ffmpeg.wasm](https://github.com/ffmpegwasm/ffmpeg.wasm)



## godot video stream

[godot ogv](https://github.com/godotengine/godot/issues/72976)

[AnimationPlayer](https://github.com/godotengine/godot/issues/72588)

> ```
> AnimationPlayer
> AudioStreamPlayer
> ```

[Godot 4: How to play a video from YouTube](https://www.reddit.com/r/godot/comments/117h6jg/godot_4_how_to_play_a_video_from_youtube/)

[godot-yt-dlp](https://github.com/Nolkaloid/godot-yt-dlp) 下载 yt video

```
if not YtDlp.is_setup():
    YtDlp.setup()
await YtDlp.setup_completed

var download := YtDlp.download("https://youtu.be/Ya5Fv6VTLYM") \
        .set_destination("user://audio/") \
        .set_file_name("ok_computer") \
        .convert_to_audio(YtDlp.Audio.MP3) \
        .start()

await download.download_completed

var stream = AudioStreamMP3.new()
var audio_file = FileAccess.open("user://audio/ok_computer.mp3", FileAccess.READ)

stream.data = audio_file.get_buffer(audio_file.get_length())
audio_file.close()

$AudioStreamPlayer.stream = stream
$AudioStreamPlayer.play()
```



[FFMpeg streaming frames to Godot Textures through GDNative](https://www.reddit.com/r/godot/comments/siwxhg/ffmpeg_streaming_frames_to_godot_textures_through/) [gist](https://gist.github.com/netshade/867cef0c749ebb5624d9e0a0d1ff59f6)

[ogv.js让iPhone支持webM视频解析播放](https://www.zhangxinxu.com/wordpress/2021/07/ogv-js-android-webm-video/comment-page-1/)

[以20像素为基准的CSS网页布局实践分享](https://www.zhangxinxu.com/wordpress/2016/03/css-layout-base-20px/)

[GDQuest](https://github.com/GDQuest)

[cozodb图数据库](https://docs.cozodb.org/zh_CN/latest/index.html)



```
resizes a video to be 720 pixels tall (720p), while preserving its existing aspect ratio. This helps decrease the file size significantly if the source is recorded at a higher resolution than 720p:

ffmpeg -i input.mp4 -vf "scale=-1:720" -q:v 6 -q:a 6 output.ogv

```





# gitlab

[Git 管理实战（五）：二进制大文件的版本控制](http://www.uml.org.cn/pzgl/201901233.asp)





# chatGPT



```
1.新账号有并发量限制
如果你是新账号，你会发现你有 18 刀的免费余额，但是如果你没有绑定信用卡，那么 chatgpt api 的并发量控制在每分钟 20 次请求，所以一分钟内调用 chatgpt api 超过 20 次，你问它问题只会回答你 rate limit 、要你绑定信用卡之类的消息了。

如何解除 rate limit 限制？？？只能绑定信用卡，在绑定了信用卡的 48 小时内并发量会提升到每分钟 60 次，绑定了信用卡 48 小时后候则是每分钟 3500 次。

2.他收费是把上下文的 token 都算上去的
chatgpt api 的收费标准0.002 美刀 /1000token，看起来很便宜是吧，你开发 chatgpt ai 的时候，如果请求参数没加上 parentMessageId 的参数，那他就不会有上下文功能，相当于是一问一答，那收费的确便宜。

如果你想实现上下文，请求的时候就必须把 parentMessageId 的参数加上去，然后你每次提问问题的时候，他都会把之前的上下文纪录都一起累积提交过去，这些也是要算钱的，导致你每一次问问题，越往后消耗的 token 量越恐怖，特别是喜欢让 chatgpt 生成 1000 字论文的那种。

而且上下文容量是有限制的，如果你聊天纪录过长，总 token 超过大概几万个的时候，open ai 只会回复你 token 太长的错误，要你清空 token 。

道德标准都这么高吗?起码我知道之前还有 3.5api 刚开放的时候,有些大厂拿 18 美金的账号在做蒸馏训练,这就不承认啦?

```



```
可以看看 Wise 官网 ( https://wise.com/invite/u/cheng140)，链接带推广，虽然也没啥鸟用。wise 是英国上市公司，正规的银行。但是有一定的注册门槛。

新手注册 Wise 图文教程
所需材料：
本人有效护照（身份证不行）
国外手机号（+86 也可以，不建议）
1 个护照仅能注册 1 个 wise ，多开必 ban

1 、Wise 官网 ( https://wise.com/invite/u/cheng140) 点击注册、不限制 IP
2 、输入邮箱，不建议 QQ 邮箱
3 、创建个人账户
4 、选择居住国，（建议英、加拿大、新加坡、马来西亚）
5 、绑定电话号码（不建议+86 ，可 GV ）
6 、创建强密码
7 、开设账户，已完成 50%
8 、输入护照信息和居住地址信息（居住地址决定哪个地区的 wise ）
9 、首次入金激活 wise


入金激活有一定的门槛，切记要同名入金激活。怕麻烦可以小黄鱼找代激活的。
```



```
获取一个美国的个人税号，如果你在油管有有收益很快就能获得，然后就可以申请办理美国信用卡
```



```
快捷指令，直接填入 api 即可
快捷指令传送门： https://www.icloud.com/shortcuts/345252df9bc14dfbb1f63577375470e7
整个过程 30s 不到 hh
```



## nobepay

```
nobepay.com
173xxxx3
sply@gmail.com

您可以点击左侧共享钱包管理并按照流程进行开通，开通后可一次享受近20个共享额度卡段。
共享钱包有以下优点：
1、解决资金调度问题，资金调度更灵活，【所有卡片共享钱包余额】，并在消费时实时进行扣除；
2、多卡段支持，一经开通可直接【享受近20个共享卡段】，卡段陆续开放，目前开通可直接使用的有：553231、524897、559666、559292、556371、556150、553437、534786、531993、519075、441112、404038、553370；

```



[N26](https://www.kivinsae.com/2023/03/05/2023-03-05-N26/)



nobepay+卡段

派安盈



## POW工作量证明

https://linux.do/t/topic/61556

```

# OpenAI-Sentinel-Proof-Token

async _getAnswer(e)
{
    var t,
        n;
    if (!(null != e && null !== (t = e.proofofwork) && void 0 !== t && t.required))
        return null;
    let {seed: a, difficulty: r} = e.proofofwork;
    return "string" == typeof a && "string" == typeof r ? "gAAAAAB" + (null !== (n = this.answers.get(a)) && void 0 !== n ? n : await this._generateAnswer(a, r)) : null
}
async _generateAnswer(e, t)
{
    let n = "e";
    try {
        let n = null,
            a = this.getConfig();
        for (let s = 0; s < this.maxAttempts; s++) {
            (!n || 0 >= n.timeRemaining()) && (n = await new Promise(e => {
                (window.requestIdleCallback || function(e) {
                    return setTimeout(() => {
                        e({
                            timeRemaining: () => 1,
                            didTimeout: !1
                        })
                    }, 0), 0
                })(t => {
                    e(t)
                })
            })),
            a[3] = s;
            let o = i(a);
            if ((await (0, r.ki)(e + o)).substring(0, t.length) <= t)
                return this.answers.set(e, o), o
        }
    } catch (e) {
        n = i("" + e)
    }
    return "wQ8Lk5FbGpA2NcR9dShT6gYjU7VxZ4D" + n
}
getConfig()
{
    var e,
        t,
        n,
        a,
        r;
    return [(null === (e = navigator) || void 0 === e ? void 0 : e.hardwareConcurrency) + (null === (t = screen) || void 0 === t ? void 0 : t.width) + (null === (n = screen) || void 0 === n ? void 0 : n.height), "" + new Date, null === (a = performance) || void 0 === a || null === (a = a.memory) || void 0 === a ? void 0 : a.jsHeapSizeLimit, null == Math ? void 0 : Math.random(), null === (r = navigator) || void 0 === r ? void 0 : r.userAgent]
}

function i(e) {
	return (e = JSON.stringify(e), window.TextEncoder) ? btoa(String.fromCharCode(...new TextEncoder().encode(e))) : btoa(unescape(encodeURIComponent(e)))
}

接下来取 seed 和 difficulty 参数去碰撞。最后拿碰撞的答案 gAAAAAB + base64(answer)

answer 生成在 _generateAnswer 中，简单来说就是用 getConfig() 生成字符串，大概是：

[1850,"Fri Apr 19 2024 11:51:38 GMT+0800 (中国标准时间)",null,46,"<user agent>"]

这种，具体看js代码。比如第一个参数就是 navigator.hardwareConcurrency+screen.width+screen.height

然后拿这个字符串base64之后，在前面放seed，形成如：0.2616356464867712WzE4MDMsIkZyaSBBcHxxxx 这样的字符串。

重点来了，这个js里隐藏了hash算法，跟进去也是wasm的，但其实hash算法是 SHA3-512。

算出来hash截取 difficulty 的长度来跟 difficulty 比较即可。符合就返回这个 base64 的字符串，跟 gAAAAAB 拼接成最终 OpenAI-Sentinel-Proof-Token。否则就重复这个过程。

最终撞不撞的到，看 getConfig() 里的 Math.random() 灵不灵了。最多撞 this.maxAttempts 也就是 10w 次。

```





## prompts

[日语提示66的](https://github.com/f/awesome-chatgpt-prompts)

<img src="nodejs summary.assets/image-20230419113115514.png" alt="image-20230419113115514" style="zoom: 50%;" />

```
    prompt = f"请为以下内容生成一个简短的摘要：\n{text}\n摘要："
    response = openai.Completion.create(
    
    prompt = f"请用五个关键词描述以下文本：\n{text}\n关键词："
```





## api

[详细文档](https://platform.openai.com/docs/api-reference/introduction)

```
(async () => {
    // npm install openai
    // https://github.com/openai/openai-node
    // https://github.com/openai/openai-node/issues/18#issuecomment-1369996933  // 流式输出

    let userMsg =  "翻译成英语：豆浆应该加糖还是加盐"
    
    let api_key = ""

    const { Configuration, OpenAIApi } = require("openai")

    const configuration = new Configuration({
        apiKey: api_key,
    })
    const openai = new OpenAIApi(configuration)
    try {
        const completion = await openai.createChatCompletion({
            model: "gpt-3.5-turbo",
            messages: [{role: "user", content: userMsg}],
        })
        console.log(completion.data.choices[0].message.content)
    } catch (error) {
        if (error.response) {
            console.log(error.response.status);
            console.log(error.response.data);
        } else {
            console.log(error.message);
        }
    }
})()
```



```

"""
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "text=翻译成英语：豆浆应该加糖还是加盐" http://127.0.0.1:505/ai/chatgpt
"""
import openai
# Set up OpenAI API key
api_key = ""
openai.api_key = api_key

def send_message(message_log):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
        # The conversation history up to this point, as a list of dictionaries
        messages=message_log,
        # The maximum number of tokens (words or subwords) in the generated response
        max_tokens=3800,
        # The stopping sequence for the generated response, if any (not used here)
        stop=None,
        # The "creativity" of the generated response (higher temperature = more creative)
        temperature=0.7,
    )

    # Find the first response from the chatbot that has text in it (some responses may not have text)
    for choice in response.choices:
        if "text" in choice:
            return choice.text

    # If no response with text is found, return the first response's content (which may be empty)
    return response.choices[0].message.content


if __name__ == "__main__":

    user_input = '翻译成英语：豆浆应该加糖还是加盐'

    message_log = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input[0:1024]}
    ]
    
    response = send_message(message_log)
    print(f"You: {user_input}")
    print(f"AI assistant: {response}")
```



### fake api

[fake api](https://github.com/xqdoo00o/ChatGPT-to-API)



```

git clone -b gpt4-enabled https://github.com/acheong08/ChatGPT-to-API.git
	# 支持 gpt4 的分支

dnf makecache --refresh && \
dnf -y install golang
	# dnf remove golang

cd /root/ChatGPT-to-API/tools/authenticator && \
touch access_tokens.txt authenticated_accounts.txt

vi access_tokens.txt
	# email:password
		# 填 openai 的账号和密码

vscode 直接运行 main.go
	# 生成 access_tokens.txt
	
cat access_tokens.txt
	# 输出一串长长的 tokens
	
cd /root/ChatGPT-to-API
vi access_tokens.json
	[ "这里填刚才输出的长长tokens" ]


注意：google 账号登录的话，没办法用 openai 账号密码登录
1. 先正常登录 chat.openai.com
2. 能聊天以后访问这个地址： https://chat.openai.com/api/auth/session
3. 把 accessToken 复制出来，
4. cd /root/ChatGPT-to-API
	vi access_tokens.json
		[ "这里填刚才的 accessToken" ]

./freechatgpt
	# 启动服务



# 访问接口
  curl 127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer no need key" \
  -d '{
    "model": "text-davinci-003",
    "prompt": "Say this is a test",
    "max_tokens": 7,
    "temperature": 0
  }'

# GPT4 接口
  curl 127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer " \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "你会说中文吗"}]
  }'


# nginx 转发，远程访问成功
curl echodict.com:8880/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer " \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "你会说中文吗"}]
  }'
  
  gpt-3.5-turbo
  gpt-4
  
http://et.com:2082/
	# 前端	
	
pm2 --name "chatgpt4_browser_8080" start "./freechatgpt"

```







```

vscode 安装 go 插件，断点调试 go 很方便


go.dev  # install go on windows


dnf makecache --refresh && \
dnf -y install golang
	# dnf remove golang

git clone https://github.com/acheong08/ChatGPT-to-API.git && \
cd ChatGPT-to-API && \
go build



cd /root/ChatGPT-to-API/tools/authenticator && \
touch access_tokens.txt authenticated_accounts.txt

vi access_tokens.txt
	# email:password
		# 填 openai 的账号和密码

vscode 直接运行 main.go
	# 生成 access_tokens.txt
	
cat access_tokens.txt
	# 输出一串长长的 tokens
	
cd /root/ChatGPT-to-API
vi access_tokens.json
	[ "这里填刚才输出的长长tokens" ]

./freechatgpt
	# 启动服务


# 访问接口
  curl 127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer no need key" \
  -d '{
    "model": "text-davinci-003",
    "prompt": "Say this is a test",
    "max_tokens": 7,
    "temperature": 0
  }'



```



```
curl https://api.openai.com/v1/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "text-davinci-003",
    "prompt": "Say this is a test",
    "max_tokens": 7,
    "temperature": 0
  }'
  
  
  curl 127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer no need key" \
  -d '{
    "model": "text-davinci-003",
    "prompt": "Say this is a test",
    "max_tokens": 7,
    "temperature": 0
  }'
  
```



### chatgpt-clone

[chatgpt-clone](https://github.com/xtekky/chatgpt-clone)



### pandora 必看

[账号登录方法](https://gist.github.com/pengzhile/448bfcfd548b3ae4e665a84cc86c4694)

```
  代码在 pandora\src\pandora\openai\auth.py
  if __name__ == '__main__':
    tokon = Auth0('echoplayorg@gmail.com', '1q2w!Q@W', None).auth(True)
      # 这样用 Your version of the ChatGPT app is out of date
      # 出错了，等他解决问题再看
```

[pandora](https://github.com/pengzhile/pandora/blob/master/doc/wiki.md)

[api 接口定义](https://github.com/pengzhile/pandora/blob/master/doc/HTTP-API.md)

[另一个GO API](https://github.com/linweiyuan/go-chatgpt-api)

[nginx 反代替换 pandora api调用到 go-chatgpt-api](https://www.v2ex.com/t/947707)

- [go-chatgpt](https://github.com/linweiyuan/go-chatgpt)

- [纯js实现](https://github.com/PawanOsman/ChatGPT)

[nodejs前后端备用](https://github.com/zhpd/chatgpt-plus)

[chatbox 前端仿得像](https://github.com/Bin-Huang/chatbox)

```

et.com:2086
	# 输入 token 能正常访问 

pandora --tokens_file "C:/Users/Administrator/tokens.json"

git clone https://github.com/pengzhile/pandora.git && \
cd pandora && \
pip3.9 install . && \
pip3.9 install '.[api]' && \
pip3.9 install '.[cloud]'

pandora-cloud 
	# 运行

pandora.cloud_launcher:run
/root/pandora/src/pandora/cloud_launcher.py
	# 入口点是这个


改默认端口和监听 ip
/root/pandora/src/pandora/cloud_launcher.py
	default='127.0.0.1:8018'
	default='0.0.0.0:2086'
		# 改成这个


pandora\build\lib\pandora\bots\server.py
    __default_ip = '0.0.0.0'
    __default_port = 2086

新建一个入口点, vscode 运行
# pandora\main.py
import src.pandora.cloud_launcher as cloud_launcher

if __name__ == "__main__":
	#sys.argv.append( '--tokens_file' )
    #sys.argv.append( '1' )
    cloud_launcher.run()

```

可通过 pandora --help 查看。
-p 或 --proxy 指定代理，格式：protocol://user:pass@ip:port。
-t 或 --token_file 指定一个存放Access Token的文件，使用Access Token登录。
-s 或 --server 以http服务方式启动，格式：ip:port。
-a 或 --api 使用gpt-3.5-turboAPI请求，你可能需要向OpenAI支付费用。
--tokens_file 指定一个存放多Access Token的文件，内容为{"key": "token"}的形式。
--threads 指定服务启动的线程数，默认为 8，Cloud模式为 4。
--sentry 启用sentry框架来发送错误报告供作者查错，敏感信息不会被发送。
-v 或 --verbose 显示调试信息，且出错时打印异常堆栈信息，供查错使用。



- 也可以官方登录，然后访问 [这里](http://chat.openai.com/api/auth/session) 拿 `Access Token`



#### 代码结构

```
# 对源有代码作了移动，不再依赖外部包
pandora\main.py
from src.pandora_cloud.server import ChatBot as CloudServer
if __name__ == "__main__":
    #sys.argv.append( '--tokens_file' )
    #sys.argv.append( 'D:/Github/echodict/pandora/tokens.json' )
    CloudServer(proxy=None, debug=False, sentry=False, login_local=True, CHATGPT_API_PREFIX="https://ai.fakeopen.com").run(bind_str="0.0.0.0:80", threads=8)
  

pandora\src\pandora_cloud\server.py
	chat(self, conversation_id=None):
		# 入口点在这
		__get_userinfo():
			# 通过 accessToken 拿到用户ID和email
		
		
		
		
		
		
		
		
		
		
		
		
		
		
# 拿历史聊天记录列表等
			
```



#### pgvector 存储openai embeddings

[pgvector 存储openai embeddings](https://supabase.com/blog/openai-embeddings-postgres-vector)



### whisperX 

[whisperX 字级的时间戳](https://github.com/m-bain/whisperX)



## finetune api

[fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)

[详细过程](https://juejin.cn/post/7218001191703068729)

[GPT-3: Fine-Tuning for Superhero Descriptions 结果更清晰](https://towardsdatascience.com/unleashing-the-power-of-gpt-how-to-fine-tune-your-model-da35c90766c4)

[如何使用OpenAI fine-tuning(微调)训练属于自己的专有模型？](https://www.zhihu.com/question/591066880/answer/2961747033)

[Prompt Tuning 相比于 Fine Tuning 在哪些场景下表现更好？](https://www.zhihu.com/question/504324484/answer/2962134008)

```
Prompt: 模仿以下示例的风格，写一篇关于中考是否会取消英语的分析
示例1：……
示例2：……
```



1. Prepare and upload training data
2. Train a new fine-tuned model
3. Use your fine-tuned model

```
pip install openai && \
pip install openai[datalib] && \
pip install --upgrade openai

export OPENAI_API_KEY="<OPENAI_API_KEY>"

openai tools fine_tunes.prepare_data -f QA.jsonl
	# 格式化数据
	# 生成 QA_prepared.jsonl
	
openai api fine_tunes.create -t 'QA.jsonl' -m davinci
{"prompt": "xxx "completion": "xxx"}
{"prompt": "xxx "completion": "xxx"}

测试微调好的模型：
openai api completions.create -m davinci:ft-personal-2023-04-06-08-48-39 -p  "为什么药物需要制成适合医疗或预防应用的形式？"

```



```
python 命令行
>>import openai
>>openai.FineTune.retrieve(id="ft-P32aMbdXrINtOPxsMa5XewOL")
	# 反复运行这一句就能取到最新的训练状态
```



```
600 * 1024 / 750 * 0.03 * 2 = 49.152 $
	# 600K 的文件大概是这么多钱

```



```
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="davinci:ft-personal-2023-04-17-01-29-32",
  prompt="一、呼吸系统的结构与功能/（一）呼吸道 ->\n",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["END"]
)

# 好像只有 Completion 可选， chat 那里不可以选 finetune 好的模型


curl https://api.openai.com/v1/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": YOUR_PROMPT, "model": FINE_TUNED_MODEL}'



```







[api](https://openai.com/blog/introducing-chatgpt-and-whisper-apis)

[完整的语音助手带录音](https://github.com/IanDublew/Virtual-Voice-Assisant/blob/main/gpt3%2Bwhisper%2Bgtts.py)

[提问案例 ](https://github.com/howl-anderson/unlocking-the-power-of-llms)

```
在上一次对话中我问了你这样一个问题:
xxx
你的回答是:
xxx
于是我又追问道:
xxx
而你给出的回答是:
xxx
···
```



[wechat](https://github.com/zhayujie/chatgpt-on-wechat)

[ChatGPT Telegram 机器人](https://v2ex.com/t/920842#reply96)

| ***\*#\** LLaMA** |      |                                                              |
| ----------------- | ---- | ------------------------------------------------------------ |
|                   |      |                                                              |
|                   |      | This repository is intended as a minimal, hackable and readable example to load [LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/) ([arXiv](https://arxiv.org/abs/2302.13971v1)) models and run inference. |
|                   |      | In order to download the checkpoints and tokenizer, fill this [google form](https://forms.gle/jk851eBVbX1m5TAv5) |
|                   |      | In order to download the checkpoints and tokenizer, fill this [google form](https://forms.gle/jk851eBVbX1m5TAv5) or if you want to save our bandwidth use this BitTorrent link: "[magnet:?xt=urn:btih:ZXXDAUWYLRUXXBHUYEMS6Q5CE5WA3LVA&dn=LLaMA](magnet:?xt=urn:btih:ZXXDAUWYLRUXXBHUYEMS6Q5CE5WA3LVA&dn=LLaMA)". |
|                   |      |                                                              |
|                   |      | ***\*###\** Setup**                                          |
|                   |      | In a conda env with pytorch / cuda available, run            |

30b 参数，四张卡就能跑。。

65b 八卡能耍咯。不嫌慢可以 CPU 跑。



```
分析日语的语法：レオナにしかできないことってそれだったんだ
这个句子可以分为以下几个部分：

レオナにしかできないこと (Leona ni shika dekinai koto) - 这是一个名词短语，意思是“只有蕾欧娜能做的事情”。

って (tte) - 这是一个简化的语法结构，相当于「と言っている」(to itteiru)，意思是“说”。

それ (sore) - 这是一个代词，指代前面提到的“只有蕾欧娜能做的事情”。

だった (datta) - 这是“だ”(da)的过去时态形式，用来表示过去的状态或情况。在这个句子中，它表示之前“只有蕾欧娜能做的事情”是“那个”。

んだ (nda) - 这是“のだ”(no da)的缩略形式，用来解释或强调先前提到的内容。在这个句子中，它强调之前提到的“只有蕾欧娜能做的事情是那个”。

因此，整个句子的意思是：“只有蕾欧娜能做的事情，就是那个（指代前面提到的某件事情）。”



しかできない 是什么语法
"しかできない"是一种日语的表达方式，其中“しか”是一个助词，用于强调某个事物是唯一的、不可替代的，而“できない”则表示“无法做到”或“不能做到”的意思。这个短语的字面意思是“只有……，不能做到……”。

因此，“しかできない”可以用来表达某个人或事物具有某种特殊能力或技能，其他人或事物无法替代或做到。在这个句子中，“レオナにしかできないこと”意思是“只有蕾欧娜能做的事情”。



そんなことぐらいしかできないからな 是什么语法
这句话中的语法结构是：

「そんなことぐらいしかできないからな。」

其中，“そんなことぐらい”表示“那种事情只有那种程度的”的意思，而“しかできない”表示“只能做那个程度”的意思。这两个部分连在一起就是“只能做那种程度的事情”。

因此，整个句子的意思是“因为只能做那种程度的事情，所以……”。这种句子结构中，“しか”表示“只有……”或“仅有……”，常常用于表示一种限制或局限性，同时也能够强调某种特殊性或独特性。


分析日语语法 お〜っと！ ここなら 女子更衣室が のぞけんな
这是一个包含以下成分的简短日语短语：

お〜っと！ここなら女子更衣室がのぞけんな

其中，每个成分的含义如下：

お〜っと！：表示惊讶或者意外，类似于英语中的 “Oops!” 或者 “Oh no!”
ここなら：表示地点，意思是“在这里的话”，这里指的是当前位置。
女子更衣室が：女子更衣室的主语。更衣室表示“更衣室”，女子表示“女子的”。
のぞけんな：否定命令形态，表示“不要偷看”或“不能偷看”。
因此，整个短语的意思是：“哎呀！如果你在这里的话，就不要偷看女子更衣室！”
```





分析日语词汇和语法：あのピカチュウのせいよね



Velo 可绑定
Coinbase Card （欧洲版）可绑定



其实你可以搞个博客，把对话记录全部记下来，然后让它去看你的博客，就能继承上下文了。



一定要美国卡才行，自己没有的话建议淘宝买一个简单一些，大猫二猫和三猫这家店



需要邀请的,我没邀请权限 你加这个官方微信号 nobe_ghost 自己去要,或者网上搜一个邀请号
需要国内微信 /支付宝实6174名认证
充值 500 起, 1%手续费, 1000 以上可以找客服充值 免手续费.
汇率涨了貌似,所以比我前面贴的贵了一点点, 但费用结构就如下,开卡费一次性
*费用明细：
开卡费: $1.00 + 充值: $40.00 + 服务费: $40.00 * 3.00%
= $42.20 * 7.0852
= ￥ 298.99



https://www.v2ex.com/t/920673#reply1 Chatgpt api 的 Siri shortcut



```
你好，下面我将给你提供一个词汇表，其中包含一些一些动词或名词，你需要理解并记住这些词，当我请你将一段话改写为互联网黑话的时候，你要尽可能多地在从下面词汇表中选择词汇对语句进行重写、扩写或缩写，从而让整段话显得更加专业凝练，注意，不要将下面词汇表的名词部分连续使用，不要改变句子原有的意思，但可以进行适当的扩展。

下面是我要提供的词汇表：

二字动词:

复盘，赋能，沉淀，倒逼，落地，串联，协同，反晡，兼容，包装，重组，履约，晌应，量化,发力，布局，联动，细分，梳理，输出，加速，共建，支撑，融合,聚合，集成，对齐，对标，对焦，抓手，拆解，拉通，抽象，摸索，提炼,打通，打透，吃透，迁移，分发，分层，分装，穿梭,辐射，围绕，复用，渗透，扩展，开拓。


二字名词:

漏斗，中台，闭环，打法，拉通，纽带，矩阵，刺激，规模，场景，聚焦，维度，格局，形态,生态，话术，体系,认知，玩法，体感，感知，调性，心智，战役，合力，心力。


三字名词:

颗粒度，感知度，方法论，组合拳，引爆点，点线面，精细化，差异化，平台化，结构化，影响力，耦合性，易用性，-致性,端到端，短平快。

```





```
如果一个人已经赚了一辈子都花不完的钱，为什么他还想要赚得更多？

你好，这是必应。这是一个很有意思的问题，可能没有一个确定的答案。不同的人可能有不同的动机和目标。根据一些网上的文章，有些可能的原因是：

社会比较：有钱人的朋友都是有钱人，他们可能会担心自己在圈子里不够优秀或者被落后12。他们可能会追求更高的社会地位或者更多的影响力3。
乐趣：有钱人可能享受赚钱的过程，比如投资、收购、创业等23。他们可能会把赚钱当作一种娱乐或者挑战，而不是一种负担2。
安全感：有钱人可能担心自己的财富会受到威胁，比如通货膨胀、税收、竞争等4。他们可能会想要储备更多的钱以防万一4。
慈善：有钱人可能想要用自己的钱来帮助别人，比如捐赠、慈善基金、公益项目等5。他们可能会认为自己有责任和义务来改善世界5。
当然，这些原因并不是互斥的，有钱人可能同时有多种动机。也有可能有些有钱人并不想要赚更多的钱，而是想要享受自己的生活。这可能取决于每个人的价值观和个性。
```

![image-20230311170337928](./nodejs summary.assets/image-20230311170337928.png)



## embeddings

[openai embeddings 各种宝藏](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)

[语义文本搜索](https://github.com/openai/openai-cookbook/blob/main/examples/Semantic_text_search_using_embeddings.ipynb)



### 问答和语义搜索

[问答和语义搜索](https://github.com/openai/openai-cookbook/tree/main/examples/vector_databases/pinecone)

[必看 问答实例](https://github.com/ruoccofabrizio/azure-open-ai-embeddings-qna)

> 书籍文本（目录+正文，多条） -> 文本向量
>
> 用户问题 -> 问题向量
>
> 比较向量相似度（语义级的相似度对比），找到最相关的书籍文本
>
> creating embeddings vectors from documents. For answering the question of a user, it retrieves the most relevant document and then uses GPT-3, GPT-3.5 or GPT-4 to extract the matching answer for the question.

[weaviate 图像向量搜索](https://weaviate.io/blog/how-to-build-an-image-search-application-with-weaviate)

[LangChain+ChatGLM-6B实现本地知识库自动问答](https://www.bilibili.com/video/BV1So4y1L7Hb/)

```
Github地址：
https://github.com/thomas-yanxin/LangChain-ChatGLM-Webui

ModelScope在线体验：
https://modelscope.cn/studios/AI-ModelScope/LangChain-ChatLLM/summary

OpenI地址：
https://openi.pcl.ac.cn/Learning-Develop-Union/LangChain-ChatGLM-Webui
```



#### chatPDF

[PDFChat](https://github.com/dotvignesh/PDFChat)

- [测试论文](https://arxiv.org/pdf/2304.01089.pdf)

[gpt4-pdf-chatbot-langchain nodejs版](https://github.com/mayooear/gpt4-pdf-chatbot-langchain)

> set the vector dimensions to 1536

[chatpdf 在线使用](https://www.chatpdf.com/)



```
# 正常输出了历史聊天记录后的内容

  // https://js.langchain.com/docs/modules/chains/index_related_chains/retrieval_qa
  // https://platform.openai.com/docs/guides/embeddings/what-are-embeddings

  /*

  ConversationChain
  
  curl https://api.openai.com/v1/embeddings \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
  "input": "Your text string goes here",
  "model": "text-embedding-ada-002"
}'
  
  */
  let { ChatOpenAI } = await import('langchain/chat_models/openai')
  let { HumanChatMessage, SystemChatMessage } = await import('langchain/schema')
  let { RetrievalQAChain, loadQAChain, loadQARefineChain, ConversationalRetrievalQAChain } = await import('langchain/chains')
  let { ChatMessageHistory } = await import('langchain/memory')

  let { HNSWLib } = await import('langchain/vectorstores/hnswlib')
  let { OpenAIEmbeddings } = await import('langchain/embeddings/openai')
  let { RecursiveCharacterTextSplitter } = await import('langchain/text_splitter')

  // let { ConversationalRetrievalChain } = await import('langchain/chains')

  // let { FAISS } = await import('langchain/vectorstores')


  test: {
    // let vectorStore = await HNSWLib.fromTexts(
    //   ["Hello world", "Bye bye", "hello nice world"],
    //   [{ id: 2 }, { id: 1 }, { id: 3 }],
    //   new OpenAIEmbeddings({
    //     openAIApiKey, 
    //     modelName:'text-embedding-ada-002',
    //     maxConcurrency: 1, timeout: 30000
    //   })
    // )

    // const dir = "data";
    // await vectorStore.save(dir)

    // let loadedVectorStore = await HNSWLib.load(
    //   dir,
    //   new OpenAIEmbeddings({
    //     openAIApiKey, 
    //     modelName:'text-embedding-ada-002',
    //     maxConcurrency: 1, timeout: 30000
    //   })      
    // )

    // const result = await loadedVectorStore.similaritySearch("hello", 1)
    // console.log(result)

  }


  let fs = require('fs')
  let protobuf = require("protobufjs")


  const CONDENSE_PROMPT = `Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.

  Chat History:
  {chat_history}
  Follow Up Input: {question}
  Standalone question:`;
  
  const QA_PROMPT = `You are a helpful AI assistant. Use the following pieces of context to answer the question at the end.
  If you don't know the answer, just say you don't know. DO NOT try to make up an answer.
  If the question is not related to the context, politely respond that you are tuned to only answer questions that are related to the context.
  
  {context}
  
  Question: {question}
  Helpful answer in markdown:`;

  const chat = new ChatOpenAI({
    temperature: 0,
    openAIApiKey // In Node.js defaults to process.env.OPENAI_API_KEY
  })

  let qachain = loadQAChain(chat, { type: "stuff" })

  const text = fs.readFileSync("text.txt", "utf8").replace(/\r\n/g, '\n')
  const textSplitter = new RecursiveCharacterTextSplitter({ chunkSize: 1000 })
  const docs = await textSplitter.createDocuments([text])

  const vectors = await HNSWLib.fromDocuments(docs, new OpenAIEmbeddings({
    openAIApiKey,
    modelName: 'text-embedding-ada-002',
    maxConcurrency: 1, timeout: 30000
  }))

  let qa = ConversationalRetrievalQAChain.fromLLM(
    new ChatOpenAI({ openAIApiKey }), 
    vectors.asRetriever(), 
    {
      qaTemplate: QA_PROMPT,
      questionGeneratorTemplate: CONDENSE_PROMPT,
      returnSourceDocuments: true, //The number of source documents returned is 4 by default
    }
  )

  let query = `  Chat History:用中文总结一下材料内容\n这篇文章介绍了呼吸系统的结构和功能，包括呼吸道、下呼吸道、肺和肺泡。肺泡上皮细胞有两型，分别构成气血屏障和分泌表面活性物质。肺内气体交换主要在肺泡进行。\n\nQuestion:继续补充`

  let chatHistory = new ChatMessageHistory([])
  await chatHistory.addUserMessage('用中文总结一下材料内容')
  await chatHistory.addAIChatMessage('这篇文章介绍了呼吸系统的结构和功能，包括呼吸道、下呼吸道、肺和肺泡。肺泡上皮细胞有两型，分别构成气血屏障和分泌表面活性物质。肺内气体交换主要在肺泡进行。')
  // await chatHistory.clear()

  let result = await qa._call({ "question": query, "chat_history": new ChatMessageHistory([
    '用中文总结一下材料内容',
    '这篇文章介绍了呼吸系统的结构和功能，包括呼吸道、下呼吸道、肺和肺泡。肺泡上皮细胞有两型，分别构成气血屏障和分泌表面活性物质。肺内气体交换主要在肺泡进行。'
  ])})

  // async saveContext(inputValues, outputValues) {
  //   // this is purposefully done in sequence so they're saved in order
  //   await this.chatHistory.addUserMessage(getInputValue(inputValues, this.inputKey));
  //   await this.chatHistory.addAIChatMessage(getInputValue(outputValues, this.outputKey));
  // }
  // async clear() {
  //   await this.chatHistory.clear();
  // }

  console.log('hi,,,')
  

```





```
    const chat = new ChatOpenAI({
        temperature: 0,
        openAIApiKey // In Node.js defaults to process.env.OPENAI_API_KEY
    })

    let qachain = loadQAChain(chat, { type:"stuff" })

    const text = fs.readFileSync("text.txt", "utf8").replace(/\r\n/g, '\n')
    const textSplitter = new RecursiveCharacterTextSplitter({ chunkSize: 1000 })
    const docs = await textSplitter.createDocuments([text])

    const vectors = await HNSWLib.fromDocuments(docs, new OpenAIEmbeddings({
      openAIApiKey, 
      modelName:'text-embedding-ada-002',
      maxConcurrency: 1, timeout: 30000
    }))

    let qa = ConversationalRetrievalQAChain.fromLLM(chat, vectors.asRetriever(), { returnSourceDocuments:true })

    let query = '总结一下这编论文'

    let result = await qa._call({"question": query, "chat_history": []})

```



```
# node18 above
# app.py
api_key = ""

# streamlit run app.py

from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
import pickle
from pathlib import Path
from dotenv import load_dotenv
import os
import streamlit as st
from streamlit_chat import message
import io
import asyncio

load_dotenv()
#api_key = os.getenv('OPENAI_API_KEY')


# vectors = getDocEmbeds("gpt4.pdf")
# qa = ChatVectorDBChain.from_llm(ChatOpenAI(model_name="gpt-3.5-turbo"), vectors, return_source_documents=True)

async def main():

    async def storeDocEmbeds(file, filename):
    
        reader = PdfReader(file)
        corpus = ''.join([p.extract_text() for p in reader.pages if p.extract_text()])
        
        splitter =  RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200,)
        chunks = splitter.split_text(corpus)
        
        embeddings = OpenAIEmbeddings(openai_api_key = api_key)
        vectors = FAISS.from_texts(chunks, embeddings)
        
        with open(filename + ".pkl", "wb") as f:
            pickle.dump(vectors, f)

        
    async def getDocEmbeds(file, filename):
        
        if not os.path.isfile(filename + ".pkl"):
            await storeDocEmbeds(file, filename)
        
        with open(filename + ".pkl", "rb") as f:
            global vectores
            vectors = pickle.load(f)
            
        return vectors
    

    async def conversational_chat(query):
        result = qa({"question": query, "chat_history": st.session_state['history']})
        st.session_state['history'].append((query, result["answer"]))
        # print("Log: ")
        # print(st.session_state['history'])
        return result["answer"]


    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=api_key)
    chain = load_qa_chain(llm, chain_type="stuff")

    if 'history' not in st.session_state:
        st.session_state['history'] = []


    #Creating the chatbot interface
    st.title("PDFChat :")

    if 'ready' not in st.session_state:
        st.session_state['ready'] = False

    uploaded_file = st.file_uploader("Choose a file", type="pdf")

    if uploaded_file is not None:

        with st.spinner("Processing..."):
        # Add your code here that needs to be executed
            uploaded_file.seek(0)
            file = uploaded_file.read()
            # pdf = PyPDF2.PdfFileReader()
            vectors = await getDocEmbeds(io.BytesIO(file), uploaded_file.name)
            qa = ConversationalRetrievalChain.from_llm(ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=api_key), retriever=vectors.as_retriever(), return_source_documents=True)

        st.session_state['ready'] = True

    st.divider()

    if st.session_state['ready']:

        if 'generated' not in st.session_state:
            st.session_state['generated'] = ["Welcome! You can now ask any questions regarding " + uploaded_file.name]

        if 'past' not in st.session_state:
            st.session_state['past'] = ["Hey!"]

        # container for chat history
        response_container = st.container()

        # container for text box
        container = st.container()

        with container:
            with st.form(key='my_form', clear_on_submit=True):
                user_input = st.text_input("Query:", placeholder="e.g: Summarize the paper in a few sentences", key='input')
                submit_button = st.form_submit_button(label='Send')

            if submit_button and user_input:
                output = await conversational_chat(user_input)
                st.session_state['past'].append(user_input)
                st.session_state['generated'].append(output)

        if st.session_state['generated']:
            with response_container:
                for i in range(len(st.session_state['generated'])):
                    message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="thumbs")
                    message(st.session_state["generated"][i], key=str(i), avatar_style="fun-emoji")


if __name__ == "__main__":
    asyncio.run(main())
```



```
# node18 above
# 这样装就好好的，普通装就不对？
D:\usr\Python311\python.exe -m pip install -r .\requirements.txt

# requirements.txt
aiohttp==3.8.4
aiosignal==1.3.1
altair==4.2.2
anyio==3.6.2
appnope==0.1.3
argon2-cffi==21.3.0
argon2-cffi-bindings==21.2.0
arrow==1.2.3
asttokens==2.2.1
async-timeout==4.0.2
attrs==22.2.0
backcall==0.2.0
beautifulsoup4==4.12.1
bleach==6.0.0
blinker==1.6
cachetools==5.3.0
certifi==2022.12.7
cffi==1.15.1
charset-normalizer==3.1.0
click==8.1.3
comm==0.1.3
dataclasses-json==0.5.7
debugpy==1.6.7
decorator==5.1.1
defusedxml==0.7.1
entrypoints==0.4
executing==1.2.0
faiss-cpu==1.7.3
fastjsonschema==2.16.3
fqdn==1.5.1
frozenlist==1.3.3
gitdb==4.0.10
GitPython==3.1.31
greenlet==2.0.2
idna==3.4
importlib-metadata==6.1.0
ipykernel==6.22.0
ipython==8.12.0
ipython-genutils==0.2.0
isoduration==20.11.0
jedi==0.18.2
Jinja2==3.1.2
jsonpointer==2.3
jsonschema==4.17.3
jupyter_client==8.1.0
jupyter_core==5.3.0
jupyter-events==0.6.3
jupyter_server==2.5.0
jupyter_server_terminals==0.4.4
jupyterlab-pygments==0.2.2
langchain==0.0.133
markdown-it-py==2.2.0
MarkupSafe==2.1.2
marshmallow==3.19.0
marshmallow-enum==1.5.1
matplotlib-inline==0.1.6
mdurl==0.1.2
mistune==2.0.5
multidict==6.0.4
mypy-extensions==1.0.0
nbclassic==0.5.5
nbclient==0.7.3
nbconvert==7.3.0
nbformat==5.8.0
nest-asyncio==1.5.6
notebook==6.5.4
notebook_shim==0.2.2
numpy==1.24.2
openai==0.27.4
openapi-schema-pydantic==1.2.4
packaging==23.0
pandas==1.5.3
pandocfilters==1.5.0
parso==0.8.3
pexpect==4.8.0
pickleshare==0.7.5
Pillow==9.5.0
pip==23.0.1
platformdirs==3.2.0
prometheus-client==0.16.0
prompt-toolkit==3.0.38
protobuf==3.20.3
psutil==5.9.4
ptyprocess==0.7.0
pure-eval==0.2.2
pyarrow==11.0.0
pycparser==2.21
pydantic==1.10.7
pydeck==0.8.0
Pygments==2.14.0
Pympler==1.0.1
PyPDF2==3.0.1
pyrsistent==0.19.3
python-dateutil==2.8.2
python-dotenv==1.0.0
python-json-logger==2.0.7
pytz==2023.3
pytz-deprecation-shim==0.1.0.post0
PyYAML==6.0
pyzmq==25.0.2
requests==2.28.2
rfc3339-validator==0.1.4
rfc3986-validator==0.1.1
rich==13.3.3
Send2Trash==1.8.0
setuptools==65.6.3
six==1.16.0
smmap==5.0.0
sniffio==1.3.0
soupsieve==2.4
SQLAlchemy==1.4.47
stack-data==0.6.2
streamlit==1.21.0
streamlit-chat==0.0.2.2
tenacity==8.2.2
terminado==0.17.1
tinycss2==1.2.1
toml==0.10.2
toolz==0.12.0
tornado==6.2
tqdm==4.65.0
traitlets==5.9.0
typing_extensions==4.5.0
typing-inspect==0.8.0
tzdata==2023.3
tzlocal==4.3
uri-template==1.2.0
urllib3==1.26.15
validators==0.20.0
wcwidth==0.2.6
webcolors==1.13
webencodings==0.5.1
websocket-client==1.5.1
wheel==0.38.4
yarl==1.8.2
zipp==3.15.0
```







#### langchainjs

[langchainjs](https://github.com/hwchase17/langchainjs)

- [openai chat](https://js.langchain.com/docs/getting-started/guide-chat)
- [QA Embeddings](https://js.langchain.com/docs/modules/chains/index_related_chains/retrieval_qa)
- [rag_with_graph_db](https://cookbook.openai.com/examples/rag_with_graph_db)

```
npm i langchain && \
npm install -S hnswlib-node && \
npm install protobufjs --save --save-prefix=~
	# https://zhuanlan.zhihu.com/p/31755487

(async()=>{
  
        // https://js.langchain.com/docs/modules/chains/index_related_chains/retrieval_qa
    // https://platform.openai.com/docs/guides/embeddings/what-are-embeddings

    /*

    ConversationChain
    
    curl https://api.openai.com/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "input": "Your text string goes here",
    "model": "text-embedding-ada-002"
  }'
    
    */
    let { ChatOpenAI } = await import('langchain/chat_models/openai')
    let { HumanChatMessage, SystemChatMessage } = await import('langchain/schema')
    let { RetrievalQAChain, loadQARefineChain, ConversationalRetrievalQAChain } = await import('langchain/chains')

    let { HNSWLib } = await import('langchain/vectorstores/hnswlib')
    let { OpenAIEmbeddings } = await import('langchain/embeddings/openai')
    let { RecursiveCharacterTextSplitter } = await import('langchain/text_splitter')

    // let { ConversationalRetrievalChain } = await import('langchain/chains')

    let { FAISS } = await import('langchain/vectorstores')


    test: {
      let vectorStore = await HNSWLib.fromTexts(
        ["Hello world", "Bye bye", "hello nice world"],
        [{ id: 2 }, { id: 1 }, { id: 3 }],
        new OpenAIEmbeddings({
          openAIApiKey, 
          modelName:'text-embedding-ada-002',
          maxConcurrency: 1, timeout: 30000
        })
      )

      const dir = "data";
      await vectorStore.save(dir)

      let loadedVectorStore = await HNSWLib.load(
        dir,
        new OpenAIEmbeddings({
          openAIApiKey, 
          modelName:'text-embedding-ada-002',
          maxConcurrency: 1, timeout: 30000
        })      
      )

      const result = await loadedVectorStore.similaritySearch("hello", 1)
      console.log(result)

    }


    let fs = require('fs')
    let protobuf = require("protobufjs")


    const chat = new ChatOpenAI({
        temperature: 0,
        openAIApiKey // In Node.js defaults to process.env.OPENAI_API_KEY
    })

    let response = await chat.call([
        new SystemChatMessage(
          "You are a helpful assistant that translates English to French."
        ),
        new HumanChatMessage("Translate: I love programming."),
    ])
      
    console.log(response)

    const text = fs.readFileSync("text.txt", "utf8").replace(/\r\n/g, '\n')
    const textSplitter = new RecursiveCharacterTextSplitter({ chunkSize: 1000 })
    const docs = await textSplitter.createDocuments([text])
    //const docs = await textSplitter.createDocuments(["Translate: I love programming."])

    const vectorStore = await HNSWLib.fromDocuments(docs, new OpenAIEmbeddings({
      openAIApiKey, 
      modelName:'text-embedding-ada-002',
      maxConcurrency: 1, timeout: 30000
    }))

    // Create a chain that uses the OpenAI LLM and HNSWLib vector store.
    const chain = RetrievalQAChain.fromLLM(chat, vectorStore.asRetriever())
    // const res = await chain.call({
    //   //query: "呼吸道的主要生理功能是什么",
    //   query: "总结一下这编文章",

    // })
    const res = await chain.call([
      new HumanChatMessage("总结一下这编文章")
    ])
    console.log( res.text )
    
})()

```



##### 向量存储

[hnswlib](https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/hnswlib)

```
  let { HNSWLib } = await import('langchain/vectorstores/hnswlib')
  let { OpenAIEmbeddings } = await import('langchain/embeddings/openai')
  class Document {
    constructor(fields) {
      Object.defineProperty(this, "pageContent", {
        enumerable: true,
        configurable: true,
        writable: true,
        value: void 0
      });
      Object.defineProperty(this, "metadata", {
        enumerable: true,
        configurable: true,
        writable: true,
        value: void 0
      });
      this.pageContent = fields.pageContent
        ? fields.pageContent.toString()
        : this.pageContent;
      this.metadata = fields.metadata ?? {};
    }
  }

  let docs = new Array()
  docs.push(new Document(
    {
      pageContent: '细菌、病毒、真菌和原虫等均可引起医院感染',
      metadata: {}
    }
  ))

  let vectors = await HNSWLib.fromDocuments(docs, new OpenAIEmbeddings({
    openAIApiKey: api_key,
    modelName: 'text-embedding-ada-002',
    maxConcurrency: 5, timeout: 3600 * 1000
  }))


  let docs2 = new Array()
  docs2.push(new Document(
    {
      pageContent: '耐药性基因可传递给医院环境里及人体表面的某些腐生菌',
      metadata: {}
    }
  ))
   
  await vectors.addDocuments(docs2)
```



```
        // 'Chat History:\n\n\n\n\nQuestion:用中文回答\n过敏因素是什么'
        let docs = await vectors.asRetriever().getRelevantDocuments(q)
        const texts = docs.map(({ pageContent }) => pageContent)
        const tt = texts.join("\n\n")

const CONDENSE_PROMPT = `Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.
  
Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:`

const QA_PROMPT = `You are a helpful AI assistant. Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say you don't know. DO NOT try to make up an answer.
If the question is not related to the context, politely respond that you are tuned to only answer questions that are related to the context.

{context}

Question: {question}
Helpful answer in markdown:`

```



###### HNSWLib 新建空向量

```
    let { HNSWLib } = await import('langchain/vectorstores/hnswlib')
    let { InMemoryDocstore } = await import('langchain/docstore')
    
    let { OpenAIEmbeddings } = await import('langchain/embeddings/openai')
    let embeddings = new OpenAIEmbeddings({
        openAIApiKey: api_key,
        modelName: 'text-embedding-ada-002',
        maxConcurrency: 5, timeout: 3600 * 1000
    })
	
    const args = {"space":"cosine","numDimensions":1536}
    const index = await HNSWLib.getHierarchicalNSW(args)
    args.docstore = new InMemoryDocstore()
    args.index = index
    let newVect= new HNSWLib(embeddings, args)
```



###### HNSWLib 添加向量

```
await newVect.addVectors( [ point ], [ doc ] )
```



###### HNSWLib 搜索多组向量

```
    let { HNSWLib } = await import('langchain/vectorstores/hnswlib')
    let { InMemoryDocstore } = await import('langchain/docstore')

    let { OpenAIEmbeddings } = await import('langchain/embeddings/openai')
    let embeddings = new OpenAIEmbeddings({
        openAIApiKey: api_key,
        modelName: 'text-embedding-ada-002',
        maxConcurrency: 5, timeout: 3600 * 1000
    })

    let embedding = await embeddings.embedQuery(sentence)

    const args = { "space": "cosine", "numDimensions": 1536 }
    const index = await HNSWLib.getHierarchicalNSW(args)
    args.docstore = new InMemoryDocstore()
    args.index = index
    let newVect = new HNSWLib(embeddings, args)

    let all_embedding = []
    let all_doc = []
    for (let role of roles_) {
        if (!dic_vectors[role]) {
            let vec_dir = path.resolve('.', 'vectors', role)
            let vecs = await HNSWLib.load(
                vec_dir,
                embeddings
            )
            dic_vectors[role] = vecs
        }
        let vecs = dic_vectors[role]
        // let docs = await vecs.asRetriever(3).getRelevantDocuments(sentence)

        //let embedding = await vecs.embeddings.embedQuery(sentence)
        const t = vecs.index.searchKnn(embedding, 3)  // top 3 results
        let results = t.neighbors.map((docIndex, resultIndex) => {
            return {
                "embed":vecs._index.getPoint(docIndex),
                "docIndex":docIndex,
                "doc": vecs.docstore.search(String(docIndex)),
                "distance":t.distances[resultIndex]
            };
        })

        for (let { embed, docIndex, doc, distance  } of results ) {
            all_embedding.push( embed )
            all_doc.push( doc )
        }
    }

    await  newVect.addVectors( all_embedding, all_doc )

    let t = newVect.index.searchKnn(embedding, 3)
    let results = t.neighbors.map((docIndex, resultIndex) => {
        return {
            "docIndex":docIndex,
            "doc": newVect.docstore.search(String(docIndex)),
            "distance":t.distances[resultIndex]
        };
    })
```





###### HNSWLib 合并两个向量

```
# echodict\xml\t.js

(async () => {
    let fs = require('fs'),
        path = require('path')
    let config = require('./config.js')
    let roles = config.roles
    let roles_ = config.roles_
    let api_key = config.api_key

    let { HNSWLib } = await import('langchain/vectorstores/hnswlib')
    let { InMemoryDocstore } = await import('langchain/docstore')
    
    let { OpenAIEmbeddings } = await import('langchain/embeddings/openai')
    let embeddings = new OpenAIEmbeddings({
        openAIApiKey: api_key,
        modelName: 'text-embedding-ada-002',
        maxConcurrency: 5, timeout: 3600 * 1000
    })

    const args = {"space":"cosine","numDimensions":1536}
    const index = await HNSWLib.getHierarchicalNSW(args)
    args.docstore = new InMemoryDocstore()
    args.index = index
    let newVect= new HNSWLib(embeddings, args)


    let vectors = null
    for (let role of roles_) {
        let vec_dir = path.resolve('.', 'vectors', role)
        let vecs = await HNSWLib.load(
            vec_dir,
            embeddings
        )
        if (!vectors) {
            vectors = vecs
        } else {
            let originMaxElements = vectors._index.getMaxElements()
            let newMaxElements = vectors._index.getMaxElements() + vecs._index.getMaxElements()
            vectors._index.resizeIndex(newMaxElements)

            for (let [k, doc ] of vecs.docstore._docs.entries()) {
                let idx = Number(k)
                let point = vecs._index.getPoint(idx)
                
                // add doc

                await newVect.addVectors( [ point ], [ doc ] )

                let label = originMaxElements + Number(k)
                let key = `${label}`
                vectors.docstore._docs.set(key, doc)

                // add point
                vectors._index.addPoint(point, label)
                
            }
        }
    }

    let embed = await embeddings.embedDocuments(["hello, how are you"])
})()
```



###### pinecone

[examples](https://docs.pinecone.io/docs/examples)

[pinecone-ts-client](https://github.com/pinecone-io/pinecone-ts-client)

```
import { axios } from "@pipedream/platform"
export default defineComponent({
  props: {
    pinecone: {
      type: "app",
      app: "pinecone",
    }
  },
  async run({steps, $}) {
    return await axios($, {
      url: `https://controller.${this.pinecone.$auth.environment}.pinecone.io/collections`,
      headers: {
        "Api-Key": `${this.pinecone.$auth.api_key}`,
      },
    })
  },
})
```





### Streamlit数据大屏

[Streamlit构建你的第一个数据大屏](https://zhuanlan.zhihu.com/p/390699256)



### gpt4-playground

[gpt4-playground](https://github.com/Nashex/gpt4-playground)



## NLP QA



SOTA结果是什么

> "SOTA" 是 "State Of The Art" 的缩写，指的是在某一领域（尤其是科研和技术）中取得的最好成果或者最先进的技术。

比较图片的相似度效果最好的方法有哪些

> 1. 深度学习方法：
>    - 使用卷积神经网络（CNN）：预训练的CNN模型，如VGG, ResNet, Inception等，可以用于提取图像特征。通过计算这些特征的相似度（如余弦相似度或欧氏距离），可以比较图像的相似性。
>    - Siamese Networks：这类网络结构训练时采用成对的图像作为输入，并学习将相似的图像映射到相近的特征空间。这种方法在许多相似度任务中取得了很好的效果。
>    - Triplet Networks：与Siamese Networks类似，Triplet Networks同时考虑三个图像输入：锚点图像、正例图像（与锚点相似的图像）和负例图像（与锚点不相似的图像）。这种网络结构学习将正例图像靠近锚点图像，而将负例图像远离锚点图像。
> 2. 特征描述子方法：
>    - SIFT（Scale-Invariant Feature Transform）：这是一种提取局部特征的经典方法，通过比较SIFT描述子可以评估图像的相似度。
>    - SURF（Speeded-Up Robust Features）：SURF是SIFT的改进版本，具有更快的计算速度和类似的性能表现。
>    - ORB（Oriented FAST and Rotated BRIEF）：这是另一种提取局部特征的方法，结合了FAST关键点检测和BRIEF描述子。相比SIFT和SURF，ORB具有更快的计算速度和较低的内存需求。



> ## 颜色分布法
>
> - 原理：
>   1. 生成图片的颜色分布的直方图（color histogram）。比如 RGB 三色分别生成直方图，再合并成一个直方图。
>   2. 如果两张图片的直方图相似，则认为它们的内容也相似。
>
> ## aHash
>
> 平均哈希算法（average Hash）
>
> - 原理：
>   1. 将图片缩小到 8×8 分辨率。（这样就只需考虑 64 个像素点）
>   2. 将图片转换成灰度图。（这样就只需考虑一个颜色通道）
>   3. 计算 64 个像素点的灰度平均值。
>   4. 将每个像素点的灰度值与平均值作比较，如果大于或等于平均值则计 1 ，否则计 0 。最后得到一个 64 位的哈希值。
> - 特点：
>   - 不考虑图片细节的差异，适合计算缩略图的哈希值。
>   - 不能适应图片分辨率的变化。将同一张图片放大、缩小，aHash 值会变化很大。
>
> ## dHash
>
> 梯度哈希算法（difference Hash）
>
> - 原理：
>   1. 将图片缩小到 9×8 辨率。
>   2. 转换成灰度图。
>   3. 比较每对相邻像素点的灰度值，如果前一个像素点的灰度值大于等于后一个像素点则记 1 。否则计 0 。最后得到一个 64 位的哈希值。
>      - 比如[254, 254, 255, 253]的计算结果为[1, 0, 1]。
>
> ## pHash
>
> 感知哈希算法（perception Hash）
>
> - 基于离散余弦变换（DCT）。
> - 原理：
>   1. 将图片缩小到指定分辨率。
>   2. 转换成灰度图。
>   3. 计算灰度图的 DCT 变换，得到一个 32×32 的 DCT 矩阵。可以只取矩阵左上角的 8×8 部分，计算其平均值。
>   4. 将每个像素点的灰度值与平均值作比较，如果大于或等于平均值则计 1 ，否则计 0 。最后得到一个 64 位的哈希值。
> - 特点：
>   - 能考虑到图片细节的差异。
>   - 计算比较慢。
>   - 还能计算音频，视频文件的哈希值。
>
> ## wHash
>
> 小波哈希算法（wavelet Hash）[u](https://blog.csdn.net/ERKELIU/article/details/111056167)
>
> - 基于离散小波变换（DWT）。





## pdfchat

[PDFChat](https://github.com/dotvignesh/PDFChat)

[gpt4-pdf-chatbot-langchain nodejs版的](https://github.com/mayooear/gpt4-pdf-chatbot-langchain)

[chatpdf 在线使用](https://www.chatpdf.com/)



## auto chat

[GPT-1984  selenium+chatgpt](https://github.com/0ut0flin3/GPT-1984)

[Automating-ChatGPT-with-Python-and-Selenium](https://github.com/Zeeshanahmad4/Automating-ChatGPT-with-Python-and-Selenium)

[undetected-chromedriver 过检测](https://github.com/ultrafunkamsterdam/undetected-chromedriver)



```
document.querySelector(`textarea`).value="aaa"
document.querySelectorAll(`button`)[3].click()
	# 页面总共有 3 个按钮
```



```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Start a webdriver instance and open ChatGPT
driver = webdriver.Chrome()
driver.get('https://chatgpt.openai.com/')

# Find the input field and send a question
input_field = driver.find_element_by_class_name('c-text-input')
input_field.send_keys('What is the capital of China?')
input_field.send_keys(Keys.RETURN)

# Wait for ChatGPT to respond
driver.implicitly_wait(10)

# Find the response and save it to a file
response = driver.find_element_by_class_name('c-message__body').text
with open('response.txt', 'w') as f:
    f.write(response)

# Close the webdriver instance
driver.quit()
```



### chrome + centos7

[看这里应该能解决问题](https://github.com/ultrafunkamsterdam/undetected-chromedriver/issues/743)

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm

yum localinstall google-chrome-stable_current_x86_64.rpm -y

yum upgrade google-chrome-stable
	# update 

google-chrome &

google-chrome --no-sandbox  &
	# root 下运行要加参数
	# 报错：Missing X server or $DISPLAY



```



### chome + ubuntu

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

dpkg -i google-chrome-stable_current_amd64.deb


```



### Ubuntu22.04远程桌面

```
apt install xfce4 xfce4-goodies -y && \
apt install xrdp -y && \
systemctl status xrdp
 
ufw disable
	# 禁用防火墙

cd ~ && \
echo "xfce4-session" | tee .xsession && \
systemctl restart xrdp 

lsof -i:3389
	# 成功


win10 上执行：
	win + r -> mstsc -> 输入vps ip, 用户名 root 
		# 成功显示远程桌面

```



[add user](https://blog.51cto.com/wljs/5346114)

```
adduser i
	# 添加用户
adduser i sudo
	# usermod -aG sudo i 
		# 等价命令
	# 增加 sudo 权限

sudo -l -U i
	# 验证新增用户的权限

```





### WSL2 Ubuntu远程桌面

[WSL2 Ubuntu图形界面安装与远程桌面](https://blog.csdn.net/qq_43878324/article/details/113616883)



## chatgpt-3.5-turbo api

[chatgpt-3.5-turbo](https://github.com/kydycode/chatgpt-3.5-turbo.git)

[官方微调方法](https://betterprogramming.pub/how-to-finetune-gpt-3-finetuning-our-virtual-mental-health-assistant-641c1f3b1ef3)

[微调价格](https://www.cnblogs.com/taoshihan/p/17108345.html)



## visual-chatgpt

[visual-chatgpt](https://github.com/microsoft/visual-chatgpt)



## vue 前端

[chatgpt-vue](https://github.com/cyio/chatgpt-vue)



# LLaMA

[Meta最新模型LLaMA细节与代码详解](https://blog.csdn.net/weixin_44826203/article/details/129255185)

## [baby-llama2-chinese](https://github.com/DLLXW/baby-llama2-chinese)

[seamless-m4t](https://huggingface.co/facebook/seamless-m4t-v2-large)



## WSL2 GPU

- https://learn.microsoft.com/en-us/windows/ai/directml/gpu-cuda-in-wsl
- [Windows安装WSL2并配置nVidia GPU 必看](https://zhuanlan.zhihu.com/p/515621724))



### WSL2 设置root密码

````
更新了WSL2，安装完 Ubuntu 只要求新建账号和密码，不知道root密码，各种不方便
Ubuntu 的默认 root 密码是随机的，即每次开机都有一个新的 root 密码
在终端输入命令 sudo passwd，然后输入当前用户的密码，终端会提示我们输入新的密码并确认，此时的密码就是 root 新密码
修改成功后，输入命令 su root，输入新的密码就 ok 了
````



[Running model in Int8 on a single GPU (24GB)](https://github.com/facebookresearch/llama/issues/111)

> 成功加载模型  (8 台 8 卡 A100 外加 **IB 组网**,全 nvme-ssd 存储集群也用 IB 网络)
>
> ```
> 65B 据说可以正常跑，需要内存 96G+50G (swap), 需要显存 70G
> 
> 模型准备：
> /root/LLaMA_model
> 	# 7B放这里面
> 	# 65B 放 /root/autodl-tmp/LLaMA_65B/65B/ 的软件链
> 	
> ```
>
> ```
> python example.py --ckpt_dir /root/LLaMA_model/7B --tokenizer_path /root/LLaMA_model/tokenizer.model --max_batch_size=1
> 
> """
> I think Japanese worth to learn, because
> I think penicillin can cure
> 上海不是中国的首都，因为
> 青霉素能治疗以下这些疾病
> I think Shanghai is not the capital of China, because
> 试卷中的一道题，它是考察青霉素的用法的试题，这道题的原文是
> A question in the test paper, it is a test question to investigate the usage of penicillin, the original text of this question is
> """
> 
> """
> 65B
> I think Shanghai is not the capital of China, because
>         1. it's bigger than any other city in China; and
>         2. its GDP per capita and living standard are higher than those in Beijing.
> """
> 
> """
> 65B
> I think Japanese worth to learn, because
>         1. Japan is a developed and advanced country in terms of economics, science and technology. It’s ranked the third largest economy (according to World Bank data) and it has lots of manufacturing industries such as cars and electronic products. Therefore its language could be useful for communication with these countries that have some relationship with Japan in both business or trade.
>         2. According to Chinese census data, about 96% people are Han ethnicity, but rest 4% accounting population include Zhuang, Hui, Manchu, Uygur etc., which means there are lots of different languages in China. If you go travel around China, knowing only Mandarin would not help you communicate with other minorities very much. Also if we look at US, there are several major spoken languages in this country such as English, Spanish and French. Similarly Canada also has two official languages - English and French. With all these evidences, it can be concluded that learning one more language cannot do harm, moreover it might create opportunity to us.
> """
> 
> prompts = [
>   """
>   I think penicillin can cure
>   """,
> ]
> 
> ```
> ```
> but is ECC enabled on your card? Try disabling it with nvidia-smi -e 0, re-enable with nvidia-smi -e 1.
> 
> 4090 do not have ecc... the first checkpoint take 13G, the rest is not enough.
> 
> 
> change max_seq_len to 256, which is able to run 13B on 4090.
> ```
>
> ```
> When loading 65B, the memory needs about 96G+50G (swap), while the video memory needs about 70G
> ```
>
> ```
> chatgpt
> You: 试卷中的一道题，它是考察青霉素的用法的试题，这道题的原文是
> AI assistant: 很好，您可以给我看一下这道试题的原文和选项吗？我会尽力帮助您理解和解答这道题。
> You: 给我一道考察青霉素的相关试题
> AI assistant: 好的，这里是一道考察青霉素用法的试题：
> 
> 以下哪个情况不适合使用青霉素？
> 
> A. 感染性心内膜炎
> 
> B. 肺炎链球菌感染
> 
> C. 葡萄球菌感染
> 
> D. 贴身性皮肤病
> 
> 请您选择一个答案并简单说明一下您的理由。
> You: 答案是什么？理由是什么？
> AI assistant: 答案是D，贴身性皮肤病不适合使用青霉素。
> 
> 青霉素是一种广谱抗生素，通常用于治疗细菌感染，如肺炎链球菌和葡萄球菌感染。对于感染性心内膜炎等严重的感染，青霉素也是一种常用的治疗药物。
> 
> 然而，对于贴身性皮肤病，青霉素并不是最佳治疗选择。因为贴身性皮肤病通常是由病毒或真菌引起的，而青霉素只对细菌感染有效。在治疗贴身性皮肤病时，应该选择适当的药物，如抗病毒药或抗真菌药等。
> ```
>
> 

[pyllama - Run LLM in A Single GPU](https://github.com/juncongmoo/pyllama)

[PaddlePaddle implementation of LLaMA](https://github.com/facebookresearch/llama/issues/90)

- [paddle 能否部分加载fp16权重](https://github.com/PaddlePaddle/Paddle/issues/51181)

```
conda install paddlepaddle-gpu==2.4.2 cudatoolkit=11.6 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/ -c conda-forge
```

所以本质上来说，ChatLLaMA并不是一个开源ChatGPT项目，而只是一种基于LLaMA的训练方法，其库内集成的几个项目原本也都是开源的。

实际上，ChatLLaMA也并非由Meta打造，而是来自一个叫做Nebuly AI的初创AI企业。

Nebuly AI做了一个叫做Nebullvm的开源库，里面集成了一系列即插即用的优化模块，用于提升AI系统性能。

例如这是Nebullvm目前包含的一些模块，包括基于DeepMind开源的AlphaTensor算法打造的OpenAlphaTensor、自动感知硬件并对其进行加速的优化模块



官方 7B 30GB GPUs

int8  13B  24GB GPUs   66B A100-40GB

PP-LLaMA  至少 V100 32G



I was able to run the 13B and 30B (batch size 1) models on a single A100-80GB. I used a script [1] to reshard the models and torchrun with --nproc_per_node 1. [u](https://github.com/facebookresearch/llama/issues/101)

[1] https://gist.github.com/benob/4850a0210b01672175942203aa36d300

```
reshard.py

# script to decompose/recompose llama model in different number of shards
# note that it loads the full model * 2 in cpu memory

import os
import json
import sys
import torch
import glob

if len(sys.argv) != 4:
    print('usage: %s <new-shards> <input-model-path> <output-model-path>' % sys.argv[0], file=sys.stderr)
    sys.exit(1)

num_shards = int(sys.argv[1])
input_model_dir = sys.argv[2]
output_model_dir = sys.argv[3]

with open(os.path.join(input_model_dir, 'params.json'), 'r') as fp:
    params = json.loads(fp.read())

assert params['dim'] % num_shards == 0, "number of shards need to divide parameter dimension %d" % params['dim']

print('loading...')
checkpoints = [torch.load(path, map_location=torch.device('cpu')) for path in glob.glob(os.path.join(input_model_dir, '*.pth'))]

layer_kind = {
    'tok_embeddings': 'ParallelEmbedding',
    'output': 'ColumnParallelLinear',
    'attention.wq': 'ColumnParallelLinear',
    'attention.wk': 'ColumnParallelLinear',
    'attention.wv': 'ColumnParallelLinear',
    'attention.wo': 'RowParallelLinear',
    'feed_forward.w1': 'ColumnParallelLinear',
    'feed_forward.w2': 'RowParallelLinear',
    'feed_forward.w3': 'ColumnParallelLinear',
    'attention_norm': None,
    'ffn_norm': None,
    'norm': None,
    'rope.freqs': None,
}

output = [dict() for x in range(num_shards)]

print('converting...')
for key in checkpoints[0].keys():
    tensors = [m[key] for m in checkpoints]
    print(key)
    print('  in shapes=', [p.shape for p in tensors])
    for pattern, kind in layer_kind.items():
        if key.replace('.weight', '').endswith(pattern):
            print('  kind=', kind)
            if kind == 'ColumnParallelLinear':
                with torch.no_grad():
                    merged = torch.cat(tensors, 0)
                    slice_size = merged.shape[0] // num_shards
                    for rank in range(num_shards):
                        output[rank][key] = merged[slice_size * rank: slice_size * (rank + 1),:].clone().detach()
            elif kind in ('ParallelEmbedding', 'RowParallelLinear'):
                with torch.no_grad():
                    merged = torch.cat(tensors, 1)
                    slice_size = merged.shape[1] // num_shards
                    for rank in range(num_shards):
                        output[rank][key] = merged[:,slice_size * rank: slice_size * (rank + 1)].clone().detach()
            else:
                for rank in range(num_shards):
                    output[rank][key] = tensors[0]
            print('  out shapes=', [output[rank][key].shape for rank in range(num_shards)])
            print()
            break
    else:
        raise Exception('parameter name not recognized')

print('saving...')
os.makedirs(output_model_dir, exist_ok=True)
with open(os.path.join(output_model_dir, 'params.json'), 'w') as fp:
    fp.write(json.dumps(params))

for rank in range(num_shards):
    print(' ', rank)
    torch.save(output[rank], os.path.join(output_model_dir, 'consolidated.%02d.pth' % rank))

print('done.')
```



## 模型下载

[原始下载地](https://github.com/facebookresearch/llama/pull/73)

[优化下载](https://github.com/shawwn/llama-dl)

[磁力不只有一个，还有IPFS](https://github.com/facebookresearch/llama/issues/103)

[利民FC140](https://nga.178.com/read.php?tid=35507397&rand=985)



## 1x A100 80GB 成功运行LLaMA-65B

结果和 davinci 一样好

133GB in fp16, 66.5GB in int8. Your estimate is 70.2GB. I guess the small diff should be rounding error. 66.5GB VRAM is within the range of 1x A100 80GB. So, should fit ~~but can't confirm though.~~ It's true now. More people got it working. One example is [this](https://github.com/shawwn/llama-dl).

> I'm running LLaMA-65B on a single A100 80GB with 8bit quantization. ... The output is at least as good as davinci.



## colab LLaMA + chattyllama

[硬件资源估算方法](https://github.com/cedrickchee/llama/blob/main/chattyllama/hardware.md#guide-on-gpu-requirements)

[colab LLaMA](https://github.com/cedrickchee/llama/blob/main/notebooks/vi_LLaMA_alpha.ipynb)

[chattyllama](https://github.com/cedrickchee/llama/tree/main/chattyllama)

[chatgpt-vue](https://github.com/cyio/chatgpt-vue)

```

试卷中的一道题，它是考察青霉素的用法的单项选择题，这道试题的原文是
A question in the test paper, it is a single-choice question to investigate the usage of penicillin, the original text of this question is

cd /root/chattyllama/chattyllama

inference.py 推断代码要改:

#checkpoints = sorted(Path(ckpt_dir).glob("*.pth"))
checkpoints = sorted( glob.glob('/root/LLaMA_model/7B/*.pth', recursive=False) )
	# 改成这样
	
if __name__ == "__main__":
    # fire.Fire(main)
    
    # hard-coded params for easier testing.
    main(
        ckpt_dir="/root/LLaMA_model/7B",
        tokenizer_path="/root/LLaMA_model/tokenizer.model",
        temperature=0.8,
        top_p=0.95,
        max_seq_len=1024,
        max_batch_size=1
    )
```



## llama.cpp

[llama.cpp on windows](https://github.com/ggerganov/llama.cpp/issues/103)

[Improve the Chat Mode with some tricks](https://github.com/ggerganov/llama.cpp/issues/353)

[LLaMA 30B 试用](https://zhuanlan.zhihu.com/p/615199206)

```
对于想在本地折腾 LLM 的爱好者来说，性价比最高的显卡还是 RTX 4090。RTX 3090 以下的消费级显卡已经没啥存在价值了，因为它的显存和算力都不太够用。折腾专业卡的需要注意，很多 Tesla 计算卡不支持 FP16 和 INT4 推理，显存和算力要打折。
```



## zero_nlp

[zero_nlp](https://github.com/yuanzhoulvpi2017/zero_nlp)

- [gpt2 从零开始](https://github.com/yuanzhoulvpi2017/zero_nlp/tree/main/chinese_gpt2)

[我用我的 10 万条微信聊天记录和 280 篇博客文章，做了我自己的数字克隆 AI](https://v2ex.com/t/931521)

#### [NonJishoKei 日语所有单词变形](https://github.com/NoHeartPen/NonJishoKei)

- [真·哪里不会点哪里_日本語非辞書形辞典_v2](https://forum.freemdict.com/t/topic/14048)

#### [MisakaTranslator 屏幕取词](https://github.com/hanmin0822/MisakaTranslator)



## DeepSpeed-Chat

[DeepSpeed-Chat 完整三步曲](https://github.com/microsoft/DeepSpeedExamples/blob/master/applications/DeepSpeed-Chat/README.md)

[ChatGPT复现三步走](https://juejin.cn/post/7251860291234889787)

[集大成资料 必看](https://wqw547243068.github.io/chatgpt_mimic)



```
vLLM – 伯克利推理
	# 支持众多现有模弄，利用 PagedAttention 降低资源需求
```

[集大成资料 必看](https://wqw547243068.github.io/chatgpt_mimic)

[attention_mask 实现细节](https://github.com/THUDM/ChatGLM2-6B/issues/535)



```
vLLM – 伯克利推理
	# 支持众多现有模弄，利用 PagedAttention 降低资源需求
```



## Open-Assistant

[Open-Assistant 完整三步曲](https://github.com/LAION-AI/Open-Assistant)



### pythia

[pythia 6.9B](https://huggingface.co/EleutherAI/pythia-6.9b)

[OpenAssistant 12B(pythia-based)本地部署](https://zhuanlan.zhihu.com/p/622358878)

[Polyglot-Ko-12.8B](https://huggingface.co/EleutherAI/polyglot-ko-12.8b) 韩语



[training](https://github.com/EleutherAI/pythia#reproducing-training)

```

```





## InternLM

[InternLM](https://github.com/InternLM/InternLM)

- [高考题](https://github.com/OpenLMLab/GAOKAO-Bench)  [开源语料](https://opendatalab.org.cn/OpenDataLab/WanJuan1_dot_0) [Label Studio 数据打标](https://zhuanlan.zhihu.com/p/661655147) [2](https://zhuanlan.zhihu.com/p/619033550)

- [xtuner 官方 lora 微调](https://github.com/InternLM/xtuner)

[InternLM-20B 在线使用](https://zhuanlan.zhihu.com/p/658368644)

[分词器](https://github.com/InternLM/InternLM/issues/340) [bug](https://github.com/InternLM/InternLM/pull/342)

[nvidia-docker 先装这个](https://www.codewithgpu.com/docs/nvidia-docker/)

[InternLM-SFT Lora微调 必看](https://github.com/yongzhuo/InternLM-SFT)

- ```
  git clone https://github.com/yongzhuo/InternLM-SFT.git && \
  cd InternLM-SFT
  
  
  
  
  ```

  

response.decode('utf-8')



see echodict\bytepiece\InternLM\tools\tokenizer.py

它的分词器是有 jp 词表的



\\wsl$   win10 在 地址栏输入这个，直接定位到 wsl ubuntu 根目录



wsl 里不需要装显卡驱动，中需要在 ubuntu 里装 cuda toolkit



```

docker run -tid --name nvidia -p 222:22 --privileged=true 95d242fe9108

docker exec -it nvidia /bin/bash


docker run --rm --gpus=all nvidia/cuda:11.8.0-cudnn8-devel-ubuntu20.04 nvidia-smi


wsl --install

curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
  && \
    sudo apt-get update

sudo apt-get install -y nvidia-container-toolkit


wget -O cg-client https://codewithgpu.ks3-cn-beijing.ksyuncs.com/cg-client
chmod +x cg-client


sudo service docker start 
sudo ./cg-client


jupylab -> 打开终端
bash /root/get_started.sh
	# 从 autodl 下载 9.9 G 模型，启动成功后 -> 容器 -> web 服务 就可以玩要了


netsh winsock reset
wsl --unregister Ubuntu

```





```
apt update && \
apt install tmux && \
tmux

source /etc/network_turbo && \
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash && \
apt-get install git-lfs && \
git lfs install && \
cd /root/autodl-tmp && \
git clone https://huggingface.co/internlm/internlm-chat-7b-v1_1



git restore --source=HEAD :/
	# retry

```







```
https://www.codewithgpu.com/i/InternLM/lmdeploy/internlm-chat-20b-lmdeploy

-> AutoDL创建实例 -> 运行中, JupyterLab -> 找开 "终端" ->
bash /root/get_started.sh

server is gonna mount on: http://0.0.0.0:6006
Running on local URL:  http://0.0.0.0:6006
	# 出现这个
	
容器面板 ->自定义服务 -> 应该就可以玩耍了


# 本地安装方法
pip3.10 install codewithgpu && \
cg down InternLM/turbomind-internlm-chat-20b-w4/model.zip


wget -O cg-client https://codewithgpu.ks3-cn-beijing.ksyuncs.com/cg-client && \
chmod +x cg-client && \
./cg-client

```



### ubuntu 22.04

```

disable secure boot in bios
apt install --reinstall linux-headers-$(uname -r)

关闭安全启动 nvidia 驱动就正常加载了。

nvidia-smi

disable secure boot

The target kernel has CONFIG_MODULE_SIG set
UEFI Secure Boot enabled

disable secure boot in bios
apt install --reinstall linux-headers-$(uname -r)


wget https://us.download.nvidia.com/XFree86/Linux-x86_64/535.113.01/NVIDIA-Linux-x86_64-535.113.01.run
	# 下载驱动

 # sh ./NVIDIA-Linux-x86_64-535.113.01.run -s \
--module-signing-secret-key=/usr/share/nvidia/nvidia-modsign-key-C4BF4B44.key \
--module-signing-public-key=/usr/share/nvidia/nvidia-modsign-crt-C4BF4B44.der

Unable to determine the path to install the libglvnd EGL vendor library    
           config files. Check that you have pkg-config and the libglvnd development  
           libraries installed, or specify a path with --glvnd-egl-config-path.

nvidia-smi

NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.

ls /usr/src | grep nvidia
	nvidia-535.113.01

apt install dkms
dkms install -m nvidia -v 535.113.01
	# 安全启动密码是: rootroot
	
dpkg --get-selections | grep linux-image
	linux-image-5.15.0-86-generic                   install
	linux-image-generic                             install
	# 查看已安装内核
	
uname -a
	# 查看正在使用的内核
	
ll /usr/src



wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
	# 下载 cuda toolkit


sh cuda_11.8.0_520.61.05_linux.run
	# /usr/local/cuda-11.8/bin
	# /usr/local/cuda-11.8/lib64

echo 'export PATH=/usr/local/cuda-11.8/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
sudo ldconfig

nvcc
nvidia-smi

```







### wsl 装 cuda toolkit

[WSL2 和 Ubuntu 配置 GPU 机器学习环境](https://leovan.me/cn/2023/03/gpu-machine-learning-environment-configuration-under-windows-with-wsl2-and-ubuntu/)

[cuda-toolkit-archive](https://developer.nvidia.com/cuda-toolkit-archive)



```
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
	# 这是专门 for wsl 版的 cuda toolkit
	
sudo sh cuda_11.8.0_520.61.05_linux.run

Please make sure that
 -   PATH includes /usr/local/cuda-11.8/bin
 -   LD_LIBRARY_PATH includes /usr/local/cuda-11.8/lib64, or, add /usr/local/cuda-11.8/lib64 to /etc/ld.so.conf and run ldconfig as root

To uninstall the CUDA Toolkit, run cuda-uninstaller in /usr/local/cuda-11.8/bin


vi ~/.bashrc # 加在文件尾
export PATH=/usr/local/cuda-11.8/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH


wget https://developer.download.nvidia.com/compute/cuda/11.7.0/local_installers/cuda_11.7.0_515.43.04_linux.run
sudo sh cuda_11.7.0_515.43.04_linux.run

	
```





### trainning

[install 按官方安装指南不出错？](https://github.com/InternLM/InternLM/blob/main/doc/en/install.md)

[FSDP 节省显存？](https://github.com/InternLM/InternLM/pull/273)

[XTuner 微调](https://zhuanlan.zhihu.com/p/663510798)

[How to display output results during the training process](https://github.com/InternLM/InternLM/issues/501)

- ```
              output, label, loss = trainer.execute_schedule(
                  batch, forward_only=False, return_loss=True, return_output_label=True
              )
              """
                  output:
                      len():4
                  output[1]:
                      shape:torch.Size([2048, 103168])
              """
                
              from tools.transformers.tokenization_internlm import InternLMTokenizer as InternLMTokenizer
              tokenizer = InternLMTokenizer(vocab_file='/root/autodl-tmp/internlm-chat-7b-v1_1/tokenizer.model')
              
              tokens = []
              for i in range(2048):
              	probs = output[0][i].tolist()
              	max_val = max(probs)
              	idx = probs.index(max_val)
              	tokens += tokenizer.convert_ids_to_tokens([idx])
                
              result = "".join(tokens)
              print(result)
  ```

  

```

wget https://developer.download.nvidia.com/compute/cuda/11.7.0/local_installers/cuda_11.7.0_515.43.04_linux.run

sudo sh cuda_11.7.0_515.43.04_linux.run

Please make sure that
 -   PATH includes /usr/local/cuda-11.7/bin
 -   LD_LIBRARY_PATH includes /usr/local/cuda-11.7/lib64, or, add /usr/local/cuda-11.7/lib64 to /etc/ld.so.conf and run ldconfig as root


vi ~/.bashrc # 加在文件尾
export PATH=/usr/local/cuda-11.7/bin:$PATH && \
export LD_LIBRARY_PATH=/usr/local/cuda-11.7/lib64:$LD_LIBRARY_PATH




	

# autodl
source /etc/network_turbo && \
~/miniconda3/bin/conda init && \
ln -s ~/miniconda3/bin/conda /usr/local/bin && \
ln -s ~/miniconda3/bin/activate /usr/local/bin && \
ln -s ~/miniconda3/bin/deactivate /usr/local/bin && \
source ~/miniconda3/etc/profile.d/conda.sh

vi /etc/hosts
140.82.112.3 github.com
185.199.108.153 pytorch.org


conda create --name internlm-env python=3.10 -y && \
conda activate internlm-env

conda install -y pytorch==2.0.0 cudatoolkit=11.8 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/linux-64/


export CUDA_HOME=/usr/local/cuda-11.8 && \
export LD_LIBRARY_PATH=${CUDA_HOME}/lib64 && \
PATH=${CUDA_HOME}/bin:${PATH} && \
export PATH


git clone https://github.com/Dao-AILab/flash-attention.git &&＼
cd flash-attention && \
python setup.py install

pip install packaging ninja && \
pip install flash-attn==1.0.5 --no-build-isolation -i https://pypi.tuna.tsinghua.edu.cn/simple






python -m pip install --upgrade pip && \
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
	# pip 换清华源
	

/root/miniconda3/lib/python3.8/site-packages
	# autodl 只有 python3.8 + torch2.0，但需要 python3.10，
    # 打算从这里拷需要的包
    >>> from distutils.sysconfig import get_python_lib
	>>> print(get_python_lib())
/root/miniconda3/envs/internlm-env/lib/python3.10/site-packages
	# /usr/bin/cp -rf /root/miniconda3/lib/python3.8/site-packages /root/miniconda3/envs/internlm-env/lib/python3.10
		# 行不通，弃用


apt update && \
apt install tmux && \
tmux


source /etc/network_turbo && \
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash && \
apt-get install git-lfs && \
git lfs install


git clone https://github.com/InternLM/InternLM.git --recurse-submodules && \
cd InternLM


pip install torch==2.0.0+cu118 torchvision==0.15.1+cu118 torchaudio==2.0.1 --index-url
https://download.pytorch.org/whl/cu118

conda install -c conda-forge pytorch-gpu

pip install -r requirements/runtime.txt && 
pip install tensorboard


cd ./third_party/flash-attention && \
cd ./csrc && \
cd fused_dense_lib && pip install -v . &&\
cd ../xentropy && pip install -v . && \
cd ../rotary && pip install -v . && \
cd ../layer_norm && pip install -v . && \
cd ../../../../


cd ./third_party/apex && \
pip install -v --disable-pip-version-check --no-cache-dir --no-build-isolation --config-settings "--build-option=--cpp_ext" --config-settings "--build-option=--cuda_ext" ./ && \
cd ../../ 
	# 用官网的安装方法，因为 cuda 版本变成　１１．７　

/root/InternLM/configs/i7B_sft.py
SEQ_LEN = 128
HIDDEN_SIZE = 512
NUM_ATTENTION_HEAD = 8
MLP_RATIO = 8 / 3
NUM_LAYER = 4
VOCAB_SIZE = 103168
	# 2080ti 可以
	
SEQ_LEN = 1024
HIDDEN_SIZE = 1024
NUM_ATTENTION_HEAD = 32
MLP_RATIO = 8 / 3
NUM_LAYER = 32
VOCAB_SIZE = 103168
	# 4090 + 80G RAM 正常训练


SAVE_CKPT_FOLDER = "local:/root/saved"
	# 保存目录

ckpt = dict(
    enable_save_ckpt=True,  # 允许保存

TRAIN_FOLDER = "/root/InternLM/traindata_alpaca_nlpp/train"
VALID_FOLDER = "/root/InternLM/traindata_alpaca_nlpp/valid"

parallel = dict(
    zero1=0,　＃改成０
    

torchrun --nnodes=1 --nproc_per_node=1 train.py --config ./configs/i7B_sft.py --launcher "torch"
	＃ 成功运行


internlm/core/scheduler/no_pipeline_scheduler.py
	batch_data, batch_size = engine.load_batch(data_iter)
		# 不知道为什么 batch_size 是 4
	

InternLM/train.py
            output, label, loss = trainer.execute_schedule(
                batch, forward_only=False, return_loss=True, return_output_label=True
            )
            """
                output:
                    len():4
                output[0]:
                    shape:torch.Size([2048, 103168])
            """
            import sentencepiece as spm
            sp_model = spm.SentencePieceProcessor(model_file='/root/autodl-tmp/internlm-chat-7b-v1_1/tokenizer.model')

            # output2 = sp_model.decode(output[0].tolist())


InternLM 目录执行:
export PYTHONPATH=$PWD:$PYTHONPATH && \
python tools/transformers/convert2hf.py --src_folder /root/autodl-tmp/saved/1000 --tgt_folder  /root/autodl-tmp/hf_1000 --tokenizer  /root/autodl-tmp/internlm-chat-7b-v1_1/tokenizer.model
	# 转成 hf 格式
	# https://github.com/InternLM/InternLM/issues/107
		# ~/InternLM# export PYTHONPATH=$PWD:$PYTHONPATH
		# 在 InternLM 根目录执行这一句它才不错


cd /root/autodl-tmp && \
git clone https://huggingface.co/internlm/internlm-chat-7b-v1_1

git restore --source=HEAD :/
	# retry

aliyunpan
login
d --saveto /root/autodl-tmp internlm-chat-7b-v1_1/



pip install tensorboard tensorboardX datasets bitsandbytes peft scipy nltk pydantic rouge

pip install packaging ninja && \
pip install flash_attn==1.0.5 -i https://pypi.tuna.tsinghua.edu.cn/simple

Python == 3.10
GCC == 10.2.0
MPFR == 4.1.0
CUDA >= 11.7
Pytorch >= 1.13.1
Transformers >= 4.28.0
Flash-Attention >= v1.0.5
Apex == 23.05


echodict/bytepiece/InternLM/alpaca_data.json
	# 复制到项目根目录
	# echodict/InternLM-SFT/internlm_sft/dataset/traindata_alpaca_nlpp.json
		# 用这个 nlpp

mkdir traindata_alpaca && \
python tools/alpaca_tokenizer.py alpaca_data.json traindata_alpaca /root/autodl-tmp/internlm-chat-7b-v1_1/tokenizer.model --split_ratio 0.1

InternLM/tools/alpaca_tokenizer.py 改成这样：
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_path", type=str, help="path of dataset json file")
    parser.add_argument("--output_path", type=str, help="path of processed dataset")
    parser.add_argument("--tokenizer_path", type=str, help="path of tokenizer")
    parser.add_argument("--split_ratio", type=float, default=0.1, help="ratio for validation dataset splitting")

    import sys
    sys.argv.append( '--dataset_path' )
    sys.argv.append( 'alpaca_data.json' )
    sys.argv.append( '--output_path' )
    sys.argv.append( 'traindata_alpaca' )
    sys.argv.append( '--tokenizer_path' )
    sys.argv.append( '/root/autodl-tmp/internlm-chat-7b-v1_1/tokenizer.model' )



torchrun --nnodes=1 --nproc_per_node=8 train.py --config ./configs/i7B_sft.py --launcher "torch"
	# 启动训练


/root/InternLM/tools/transformers/evl.py 新建文件
from modeling_internlm import InternLMConfig, InternLMForCausalLM
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("/root/hf", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("/root/hf", trust_remote_code=True).cuda()
model = model.eval()
response, history = model.chat(tokenizer, "hello", history=[])
print(response)
	# 实测正常
	# ~/InternLM# export PYTHONPATH=$PWD:$PYTHONPATH
	# 在 InternLM 根目录执行这一句它才不错


```



```
# 配置含义

TRAIN_FOLDER = "traindata_alpaca"


MODEL_ONLY_FOLDER
	# Path to initialize with given model weights.
	# 官方模型目录
	
LOAD_CKPT_FOLDER
	# Ckpt path to resume training(load weights and scheduler/context states).
	# 微调中间存档目录 应该同 SAVE_CKPT_FOLDER ?
	
SAVE_CKPT_FOLDER
	# 微调结果保存目录
	


```



#### vscode + torchrun

```
lanch.json
{
    // torchrun --nnodes=1 --nproc_per_node=1 train.py --config ./configs/i7B_sft.py --launcher torch
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "/root/miniconda3/envs/internlm-env/bin/torchrun",
            "console": "integratedTerminal",
            "justMyCode": true,
            "args": [
                "--nnodes=1",
                "--nproc_per_node=1",
                "train.py",
                "--config",
                "./configs/i7B_sft.py",
                "--launcher",
                "torch"
            ]
        }
    ]
}
```





### sft nlpp

```
mkdir traindata_alpaca_nlpp && \
python tools/alpaca_tokenizer.py traindata_alpaca_nlpp.json traindata_alpaca_nlp /root/autodl-tmp/internlm-chat-7b-v1_1/tokenizer.model --split_ratio 0.1
```





## nanoGPT

[nanoGPT](https://github.com/karpathy/nanoGPT)

[nanoChatGPT](https://github.com/sanjeevanahilan/nanoChatGPT) 训练奖励模型

[在线使用](https://llava.hliu.cc/)

[nanoGPT源码阅读](https://zhuanlan.zhihu.com/p/601044938)

[issues nanoChatGPT](https://github.com/karpathy/nanoGPT/issues/92)

[极简中英翻译](https://github.com/algernonx/Transformer-Translate-Demo) [1](https://zhuanlan.zhihu.com/p/360343417)



### nanoChatGPT

[nanoChatGPT](https://github.com/VatsaDev/nanoChatGPT)

[nanoT5](https://github.com/PiotrNawrot/nanoT5)

[pythia-12b 微调](https://huggingface.co/OpenAssistant/oasst-sft-1-pythia-12b) 



```
git clone https://github.com/VatsaDev/nanoChatGPT.git
	# source /etc/network_turbo
pip install torch numpy transformers datasets tiktoken wandb tqdm

python data/Chat/prepComm.py 
	# makes train and val

python train.py config/finetune-gpt2.py 
	# finetune

# chatting with the bot
!python chat.py \
    --init_from="huggingface" --context="<human>Hello I like memes<endOfText><bot>I like memes, especially pepe the frog<endOfText>"


https://colab.research.google.com/drive/1a2aW5eClKjHVQJp-qtHDz4m6ai4yh49Z?usp=sharing
```





### Open-GPT

[colab 实战](https://github.com/ShenDezhou/Open-GPT/blob/main/colab/gpt_pretraining_for_beginner_en.ipynb)



see echodict\bytepiece\IGPT



```
pip install transformers datasets tiktoken blobfile
python prepare.py

```





```
只需将“http:// github.com/”替换为“https://colab.research.google.com/github/”，就会直接加载到Colab中 

https://colab.research.google.com/github/ShenDezhou/Open-GPT/blob/main/colab/gpt_pretraining_for_beginner_en.ipynb

```



### gpt2xl

[finetune-gpt2xl  单GPU训练1.5亿参数](https://github.com/Xirider/finetune-gpt2xl)

```
DialoGPT2 是微软在 GPT2 基础上使用对话数据微调过的模型，同样在 Hugging Face 上已经开源，模型已具备对话性能，因此在对话任务上表现会更好，关于 DialoGPT 的文章已发表在 DIALOGPT : Large-Scale Generative Pre-training for Conversational Response Generation 上。
```




## Tokenizer

see echodict\bytepiece\IToken\train_tiktoken.py

​	# 完整训练和使用过程

[How to count tokens with tiktoken](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb)

- [openai tokenizer 在线试用](https://platform.openai.com/tokenizer)
- [tiktoken 训练自已的 tokenizer](https://github.com/ShenDezhou/Open-GPT/blob/main/tokenizer%2Ftrain_tiktoken.py)
- [gpt-tokenizer nodejs实现(有词表)](https://github.com/niieani/gpt-tokenizer)
- [词表扩充实战](https://zhuanlan.zhihu.com/p/631360711)
  - [合并词表的代码](https://github.com/ymcui/Chinese-LLaMA-Alpaca/blob/main/scripts/merge_tokenizer/merge_tokenizers.py)
- [C# 版移值 SharpToken](https://github.com/dmitry-brazhenko/SharpToken)
- [高效Tokenizer: tictoken](https://zhuanlan.zhihu.com/p/631840697)
- [高效中文BPE实现](https://lyk-ai.com/post/2)

| Encoding name           | OpenAI models                                        |
| ----------------------- | ---------------------------------------------------- |
| `cl100k_base`           | `gpt-4`, `gpt-3.5-turbo`, `text-embedding-ada-002`   |
| `p50k_base`             | Codex models, `text-davinci-002`, `text-davinci-003` |
| `r50k_base` (or `gpt2`) | GPT-3 models like `davinci`                          |

[浅谈ChatGPT的Tokenizer](https://zhuanlan.zhihu.com/p/626621158)

[tokenizer 分词器词汇表添加新词](https://blog.csdn.net/weixin_43290383/article/details/128874925)



```
预训练部分又分为两个阶段：

第一阶段：冻结transformer参数，仅训练embedding，在尽量不干扰原模型的情况下适配新增的中文词向量。
第二阶段：使用 LoRA 技术，为模型添加LoRA权重（adapter），训练embedding的同时也更新LoRA参数。

第一步：在训练之前，将除了Embedding之外的层设置为param.requires_grad = False，如下所示：
for name, param in model.named_parameters():
    if "model.embed_tokens" not in name:
        param.requires_grad = False
第二步：在训练的时候，在优化器中添加过滤器filter把requires_grad = False的参数过滤掉，这样在训练的时候，不会更新这些参数，如下所示：
optimizer = AdamW(filter(lambda p: p.requires_grad, model.parameters()))
```





```
pip3.11 install --upgrade tiktoken
pip3.11 install --upgrade openai


```



```
# see echodict\bytepiece\main.py

https://github.com/bojone/bytepiece

AHOCORASICK_BYTES=1 && \
pip3.10 uninstall pyahocorasick && \
proxychains4 pip3.10 install git+https://github.com/WojciechMula/pyahocorasick.git && \
proxychains4 pip3.10 install bytepiece==0.4.1


https://github.com/openai/tiktoken
    # openai 的分词器

```



### 高考题

[高考题](https://github.com/OpenLMLab/GAOKAO-Bench)



## ChatGLM2-6B 全参数微调

[Finetune-ChatGLM2-6B](https://github.com/SpongebBob/Finetune-ChatGLM2-6B/issues/1)

[ChatGLM-Finetuning](https://github.com/liucongg/ChatGLM-Finetuning)

- [zero2](https://blog.csdn.net/weixin_43301333/article/details/127237122)  [zero-offload](https://www.deepspeed.ai/tutorials/zero-offload/) [zero详细说明](https://zhuanlan.zhihu.com/p/646712303) 

  - ```
    ZeRO-1 优化了optimizer state的内存；
    ZeRO-2 优化了optimizer state + gradient的内存；
    ZeRO-3 优化了optimizer state + gradient + weight的内存；
    offload 把一部分GPU内存移到CPU上，进一步节省内存，说是可以让13B的模型在单卡上训练。
        # fp16精度训练，如果你用的是带Tensor Cores的nvidia v100或A100，开这个可以把计算加速8倍。
        # 存的模型参数也会是fp16
        "fp16": {
            "enabled": True  
        },
        # 可以减少GPU的内存消耗
        "zero_optimization": {
            "stage": 3,
            # GPU内存不够，CPU来凑（会降低速度）
            "offload_optimizer": {
                "device": "cpu"
            }
        }
    }
    ```
  
    
  
  ```
  source /etc/network_turbo && \
  conda env list && \
  conda activate internlm-env
  
  # vscode launch.json
  {
      "version": "0.2.0",
      "configurations": [
          {
              "name": "Python: Current File",
              "type": "python",
              "request": "launch",
              "program": "/root/miniconda3/envs/internlm-env/bin/deepspeed",
              "console": "integratedTerminal",
              "justMyCode": true,
              "args": [
                  "--num_gpus=4",
                  "--master_port=7777",
                  "main.py",
                  "--deepspeed",
                  "deepspeed.json",
                  "--do_train",
                  "True",
                  "--do_eval",
                  "False",
                  "--train_file",
                  "belleMath.json",
                  "--validation_file",
                  "belleMath-dev1K.json",
                  "--prompt_column",
                  "conversations",
                  "--overwrite_cache",
                  "True",
                  "--model_name_or_path",
                  "/root/autodl-tmp/chatglm2-6b",
                  "--output_dir",
                  "./output/adgen-chatglm-6b-ft-6e-6-0704",
                  "--overwrite_output_dir",
                "True",
                  "--max_length",
                  "762",
                  "--per_device_eval_batch_size",
                  "1",
                  "--per_device_train_batch_size",
                  "1",
                  "--gradient_accumulation_steps",
                  "12",
                  "--predict_with_generate",
                  "True",
                  "--num_train_epochs",
                  "3",
                  "--logging_steps",
                  "20",
                  "--save_steps",
                  "1000",
                  "--learning_rate",
                  "6e-6",
                  "--fp16",
                  "True",
                  "--save_total_limit",
                  "5"
              ]
          }
      ]
  }
  
  
  /root/miniconda3/envs/internlm-env/bin/python -u -m deepspeed.launcher.launch --world_info=eyJsb2NhbGhvc3QiOiBbMF19 --master_addr=127.0.0.1 --master_port=7777 --enable_each_rank_log=None main.py --deepspeed zero2.json --do_train True --train_file belleMath.json --validation_file belleMath-dev1K.json --prompt_column conversations --overwrite_cache True --model_name_or_path /root/autodl-tmp/chatglm2-6b --output_dir ./output/adgen-chatglm-6b-ft-6e-6-0704 --overwrite_output_dir True --max_length 512 --per_device_eval_batch_size 1 --per_device_train_batch_size 1 --gradient_accumulation_steps 12 --predict_with_generate True --num_train_epochs 3 --logging_steps 20 --save_steps 1000 --learning_rate 6e-6 --fp16 True --save_total_limit 5
  
  https://github.com/THUDM/ChatGLM-6B/issues/530
  在使用 DeepSpeed 进行分布式训练时，DeepSpeed 会将模型分割成多个分块并分配给不同的 GPU 进行训练。在这个过程中，DeepSpeed 会使用 PyTorch 的 DistributedDataParallel 包装器来实现分布式训练，而 DistributedDataParallel 需要对模型进行初始化。
  当您使用 AutoModel.from_pretrained() 方法加载预训练模型时，模型权重会被存储在 PyTorch 的 nn.Parameter 对象中。在没有指定 empty_init=False 参数时，nn.Parameter 对象的值将被初始化为全零的张量。但是，由于 nn.Parameter 对象不是真正的张量，而是具有元数据的张量包装器，因此无法将这些对象直接复制到 DeepSpeed 使用的元数据张量中。
  在指定 empty_init=False 参数后，nn.Parameter 对象将被初始化为包含预训练权重的张量，这使得 DeepSpeed 能够正常地将权重复制到元数据张量中，从而避免了 NotImplementedError: Cannot copy out of meta tensor; no data! 错误的出现。
  综上所述，您遇到的问题是因为在使用 DeepSpeed 进行分布式训练时，模型权重的初始化方式与普通的训练方式不同，因此需要通过指定 empty_init=False 参数来解决。
  
  NotImplementedError: Cannot copy out of meta tensor; no data! 这个错误通常是由于Deepspeed在使用自定义权重初始化时出现问题，而这些初始化可能需要从先前的训练中加载权重。如果在使用Deepspeed进行分布式训练时出现此错误，则需要在初始化模型时指定empty_init=False，以便在加载权重之前，权重矩阵不会被初始化为空。
  AutoModel.from_pretrained是Hugging Face Transformers库中的一个方法，用于从预训练模型中加载权重。在Deepspeed分布式训练中，模型的初始化和权重加载可能需要特殊处理，因此需要使用empty_init=False参数来指定在加载权重之前不要将权重矩阵初始化为空。
  在其他模型中，可能不需要这个参数是因为它们的初始化和权重加载不需要特殊处理，或者因为它们的代码已经进行了相应的修改以适应Deepspeed的分布式训练流程。
  
  2*V100-32G成功跑起来了，我建议的步骤是：
  
  拉取最新的chatglm代码和模型，最新的transformers，最新的deepspeed，分别安装好。我的transformers版本为4.28.1，deepspeed版本为0.9.0
  main.py文件，修改模型读取参数，model = AutoModel.from_pretrained(model_args.model_name_or_path, config=config, empty_init=False, trust_remote_code=True)
  ds_train_finetune.sh，删除quantization_bit参数，per_device_train_batch_size、max_source_length、max_target_length调低
  修改deepspeed.json文件，我的配置如下：
  {
    "train_micro_batch_size_per_gpu": "auto",
    "zero_allow_untested_optimizer": true,
    "fp16": {
      "enabled": "auto",
      "loss_scale": 0,
      "initial_scale_power": 16,
      "loss_scale_window": 1000,
      "hysteresis": 2,
      "min_loss_scale": 1
    },
    "bf16": {
      "enabled": "auto"
  },
  "optimizer": {
    "type": "AdamW",
    "params": {
        "lr": "auto",
        "betas": "auto",
        "eps": "auto",
        "weight_decay": "auto"
    }
  },
    "zero_optimization": {
      "stage": 3,
      "offload_optimizer": {
        "device": "cpu",
        "pin_memory": true
    },
    "offload_param": {
        "device": "cpu",
        "pin_memory": true
    },
      "allgather_partitions": true,
      "allgather_bucket_size": 5e8,
      "reduce_scatter": true,
      "contiguous_gradients" : true,
      "overlap_comm": true,
      "sub_group_size": 1e9,
      "reduce_bucket_size": "auto",
      "stage3_prefetch_bucket_size": "auto",
      "stage3_param_persistence_threshold": "auto",
      "stage3_max_live_parameters": 1e9,
      "stage3_max_reuse_distance": 1e9,
      "stage3_gather_16bit_weights_on_model_save": true
    }
  }
  
  ```
  



4 * 3090 就可以?

```
用dp zero 2， 长度拉小点一般256-512就够了，我用2个40g，4个3090 都测试过，可以跑，如果跑一半不可以，就可能是长度问题。

我的deepspeed用的是zero3，把优化器和模型参数都offload到内存，以便减少GPU显存的使用

不过在较小的batch size、较短的长度、启用deepspeed zero-3、有充足的内存的情况下，8张32GB的V100也可以运行


如果显存不足，可采用stage 3，该模式下模型参数将分布在多张显卡上，可显著减小显存占用，对应的配置文件是configs/deepspeed_config_stage3.json
	# https://blog.csdn.net/sinat_37574187/article/details/132088723
	# https://github.com/LianjiaTech/BELLE/blob/main/train/configs/deepspeed_config_stage3.json
	

```



```
git clone https://github.com/SpongebBob/Finetune-ChatGLM2-6B.git && \
cd Finetune-ChatGLM2-6B

wget https://huggingface.co/datasets/BelleGroup/school_math_0.25M/resolve/main/school_math_0.25M.json

python convert_to_conv_data.py --orig_data school_math_0.25M.json --write_data school_math_0.25M_conv.json --dataset_name bellemath && \
head -n 1000 school_math_0.25M_conv.json > belleMath-dev1K.json && \
tail -n +1001 school_math_0.25M_conv.json > belleMath.json

取前1000条作为验证集，其余数据作为训练集


# 先装好 chatglm2-6B 的依赖包，再装：
pip uninstall transformers && \
pip install transformers==4.28.1 && \
pip install rouge_chinese nltk jieba datasets


Finetune-ChatGLM2-6B/ds_train_finetune.sh
	MASTER_PORT=7777
	--num_gpus=4
	--max_length 512
	--model_name_or_path /root/autodl-tmp/chatglm2-6b
	# 改这里, max_length 512 调下点显存占用就会大大降低
	
pip install deepspeed && \
ds_report



bash ds_train_finetune.sh
	# 开始全量微调


--deepspeed ds_config.json


注意：如果打开自定义服务提示使用ssh隧道，请参考这个视频操作：https://www.bilibili.com/video/BV1Pk4y1w7Pk


```



```
Finetune-ChatGLM2-6B/ds_train_finetune.sh

#!/bin/bash

LR=6e-6
DATE=0704

MASTER_PORT=7777

deepspeed --num_gpus=4 --master_port $MASTER_PORT main.py \
    --do_train \
    --do_eval \
    --train_file belleMath.json \
    --validation_file belleMath-dev1K.json \
    --prompt_column conversations \
    --overwrite_cache \
    --model_name_or_path /root/autodl-tmp/chatglm2-6b \
    --output_dir ./output/adgen-chatglm-6b-ft-$LR-$DATE \
    --overwrite_output_dir \
    --max_length 256 \
    --deepspeed ds_zero2_no_offload.json \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 12 \
    --predict_with_generate \
    --num_train_epochs 3 \
    --logging_steps 20 \
    --save_steps 1000 \
    --learning_rate $LR \
    --do_eval False \
    --fp16 True \
    --save_total_limit 5 \

```





```

链接：https://www.zhihu.com/question/591112394/answer/3251379946

经实践过，在一些特定的限制资料的场景，可以用来当一个极其节省现存的推断方案。具体的流程可以讲解为：1.创建一个空的（例如，没有权重的）模型2.决定每一层将要去哪里（当有多个设备可用时）3.在内存中加载其权重的一部分4.在空模型中加载这些权重5.将权重移动到设备上进行推理 6.从第3步重复，直到所有的权重都被加载这个过程实现得益得以依赖于pytorch 1.9的一个叫meta device的玩意儿，PyTorch 1.9引入了一种新的设备，称为元设备(meta device)。这使我们能够创建没有任何数据附加的张量，元设备上的张量只需要一个shape，只要你在元设备上，你就可以创建任意大的张量，而不必担心CPU（或GPU）的RAM够不够。比如下面的代码，内存不够的话就会崩掉import torch
large_tensor = torch.randn(100000, 100000)
这个大张量需要4 * 10**10字节（默认精度是FP32，所以张量的每个元素占用4字节），因此需要40GB的RAM。然而，在元设备上执行相同的操作就可以正常运行：import torch
large_tensor = torch.randn(100000, 100000, device="meta")
这个张量没有关联的数据，只有一个形状。你可以直接在元设备上实例化一个模型：large_model = torch.nn.Linear(100000, 100000, device="meta")
但是对于现成的模型来说，这种语法需要你重写所有的建模代码，以便每个模型的子部分都接受并传递一个设备关键字参数。由于这对Transformers库的预训练模型来说不切实际，accelerate库有一个context manager，整合了meta device可以实例化一个空模型。# Load meta model (no memory used)
with init_empty_weights():
    self.model = AutoModelForCausalLM.from_config(self.config, trust_remote_code=True)
    self.model.tie_weights()
这一步很关键，我们知道每个权重的形状，因此我们可以知道一旦我们完全加载预训练的张量，它们将消耗多少内存。因此，我们可以决定如何在CPU和GPU之间分割我们的模型。除此之外，定义了两个关键的方法，分别是load_layer_to_cpu，负责把 权重从disk挪到CPU，另外一个是move_layer_to_device，负责把权重从cpu挪到显卡。还有一个释放显存的方法clean_memory，负责清空显存。def load_layer_to_cpu(self, layer_name):
    self.weights_loader.set_state_dict(layer_name, self.device)
    state_dict = self.weights_loader.get_state_dict(self.device)
    if "value_head.weight" in state_dict:
        state_dict = {"lm_head.weight" : state_dict["value_head.weight"]}
    return state_dict
    
def move_layer_to_device(self, state_dict):
    for param_name, param in state_dict.items():
        assert param.dtype != torch.int8, "int8 not supported (need to add fp16_statistics)"
        set_module_tensor_to_device(self.model, param_name, self.device, value=param, dtype=self.dtype)

def clean_memory():
    gc.collect()
    ctypes.CDLL("libc.so.6").malloc_trim(0)
    torch.cuda.empty_cache()
好了，对过程大概弄懂了就可以看完整的代码了。注意，下面的代码也包含了题目设定里特定的prefix和suffix，正常的推理可以忽略相关的逻辑，仅保留一个prompt即可。下面展示完整的代码# For LLM
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer, AutoModel
from accelerate import init_empty_weights
from accelerate.utils.modeling import set_module_tensor_to_device
from safetensors.torch import load_file
from optimum.bettertransformer import BetterTransformer

N_BATCHES = 3
MAX_LENGTH = 4096

def clean_memory():
    gc.collect()
    ctypes.CDLL("libc.so.6").malloc_trim(0)
    torch.cuda.empty_cache()


# Class for sharded llama
class ShardedLlama:
    def __init__(self, checkpoint_path, weights_loader, device="cuda:0", dtype=torch.float16):

        # Save parameters
        self.checkpoint_path = Path(checkpoint_path)
        self.weights_loader = weights_loader
        self.device = device 
        self.dtype = dtype

        # Create model
        self.config = AutoConfig.from_pretrained(self.checkpoint_path)   
        self.tokenizer = AutoTokenizer.from_pretrained(checkpoint_path)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.tokenizer.padding_side = "right"
        self.init_model()
        self.layer_names = ["model.embed_tokens"] + [f"model.layers.{i}" for i in range(len(self.model.model.layers))] + ["model.norm", "value_head"]

    def init_model(self):
    
        # Load meta model (no memory used)
        with init_empty_weights():
            self.model = AutoModelForCausalLM.from_config(self.config)
            self.model.lm_head = torch.nn.Linear(8192, 8, bias=False) # originally 32k
            self.model.eval()
            self.model = BetterTransformer.transform(self.model) # enable flash attention
            self.model.tie_weights()
            
        self.layers = [self.model.model.embed_tokens] + list(self.model.model.layers) + [self.model.model.norm, self.model.lm_head]

        # Move buffers to device (note that much GPU memory used)
        for buffer_name, buffer in self.model.named_buffers():
            set_module_tensor_to_device(self.model, buffer_name, self.device, value=buffer, dtype=self.dtype)

    def load_layer_to_cpu(self, layer_name):
        self.weights_loader.set_state_dict(layer_name, self.device)
        state_dict = self.weights_loader.get_state_dict(self.device)
        if "value_head.weight" in state_dict:
            state_dict = {"lm_head.weight" : state_dict["value_head.weight"]}
        return state_dict
        
    def move_layer_to_device(self, state_dict):
        for param_name, param in state_dict.items():
            assert param.dtype != torch.int8, "int8 not supported (need to add fp16_statistics)"
            set_module_tensor_to_device(self.model, param_name, self.device, value=param, dtype=self.dtype)

    def __call__(self, inputs):
        # inputs = [(prefix, suffix), ...] with prefix.shape[0] = 1 and suffix.shape[0] = 5
        
        # Reboot the model to make sure buffers are loaded and memory is clean
        del self.model
        clean_memory()
        self.init_model()
        
       # Send batch to device
        batch = [(prefix.to(self.device), suffix.to(self.device)) for prefix, suffix in inputs]
        n_suffixes = len(batch[0][1])
        suffix_eos = [(suffix != self.tokenizer.pad_token_id).sum(1) - 1 for _, suffix in inputs]

        # Create attention mask for the largest input, and position ids to use KV cache
        attention_mask = torch.ones(MAX_LENGTH, MAX_LENGTH)
        attention_mask = attention_mask.triu(diagonal=1)[None, None, ...] == 0
        attention_mask = attention_mask.to(self.device)
        position_ids = torch.arange(MAX_LENGTH, dtype=torch.long, device=self.device)[None, :]

        with ThreadPoolExecutor() as executor, torch.inference_mode():

            # Load first layer
            future = executor.submit(self.load_layer_to_cpu, "model.embed_tokens")

            for i, (layer_name, layer) in tqdm(enumerate(zip(self.layer_names, self.layers)), desc=self.device, total=len(self.layers)):

                # Load current layer and prepare next layer
                state_dict = future.result()
                if (i + 1) < len(self.layer_names):
                    future = executor.submit(self.load_layer_to_cpu, self.layer_names[i + 1])
                self.move_layer_to_device(state_dict)
                
                # Run layer
                for j, (prefix, suffix) in enumerate(batch):
                    if layer_name == "model.embed_tokens":
                        batch[j] = (layer(prefix), layer(suffix))
                    elif layer_name == "model.norm":
                        # Only keep the last token at this point
                        batch[j] = (None, layer(suffix[torch.arange(n_suffixes), suffix_eos[j]][:, None]))
                    elif layer_name == "value_head":
                        batch[j] = layer(suffix)[:, 0].mean(1).detach().cpu().numpy()
                    else:
                        # Run prefix
                        len_p, len_s = prefix.shape[1], suffix.shape[1]
                        new_prefix, (k_cache, v_cache) = layer(prefix, use_cache=True, attention_mask=attention_mask[:, :, -len_p:, -len_p:])
                        
                        # Run suffix
                        pos = position_ids[:, len_p:len_p + len_s].expand(n_suffixes, -1)
                        attn = attention_mask[:, :, -len_s:, -len_p - len_s:].expand(n_suffixes, -1, -1, -1)
                        kv_cache = (k_cache.expand(n_suffixes, -1, -1, -1), v_cache.expand(n_suffixes, -1, -1, -1))
                        new_suffix = layer(suffix, past_key_value=kv_cache, position_ids=pos, attention_mask=attn)[0]
                        batch[j] = (new_prefix, new_suffix)

                # Remove previous layer from memory (including buffers)
                layer.to("meta")
                clean_memory() # proposed by CPMP

        # Get scores
        return batch




def run_model(device, df, weights_loader):
    model = ShardedLlama(checkpoint_path, weights_loader, device=device)
    f = partial(get_tokens, tokenizer=model.tokenizer)
    inputs = df.apply(f, axis=1).values
    batches = np.array_split(inputs, N_BATCHES)
    outputs = []
    for i, batch in enumerate(batches):
        outputs += model(batch)
    return outputs
```



### LLaMA-Factory 必看

[LLaMA-Factory 必看](https://github.com/hiyouga/LLaMA-Factory)

```

影响模型训练效果的参数主要有下面几个
lora_rank(int,optional): LoRA 微调中的秩大小。这里并不是越大越好，对于小型数据集如果r=1就可以达到很不错的效果，即便增加r得到的结果也没有太大差别。

lora_alpha(float,optional): LoRA 微调中的缩放系数。

lora_dropout(float,optional): LoRA 微调中的 Dropout 系数。

learning_rate(float,optional): AdamW 优化器的初始学习率。如果设置过大会出现loss值无法收敛或过拟合现象即过度适应训练集而丧失泛化能力，对非训练集中的数据失去原本的计算能力。

num_train_epochs(float,optional): 训练轮数，如果loss值没有收敛到理想值可以增加训练轮数或适当降低学习率。


CUDA_VISIBLE_DEVICES=0 python src/train_bash.py \
    --stage sft \
    --model_name_or_path /root/autodl-tmp/chatglm2-6b \
    --do_train \
    --dataset /root/LLaMA-Factory/data/alpaca_data_zh_51k.json \
    --template default \
    --finetuning_type lora \
    --lora_target q_proj,v_proj \
    --output_dir output_sft \
    --overwrite_cache \
    --per_device_train_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --lr_scheduler_type cosine \
    --logging_steps 10 \
    --save_steps 1000 \
    --learning_rate 5e-5 \
    --num_train_epochs 3.0 \
    --plot_loss \
    --fp16

```





## LoRA 微调原理

[梯度视角下的LoRA：简介、分析、猜测及推广](https://kexue.fm/archives/9590)

[ChatGLM-6B模型结构组件源码阅读](https://blog.csdn.net/yjh_SE007/article/details/130728164)

[ChatGLM2-6B流程解析与TPU-MLIR部署](https://zhuanlan.zhihu.com/p/641975976)

[源码解析ChatGLM2多轮对话训练方法的不足](https://zhuanlan.zhihu.com/p/647733151)



### numpy-transformer

[numpy-transformer](https://github.com/AkiRusProd/numpy-transformer)

```
see huggingface/numpy-transformer
	# 已调通 cuda11.3 4090 也可以用
git clone https://github.com/AkiRusProd/numpy-transformer.git && \
cd numpy-transformer
	# 它的收敛不太好

# 它的数据集挂了 see 从零起频的
from torchtext.datasets import multi30k, Multi30k
multi30k.URL = {
    "train": r"https://raw.githubusercontent.com/neychev/small_DL_repo/master/datasets/Multi30k/training.tar.gz",
    "valid": r"https://raw.githubusercontent.com/neychev/small_DL_repo/master/datasets/Multi30k/validation.tar.gz",
    "test": r"https://raw.githubusercontent.com/neychev/small_DL_repo/master/datasets/Multi30k/mmt16_task1_test.tar.gz",
}
multi30k.MD5 = {
    "train": "20140d013d05dd9a72dfde46478663ba05737ce983f478f960c1123c6671be5e",
    "valid": "a7aa20e9ebd5ba5adce7909498b94410996040857154dab029851af3a866da8c",
    "test": "6d1ca1dba99e2c5dd54cae1226ff11c2551e6ce63527ebb072a1f70f72a5cd36",
}
data_train = Multi30k(split='train')
data_val = Multi30k(split='valid')
data_test = Multi30k(split='test')
# train, val, test = datasets.Multi30k(language_pair=("de", "en"))



```





### minGPT 两位数加法

[minGPT 两位数加法 必看](https://github.com/karpathy/minGPT/blob/master/projects/adder/adder.py)



### picoGPT Numpy 实现

[picoGPT Numpy 实现 必看](https://github.com/jaymody/picoGPT)  [simpleGPT 同作者 torch 实现](https://github.com/jaymody/simpleGPT)

- ```
  python gpt2.py \
      "Alan Turing theorized that computers would one day become" \
      --n_tokens_to_generate 40 \
      --model_size "124M" \
      --models_dir "models"
  
  
  pip install tensorflow-cpu
  	# 最新版的就行
  
  tensorflow==2.11.0
  
  
  
  
  # simpleGPT
  conda env remove -n SP
  conda create -n SP python=3.10 -y
  conda activate SP
  pip install torch==2.0.1 --index-url https://download.pytorch.org/whl/cpu
  	# ok，但是太慢
  	
  pip install torch==2.0.1 pytorch-cuda=11.7
  	# 换这个
  	# pytorch-cuda=11.8 也可以
  	# conda install -y pytorch-cuda==11.7 -c pytorch -c nvidia
  
  
  ```

[gpt2 原版 必看](https://github.com/openai/gpt-2/blob/master/DEVELOPERS.md)

- [安装指南](https://github.com/openai/gpt-2/pull/186/files) [tf+cuda](https://stackoverflow.com/questions/50622525/which-tensorflow-and-cuda-version-combinations-are-compatible) [gcc4.8](https://gist.github.com/application2000/73fd6f4bf1be6600a2cf9f56315a2d91)  [how to train it](https://github.com/openai/gpt-2/issues/19) [colab](https://colab.research.google.com/github/ak9250/gpt-2-colab/blob/master/GPT_2.ipynb)

- ```
  RTX 2080 Ti(11GB) + 
  Python3.8 + ubuntu18.04 + Cuda10.0 
  
  git clone https://huggingface.co/datasets/dlxjj/transformer
  	# 以后的代码在抱抱脸更新
  
  git clone https://github.com/openai/gpt-2.git && cd gpt-2
  
  conda create -n gpt2 pip python=3.7 && \
  conda activate gpt2
  
  pip install protobuf==3.20 && \
  pip install tensorflow-gpu==1.15.0 && \
  pip install -r requirements.txt
  
  export PYTHONIOENCODING=UTF-8 && \
  python3 src/interactive_conditional_samples.py --top_k 40
  
  
  117M model with fp16, per_gpu_train_batch_size=1 and block_size=256 on gpu 6gb
  ```

[Transformer代码复现 必看](http://www.egbenz.com/#/my_article/49)

[picoGPT 中文训练 必看](https://github.com/bigeagle/picoGPT) [blog](https://bigeagle.me/2023/03/pico-gpt-1/)

- [numpy实现embedding层的前向传播和反向传播 必看](https://zhuanlan.zhihu.com/p/642997702)
- [numpy 古诗 必看](https://github.com/ZouJiu1/numpy_transformer/blob/master/gpt/gpt_train_potry3000.py)

- [nn.Embedding的基本使用](https://blog.csdn.net/zhaohongfei_358/article/details/122809709)
- [各种归一化层及其Pytorch实现](https://blog.csdn.net/qq_23981335/article/details/106572171)

- ```
  git clone https://github.com/bigeagle/picoGPT.git && \
  cd picoGPT && \
  conda activate internlm-env && \ 
  pip3 install rich loguru
  
  python3 train.py --lr=1e-3 --batch-size=32 --block-size=128 --embed-size=512 --depth=4 --num-heads=4 --dropout=0.1
  ```

  



```

conda create -n pico pip python=3.9.10
conda activate pico
	# conda deactivate

pip3 install -r requirements.txt


```



#### TinyGPT C++实现

[手写一个 GPT (TinyGPT)](https://zhuanlan.zhihu.com/p/650022129)





### 从零起步的 Transformer 与代码拆解

see echodict\transformer\picoGPT_chinese\chat.py

https://github.com/google/jax/issues?q=autograd

[annotated transformer 必看有代码](https://github.com/harvardnlp/annotated-transformer/) [1](https://blog.csdn.net/v_JULY_v/article/details/130090649)

[torch+jax 双版本](https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial6/Transformers_and_MHAttention.html)  [flax good](https://zhuanlan.zhihu.com/p/541782955) [注意力机制 动手深度学习](https://zh.d2l.ai/chapter_attention-mechanisms/index.html)

- ```
  
  # see echodict\transformer\t3.py
  
  the attention mechanism describes a weighted average of (sequence) elements with the weights dynamically computed based on an input query and elements’ keys. 
  
  注意力机制描述了基于输入查询和元素键动态计算的权重，对（序列）元素进行加权平均。
  
  目标是对多个元素的特征取平均值。然而，我们并不想给每个元素相同的权重，而是根据它们实际的值来赋予权重。换句话说，我们想要动态地决定哪些输入我们希望“更多关注”。特别是，一个注意力机制通常有我们需要指定的四个部分：
  
  查询（Query）：查询是一个特征向量，描述了我们在序列中寻找什么，即我们可能想要关注的内容。
  
  键（Keys）：对于每个输入元素，我们都有一个键，这同样是一个特征向量。这个特征向量大致描述了该元素“提供”的内容，或者它何时可能重要。键应该被设计成能够基于查询识别出我们想要关注的元素。
  
  值（Values）：对于每个输入元素，我们还有一个值向量。这个特征向量就是我们想要取平均值的向量。
  
  评分函数（Score function）：为了评估我们想要关注哪些元素，我们需要指定一个评分函数。评分函数将查询和一个键作为输入，并输出查询-键对的得分/注意力权重。它通常由简单的相似度度量来实现，如点积或一个小的多层感知器（MLP）。
  
  平均值的权重是通过对所有评分函数输出进行softmax计算得到的。因此，我们给予那些其对应键与查询最为相似的值向量更高的权重。
  
  对于每个单词，我们有一个键向量（key vector）和一个值向量（value vector）。查询与所有键通过得分函数（在这种情况下为点积）进行比较以确定权重。为了简化，softmax没有被可视化。最后，使用注意力权重对所有单词的值向量进行平均。
  
  大多数注意力机制在它们使用的查询、如何定义键向量和值向量以及使用的得分函数方面有所不同。转换器架构内部应用的注意力称为自注意力（self-attention）。在自注意力中，每个序列元素提供一个键、一个值和一个查询。对于每个元素，我们执行一个注意力层，在这个层中，根据其查询，我们检查所有序列元素键的相似性，并为每个元素返回一个不同的、经过平均的值向量。我们现在将通过首先查看Transformer案例中的注意力机制的具体实现——缩放点积注意力——来更详细地介绍。
  
  
  import torch
  x = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
  mask = torch.Tensor([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]])
  # 将 mask 为 0 的位置替换成 -1
  new_x = x.masked_fill(mask == 0, -1)
  print(new_x)
  
  
  # pytorch
  def scaled_dot_product(q, k, v, mask=None):
      d_k = q.size()[-1]
      attn_logits = torch.matmul(q, k.transpose(-2, -1))
      attn_logits = attn_logits / math.sqrt(d_k)
      if mask is not None:
          attn_logits = attn_logits.masked_fill(mask == 0, -9e15)
      attention = F.softmax(attn_logits, dim=-1)
      values = torch.matmul(attention, v)
      return values, attention
      
  seq_len, d_k = 3, 2
  pl.seed_everything(42)
  q = torch.randn(seq_len, d_k)
  k = torch.randn(seq_len, d_k)
  v = torch.randn(seq_len, d_k)
  values, attention = scaled_dot_product(q, k, v)
  print("Q\n", q)
  print("K\n", k)
  print("V\n", v)
  print("Values\n", values)
  print("Attention\n", attention)
  
  # jax
  def scaled_dot_product(q, k, v, mask=None):
      d_k = q.shape[-1]
      attn_logits = jnp.matmul(q, jnp.swapaxes(k, -2, -1))
      attn_logits = attn_logits / math.sqrt(d_k)
      if mask is not None:
          attn_logits = jnp.where(mask == 0, -9e15, attn_logits)
      attention = nn.softmax(attn_logits, axis=-1)
      values = jnp.matmul(attention, v)
      return values, attention
  
  seq_len, d_k = 3, 2
  main_rng, rand1 = random.split(main_rng)
  qkv = random.normal(rand1, (3, seq_len, d_k))
  q, k, v = qkv[0], qkv[1], qkv[2]
  values, attention = scaled_dot_product(q, k, v)
  
  
  k.transpose(-2, -1)
  	# -2 表示倒数第二个维度
  	# -1 表示倒数第一个维度
  	# 函数把指定的两个维度互换
  	
  
  缩放点积注意力机制允许网络对序列进行关注。然而，通常一个序列元素想要关注多个不同的方面，单一加权平均并不是一个好的选择。这就是为什么我们将注意力机制扩展到多头上，即在相同特征上应用多组不同的查询-键-值三元组。具体来说，给定查询矩阵、键矩阵和值矩阵，我们将它们转换为子查询、子键和子值，并将它们分别通过缩放点积注意力处理。之后，我们将各个头连接起来，并用最终的权重矩阵结合它们。
  
  
  # pytorch
  def expand_mask(mask):
      assert mask.ndim >= 2, "Mask must be at least 2-dimensional with seq_length x seq_length"
      if mask.ndim == 3:
          mask = mask.unsqueeze(1)
      while mask.ndim < 4:
          mask = mask.unsqueeze(0)
      return mask
  
  class MultiheadAttention(nn.Module):
  
      def __init__(self, input_dim, embed_dim, num_heads):
          super().__init__()
          assert embed_dim % num_heads == 0, "Embedding dimension must be 0 modulo number of heads."
  
          self.embed_dim = embed_dim
          self.num_heads = num_heads
          self.head_dim = embed_dim // num_heads
  
          # Stack all weight matrices 1...h together for efficiency
          # Note that in many implementations you see "bias=False" which is optional
          self.qkv_proj = nn.Linear(input_dim, 3*embed_dim)
          self.o_proj = nn.Linear(embed_dim, embed_dim)
  
          self._reset_parameters()
  
      def _reset_parameters(self):
          # Original Transformer initialization, see PyTorch documentation
          nn.init.xavier_uniform_(self.qkv_proj.weight)
          self.qkv_proj.bias.data.fill_(0)
          nn.init.xavier_uniform_(self.o_proj.weight)
          self.o_proj.bias.data.fill_(0)
  
      def forward(self, x, mask=None, return_attention=False):
          batch_size, seq_length, _ = x.size()
          if mask is not None:
              mask = expand_mask(mask)
          qkv = self.qkv_proj(x)
  
          # Separate Q, K, V from linear output
          qkv = qkv.reshape(batch_size, seq_length, self.num_heads, 3*self.head_dim)
          qkv = qkv.permute(0, 2, 1, 3) # [Batch, Head, SeqLen, Dims]
          q, k, v = qkv.chunk(3, dim=-1)
  
          # Determine value outputs
          values, attention = scaled_dot_product(q, k, v, mask=mask)
          values = values.permute(0, 2, 1, 3) # [Batch, SeqLen, Head, Dims]
          values = values.reshape(batch_size, seq_length, self.embed_dim)
          o = self.o_proj(values)
  
          if return_attention:
              return o, attention
          else:
              return o
  
  
  # jax
  class MultiheadAttention(nn.Module):
      embed_dim : int  # Output dimension
      num_heads : int  # Number of parallel heads (h)
  
      def setup(self):
          # Stack all weight matrices 1...h and W^Q, W^K, W^V together for efficiency
          # Note that in many implementations you see "bias=False" which is optional
          self.qkv_proj = nn.Dense(3*self.embed_dim,
                                   kernel_init=nn.initializers.xavier_uniform(),  # Weights with Xavier uniform init
                                   bias_init=nn.initializers.zeros  # Bias init with zeros
                                  )
          self.o_proj = nn.Dense(self.embed_dim,
                                 kernel_init=nn.initializers.xavier_uniform(),
                                 bias_init=nn.initializers.zeros)
  
      def __call__(self, x, mask=None):
          batch_size, seq_length, embed_dim = x.shape
          if mask is not None:
              mask = expand_mask(mask)
          qkv = self.qkv_proj(x)
  
          # Separate Q, K, V from linear output
          qkv = qkv.reshape(batch_size, seq_length, self.num_heads, -1)
          qkv = qkv.transpose(0, 2, 1, 3) # [Batch, Head, SeqLen, Dims]
          q, k, v = jnp.array_split(qkv, 3, axis=-1)
  
          # Determine value outputs
          values, attention = scaled_dot_product(q, k, v, mask=mask)
          values = values.transpose(0, 2, 1, 3) # [Batch, SeqLen, Head, Dims]
          values = values.reshape(batch_size, seq_length, embed_dim)
          o = self.o_proj(values)
  
          return o, attention
  
  
  ## Test MultiheadAttention implementation
  # Example features as input
  main_rng, x_rng = random.split(main_rng)
  x = random.normal(x_rng, (3, 16, 128))
  # Create attention
  mh_attn = MultiheadAttention(embed_dim=128, num_heads=4)
  # Initialize parameters of attention with random key and inputs
  main_rng, init_rng = random.split(main_rng)
  params = mh_attn.init(init_rng, x)['params']
  # Apply attention with parameters on the inputs
  out, attn = mh_attn.apply({'params': params}, x)
  print('Out', out.shape, 'Attention', attn.shape)
  
  del mh_attn, params
  
  
  
  qkv.permute(0, 2, 1, 3)
  	# 重排列向量维度
  	# 正常的排列是 0, 1, 2, 3
  	# 函数把原来的 1 和 2 维互换了位置
  
  
  mask = mask.unsqueeze(1) # [SeqLen, SeqLen] -> [SeqLen, 1, SeqLen]
  mask = mask.unsqueeze(0) # [SeqLen, SeqLen] -> [1, SeqLen, SeqLen]
  	# 在指定位置添加一个新维度，它的后面维度依次往后挪
  	
  
  
  
  
  ```



### Transformer 中的注意力机制

Transformer是一种深度学习模型，常用于处理序列数据如自然语言处理任务。该模型的核心部分是**注意力机制**（Attention Mechanism），它使得模型能够在处理信息时，对重要的部分给予更多的关注。

#### 基本概念

- **注意力权重**：这些权重决定了模型在查看输入序列时，应该“注意”哪些部分更多。
- **查询（Query）**、**键（Key）**和**值（Value）**：这三个部分构成了注意力计算的基础。每个元素都会根据自身生成一个查询向量，同时也会产生一个键向量和一个值向量。

#### 工作原理

1. **打分**：模型通过计算每个查询与其他所有键之间的匹配程度来打分，通常使用点积来进行度量。
2. **归一化**：接着，利用softmax函数对这些分数进行归一化，以便分数的总和为1，这意味着把分数转换为概率。
3. **加权求和**：最后，将值（Value）向量与这些归一化的权重相乘，并对所有位置上的结果进行求和，得到最终的输出。

#### 举例说明

假设我们有一个句子："The cat sat on the mat." 要翻译成另一种语言。在处理"sat"这个词时，模型可能会赋予"The cat"比"the mat"更多的注意力，因为它们与"sat"在语法和意义上更相关。

#### 多头注意力

Transformer模型使用了所谓的**多头注意力**（Multi-Head Attention），可以想象成是多组不同的“查询-键-值”集合，每个集合关注不同的信息方面，增强了模型的能力去并行地处理多种类型的信息。

#### 优势

- **并行处理**：注意力机制允许模型同时处理整个序列，而非像循环神经网络（RNN）那样逐个元素处理。
- **捕获长距离依赖**：它可以轻松地捕获序列中相隔很远的元素间的相关性，这对于像语言这样有复杂结构的数据特别重要。
- **灵活性**：注意力机制在处理各种长度的序列时表现出极大的灵活性，因此可以被用于各种大小的输入数据。

总结来说，注意力机制是Transformer架构的主要创新之一，它提供了一种有效的方式来指导模型在处理一系列输入时，该聚焦在什么地方以及如何结合不同部分的信息，从而增强了模型解决复杂任务的能力。



在Transformer模型中，Q（Query），K（Key），V（Value）是通过输入数据的线性变换生成的。这些变换通常使用可训练的权重矩阵来完成。下面详细说明这个过程。

### 生成 Q, K, V 的步骤

1. **输入嵌入**：初始的输入数据首先转换成嵌入表示。如果我们处理的是文本数据，那么每个单词或者标记会被转换成一个稠密的向量表示。

2. **线性变换**：每个嵌入向量接着通过三个不同的、可训练的线性层（即权重矩阵）进行变换，产生对应的Q、K和V。具体地说，对于输入序列中的每个元素，模型学习了三组权重矩阵W_Q、W_K和W_V，用于将元素的嵌入表示映射到Q、K和V。

```plaintext
Q = W_Q * X
K = W_K * X
V = W_V * X
```

其中X是输入嵌入，W_Q、W_K、W_V是权重矩阵，Q、K、V分别是查询、键和值的向量。

3. **多头注意力**：在多头注意力机制中，这一过程会复制和并行化执行多次，每一组头使用不同的权重矩阵W_Q^i、W_K^i和W_V^i，从而能够捕获输入数据的不同方面。

### 训练过程中的更新

- **梯度下降**：在训练过程中，Transformer模型使用反向传播算法和梯度下降来持续更新这些权重矩阵。根据损失函数相对于每个权重的梯度，优化器调整权重以最小化损失。

- **参数更新**：随着训练的进行，W_Q、W_K、W_V这些权重矩阵会根据损失函数和梯度不断进行更新，使得模型能够更好地学习如何为Q、K、V生成有效的表示。

综上所述，Q、K、V是通过将输入数据的嵌入表示与学习到的权重矩阵相乘得到的，并且这些权重矩阵在模型训练过程中会不断更新，以便模型可以更好地理解数据、捕获序列间的依赖关系，并提高任务相关性能。



接下来，我们将探讨如何在Transformer架构内应用多头注意力模块。最初，Transformer模型是为了机器翻译而设计的。因此，它具有一个编码器-解码器结构，其中编码器输入原始语言中的句子，并生成基于注意力的表示。另一方面，解码器关注编码信息，并以自回归的方式生成翻译后的句子，就像标准RNN那样。虽然这种结构对于需要自回归解码的序列到序列任务非常有用，但我们这里会重点关注编码器部分。在自然语言处理（NLP）中已经通过纯编码器基础的Transformer模型取得了很多进展（如果感兴趣，这些模型包括BERT家族、视觉Transformer等），在我们的教程中，我们也主要关注编码器部分。如果你已经理解了编码器架构，那么实现解码器也只是一个很小的步骤。



多头注意力（Multi-Head Attention）是 Transformer 模型的一个关键部分，它能帮助模型在处理序列数据时同时考虑到不同位置的信息。

在 PyTorch 中实现多头注意力的一段代码如下：

```python
self.qkv_proj = nn.Linear(input_dim, 3*embed_dim)
```

这行代码中使用了PyTorch的`nn.Linear`模块。下面是对代码的逐句解释：

- `self.qkv_proj`: 这是定义在一个类里的一个属性，代表了一个全连接层（或称作线性层），用于将输入的特征投影到一个新的空间。这里 `qkv` 表示查询（Query）、键（Key）和值（Value），这三者是注意力机制的核心概念。
  
- `nn.Linear`: 这是构造一个线性映射的层，其中`input_dim`是输入特征的维数，而`3*embed_dim`是输出特征的维数。

- `input_dim`: 输入特征向量的维度。
  
- `embed_dim`: 嵌入层的维度。在多头注意力中，`embed_dim`通常会被分割成几个“头”，每个头处理一部分的嵌入维度，以并行地捕获不同的特征子空间。

- `3*embed_dim`: 输出维度是3倍的`embed_dim`因为它包含了查询、键和值三部分的投影，每一部分都有`embed_dim`维度。所以总共是`3*embed_dim`。

在多头注意力中，输入会先通过这个全连接层获取查询(query)、键(key)和值(value)的表示，然后再进行后续的注意力计算。这种方式提高了运算效率，因为它可以一次完成所有头的线性变换，而非逐个处理。





`nn.Dense` 是一种在神经网络中常用的全连接层（Fully-Connected Layer），在 Flax 框架中，`nn.Dense` 用于建立一个普通的密集连接层。这个函数创建了一个层，它的每个输入节点都与输出节点全连接，通常用于实现线性变换加上一个非线性激活函数。

以下是 `nn.Dense` 的基本参数解释：

- `features`: 输出空间的维度。
- `use_bias`: 是否添加偏置项 (默认为 `True`)。
- `kernel_init`: 权重初始化函数。
- `bias_init`: 偏置初始化函数。

用法示例

```python
from flax import linen as nn

class MyModel(nn.Module):
  @nn.compact
  def __call__(self, x):
    x = nn.Dense(features=256)(x)  # 添加一个有256个输出单元的全连接层
    x = nn.relu(x)                  # 应用ReLU激活函数
    return x
```

在这个例子中，我们首先定义了一个名为`MyModel`的模型，它包含一个`Dense`层，这个层将输入转换成一个256维的输出向量。然后接一个 ReLU 激活函数来增加非线性特征，使模型可以学习更复杂的模式。





[李宏毅 Transformer](https://speech.ee.ntu.edu.tw/~hylee/ml/2023-spring.php)

- ```
  # huggingface\annotated-transformer 主仓
  # see numpy-transformer just upper
  # 数据集已挂 换源 https://github.com/pytorch/text/issues/1756
  from torchtext.datasets import multi30k, Multi30k
  multi30k.URL = {
      "train": r"https://raw.githubusercontent.com/neychev/small_DL_repo/master/datasets/Multi30k/training.tar.gz",
      "valid": r"https://raw.githubusercontent.com/neychev/small_DL_repo/master/datasets/Multi30k/validation.tar.gz",
      "test": r"https://raw.githubusercontent.com/neychev/small_DL_repo/master/datasets/Multi30k/mmt16_task1_test.tar.gz",
  }
  multi30k.MD5 = {
      "train": "20140d013d05dd9a72dfde46478663ba05737ce983f478f960c1123c6671be5e",
      "valid": "a7aa20e9ebd5ba5adce7909498b94410996040857154dab029851af3a866da8c",
      "test": "6d1ca1dba99e2c5dd54cae1226ff11c2551e6ce63527ebb072a1f70f72a5cd36",
  }
  data_train = Multi30k(split='train')
  data_val = Multi30k(split='valid')
  data_test = Multi30k(split='test')
  # train, val, test = datasets.Multi30k(language_pair=("de", "en"))
  
  
  pip install --upgrade ipykernel
  pip install jupyterlab ipywidgets
  
  jupyter lab
  	# 先运行，后下断点
  	# 成功单步调试
  	
  Developer Command Prompt for vS 2019
  	# pip install spacy==3.2
  		# 没有少头文件，但是少链接库
  		#  linalg.obj : error LNK2001: 无法解析的外部符号 __imp__PyBaseObject_Type
  		
  		D:\usr\Python311\python.exe -m pip install -U pip setuptools wheel
  		pip install -U spacy
  
  
  ```
  
  

[解剖Transformer 第一部分](https://zhuanlan.zhihu.com/p/552543893)

- ```
  注意力机制是一种从一系列输入中选择性地提取信息的结构。
  
  序列转换有两个输入序列，一个叫做源序列，一个叫做目标序列；两个序列不一定有相同的长度。每个序列中每个元素都由一个一定维度的特征向量表示，源序列和目标序列的特征向量维度也不一定相同。序列转换操作的输出是对目标序列中的每个元素输出一个新的特征向量，叫做输出序列。
  
  最常见的方式是Transformer所使用的注意力机制，称作“点积注意力”
  
  ```

  

[从零起步的 Transformer 与代码拆解](https://leonis.cc/sui-sui-nian/2023-04-21-transformer-from-scratch.html)

[Transformer 模型的 PyTorch 实现](https://www.jianshu.com/p/3b550e903e78)

[flash attention 的python和triton实现](https://zhuanlan.zhihu.com/p/662759306)

[一文搞懂PyTorch Hook](https://zhuanlan.zhihu.com/p/662760483)

[通俗讲解pytorch中nn.Embedding原理及使用](https://www.jianshu.com/p/63e7acc5e890)

[图解 Transformer](https://zhuanlan.zhihu.com/p/196642078)

[Transformer 是如何工作的：600 行](https://arthurchiao.art/blog/transformers-from-scratch-zh/)

[Transformer 修炼之道（一）、Input Embedding](https://zhuanlan.zhihu.com/p/372279569)



```
词嵌入算法（embedding algorithm），将每个词转换为一个词向量。实际中向量一般是 256 或者 512 维。那么整个输入的句子是一个向量列表
```







### JAX 

[Jax:一个比numpy、pytorch、cupy还要理想的工具](https://zhuanlan.zhihu.com/p/536377657)

[jax_transformer](https://github.com/vpj/jax_transformer)

```

pip3 install jax jaxlib labml

pip install --upgrade "jax[cuda11_local]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html



```





```
对话：{"text": "User: 内容1\n内容1\n\nAssistant: 回答1\n回答1\n\nUser: 内容2\n内容2\n\nAssistant: 回答2\n回答2\n\nUser: 内容3\n内容3\n\nAssistant: 回答3\n回答3\n\n"}

注意上述格式：

冒号是半角。后面还有是半角空格，然后是问答、对话。

对于特别长的多段落的问题/回答，问题内部可以有换行\n，但是不能出现 \n\n。

换行必须用 \n，不能用 \r\n。 作者：czhko https://www.bilibili.com/read/cv22445881/ 出处：bilibili
```



#### 各种论文实现 必看

[annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations)

[ChatGPT使用指南——文本推理 必看](https://github.com/datawhalechina/hugging-llm/blob/main/content/ChatGPT%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97%E2%80%94%E2%80%94%E6%96%87%E6%9C%AC%E6%8E%A8%E7%90%86.ipynb)



## LongLoRA

[LongLoRA](https://github.com/dvlab-research/LongLoRA)

- [LongAlpaca-7B](https://huggingface.co/Yukang/LongAlpaca-7B) 
  - [LongAlpaca-12k 数据集](https://huggingface.co/datasets/Yukang/LongAlpaca-12k)

- [EleutherAI/pythia-1.4b-deduped 微调](https://github.com/dvlab-research/LongLoRA/pull/32)



## QLoRA 低碳微调

[chatGLM-6B-QLoRA](https://github.com/shuxueslpi/chatGLM-6B-QLoRA) [2](https://zhuanlan.zhihu.com/p/634516004) [3](https://zhuanlan.zhihu.com/p/636215898)

[issues 必看](https://github.com/shuxueslpi/chatGLM-6B-QLoRA/issues/29)



```
QLoRA本身讲的是模型本身用4bit加载，训练时把数值反量化到bf16后进行训练，利用 LoRA 可以锁定原模型参数不参与训练，只训练少量LoRA参数的特性使得训练所需的显存大大减少。例如33B的LLaMA模型经过这种方式可以在24 GB的显卡上训练，
```



QLoRA 使用一种低精度的存储数据类型（NF4）来压缩预训练的语言模型。通过冻结 LM 参数，将相对少量的可训练参数以 Low-Rank Adapters 的形式添加到模型中，LoRA 层是在训练期间更新的唯一参数，使得模型体量大幅压缩同时推理效果几乎没有受到影响。从QLoRA的名字可以看出，QLoRA实际上是Quantize+LoRA技术。



## GPTQ 低碳微调

[qlora](https://github.com/artidoro/qlora)

[GPTQ-for-LLaMa](https://github.com/qwopqwop200/GPTQ-for-LLaMa)

- [GPTQ for llama.cpp](https://github.com/qwopqwop200/GPTQ-for-LLaMa/issues/240)

[rwkv-raven-qlora-4bit-instruct](https://github.com/iantbutler01/rwkv-raven-qlora-4bit-instruct)

[VisualGLM-6B qlora](https://github.com/THUDM/VisualGLM-6B/issues/103)

```
https://github.com/iantbutler01/rwkv-raven-qlora-4bit-instruct
https://github.com/howard-hou/VisualRWKV
https://github.com/jiamingkong/rwkv_reward
```



```
太厉害了,这GPU的的成本大大缩减。EleutherAI/pythia-12b推理只需12G, finetune也只需23G. 单个3090就能搞定了。

新技术：今天刚看到的新的优化器Sophia.作者之一发文说可以让模型训练教adma提速2倍。应用在GPT, OPT, llama这样的大模型预训练能够把200wd道陈本降到100w刀。( sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training)。性能验证：52AI：ML优化器Sophia vs Adam 性能验证

QLoRA技术让650B参数训练从780G降到48G, Sophia优化器再提升两倍训练速度。两个一结合感觉咱训练大模型指日可待了，技术前进了一大步。但训练大模型所需的数据还是一个难题。
```



##  ACG2vec 二次方

[ACG2vec](https://github.com/OysterQAQ/ACG2vec)

[YuzuMarker.FontDetection 字体识别](https://github.com/JeffersonQin/YuzuMarker.FontDetection)



## LLaVA-Med

[LLaVA-Med](https://github.com/microsoft/LLaVA-Med) 视觉模型

[在线使用](https://llava.hliu.cc/)





## DeepSpeed Chat

[DeepSpeed Chat](https://github.com/microsoft/DeepSpeed/blob/master/blogs/deepspeed-chat/chinese/README.md)

[deepSpeed （DeepSpeed-Chat）体验 实战](https://zhuanlan.zhihu.com/p/624413021)

[DeepSpeed-Chat：最强ChatGPT训练框架，一键完成RLHF训练！](https://zhuanlan.zhihu.com/p/621780753)

[opt-1.3b](https://huggingface.co/facebook/opt-1.3b)

[tiktokenizer](https://github.com/dqbd/tiktokenizer)

[How to count tokens with tiktoken](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb)

[tiktoken官方](https://github.com/openai/tiktoken)

[Byte Pair Encoder，BPE 字节对编码](https://zhuanlan.zhihu.com/p/592399697)

[BPE 算法原理及使用指南【深入浅出】](https://juejin.cn/post/7088322473640329230)

> BPE 一般适用在欧美语言拉丁语系中，因为欧美语言大多是字符形式，涉及前缀、后缀的单词比较多。而中文的汉字一般不用 BPE 进行编码，因为中文是字无法进行拆分。对中文的处理通常只有分词和分字两种。理论上分词效果更好，更好的区别语义。

[从embedding讲起](https://mp.weixin.qq.com/s?__biz=MzkzMzQ3Mzk1Nw==&mid=2247483663&idx=1&sn=f1641f28e6fb18bdb84ebf3ce882bd0a&chksm=c24abac5f53d33d3f2d1bec3995053c4ff242217bb92d918625777fc380148fe8fba54d17a20&token=164424461&lang=zh_CN#rd)



## FasterTransformer

[FasterTransformer NVIDIA官方](https://github.com/NVIDIA/FasterTransformer)









## Linly-Chinese-LLaMA-2

[Linly-Chinese-LLaMA-2](https://github.com/CVI-SZU/Linly)  中英日三语，包话训练代码？

```
mount -t ntfs-3g /dev/sda1 /mnt
	# .77 挂载 512G 硬盘

dnf install git-lfs

git lfs install
git clone https://huggingface.co/Linly-AI/Chinese-LLaMA-2-13B-hf

git restore --source=HEAD :/
	# retry
	
https://zhuanlan.zhihu.com/p/37332255
	# 调大虚拟内存就没错了	
	

git config --global pack.windowMemory 50m
git config --global http.postbuffer 524288000

https://www.moguf.com/post/gitoutofmemory

```



```
# VMWare 中的 win10 用　NAT 模式，在里面开 Proxifier 连宿主机的 shocks5 代理，实测可行。
　 # 但是反过来实测不可行


```



### AutoGPTQ 量化

[AutoGPTQ 量化](https://github.com/PanQiWei/AutoGPTQ/blob/main/README_zh.md) [1](https://github.com/PanQiWei/AutoGPTQ/issues/252)

看模型的配置文件，只要它是 "model_type": "llama" 就可以支持。Linly 应该也可以

AutoGPTQ 好像还不支持 LLaMA2



### chatglm2-6b-32k

[chatglm2-6b-32k](https://huggingface.co/THUDM/chatglm2-6b-32k)

模型可以在约20G显存的情况下处理32K长度的上下文（FP/BF16格式）

```
git lfs install
git clone https://huggingface.co/THUDM/chatglm2-6b-32k
	# GIT_LFS_SKIP_SMUDGE=1 不要下载大文件
	
git restore --source=HEAD :/
	# 恢复下载


pip install protobuf transformers==4.30.2 cpm_kernels torch>=2.0 gradio mdtex2html sentencepiece accelerate -i https://pypi.tuna.tsinghua.edu.cn/simple some-package


pip3.9 cache purge
	# 删除所有缓存文件

/root/.cache/pip/
	# 缓存目录在这
	pip3.9 config list
		# 没有输出

pip3.9 config set global.cache-dir "/mnt/tmp"
	# 成功设置缓存目录
	--> Writing to /root/.config/pip/pip.conf
	

pip3.9 download -r requirements.txt -d /mnt/ChatGLM2-6B/whl 
	# 成功下载离线安装包
		# pip3.9 uninstall -r requirements.txt -y


autodl 实战：

pip3 freeze >i.txt && \
pip3 uninstall -r i.txt -y
	# 卸载所有已安装的包

pip3 download -r requirements.txt -d /root/ChatGLM2-6B/whl -i https://pypi.tuna.tsinghua.edu.cn/simple 
	# autodl 实战
	# 成功下载
	
pip3 install --no-index --find-links=/root/ChatGLM2-6B/whl -r /root/ChatGLM2-6B/requirements.txt


pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
	# 普通安装
	# 选mini conda python10 ubantu 22.04 cuda 11.8 成功安装
	
pip3.10 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
	# win10 这样装，成功运行


pip install protobuf transformers==4.30.2 cpm_kernels torch>=2.0 gradio mdtex2html sentencepiece accelerate
	# 32K 需要的

from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("/root/autodl-tmp/chatglm2-6b-32k", trust_remote_code=True)
model = AutoModel.from_pretrained("/root/autodl-tmp/chatglm2-6b-32k", trust_remote_code=True).half().cuda()
model = model.eval()
response, history = model.chat(tokenizer, "你好", history=[])
print(response)
response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", history=history)
print(response)

API 调用
pip3.10 install fastapi uvicorn

直接运行 api.py

curl -X POST "http://127.0.0.1:8000" \
     -H 'Content-Type: application/json' \
     -d '{"prompt": "你好", "history": []}'
成功



# https://github.com/fatedier/frp



pip3 install --no-index --find-links=/root/whl -r /root/whl/requirments.txt


# 阿里云 webdav 上传
https://github.com/tickstep/aliyunpan/blob/main/docs/manual.md#1-%E5%A6%82%E4%BD%95%E8%8E%B7%E5%8F%96RefreshToken

sudo curl -fsSL http://file.tickstep.com/rpm/aliyunpan/aliyunpan.repo | sudo tee /etc/yum.repos.d/tickstep-aliyunpan.repo > /dev/null && sudo yum install aliyunpan -y
	# 这样安装

从网页端获取 refresh_token

login
	# 输入刚才的 token
ls
	# 列出目录

mkdir chatglm2-6b-32k
	# 创建目录

upload /mnt/chatglm2-6b-32k /
	# 上传整个文件夹到阿里盘的根目录

upload /mnt/text2vec-large-chinese /
	# 上传 embeding 模型

pip download -d /mnt/whl protobuf transformers==4.30.2 cpm_kernels torch>=2.0 gradio mdtex2html sentencepiece accelerate
	# 只下载不安装


```



```
1、临时使用
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
2、永久更改pip源
升级 pip 到最新的版本 (>=10.0.0) 后进行配置：
pip install pip -U pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
如果您到 pip 默认源的网络连接较差，临时使用镜像站来升级 pip：
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
3、离线安装python3及依赖包
将pip3 list的信息生成文档
pip3 freeze >requirements.txt
将requirement.txt文档中列出的模块信息下载到指定目录
pip3 download -r requirements.txt -d /tmp/packages/ #推荐使用 或 pip3 install --download /tmp/packages -r requirements.txt
将下载好的模块copy到离线服务器
pip3 install xxx.tar.gz pip3 install xxx.whl pip3 install xxx.xx #是什么格式就安装什么格式的文件即可。
如果有要安装的包和依赖包有多个，且不知道先装哪个，那么就把这些文件放在一个目录中，然后进入该目录使用下面命令一起安装
pip3 install ./*
批量离线安装requirments.txt中的模块，需要将下载好的模块和requirments.txt都copy到一个目录，然后执行下面的命令
pip3 install --no-index --find-links=/tmp/packages -r requirments.txt
```



#### embeding

```

https://huggingface.co/GanymedeNil/text2vec-large-chinese

用text2vec-large-chinese模型，使用langchain的HuggingFaceEmbeddings加载调用


我尝试了直接使用ChatGLM的transformer部分输出文本的embedding，输出4096位embedding，使用相似度算法，实测效果不及chatyuan-v2和chinese_roberta_wwm_ext_large


embedding 一般需要使用专门的模型，用生成模型的 embedding 结果不会太好。

transformers 库加载的模型 model 应该也继承了 self.transformer.word_embeddings(input_ids) 这个方法吧？可以试试先把输入的字符串句子通过 tokenizer.decode() 方法转换成 token 的索引，再把这个索引输入到 model.transformer.word_embeddings() 里，应该就可以得到每个 token 的向量了。如果只想要句向量，可以看看 glm 论文里有没有什么特殊 token 能够包含句子信息的，或者对每个 token 的词向量再做一些注意力机制的操作，类似于 bert 的 [CLS] 这个特殊 token 就一般当作句向量。
```



```

from langchain.embeddings.huggingface import HuggingFaceEmbeddings

# patch HuggingFaceEmbeddings to make it hashable
def _embeddings_hash(self):
    return hash(self.model_name)

HuggingFaceEmbeddings.__hash__ = _embeddings_hash

embedding_device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

    self.embeddings = HuggingFaceEmbeddings(model_name=embedding_model_dict[embedding_model],
                                                model_kwargs={'device': embedding_device})


# 抱抱脸的嵌入模型应该都是这样用的
import os
import torch
from transformers import AutoTokenizer, AutoModel

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


# Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]  # First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('shibing624/text2vec-base-chinese')
model = AutoModel.from_pretrained('shibing624/text2vec-base-chinese')
sentences = ['如何更换花呗绑定银行卡', '花呗更改绑定银行卡']
# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)
# Perform pooling. In this case, max pooling.
sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])
print("Sentence embeddings:")
print(sentence_embeddings)
```



```
基于自训练的Embedding模型
openAI 的Embedding模型数据更多是基于普遍性数据训练，如果你要做问答的领域太过于专业有可能就会出现查询数据不准确的情况。

解决方案是自训练 Embedding 模型，在这里我推荐一个项目 text2vec ，shibing624 已经给出了一个模型基于 CoSENT + MacBERT +STS-B，shibing624/text2vec-base-chinese。

我也在前些日子训练了基于 CoSENT + LERT + STS-B的两个模型一个隐层大小是1024的text2vec-large-chinese


基于 Fine-tune
目前我自身测试下来，使用问答数据集对GPT模型进行Fine-tune后，对于该类问题的准确性大幅提高。你可以理解为GPT通过大量的专业领域数据的训练后，当你对它提问的时候会更像在和这个领域的专家对话，然后配合调小接口中temperature参数，可以得到更确定的结果。
```



##### 自已训练embeding

[自已训练embeding](https://github.com/shibing624/text2vec)

[文本匹配模型实验报告-text2vec  必看](https://github.com/shibing624/text2vec/blob/master/docs/model_report.md)



#### 微调

[微调](https://zhuanlan.zhihu.com/p/643531454)



```
# 行不通
# MSYS2 安装代理，然后用 Proxifier 连这个代理，全局上网就很稳
pacman -S python3-pip

pip3 install shadowsocksr-cli -i https://pypi.tuna.tsinghua.edu.cn/simple

shadowsocksr-cli --remove-url https://tyrantlucifer.com/ssr/ssr.txt

shadowsocksr-cli --add-url https://sub.ftwssr.win/sub/?sub=1
	# GepPNKAFVOYAcaqf

外面访问不到 它的端口？改用win10 虚拟机算了


```





```
7B用int8就占用了7G显存，梯度必须16bit甚至要32bit

24G训练7B估计勉勉强强，用int8，PEFT+LoRA
```



### 增加虚拟内存

[增加虚拟内存](http://www.lining0806.com/linux%E4%B8%8B%E5%A6%82%E4%BD%95%E6%B7%BB%E5%8A%A0%E8%99%9A%E6%8B%9F%E5%86%85%E5%AD%98/)

```
dd if=/dev/zero of=/mnt/swapfile bs=1M count=20480
	# 20G 空文件

mkswap /mnt/swapfile
	# 格式化交换文件

swapon /mnt/swapfile
	# 挂载交换文件

vi /etc/fstab
/mnt/swapfile swap swap defaults 0 0
	# 加在后面，开机自动加载
	
free -h
	# 查看内存大小


```



### frp windows远程桌面

[使用frp实现windows远程桌面连接](https://blog.ligengxin.me/posts/frp-windows-remote/) [s](https://github.com/fatedier/frp/releases/download/v0.51.3/frp_0.51.3_linux_amd64.tar.gz) [c](https://github.com/fatedier/frp/releases/download/v0.51.3/frp_0.51.3_windows_amd64.zip)

[Frp-notes](https://github.com/onekb/Frp-notes)



```
# 服务端配置
frps.ini
[common]
bind_port = 7000 # 服务器端口 客户端必须配置一样的端口
vhost_http_port = 8880
	# 8880 是客户端 api 接口

# 客户端配置
frpc.ini 
[common]
server_addr = 服务器ip
server_port = 7000
[web]
type = http
local_port = 8880
custom_domains = 服务器ip
	# 没有域名这里就填服务器ip

实测 http://xxx.77:8880/searchExcel 能正常访问到内网的服务
	



# 服务端配置
frps.toml
bindPort = 7000
vhostHTTPPort = 506
	# 外网服务端监听 506,  访问外网 506 会被转发到内网 506

./frps -c ./frps.toml


serverAddr = "118.xxx"
serverPort = 7000

[[proxies]]
name = "web"
type = "http"
localPort = 506
customDomains = ["118.xxx"]

./frpc -c ./frpc.toml




[ssh]
type = tcp
local_ip = 127.0.0.1
local_port = 3389  # 远程桌面端口
remote_port = 7004 #这个是远程桌面连接主机的时候输入的ip后加上的端口

# 或者这样
[RDP]
type = tcp
local_ip = 127.0.0.1
local_port = 3389
remote_port = 7004

# 或着开放 http 端口
[web]
type = http
local_port = 8880
custom_domains = 127.0.0.1
	# 没有域名就先这样



# 启动服务端
./frps -c ./frps.ini

# 启动客户端
./frpc -c frpc.ini


# 客户端开机自启 frp 
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp 目录下写一个bat文件

cmd /k "cd /d D:\Downloads\frp_0.33.0_windows_amd64 && frpc -c frpc.ini"  


# 静默后台运行
+@echo off
+if "%1" == "h" goto begin
+mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit
+:begin
cmd /k "cd /d D:\Downloads\frp_0.33.0_windows_amd64 && frpc -c frpc.ini"


Windows 10/11 系统是可以开启 openssh server 的。



```







## MiniGPT-4

[MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4/issues/4)

```
We are currently working on an official solution to make it run in a 24G memory GPU. Will return to you once it is finished
```



#### PEFT 低碳微调

[PEFT: 在低资源硬件上对十亿规模模型进行参数高效微调](https://zhuanlan.zhihu.com/p/610503561)

[zero3+offload](https://zhuanlan.zhihu.com/p/513571706)

[SpeechT5 语音文本全都要](https://zhuanlan.zhihu.com/p/613644440)

```
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
apt-get install git-lfs

./main -m ../ChatLLaMA-zh-7B-int4/chatllama-ggml-q4_0.bin -p "北京有什么好玩的地方？\n" -n 256

```



## gpt-neox-japanese

[gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) 抱抱脸日语gpt **直接可用**

[huggingface 官方finetune](https://huggingface.co/docs/transformers/model_doc/funnel)



## BELLE

[BELLE](https://github.com/LianjiaTech/BELLE) **训练友好**



## Chinese-LLaMA-Alpaca

[Chinese-LLaMA-Alpaca](https://github.com/ymcui/Chinese-LLaMA-Alpaca)

```
nodejs执行避开wsl中文输入bug：
child_process = require('child_process')
child = child_process.spawn('D:\proj\llama.cpp-master\bin\main', [
'-m', 'D:\proj\llama.cpp-master\models\zh-models\7B\ggml-model-q4_0.bin',
'--color', '-f', 'D:\proj\llama.cpp-master\prompts\alpaca.txt', '-ins',
'-c', '2048', '--temp', '0.2', '-n', '256', '--repeat_penalty', '1.3'])
child.stdout.pipe(process.stdout)
child.stdin.setEncoding('utf-8')
process.stdin.pipe(child.stdin)
```



```
只需要用llama的hf+你huggingface上的ziqingyang/chinese-alpaca-lora-7b进行merge就可以了
```



```
python transformers/src/transformers/models/llama/convert_llama_weights_to_hf.py  --input_dir E:\ai\LLaMA_7B --model_size 7B --output_dir E:\ai\LLaMA_7B_HF
	# 原始llama模型转换为HF模型

python Chinese-LLaMA-Alpaca/scripts/merge_llama_with_chinese_lora.py  --base_model  LLaMA_7B_HF  --lora_model chinese-alpaca-lora-7b  --output_dir Merge_7B
	# 对HF模型扩充词表，并用训练好的中文权重模型与它合并



编译 llama.cpp
	https://cmake.org/download/ 
		# 安装 CMake
cmake -S . -B build/ -D CMAKE_BUILD_TYPE=Release
cmake --build build/ --config Release

复制文件
lama.cpp/zh-models/
   - 7B/
     - consolidated.00.pth
     - params.json
	# 这两个合并得到的文件
   - tokenizer.model
	# 这个是训练好的中文模型文件夹内的文件

16位量化
python llama.cpp/convert-pth-to-ggml.py  llama.cpp/zh-models/7B/  1
	# 将上述.pth模型权重转换为ggml的FP16格式，生成文件路径为zh-models/7B/ggml-model-f16.bin

4位量化
llama.cpp/build/bin/Release/quantize.exe  llama.cpp/zh-models/7B/ggml-model-f16.bin  llama.cpp/zh-models/7B/ggml-model-q4_0.bin  2

运行4位量化
	# 注意在 git bash 内执行, powershell 会回答不正常
llama.cpp/build/bin/Release/main -m  llama.cpp/zh-models/7B/ggml-model-q4_0.bin --color -f llama.cpp/prompts/alpaca.txt -ins -c 2048 --temp 0.2 -n 256 --repeat_penalty 1.3


llama.cpp/main -m  llama.cpp/zh-models/7B/ggml-model-q4_0.bin --color -f llama.cpp/prompts/alpaca.txt -ins -c 2048 --temp 0.2 -n 256 --repeat_penalty 1.3
	# wls 内执行这个

在提示符 > 之后输入你的prompt，command+c中断输出，多行信息以\作为行尾。如需查看帮助和参数说明，请执行./main -h命令。

简要介绍几个重要参数：

-c 控制上下文的长度，值越大越能参考更长的对话历史
-ins 启动类ChatGPT的对话交流模式
-n 控制回复生成的最大长度
--repeat_penalty 控制生成回复中对重复文本的惩罚力度
--temp 温度系数，值越低回复的随机性越小，反之越大
--top_p, top_k 控制采样的相关参数


> 你能不能详细介绍一下怎么做披萨？
制作披萨的步骤如下所示：首先，准备面饼皮。将面粉、盐和水混合成柔软的面团；然后用擀板将其压平并烤制至金黄色；最后在上面饼皮上涂上番茄酱或奶酪等配料。接着，把切好的蔬菜放在披萨中，再撒上一些香草或其他调味品即可享用了美味的披萨！
> 如果是海鲜披萨呢？
制作海鲜披萨时要做以下步骤：首先将面饼皮擀平并烤至金黄色；然后在上面上一层奶油或番茄酱，再加入切好的虾、鱼片和蔬菜。最后撒上一些香草或其他调味品即可享用了美味的海鲜披萨！
> 我想吃菠萝披萨
制作菠萝披萨时要做以下步骤：首先将面饼皮擀平并烤至金黄色；然后在上面上一层奶油或番茄酱，再加入切好的菠萝片和蔬菜。最后撒上一些香草或其他调味品即可享用了美味的菠萝披萨！


我能用lightning数据线给安卓手机充电吗？

为什么天空是蓝色的？

我得了流感，请帮我写一封假条。

你是一个作文生成器，请以《绿水青山就是金山银山》为题写一篇议论文。

```



### 微调

```
在 prepare for traning 前 resize_token_embeddings 就可以训练了
如果有其它方式 大佬们多交流说说

vocab_size = len(tokenizer.get_vocab())
print("Tokenizer的词表数量为：", vocab_size)
model.resize_token_embeddings(vocab_size)

可能要注意的是config.json中的词表大小是否与模型的embedding大小一致。如果不一致（比如config.json中仍然是32000，而模型embedding大小是49953），可以手动修改config.json中的相关配置参数。

加入词表是有一定破坏性的， 一是破坏原有分词体系，二是增加了未训练的权重。所以如果不能进行充分训练的话，可能会有比较大的问题。个人觉得如果不是特别专的领域（比如生物医学等涉及很多专业词汇的领域）没有太大必要去扩充英文词表。

请问20G数据大概训练了多久？
预训练第一阶段和预训练第二阶段有什么区别？
训练时间换算成8卡约不到一周的时间；



```





## llama-chat

[llama-chat](https://github.com/randaller/llama-chat)

[多卡运行](https://github.com/randaller/llama-chat/issues/15)

[最佳提示](https://github.com/randaller/llama-chat/issues/7)

[清理系统盘](https://www.autodl.com/docs/qa1/)



```
按下 Windows + R  执行 systempropertiesadvanced 命令 — 在性能中点击设置 — 选择高级选项卡 — 虚拟内存中进行更改。
```



```

conda create -n llama python=3.10 && \
conda activate llama && \
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia

git clone https://github.com/randaller/llama-chat.git &&
cd llama-chat &&
pip install -r requirements.txt && \
pip install -e .

python merge-weights.py --input_dir /root/autodl-tmp/LLaMA_30B --model_size 30B
	# 合并 30B 至少需要 130G 内存，不够的部分用 swap 空间来补
	
	mkdir -p /root/autodl-tmp/swap # 新建交换目录
	cd /root/autodl-tmp/swap
	dd if=/dev/zero of=swapfile bs=1M count=160k
		# 总共 160G
		# 分区的大小就= bs * count
	mkswap swapfile
	
		
	

```



## ColossalAI

[colossalAI](https://github.com/hpcaitech/ColossalAI)



## alpaca-lora

[alpaca-lora](https://github.com/tloen/alpaca-lora)

[alpaca.cpp](https://github.com/antimatter15/alpaca.cpp)

[Tune-A-Video](https://github.com/showlab/Tune-A-Video)



## Chinese-alpaca-lora

[Chinese-alpaca-lora](https://zhuanlan.zhihu.com/p/615968438)



## ChatGpt 微调方案

[llama_index](https://github.com/jerryjliu/llama_index/issues/712)

> [中文使用案例](https://www.cnblogs.com/v3ucn/p/17285124.html)
>
> [llama_index使用踩坑](https://zhuanlan.zhihu.com/p/617229222)

[paul-graham-gpt](https://github.com/mckaywrigley/paul-graham-gpt)

[微调好文必看](https://cloud.tencent.com/developer/article/2245743)

[new bing api 接口](https://rapidapi.com/stefano-pochet-stefano-pochet-default/api/chatgpt-4-bing-ai-chat-api/details)

[new bing api 逆向](https://github.com/acheong08/EdgeGPT)



## ChatGLM-6B

[ChatGLM-6B 清华GPT](https://github.com/THUDM/ChatGLM-6B)

- ```
  C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA
  	# 需要设置环境变量，用 cuda toolkit 11.8 (whisperx 用的是这个 + pytorch2.0)
  ```

- [BaiYang-chatGLM2-6B 旋转位置编码](https://github.com/lilongxian/BaiYang-chatGLM2-6B)

[ChatGLM2-6B 微调(初体验) 语料多](https://zhuanlan.zhihu.com/p/643856746) 

### [ChatGLM-Tuning](https://github.com/mymusise/ChatGLM-Tuning) 24G可训练

- [中文微调数据集](https://github.com/carbonz0/alpaca-chinese-dataset/issues/3)
- [中文小数据集上finetune后效果怎么样](https://github.com/mymusise/ChatGLM-Tuning/issues/64)

[ChatGLM-chinese-insturct](https://github.com/27182812/ChatGLM-chinese-insturct) 中文训练成品

```
7za a -t7z -m0=lzma -mx=9 -mfb=64 -md=32m -ms=on ChatGLM-chinese-insturct_dot_cache.7z .cache/
	# 模型下载好以后打包模型，上传 阿里云盘
```



#### kanchil

[kanchil](https://github.com/vxfla/kanchil)

[gpt_neox_japanese 这个好](https://huggingface.co/docs/transformers/model_doc/gpt_neox_japanese)

[google mt5支持101种语言](https://huggingface.co/google/mt5-base)

```
conda create -n kan pip python=3.9 && \
conda activate kan && \
proxychains4 pip install -r requirements.txt
	# 装不上 1.10.0+cu111

wget https://download.pytorch.org/whl/cu111/torch-1.10.0%2Bcu111-cp39-cp39-linux_x86_64.whl

conda deactivate && \
conda env remove -n kan


```



#### chatglm-tiny

[chatglm-tiny 从头开始训练一个chatglm小模型](https://zhuanlan.zhihu.com/p/642355086) [code](https://github.com/xinsblog/chatglm-tiny)



```

git clone https://github.com/xinsblog/chatglm-tiny.git && \
cd chatglm-tiny
	# 实测 3090 正常训练和推理

```





### [ChatGLM-Finetuning](https://github.com/liucongg/ChatGLM-Finetuning) 参数冻结





## GLM-130B

[GLM-130B](https://github.com/THUDM/GLM-130B)

[GLM-130B 开源的双语千亿预训练模型](https://www.bilibili.com/video/BV1L8411E7N8)

[训练细节](https://chatglm.cn/blog)

[微调](https://huggingface.co/THUDM/chatglm-6b/discussions/1) [FinetuneGLMWithPeft](https://github.com/thaumstrial/FinetuneGLMWithPeft)



## ChatRWKV

[论文本体](https://arxiv.org/abs/2305.13048)

[论文思维树ToT](https://arxiv.org/abs/2305.10601)

[RWKV将对GPT实施降维打击](https://zhuanlan.zhihu.com/p/619721229)

[ChatRWKV](https://zhuanlan.zhihu.com/p/603840957)

[Making this library more like Hugging Face ](https://github.com/BlinkDL/ChatRWKV/issues/25)

[Add RWKV2 (fast)](https://github.com/huggingface/transformers/issues/17230)

[Can't determine model type from model name](https://github.com/oobabooga/text-generation-webui/issues/581)



```
24g显存用offload全量微调6b

内存占用100g左右

```



### RWKV 4 

- [instruction-following version](https://github.com/BlinkDL/RWKV-LM/issues/55)

- [RWKV-infctx-trainer 任意长度](https://github.com/RWKV/RWKV-infctx-trainer)

- [干货训练多轮对话系统](https://github.com/BlinkDL/ChatRWKV/issues/118) [细](https://zhuanlan.zhihu.com/p/639629050) [源码解读](https://zhuanlan.zhihu.com/p/620469303)

- [on windows](https://github.com/BlinkDL/RWKV-LM/issues/158)

  - ```
    Install VS2022 build tools (https://aka.ms/vs/17/release/vs_BuildTools.exe select Desktop C++). Reinstall CUDA 11.7 (install VC++ extensions). Run train.py in "x64 native tools command prompt".
    ```

    

```
conda create -n rwkv pip python=3.10
conda activate rwkv

pip install ninja

pip install pytorch-lightning==1.9.5 

apt-get install ninja-build
```



#### RWKV-v4neo



v4neo 可以用v4 代码推理，**v5 用 v4 推理出错** 



```
	import sys
    sys.argv.append( '--data_file' )
    sys.argv.append( '/root/RWKV-LM/RWKV-v4neo/hongloumeng.txt' )
    sys.argv.append( '--warmup_steps' )
    sys.argv.append( '0' )
    sys.argv.append( '--accelerator' )
    sys.argv.append( 'gpu' )
    sys.argv.append( '--devices' )
    sys.argv.append( '1' )
    sys.argv.append( '--precision' )
    sys.argv.append( 'fp16' )
    sys.argv.append( '--strategy' )
    sys.argv.append( 'deepspeed_stage_2' )
   		# 能正常运行
   	
因为你的tokenizer是自己训练的。用 RWKV-v4/run.py 运行
是的，只能在 ./RWKV-v4/run.py 中运行，但不能在 RWKV-v4neo/run.py中运行 ~~ ,自己训练的还要如果想要chat.py效果的话，估计有点棘手~~
   	
   	
/root/RWKV-LM/RWKV-v4neo/out/rwkv-15.pth
	# 生成的输出用 kv4 运行试试
	
```



#### RWKV5



```
conda create -n KV5 pip python=3.10 && \
conda activate KV5
pip install torch==1.13.1+cu117 --extra-index-url https://download.pytorch.org/whl/cu117
pip3 install torch --index-url https://download.pytorch.org/whl/cu118
	# 试试行不行, 实测 4090 可以训练, deepspeed 要装最新版
pip install pytorch-lightning==1.9.5 deepspeed==0.7.0 wandb ninja
pip install --force-reinstall -v "fastapi==0.99.1"
cd RWKV-v5/
./demo-training-prepare.sh
./demo-training-run.sh

conda install pytorch pytorch-cuda=11.8 -c pytorch -c nvidia
	# 4090 只支持 11.8+
	# conda env remove -n KV5
	wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
sudo sh cuda_11.8.0_520.61.05_linux.run
	# 不能行


Data has 200499 tokens
therefore set my_exit_tokens to 200499, and note:
magic_prime = the largest 3n+2 prime smaller than datalen/ctxlen-1 (= 200499 /512-1 = 390.599609375 in this case)
use https://www.dcode.fr/prime-numbers-search
therefore set magic_prime = 389
	# 魔数的设置，那网站列出前 500 个素数，选最接近 390 的小素数

temperature = 1.0, top_p = 0.3, top_k = 0, alpha_frequency = 1, alpha_presence = 0, alpha_decay = 0.996
	# 推理参数，这样生成内容不会重复？
	
	
	

wget https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda_12.1.0_530.30.02_linux.run
sudo sh cuda_12.1.0_530.30.02_linux.run

update-alternatives --install /usr/local/cuda cuda /usr/local/cuda-12.1/ 121
ln -sfT /usr/local/cuda-12.1/ /etc/alternatives/cuda
ln -sfT /etc/alternatives/cuda /usr/local/cuda


conda install pytorch pytorch-cuda=12.1 -c pytorch -c nvidia

	

update-alternatives --install /usr/local/cuda cuda /usr/local/cuda-11.8/ 118
ln -sfT /usr/local/cuda-11.8/ /etc/alternatives/cuda
ln -sfT /etc/alternatives/cuda /usr/local/cuda


git clone https://huggingface.co/datasets/dlxjj/RWKV-v5

这里下载：rwkv_vocab_v20230424.txt
use https://github.com/Abel2076/json2binidx_tool and rwkv_vocab_v20230424.txt to turn your JSONL into binidx format
set vocab_size to 65536


/usr/local/cuda/bin/nvcc --version

ldconfig -p | grep cuda

必须要 cuda 11.7 ，先删除 autodl 原 cuda


update-alternatives --remove cuda /usr/local/cuda-11.1
update-alternatives --remove cuda-11 /usr/local/cuda-11.1

update-alternatives --install /usr/local/cuda cuda /usr/local/cuda-11.1 111
update-alternatives --install /usr/local/cuda cuda /usr/local/cuda-11.0 110
update-alternatives --install /usr/local/cuda cuda /usr/local/cuda-10.2 102
update-alternatives --install /usr/local/cuda cuda /usr/local/cuda-10.1 101

ln -sfT /usr/local/cuda-11.1 /etc/alternatives/cuda
ln -sfT /etc/alternatives/cuda /usr/local/cuda

	# cuda 多版本切换


wget https://developer.download.nvidia.com/compute/cuda/11.7.1/local_installers/cuda_11.7.1_515.65.01_linux.run
sudo sh cuda_11.7.1_515.65.01_linux.run

Toolkit:  Installed in /usr/local/cuda-11.7/

Please make sure that
 -   PATH includes /usr/local/cuda-11.7/bin
 -   LD_LIBRARY_PATH includes /usr/local/cuda-11.7/lib64, or, add /usr/local/cuda-11.7/lib64 to /etc/ld.so.conf and run ldconfig as root

To uninstall the CUDA Toolkit, run cuda-uninstaller in /usr/local/cuda-11.7/bin

install the CUDA Driver:
    sudo <CudaInstaller>.run --silent --driver


update-alternatives --install /usr/local/cuda cuda /usr/local/cuda-11.7 117
ln -sfT /usr/local/cuda-11.7 /etc/alternatives/cuda
ln -sfT /etc/alternatives/cuda /usr/local/cuda

https://blog.csdn.net/sinat_40245632/article/details/109330182
	# 


# 错误 'FieldInfo' object has no attribute 'field_info'
pip install --force-reinstall -v "fastapi==0.99.1"
	# 或着 downgrade pydantic==1.10.13 ? 这个是上游？

# 改 deepspeed_stage_3_offload 以后格式变了，要执行一次转换
/root/RWKV-v5/out/rwkv-5.pth/zero_to_fp32.py
    parser.add_argument("-d", "--debug", action='store_true', help="enable debug")
    args = parser.parse_args()
    args.checkpoint_dir="/root/RWKV-v5/out/rwkv-5.pth"
    args.output_file="5.pth"


# 改好参数成功训练
RWKV-v5/train.py
    parser = ArgumentParser()

    parser.add_argument("--load_model", default="", type=str)  # full path, with .pth
    parser.add_argument("--wandb", default="", type=str)  # wandb project name. if "" then don't use wandb
    parser.add_argument("--proj_dir", default="out", type=str)
    parser.add_argument("--random_seed", default="-1", type=int)

    parser.add_argument("--data_file", default="demo", type=str)
    parser.add_argument("--data_type", default="binidx", type=str)
    parser.add_argument("--vocab_size", default=65536, type=int)  # vocab_size = 0 means auto (for char-level LM and .txt data)

    parser.add_argument("--ctx_len", default=1024, type=int)
    parser.add_argument("--epoch_steps", default=1000, type=int)  # a mini "epoch" has [epoch_steps] steps
    parser.add_argument("--epoch_count", default=500, type=int)  # train for this many "epochs". will continue afterwards with lr = lr_final
    parser.add_argument("--epoch_begin", default=0, type=int)  # if you load a model trained for x "epochs", set epoch_begin = x
    parser.add_argument("--epoch_save", default=5, type=int)  # save the model every [epoch_save] "epochs"

    parser.add_argument("--micro_bsz", default=12, type=int)  # micro batch size (batch size per GPU)
    parser.add_argument("--n_layer", default=12, type=int)
    parser.add_argument("--n_embd", default=768, type=int)
    parser.add_argument("--dim_att", default=0, type=int)
    parser.add_argument("--dim_ffn", default=0, type=int)
    parser.add_argument("--pre_ffn", default=0, type=int)  # replace first att layer by ffn (sometimes better)
    parser.add_argument("--head_qk", default=0, type=int)  # my headQK trick
    parser.add_argument("--tiny_att_dim", default=0, type=int)  # tiny attention dim
    parser.add_argument("--tiny_att_layer", default=-999, type=int)  # tiny attention @ which layer

    parser.add_argument("--lr_init", default=6e-4, type=float)  # 6e-4 for L12-D768, 4e-4 for L24-D1024, 3e-4 for L24-D2048
    parser.add_argument("--lr_final", default=1e-5, type=float)
    parser.add_argument("--warmup_steps", default=-1, type=int)  # try 50 if you load a model
    parser.add_argument("--beta1", default=0.9, type=float)
    parser.add_argument("--beta2", default=0.99, type=float)  # use 0.999 when your model is close to convergence
    parser.add_argument("--adam_eps", default=1e-8, type=float)
    parser.add_argument("--grad_cp", default=0, type=int)  # gradient checkpt: saves VRAM, but slower
    parser.add_argument("--dropout", default=0, type=float) # try 0.01 / 0.02 / 0.05 / 0.1
    parser.add_argument("--weight_decay", default=0, type=float) # try 0.1 / 0.01 / 0.001
    parser.add_argument("--weight_decay_final", default=-1, type=float)

    parser.add_argument("--my_pile_version", default=1, type=int)  # my special pile version
    parser.add_argument("--my_pile_stage", default=0, type=int)  # my special pile mode
    parser.add_argument("--my_pile_shift", default=-1, type=int)  # my special pile mode - text shift
    parser.add_argument("--my_pile_edecay", default=0, type=int)
    parser.add_argument("--layerwise_lr", default=1, type=int)  # layerwise lr for faster convergence (but slower it/s)
    parser.add_argument("--ds_bucket_mb", default=200, type=int)  # deepspeed bucket size in MB. 200 seems enough
    # parser.add_argument("--cuda_cleanup", default=0, type=int)  # extra cuda cleanup (sometimes helpful)

    parser.add_argument("--my_sample_len", default=0, type=int)
    parser.add_argument("--my_ffn_shift", default=1, type=int)
    parser.add_argument("--my_att_shift", default=1, type=int)
    parser.add_argument("--head_size_a", default=64, type=int) # can try larger values for larger models
    parser.add_argument("--head_size_divisor", default=8, type=int)
    parser.add_argument("--my_pos_emb", default=0, type=int)
    parser.add_argument("--load_partial", default=0, type=int)
    parser.add_argument("--magic_prime", default=0, type=int)
    parser.add_argument("--my_qa_mask", default=0, type=int)
    parser.add_argument("--my_random_steps", default=0, type=int)
    parser.add_argument("--my_testing", default='', type=str)
    parser.add_argument("--my_exit", default=99999999, type=int)
    parser.add_argument("--my_exit_tokens", default=0, type=int)


    if pl.__version__[0]=='2':
        parser.add_argument("--accelerator", default="gpu", type=str)
        parser.add_argument("--strategy", default="deepspeed_stage_2", type=str)
        parser.add_argument("--devices", default=1, type=int)
        parser.add_argument("--num_nodes", default=1, type=int)
        parser.add_argument("--precision", default="fp16", type=str)
        parser.add_argument("--accumulate_grad_batches", default=1, type=int)
    else:
        parser = Trainer.add_argparse_args(parser)
    args = parser.parse_args()
    args.accelerator = "gpu"
    args.strategy = "deepspeed_stage_2"
    args.devices = 1
    args.num_nodes = 1
    args.precision = "bf16"
    args.accumulate_grad_batches=1
	


https://github.com/shengxia/RWKV_Role_Playing
	# rwkv5 角色扮演 
	


# 训练完后成功运行
run_rwkv5.py

# pip install rwkv

import os
os.environ['RWKV_JIT_ON'] = '1'

from rwkv.model import RWKV
from rwkv.utils import PIPELINE, PIPELINE_ARGS

model = RWKV(model='rwkv-5', strategy='cpu fp32')
pipeline = PIPELINE(model, "rwkv_vocab_v20230424")

ctx = "\nIn a shocking finding, scientist discovered a herd of dragons living in a remote, previously unexplored valley, in Tibet. Even more surprising to the researchers was the fact that the dragons spoke perfect Chinese."
print(ctx, end='')

def my_print(s):
    print(s, end='', flush=True)

args = PIPELINE_ARGS(temperature = 1.0, top_p = 0.7, top_k = 100, # top_k = 0 then ignore
                     alpha_frequency = 0.25,
                     alpha_presence = 0.25,
                     alpha_decay = 0.996, # gradually decay the penalty
                     token_ban = [0], # ban the generation of some tokens
                     token_stop = [], # stop generation whenever you see any token here
                     chunk_len = 256) # split input into chunks to save VRAM (shorter -> slower)

pipeline.generate(ctx, token_count=200, args=args, callback=my_print)
print('\n')

out, state = model.forward([187, 510, 1563, 310, 247], None)
print(out.detach().cpu().numpy())                   # get logits
out, state = model.forward([187, 510], None)
out, state = model.forward([1563], state)           # RNN has state (use deepcopy to clone states)
out, state = model.forward([310, 247], state)
print(out.detach().cpu().numpy())                   # same result as above
print('\n')


```





```
    import sys
    sys.argv.append( '--data_file' )
    sys.argv.append( '/root/RWKV-LM/RWKV-v4neo/hongloumeng.txt' )
    sys.argv.append( '--warmup_steps' )
    sys.argv.append( '0' )
    sys.argv.append( '--accelerator' )
    sys.argv.append( 'gpu' )
    sys.argv.append( '--devices' )
    sys.argv.append( '1' )
    sys.argv.append( '--precision' )
    sys.argv.append( 'bf16' )
    sys.argv.append( '--strategy' )
    sys.argv.append( 'deepspeed_stage_2' )
    	# 正常运行
    
    
    
    /root/RWKV-LM/RWKV-v5/src/model.py
    	# from torch.nn import functional as F
    	# 483 行
            idx, targets = batch
            	# tensor
            	# device:device(type='cuda', index=0)
            	# dtype:torch.int64
            	# shape:torch.Size([12, 1024])
            	# 两向量的维度一样的
            	
            logits = self(idx)
            	# tensor
            	# device:device(type='cuda', index=0) 
            	# dtype:torch.bfloat16
            	# shape:torch.Size([12, 1024, 4447])
            
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), targets.view(-1))
           # input 是概率值   target 是真实类别的 index
           # 这个函数就是这样定义的
    
```







```
# 无限版本会爆显存
git clone https://github.com/RWKV/RWKV-infctx-trainer.git && \
cd RWKV-infctx-trainer/RWKV-v5
	
conda create -n rwkv python=3.10 pip -y && \
conda activate rwkv

conda install -y pytorch-cuda=11.8 -c pytorch -c nvidia -y && \
conda install -y pytorch==2.1.1 -c pytorch -c nvidia -y && \
python -m pip install lightning==2.0.5 deepspeed==0.10.0 && \
python -c "import torch; print(torch.__version__)"


python -m pip install datasets transformers && \
python -m pip install ninja numexpr jsonargparse 'jsonargparse[signatures]' && \
python -m pip install lm-dataformat ftfy sentencepiece tokenizers wandb & \
python -m pip install papermill


python3 init_model.py --n_layer 6 --n_embd 512 --vocab_size 50277 --skip-if-exists ./model/L6-D512-neox-init.pth

python3 init_model.py --n_layer 3 --n_embd 512 --vocab_size 50277 --skip-if-exists ./model/L3-D512-neox-init.pth
	# 初始化空权重
	# 成功

python3 preload_datapath.py text.yaml
	# 成功生成训练数据
	
python3 lightning_trainer.py fit -c text.yaml
	

```



```
vi text.yaml
trainer:
  max_steps: 10
  target_batch_size: 32
model:
  load_model: ./model/L6-D512-neox-init.pth
  ctx_len: 1024
  lr_init: 3e-4
  bptt_learning: true
  bptt_learning_range: -1
data:
  data_path: "./train_data"
  source: "text"
  source_data_dir: "./data"
  tokenizer: neox
  text_rechunk_size: 1024
  test_split: 0.01
  test_split_shuffle: false

```



##### MyDataset char模式

```
import linecache

class MyDataset(Dataset):
    def __init__(self, args):
        self.args = args
        self.data_file = args.data_file
        # 计算文件中的数据行数，该步骤需要时间，因为要遍历整个文件
        self.num_entries = sum(1 for line in open(self.data_file))
		...
		else:
                self.data = open(args.data_file, "r", encoding=args.data_type).read()
            rank_zero_info("Building token list...")
            unique = sorted(list(set(self.data)))
            self.vocab_size = len(unique)
            # rank_zero_info()
            # for u in unique:
            #     print(u, end=' ')
            # rank_zero_info('\n\n')
            xx = 0
            xxObj = {}
            for u in unique:
                xxObj[xx] = u
                xx += 1
            with open(f"{args.proj_dir}/vocab.json", "w", encoding="utf-8") as vocab_file:
                vocab_file.write(json.dumps(xxObj, ensure_ascii=False))
            self.data_size = len(self.data)
            rank_zero_info(f"Data has {self.data_size} tokens, {self.vocab_size} vocab size.")
            self.stoi = {ch: i for i, ch in enumerate(unique)}
            self.itos = {i: ch for i, ch in enumerate(unique)}


    def __len__(self):
        return self.args.epoch_steps * self.args.micro_bsz

    def __getitem__(self, idx):

        idx = np.random.randint(0, self.num_entries)


        ctx_len = self.args.ctx_len
        req_len = ctx_len + 1

        line = linecache.getline(self.data_file, idx+1)
        js = json.loads(line)
        dlg = js['dlg']
        gpt = js['gpt']
        dlg_gpt = '\ndlg:' + dlg + '\ngpt:' + gpt + '<eNd>'
        dlg_gpt_repeat = dlg_gpt * ctx_len

        # cheat: pick a random spot in dataset
        i = np.random.randint(0, len(dlg_gpt_repeat) - req_len)

        dix = [self.stoi[s] for s in dlg_gpt_repeat[i : i + req_len]]

        x = torch.tensor(dix[:-1], dtype=torch.long)
        y = torch.tensor(dix[1:], dtype=torch.long)

        return x, y




```





##### 边训练边输出

```
RWKV-LM/RWKV-v5/train.py
    from src.model import RWKV
    model = RWKV(args, train_data)
    	# 额外加一个参数，里面有分词器

RWKV-LM/RWKV-v5/src/model.py
class RWKV(pl.LightningModule):
    def __init__(self, args, train_data):
        self.train_data = train_data
        	# 赋值
 
# 这函数是 Lightning 框架的约定，在这里输出 ai 回答  
     def training_step(self, batch, batch_idx):
        args = self.args
        if args.my_qa_mask != 1:
            idx, targets = batch
            i1 = idx[0].tolist()
            iS = [ self.train_data.itos[i] for i in i1 ]
            t1 = targets[0].tolist()
            tS = [ self.train_data.itos[i] for i in t1 ]
            logits = self(idx)

            tokens = []
            for i in range(1024):
                probs = logits[0][i].tolist()
                max_val = max(probs)
                idx = probs.index(max_val)
                tokens += self.train_data.itos[idx]
      
            result = "".join(tokens)
            print(result)
 


```





#####  nanoRWKV

```
# nanoRWKV/train.py
# 加入
import torch.nn.functional as F
import tiktoken
# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
encode = lambda s: enc.encode(s, allowed_special={"<|endoftext|>"})
decode = lambda l: enc.decode(l)


        with ctx:
            logits, loss = model(X, Y)
            loss = loss / gradient_accumulation_steps # scale the loss to account for gradient accumulation

            x0 = list( X[0].cpu().numpy() )
            x0_str = decode(x0)

            y0 = list( Y[0].cpu().numpy() )
            y0_str = decode(y0)

            probs = logits.cpu().detach().numpy()
            out_tokens = np.argmax(probs[0], axis=1)
            out_str = decode(out_tokens)

```



##### mamba-gpt

[mamba-gpt](https://gist.github.com/thistleknot/0d2bbced6264cd2ac508145797989638)



#### lit-llama deepspeed zero-3-offload

[How to use deepspeed zero-3-offload](https://github.com/Lightning-AI/lit-llama/issues/84)



### RWKV-Runner

[RWKV-Runner](https://github.com/josStorer/RWKV-Runner) 立等可取 [rust 推理](https://github.com/cgisky1980/ai00_rwkv_server_)

[训练部署](https://zhuanlan.zhihu.com/p/616351661) [2](https://github.com/josStorer/RWKV-Runner/issues/122)

[openai 官方 tokenizer](https://github.com/openai/tiktoken)

[扩充词表](https://github.com/yuanzhoulvpi2017/zero_nlp/tree/main/model_modify) [2](https://github.com/LianjiaTech/BELLE) [3](https://github.com/liguodongiot/llm-action)

- [词表扩充必备工具SentencePiece](https://zhuanlan.zhihu.com/p/630696264)
- [词表扩充+预训练+指令精调](https://zhuanlan.zhihu.com/p/631360711)

[book txt](https://github.com/shjwudp/shu/tree/master/books)

[RWKV语言模型从入门到放弃，保姆级Training、Fine-tuning、Lora入坑教程](https://zhuanlan.zhihu.com/p/629809101?utm_id=0)

[langchain+rwkv](https://python.langchain.com/en/latest/integrations/rwkv.html)

[wenda](https://github.com/wenda-LLM/wenda)



### RWKV-Classification 24G显卡微调

[RWKV-Classification 24G显卡微调](https://github.com/yynil/RWKV-Classification)

```
在transformers的官方RWKV上，给RWKV model增加了sequence classifier，在peft上面，3B的world模型下面做训练，deepspeed stage 2 offload，2048句子长度，可以顺利在单卡24G显存下面跑起来。后续我会找更大的显存机器看看在超长文本下分类情况如何。以及超过训练context情况下预测准确度如何
```





### RWKV-LM

[RWKV-LM](https://github.com/BlinkDL/RWKV-LM) 训练方法



#### SpikeGPT

[SpikeGPT](https://github.com/ridgerchu/SpikeGPT) 轻量级实现



### Alpaca-CoT

[Alpaca-CoT](https://github.com/PhoebusSi/Alpaca-CoT/blob/main/CN_README.md) 术语解释详细



### gpt4all

[gpt4all GPT4数据很多](https://github.com/nomic-ai/gpt4all)





## RWKV speech

https://github.com/theodorblackbird/lina-speech



## Chatterbox

[Chatterbox](https://github.com/enze5088/Chatterbox)



## ZeRO-Infinity: 利用NVMe打破GPU显存墙

[ZeRO-Infinity](https://zhuanlan.zhihu.com/p/513571706)



## BMInf 显存/内存换入换出

[BMInf](https://github.com/OpenBMB/BMInf)

```
BMInf 便是为这样的需求而生。通过高效的显存/内存换入换出
```





## LLaMA 前端

[text-generation-webui](https://github.com/oobabooga/text-generation-webui/issues/147)



## Docker GPU

[官方镜像](https://hub.docker.com/r/nvidia/cuda/tags?page=1&ordering=last_updated&name=11.2)

[gist安装脚本](https://gist.github.com/RodrigoCMoraes/c559954926f70df43ee9c396ef82668c)

[docker gpu](https://www.docker.com/blog/wsl-2-gpu-support-for-docker-desktop-on-nvidia-gpus/)



## 聊天机器人

> https://fancyerii.github.io/2019/02/14/chatbot/  大佬  李理的博客

- 使用PyTorch实现Chatbot



## tts chatgpt Whisper 代码备份

```

# """
# chatgpt
# """
# import openai
# from flask import Flask, Response, stream_with_context
# from flask import request
# import std.iJson as iJson
# app = Flask(__name__)
# # Set up OpenAI API key
# api_key = "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"
# openai.api_key = api_key

# def send_message(message_log):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
#         # The conversation history up to this point, as a list of dictionaries
#         messages=message_log,
#         # The maximum number of tokens (words or subwords) in the generated response
#         max_tokens=3800,
#         # The stopping sequence for the generated response, if any (not used here)
#         stop=None,
#         # The "creativity" of the generated response (higher temperature = more creative)
#         temperature=0.7,
#     )

#     # Find the first response from the chatbot that has text in it (some responses may not have text)
#     for choice in response.choices:
#         if "text" in choice:
#             return choice.text

#     # If no response with text is found, return the first response's content (which may be empty)
#     return response.choices[0].message.content

# global first_request, message_log
# message_log = []
# first_request = True

# def init_gpt():
#     global first_request, message_log
#     message_log = [{"role": "system", "content": "You are a helpful assistant."}]
#     first_request = True

# # http://127.0.0.1:5000/ask/chatgpt  # postman 这样传参 [{"a": 1}]
# @app.route("/ai/chatgpt", methods=['POST'])
# def chatgpt(user_input='hi'):

#     global first_request, message_log

#     if __name__ != "__main__":
#         user_input = request.form['text']

#     if user_input.lower() == "quit":
#         init_gpt()
#         print("Goodbye!")
#         return f"AI assistant: Goodbye!"

#     if len(message_log) + 1 > 10:
#         init_gpt()

#     if first_request:
#         init_gpt()
#         message_log.append({"role": "user", "content": user_input})
#         response = send_message(message_log)
#         message_log.append({"role": "assistant", "content": response})
#         print(f"You: {user_input}")
#         print(f"AI assistant: {response}")
#         first_request = False
#     else:
#         message_log.append({"role": "user", "content": user_input})
#         response = send_message(message_log)
#         message_log.append({"role": "assistant", "content": response})
#         print(f"You: {user_input}")
#         print(f"AI assistant: {response}")

#     return { "msg":f"AI assistant: {response}", "raw":response, "status":200 }

# # ret = chatgpt(user_input='把下面这句翻译成英语：豆浆应该加糖还是加盐') # 豆浆应该加糖还是加盐
# # print(f"raw msg: {ret['raw']}")
# # #chatgpt(user_input='不对，没有人会在豆浆里加糖')


# """
# tts
# """
# global runtts
# runtts = None
# from PaddleSpeechLLaMA.paddlespeech.cli.asr.infer import ASRExecutor
# from typing import Optional
# import os,time
# import paddle
# print('initialize tts engin...')
# begin = time.time_ns()
# exec('from paddlespeech.cli.tts import TTSExecutor')  # 不知道为什么一定要这样导入 # 必须在全局范围执行，放函数里执行是不行的
# TTSExecutor = locals()['TTSExecutor']   # 需要的符号已经在当前局部变量里面了，取出来用
# runtts = TTSExecutor()
# print(f'initialize tts done. use time in [s]: {(time.time_ns() - begin) / int(1e6) / 1000}')

# @app.route("/ai/chineseText2Audio", methods=['POST'])
# def chineseText2Audio(text='你好，欢迎使用百度飞桨深度学习框架！' ):
#     global runtts
#     status = runtts.execute([ '--am', 'fastspeech2_male', '--voc', 'pwgan_male', '--input', text])
#     return status


# """
# whisper output.wav --language Chinese --task translate --model medium
#     # 中转英成功
# """
# global whisperModel
# whisperModel = None
# @app.route("/ai/audio2EnghlishText", methods=['POST'])
# def audio2EnghlishText(task="translate", language='Chinese'):
#     global whisperModel
#     import sys, time
#     # sys.argv = [ sys.argv[0] ]
#     # sys.argv.append( 'output.wav' )
#     # sys.argv.append( '--language' )
#     # sys.argv.append( 'Chinese' )
#     # sys.argv.append( '--task' )
#     # # sys.argv.append( 'translate' )  # 这是识别原语言，输出源语言；translate 这是固定输出英语
#     # sys.argv.append( 'translate' )
#     # sys.argv.append( '--model' )
#     # sys.argv.append( 'large-v2' )
#     # sys.argv.append( '--output_format' )
#     # sys.argv.append( 'srt' )

#     import argparse
#     import os
#     import warnings
#     from typing import TYPE_CHECKING, Optional, Tuple, Union

#     import numpy as np
#     import torch
#     import tqdm

#     from WhisperLLaMa.whisper.audio import (
#         FRAMES_PER_SECOND,
#         HOP_LENGTH,
#         N_FRAMES,
#         N_SAMPLES,
#         SAMPLE_RATE,
#         log_mel_spectrogram,
#         pad_or_trim,
#     )
#     from WhisperLLaMa.whisper.decoding import DecodingOptions, DecodingResult
#     from WhisperLLaMa.whisper.timing import add_word_timestamps
#     from WhisperLLaMa.whisper.tokenizer import LANGUAGES, TO_LANGUAGE_CODE, get_tokenizer
#     from WhisperLLaMa.whisper.utils import (
#         exact_div,
#         format_timestamp,
#         get_writer,
#         make_safe,
#         optional_float,
#         optional_int,
#         str2bool,
#     )

#     if TYPE_CHECKING:
#         from WhisperLLaMa.whisper.model import Whisper


#     from WhisperLLaMa.whisper import available_models

#     # fmt: off
#     # parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
#     # parser.add_argument("audio", nargs="+", type=str, help="audio file(s) to transcribe")
#     # parser.add_argument("--model", default="small", choices=available_models(), help="name of the Whisper model to use")
#     # parser.add_argument("--model_dir", type=str, default=None, help="the path to save model files; uses ~/.cache/whisper by default")
#     # parser.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu", help="device to use for PyTorch inference")
#     # parser.add_argument("--output_dir", "-o", type=str, default=".", help="directory to save the outputs")
#     # parser.add_argument("--output_format", "-f", type=str, default="all", choices=["txt", "vtt", "srt", "tsv", "json", "all"], help="format of the output file; if not specified, all available formats will be produced")
#     # parser.add_argument("--verbose", type=str2bool, default=True, help="whether to print out the progress and debug messages")

#     # parser.add_argument("--task", type=str, default="transcribe", choices=["transcribe", "translate"], help="whether to perform X->X speech recognition ('transcribe') or X->English translation ('translate')")
#     # parser.add_argument("--language", type=str, default=None, choices=sorted(LANGUAGES.keys()) + sorted([k.title() for k in TO_LANGUAGE_CODE.keys()]), help="language spoken in the audio, specify None to perform language detection")

#     # parser.add_argument("--temperature", type=float, default=0, help="temperature to use for sampling")
#     # parser.add_argument("--best_of", type=optional_int, default=5, help="number of candidates when sampling with non-zero temperature")
#     # parser.add_argument("--beam_size", type=optional_int, default=5, help="number of beams in beam search, only applicable when temperature is zero")
#     # parser.add_argument("--patience", type=float, default=None, help="optional patience value to use in beam decoding, as in https://arxiv.org/abs/2204.05424, the default (1.0) is equivalent to conventional beam search")
#     # parser.add_argument("--length_penalty", type=float, default=None, help="optional token length penalty coefficient (alpha) as in https://arxiv.org/abs/1609.08144, uses simple length normalization by default")

#     # parser.add_argument("--suppress_tokens", type=str, default="-1", help="comma-separated list of token ids to suppress during sampling; '-1' will suppress most special characters except common punctuations")
#     # parser.add_argument("--initial_prompt", type=str, default=None, help="optional text to provide as a prompt for the first window.")
#     # parser.add_argument("--condition_on_previous_text", type=str2bool, default=True, help="if True, provide the previous output of the model as a prompt for the next window; disabling may make the text inconsistent across windows, but the model becomes less prone to getting stuck in a failure loop")
#     # parser.add_argument("--fp16", type=str2bool, default=True, help="whether to perform inference in fp16; True by default")

#     # parser.add_argument("--temperature_increment_on_fallback", type=optional_float, default=0.2, help="temperature to increase when falling back when the decoding fails to meet either of the thresholds below")
#     # parser.add_argument("--compression_ratio_threshold", type=optional_float, default=2.4, help="if the gzip compression ratio is higher than this value, treat the decoding as failed")
#     # parser.add_argument("--logprob_threshold", type=optional_float, default=-1.0, help="if the average log probability is lower than this value, treat the decoding as failed")
#     # parser.add_argument("--no_speech_threshold", type=optional_float, default=0.6, help="if the probability of the <|nospeech|> token is higher than this value AND the decoding has failed due to `logprob_threshold`, consider the segment as silence")
#     # parser.add_argument("--word_timestamps", type=str2bool, default=False, help="(experimental) extract word-level timestamps and refine the results based on them")
#     # parser.add_argument("--prepend_punctuations", type=str, default="\"\'“¿([{-", help="if word_timestamps is True, merge these punctuation symbols with the next word")
#     # parser.add_argument("--append_punctuations", type=str, default="\"\'.。,，!！?？:：”)]}、", help="if word_timestamps is True, merge these punctuation symbols with the previous word")
#     # parser.add_argument("--threads", type=optional_int, default=0, help="number of threads used by torch for CPU inference; supercedes MKL_NUM_THREADS/OMP_NUM_THREADS")
#     # # fmt: on

#     # args = parser.parse_args().__dict__
#     from std.iJson import string, parse
#     # ags = string(args)
#     args = parse('{"audio": ["output.wav"], "model": "large-v2", "model_dir": null, "device": "cuda", "output_dir": ".", "output_format": "srt", "verbose": true, "task": "translate", "language": "Chinese", "temperature": 0, "best_of": 5, "beam_size": 5, "patience": null, "length_penalty": null, "suppress_tokens": "-1", "initial_prompt": null, "condition_on_previous_text": true, "fp16": true, "temperature_increment_on_fallback": 0.2, "compression_ratio_threshold": 2.4, "logprob_threshold": -1.0, "no_speech_threshold": 0.6, "word_timestamps": false, "prepend_punctuations": "\\"\'“¿([{-", "append_punctuations": "\\"\'.。,，!！?？:：”)]}、", "threads": 0}')
#     args['task'] = task
#     args['language'] = language
#     model_name: str = args.pop("model")
#     model_dir: str = args.pop("model_dir")
#     output_dir: str = args.pop("output_dir")
#     output_format: str = args.pop("output_format")
#     device: str = args.pop("device")
#     os.makedirs(output_dir, exist_ok=True)

#     # args = parser.parse_args().__dict__
#     # model_name: str = args.pop("model")
#     # model_dir: str = args.pop("model_dir")
#     # output_dir: str = args.pop("output_dir")
#     # output_format: str = args.pop("output_format")
#     # device: str = args.pop("device")
#     # os.makedirs(output_dir, exist_ok=True)

#     if model_name.endswith(".en") and args["language"] not in {"en", "English"}:
#         if args["language"] is not None:
#             warnings.warn(
#                 f"{model_name} is an English-only model but receipted '{args['language']}'; using English instead."
#             )
#         args["language"] = "en"

#     temperature = args.pop("temperature")
#     if (increment := args.pop("temperature_increment_on_fallback")) is not None:
#         temperature = tuple(np.arange(temperature, 1.0 + 1e-6, increment))
#     else:
#         temperature = [temperature]

#     if (threads := args.pop("threads")) > 0:
#         torch.set_num_threads(threads)
    
#     from WhisperLLaMa.whisper import load_model

#     if not whisperModel:
#         print('loading whisper model...')
#         begin = time.time_ns()
#         whisperModel = load_model(model_name, device=device, download_root=model_dir)
#         print(f'loading whisper model done. use time in [s]: {(time.time_ns() - begin) / int(1e6) / 1000}')

#     from WhisperLLaMa.whisper.transcribe import transcribe
#     writer = get_writer(output_format, output_dir)
#     for audio_path in args.pop("audio"):
#         begin = time.time_ns()
#         result = transcribe(whisperModel, audio_path, temperature=temperature, **args)
#         print(f'loading whisper model done. use time in [s]: {(time.time_ns() - begin) / int(1e6) / 1000}')
#         # writer(result, audio_path)
#         text_en = result['text']
#         return text_en

#     return None


# if __name__ == '__main__':
#     re = chatgpt(user_input='中文语音合成真好用！')
#     success = chineseText2Audio(text='中文语音合成真好用！')
#     text = audio2EnghlishText(task="transcribe", language='Chinese')
#         # ["transcribe", "translate"]
#     print(text)
#     print('done.')

# """
# TTS的主要代码在这: /root/github/echodict/LLaMA_int8/PaddleSpeech/paddlespeech/cli/tts/infer.py
# 调用方法:
#     from paddlespeech.cli.tts.infer import TTSExecutor
#     tts = TTSExecutor()
#     tts(am="fastspeech2_male", voc="pwgan_male", text="今天天气十分不错。", output="output.wav")
# """


# """
# # https://github.com/PaddlePaddle/PaddleSpeech/blob/develop/docs/source/tts/quick_start_cn.md
#     # TTS 从训练到生成音频

# # https://github.com/PaddlePaddle/PaddleSpeech/blob/develop/docs/tutorial/tts/tts_tutorial.ipynb
#     # TTS 进阶



# pip install opencv-python  # import cv2
#     # 不知道为什么，不装会出错。它自动装的依赖又没有

# git clone https://github.com/PaddlePaddle/PaddleSpeech.git
# cd PaddleSpeech
# pip install pytest-runner
# pip install .

# paddlespeech tts --am fastspeech2_male --voc pwgan_male --input "你好，欢迎使用百度飞桨深度学习框架！"
#     # 生成 output.wav

#     # https://github.com/PaddlePaddle/PaddleSpeech/pull/2660
    
#     from paddlespeech.cli.tts.infer import TTSExecutor
#     tts = TTSExecutor()
#     tts(am="fastspeech2_male", voc="pwgan_male", text="今天天气十分不错。", output="output.wav")

# """



# """
# flask --app server run --debug --host 0.0.0.0 --port 5000

# curl -d "text=hi"  "http://127.0.0.1:5000/ai/chatgpt"
# curl -d "text=quit"  "http://127.0.0.1:5000/ai/chatgpt"
# curl -d "text=hi"  "http://209.141.34.77:5000/ai/chatgpt"
# curl -d "text=quit"  "http://209.141.34.77:5000/ai/chatgpt"

# curl -d "text=这是一段中文语音合成的高品质男声"  "http://127.0.0.1:5000/ai/tts" --output out.wav
# curl -d "text=这是一段中文语音合成的高品质男声"  "http://209.141.34.77:5000/ai/tts" --output out.wav

# """
# import time
# import WhisperLLaMa

# _whisper_mode = "base" # 好像只有小模型可以中翻英
# # _whisper_mode = "medium"
# #_whisper_mode = "large-v2" # 好像不能中翻英
# print('loading whisper model...')
# begin = time.time_ns()
# whisperModel = WhisperLLaMa.load_model(_whisper_mode, device="cuda") # large-v2
#     # /root/.cache/whisper/base.pt
# print(f'loading whisper model done. use time in [s]: {(time.time_ns() - begin) / int(1e6) / 1000}')

# from PaddleSpeechLLaMA.paddlespeech.cli.asr.infer import ASRExecutor
# from typing import Optional
# import os,time
# import paddle
# print('initialize tts engin...')
# begin = time.time_ns()
# exec('from paddlespeech.cli.tts import TTSExecutor')  # 不知道为什么一定要这样导入
# TTSExecutor = locals()['TTSExecutor']   # 需要的符号已经在当前局部变量里面了，取出来用
# runtts = TTSExecutor()
# print(f'initialize tts done. use time in [s]: {(time.time_ns() - begin) / int(1e6) / 1000}')
# #status = runtts.execute([ '--am', 'fastspeech2_male', '--voc', 'pwgan_male', '--input', '你好，欢迎使用百度飞桨深度学习框架！' ])



# # http://127.0.0.1:5000/ai/tts
# # curl -d "text=这是一段中文语音合成的高品质男声"  "http://127.0.0.1:5000/ai/tts" --output out.wav
# @app.route("/ai/tts", methods=['POST'])  # 输入中文，输出音频流
# def tts():
#     if __name__ != "__main__":
#         user_input = request.form['text']
#     else:
#         user_input = '你好，欢迎使用百度飞桨深度学习框架！'

#     def generate(pth):
#         with open(pth, 'rb') as f:
#             data = f.read(1024)
#             while data:
#                 yield data
#                 data = f.read(1024)
    
#     pth = './output.wav'
#     status = runtts.execute([ '--am', 'fastspeech2_male', '--voc', 'pwgan_male', '--input', user_input ])
#     if (status):
#         if __name__ != "__main__": 
#             return Response(stream_with_context(generate(pth)), content_type='audio/mp3')
#         else:
#             with open(pth, 'rb') as f:
#                 data = f.read()
#                 return data
#     else:
#         return 'unknow error'

# @app.route("/ai/audio2text", methods=['POST'])  # 输入中文音频的 base64 串，返回 英文文本
# def audio2text():
#     import WhisperLLaMa
#     global whisperModel
#     pth = './output.wav'
#     if __name__ != "__main__":
#         user_input = request.form['audio']
#     else:
#         with open(pth, 'rb') as f:
#             audio = f.read()
#         user_input = '你好，欢迎使用百度飞桨深度学习框架！'

#     # load audio and pad/trim it to fit 30 seconds
#     audio = WhisperLLaMa.load_audio(pth)
#     audio = WhisperLLaMa.pad_or_trim(audio)

#     # make log-Mel spectrogram and move to the same device as the model
#     mel = WhisperLLaMa.log_mel_spectrogram(audio).to(whisperModel.device)

#     # detect the spoken language
#     _, probs = whisperModel.detect_language(mel)
#     print(f"Detected language: {max(probs, key=probs.get)}")

#     # decode the audio
#     # options = whisper.DecodingOptions()
#     # result_origin = whisper.decode(whisperModel, mel, options)  

#     beam_size=5
#     best_of=None
#     temperature=0.0
#     decode_options = dict(language="en", best_of=best_of, beam_size=beam_size, temperature=temperature) # --task translate 是所有语言翻译为英文，目前尚未支持翻译为其他语言
#     transcribe_options = dict(task="transcribe", **decode_options)
#     transcription = whisperModel.transcribe(pth, **transcribe_options)
    
#     # audio_text = result_origin.text
#     audio_text_en = transcription["text"]

#     # # print the recognized text
#     # print(f'audio text is: {audio_text}')
#     # print(f'transcription is: {audio_text_en}')

#     # return { "audio_text":audio_text, "audio_text_en":audio_text_en }

# if __name__ == "__main__":
#     rec_text = audio2text()
#     wav = tts()
#     result = chatgpt()
#     msg = result["msg"]
    # print( msg )



# if __name__ == '__main__':
#     import sys
#     sys.argv.append( 'tts' )
#     sys.argv.append( '--am' )
#     sys.argv.append( 'fastspeech2_male' )
#     sys.argv.append( '--voc' )
#     sys.argv.append( 'pwgan_male' )
#     sys.argv.append( '--input' )
#     sys.argv.append( '你好，欢迎使用百度飞桨深度学习框架！' )
    
#     exec('from paddlespeech.cli.tts import TTSExecutor')
#     lcls = locals()
#     _entry = lcls['TTSExecutor']
#     status = _entry().execute(sys.argv[2:])

# from PaddleSpeechLLaMA.paddlespeech.cli.entry import _execute
# from PaddleSpeechLLaMA.paddlespeech.cli.entry import _executeTTS
# _executeTTS()

# import sys
# if __name__ == '__main__':
#     sys.argv.append( 'tts' )
#     sys.argv.append( '--am' )
#     sys.argv.append( 'fastspeech2_male' )
#     sys.argv.append( '--voc' )
#     sys.argv.append( 'pwgan_male' )
#     sys.argv.append( '--input' )
#     sys.argv.append( '你好，欢迎使用百度飞桨深度学习框架！' )
#     # _execute()
#     _executeTTS()
# 	# 实际是这样运行的

# from PaddleSpeechLLaMA.paddlespeech.cli.asr.infer import ASRExecutor
# from typing import Optional
# import os
# import paddle

# # import re
# # import sys
# # from paddlespeech.cli.entry import _execute
# # _execute()

# """
# /root/miniconda3/lib/python3.8/site-packages/paddlespeech vscode 打开，调试 cli/entry.py 里的 _execute
# """

# # from PaddleSpeechLLaMA.paddlespeech.cli.executor import BaseExecutor
# # class TTSExecutor(BaseExecutor):
# #     def __init__(self):
# #         super().__init__('tts')

# # tts = TTSExecutor()

# # # from PaddleSpeech.paddlespeech.cli.tts.infer import TTSExecutor

# # # from PaddleSpeech.paddlespeech.resource import CommonTaskResource

# # def tts(text: str,
# #     am: str='fastspeech2_csmsc',
# #     am_config: Optional[os.PathLike]=None,
# #     am_ckpt: Optional[os.PathLike]=None,
# #     am_stat: Optional[os.PathLike]=None,
# #     spk_id: int=0,
# #     phones_dict: Optional[os.PathLike]=None,
# #     tones_dict: Optional[os.PathLike]=None,
# #     speaker_dict: Optional[os.PathLike]=None,
# #     voc: str='hifigan_csmsc',
# #     voc_config: Optional[os.PathLike]=None,
# #     voc_ckpt: Optional[os.PathLike]=None,
# #     voc_stat: Optional[os.PathLike]=None,
# #     lang: str='zh',
# #     device: str=paddle.get_device(),
# #     output: str='output.wav',
# #     use_onnx: bool=False,
# #     cpu_threads: int=2,
# #     fs: int=24000):
# #     paddle.set_device(device)
# #     pass

# # tts(am="fastspeech2_male", voc="pwgan_male", text="今天天气十分不错。", output="output.wav")

# global ars
# asr = ASRExecutor()
# #tts = TTSExecutor()
# # task_choices = ['asr', 'tts', 'cls', 'text', 'vector']
# # model_name_format = {
# #    'asr': 'Model-Size-Code Switch-Multilingual-Language-Sample Rate',
# #    'tts': 'Model-Language',
# #    'cls': 'Model-Sample Rate',
# #    'text': 'Model-Task-Language',
# #    'vector': 'Model-Sample Rate'
# # }

# # http://127.0.0.1:5000/ask/chatgpt  # postman 这样传参 [{"a": 1}]
# @app.route("/ask/llama", methods=['POST'])
# def llama():
#     return 'ok.'

# if __name__ == "__main__":
#     result = asr(audio_file="/root/github/echodict/LLaMA_int8/PaddleSpeechLLaMA/zh.wav")  # 识别

#     print(result)

# """
# flask --app server run --debug --host 0.0.0.0 --port 5000
# """

# import openai
# from flask import Flask
# from flask import request
# import std.iJson as iJson
# app = Flask(__name__)


# # Set up OpenAI API key
# api_key = "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"
# openai.api_key = api_key

# # Function to send a message to the OpenAI chatbot model and return its response


# def send_message(message_log):
#     # Use OpenAI's ChatCompletion API to get the chatbot's response
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
#         # The conversation history up to this point, as a list of dictionaries
#         messages=message_log,
#         # The maximum number of tokens (words or subwords) in the generated response
#         max_tokens=3800,
#         # The stopping sequence for the generated response, if any (not used here)
#         stop=None,
#         # The "creativity" of the generated response (higher temperature = more creative)
#         temperature=0.7,
#     )

#     # Find the first response from the chatbot that has text in it (some responses may not have text)
#     for choice in response.choices:
#         if "text" in choice:
#             return choice.text

#     # If no response with text is found, return the first response's content (which may be empty)
#     return response.choices[0].message.content


# # Initialize the conversation history with a message from the chatbot
# global first_request, message_log
# message_log = []
# first_request = True

# def init_gpt():
#     global first_request, message_log
#     message_log = [{"role": "system", "content": "You are a helpful assistant."}]
#     first_request = True

# # http://127.0.0.1:5000/ask/chatgpt  # postman 这样传参 [{"a": 1}]
# @app.route("/ask/chatgpt", methods=['POST'])
# def chatgpt():

#     global first_request, message_log

#     if __name__ != "__main__":
#         user_input = request.form['text']
#     else:
#         user_input = 'hi'

#     if user_input.lower() == "quit":
#         init_gpt()
#         print("Goodbye!")
#         return f"AI assistant: Goodbye!"

#     if len(message_log) + 1 > 10:
#         init_gpt()

#     if first_request:

#         init_gpt()

#         response = send_message(message_log)
#         message_log.append({"role": "assistant", "content": response})
#         print(f"You: {user_input}")
#         print(f"AI assistant: {response}")
#         first_request = False
#     else:
#         message_log.append({"role": "user", "content": user_input})
#         response = send_message(message_log)
#         message_log.append({"role": "assistant", "content": response})
#         print(f"AI assistant: {response}")

#     return f"AI assistant: {response}"

# if __name__ == "__main__":
#     chatgpt()

```



# VITS Fast Fine-tuning

[VITS Fast Fine-tuning](https://github.com/Plachtaa/VITS-fast-fine-tuning) [训练方法](https://blog.csdn.net/cf2xh123/article/details/129398162)

[VITS-Umamusume-voice-synthesizer](https://huggingface.co/spaces/Plachta/VITS-Umamusume-voice-synthesizer)  [1](https://ngabbs.com/read.php?tid=34936044&rand=2) 同时说中英日三语



```
conda create -n vits python=3.10 && \
conda activate vits
	# 它是 11.7 可以和 KV5 共用环境



```





# whisperX

[whisperX](https://github.com/m-bain/whisperX)

[VITS Fast Fine-tuning](https://github.com/Plachtaa/VITS-fast-fine-tuning) [训练方法](https://blog.csdn.net/cf2xh123/article/details/129398162)

[VITS-Umamusume-voice-synthesizer](https://huggingface.co/spaces/Plachta/VITS-Umamusume-voice-synthesizer)  [1](https://ngabbs.com/read.php?tid=34936044&rand=2) 同时说中英日三语

[lina-speech  rwkv tts 必看](https://github.com/theodorblackbird/lina-speech)

[FunASR 阿里的](https://github.com/alibaba-damo-academy/FunASR/blob/main/docs/model_zoo/modelscope_models.md)

- [可检测长语音片段中有效语音的起止时间点](https://modelscope.cn/models/damo/speech_UniASR_asr_2pass-ja-16k-common-vocab93-tensorflow1-online/summary)

[讯飞语音唤醒](https://www.xfyun.cn/doc/asr/awaken/Android-SDK.html#_1%E3%80%81%E7%AE%80%E4%BB%8B)

[Whisper WebUI with a VAD for more accurate non-English transcripts (Japanese) #397](https://github.com/openai/whisper/discussions/397)

- JP 前端

doc\lang\programming\whisper-webui.pdf 详细文档



```

# autodl
	# 重要：把所有源都弄成 default 去
~/miniconda3/bin/conda init && \
ln -s ~/miniconda3/bin/conda /usr/local/bin && \
ln -s ~/miniconda3/bin/activate /usr/local/bin && \
ln -s ~/miniconda3/bin/deactivate /usr/local/bin && \
source ~/miniconda3/etc/profile.d/conda.sh


conda create --name whisperx python=3.10 && \
conda activate whisperx
	# conda remove -n whisperx  --all


pip install torch==2.0.0+cu118 torchvision==0.15.1+cu118 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118


apt-get update -y && \
apt-get install -y libsodium-dev && \
pip install shadowsocksr-cli 


git clone https://github.com/rofl0r/proxychains-ng.git && \
cd proxychains-ng && \
./configure --prefix=/usr --sysconfdir=/etc && \
make && \
make install && \
make install-config

vi /etc/proxychains.conf
localnet 127.0.0.0/255.0.0.0
localnet 172.16.0.0/255.240.0.0
localnet 192.168.0.0/255.255.0.0
[ProxyList]
socks5  127.0.0.1 1080
	# 改成这样


source /etc/network_turbo
	# autodl 自带学术加速
	# unset http_proxy && unset https_proxy
		# 取消


# proxychains4 pip install git+https://github.com/m-bain/whisperx.git

proxychains4 git clone https://github.com/m-bain/whisperX.git && \
cd whisperX && \
pip install numba numpy tqdm more-itertools tiktoken==0.3.3 && \
pip install faster-whisper transformers ffmpeg-python==0.2.0 pandas setuptools==65.6.3 nltk

proxychains4 pip install -e .

apt install ffmpeg

whisperx /root/1.mp3

whisperx --model large --language fr examples/sample_fr_01.wav


usage: whisperx [-h] [--model MODEL] [--model_dir MODEL_DIR] [--device DEVICE] [--device_index DEVICE_INDEX] [--batch_size BATCH_SIZE] [--compute_type {float16,float32,int8}]
                [--output_dir OUTPUT_DIR] [--output_format {all,srt,vtt,txt,tsv,json}] [--verbose VERBOSE] [--task {transcribe,translate}]
                [--language {af,am,ar,as,az,ba,be,bg,bn,bo,br,bs,ca,cs,cy,da,de,el,en,es,et,eu,fa,fi,fo,fr,gl,gu,ha,haw,he,hi,hr,ht,hu,hy,id,is,it,ja,jw,ka,kk,km,kn,ko,la,lb,ln,lo,lt,lv,mg,mi,mk,ml,mn,mr,ms,mt,my,ne,nl,nn,no,oc,pa,pl,ps,pt,ro,ru,sa,sd,si,sk,sl,sn,so,sq,sr,su,sv,sw,ta,te,tg,th,tk,tl,tr,tt,uk,ur,uz,vi,yi,yo,zh,Afrikaans,Albanian,Amharic,Arabic,Armenian,Assamese,Azerbaijani,Bashkir,Basque,Belarusian,Bengali,Bosnian,Breton,Bulgarian,Burmese,Castilian,Catalan,Chinese,Croatian,Czech,Danish,Dutch,English,Estonian,Faroese,Finnish,Flemish,French,Galician,Georgian,German,Greek,Gujarati,Haitian,Haitian Creole,Hausa,Hawaiian,Hebrew,Hindi,Hungarian,Icelandic,Indonesian,Italian,Japanese,Javanese,Kannada,Kazakh,Khmer,Korean,Lao,Latin,Latvian,Letzeburgesch,Lingala,Lithuanian,Luxembourgish,Macedonian,Malagasy,Malay,Malayalam,Maltese,Maori,Marathi,Moldavian,Moldovan,Mongolian,Myanmar,Nepali,Norwegian,Nynorsk,Occitan,Panjabi,Pashto,Persian,Polish,Portuguese,Punjabi,Pushto,Romanian,Russian,Sanskrit,Serbian,Shona,Sindhi,Sinhala,Sinhalese,Slovak,Slovenian,Somali,Spanish,Sundanese,Swahili,Swedish,Tagalog,Tajik,Tamil,Tatar,Telugu,Thai,Tibetan,Turkish,Turkmen,Ukrainian,Urdu,Uzbek,Valencian,Vietnamese,Welsh,Yiddish,Yoruba}]
                [--align_model ALIGN_MODEL] [--interpolate_method {nearest,linear,ignore}] [--no_align] [--return_char_alignments] [--vad_onset VAD_ONSET]
                [--vad_offset VAD_OFFSET] [--diarize] [--min_speakers MIN_SPEAKERS] [--max_speakers MAX_SPEAKERS] [--temperature TEMPERATURE] [--best_of BEST_OF]
                [--beam_size BEAM_SIZE] [--patience PATIENCE] [--length_penalty LENGTH_PENALTY] [--suppress_tokens SUPPRESS_TOKENS] [--initial_prompt INITIAL_PROMPT]
                [--condition_on_previous_text CONDITION_ON_PREVIOUS_TEXT] [--fp16 FP16] [--temperature_increment_on_fallback TEMPERATURE_INCREMENT_ON_FALLBACK]
                [--compression_ratio_threshold COMPRESSION_RATIO_THRESHOLD] [--logprob_threshold LOGPROB_THRESHOLD] [--no_speech_threshold NO_SPEECH_THRESHOLD]
                [--max_line_width MAX_LINE_WIDTH] [--max_line_count MAX_LINE_COUNT] [--highlight_words HIGHLIGHT_WORDS] [--segment_resolution {sentence,chunk}]
                [--threads THREADS] [--hf_token HF_TOKEN]
                audio [audio ...]

--word_timestamps True

--max_line_width 42 --max_line_count 2

```



## 只下载不安装

```
# see python3 summary.md -> pip只下载不安装
dnf install python310 && \
pip3.10 config list
	-> global.cache-dir='/mnt/tmp'

pip3.10 install conan && \
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh && \
bash Miniforge3-Linux-x86_64.sh -b && \
mv ~/miniforge3 /mnt && \
ln -s /mnt/miniforge3 ~/miniforge3 && \
~/miniforge3/bin/conda init && \
ln -s ~/miniforge3/bin/conda /usr/local/bin && \
ln -s ~/miniforge3/bin/activate /usr/local/bin && \
ln -s ~/miniforge3/bin/deactivate /usr/local/bin && \
source ~/miniforge3/etc/profile.d/conda.sh
	# 关掉 shell 重新打开

conda install --download-only pytorch==2.0.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia
	# 仅下载不安装




```



## aac

```
conda activate whisperx

whisperx ./audio/Siren14Voice_39606320.s14.aac --model large-v2 --batch_size 4 --language ja --output_dir ./audio


```



```
import whisperx
import gc

device = "cuda" 
audio_file = "./audio/Siren14Voice_39606320.s14.aac"
batch_size = 16 # reduce if low on GPU mem
compute_type = "float16" # change to "int8" if low on GPU mem (may reduce accuracy)

# 1. Transcribe with original whisper (batched)
model = whisperx.load_model("large-v2", device, compute_type=compute_type)

audio = whisperx.load_audio(audio_file)
result = model.transcribe(audio, batch_size=batch_size)
print(result["segments"]) # before alignment

# delete model if low on GPU resources
# import gc; gc.collect(); torch.cuda.empty_cache(); del model

# 2. Align whisper output
model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)

print(result["segments"]) # after alignment


```



### librosa

[How to get the duration of audio in Python?](https://www.tutorialspoint.com/how-to-get-the-duration-of-audio-in-python)

- librosa 必看



```
import glob
import librosa

def get_duration_librosa(file_path):
   audio_data, sample_rate = librosa.load(file_path)
   duration = librosa.get_duration(y=audio_data, sr=sample_rate)
   return duration

pths = glob.glob("E:/NLPP_aac" + '/*.aac', recursive=False)

for pth in pths:
    if  not ("Siren14Voice_39606320.s14.aac" in pth):
        continue
    duration = get_duration_librosa(pth)
    # print(f"Duration: {duration:.2f} seconds")
    if duration < 0.5:
        continue
```






```
#　pip install librosa
import librosa
def get_duration_librosa(file_path):
   audio_data, sample_rate = librosa.load(file_path)
   duration = librosa.get_duration(y=audio_data, sr=sample_rate)
   return duration
file_path = filename
duration = get_duration_librosa(file_path)
print(f"Duration: {duration:.2f} seconds")
```





```

filename =r"E:/NLPP_aac/Siren14Voice_39606320.s14.aac"

from pydub import AudioSegment
def get_duration_pydub(file_path):
   audio_file = AudioSegment.from_file(file_path)
   duration = audio_file.duration_seconds
   return duration
file_path = filename
duration = get_duration_pydub(file_path)
print(f"Duration: {duration:.2f} seconds")
```





### ffmpeg-python

[ffmpeg-python](https://github.com/kkroening/ffmpeg-python)

```
# install from source will slove "no probe" err
import ffmpeg

filename =r"E:/NLPP_aac/Siren14Voice_39606320.s14.aac"

metadata = ffmpeg.probe(filename)
video_stream = next((stream for stream in metadata['streams'] if stream['codec_type'] == 'video'), None)

fps = metadata['streams'][0]['avg_frame_rate'].split('/')[0]
duration = metadata['streams'][0]['duration']

width = int(video_stream['width'])
height = int(video_stream['height'])

print(f'Width: {width}, Height: {height}, FPS: {fps}, Duration: {duration}')
```



### test gpu

```
>>> import torch

>>> torch.cuda.is_available()
True

>>> torch.cuda.device_count()
1

>>> torch.cuda.current_device()
0

>>> torch.cuda.device(0)
<torch.cuda.device at 0x7efce0b03be0>

>>> torch.cuda.get_device_name(0)
'GeForce GTX 950M'
```



# TTS

[tts-vue](https://github.com/LokerL/tts-vue)



# NLP

[【SimCSE】没有标注数据也能训练文本匹配模型（附源码）](https://zhuanlan.zhihu.com/p/599230890)

[【P-Tuning】 一种自动学习 prompt pattern 的方法（附源码）](https://zhuanlan.zhihu.com/p/583022692)

[mlflow](https://github.com/mlflow/mlflow) 港科大



# OpenNMT

[OpenNMT-py](https://github.com/OpenNMT/OpenNMT-py)

[finetune NLLB-200](https://forum.opennmt.net/t/finetuning-and-curating-nllb-200-with-opennmt-py/5238)



# DALLE2

[DALLE2](https://github.com/lucidrains/DALLE2-pytorch)



# SSH端口转发

[彻底搞懂SSH端口转发](https://zhuanlan.zhihu.com/p/148825449)

[Windows下，让不同程序使用不同网卡](https://blog.csdn.net/cantjie/article/details/104907455)

```
在这个vps上装一个sniproxy，设置一下代理全部80和443 端口访问（也可以设置只代理openai的网址），然后在发起访问的这一端把openai的地址解析到新加坡这个vps的ip上就行了，这一步我是用dnsmasq实现的
```



[ssh windows vscode](https://gist.github.com/john-auld/a55ffe44e9965623f530cb487e33cebd)

```
# Make sure you're running as an Administrator
Set-Service ssh-agent -StartupType Automatic
Start-Service ssh-agent
Get-Service ssh-agent

ssh-add -l
Add a ssh key

ssh-add

If you add the line $env:GIT_SSH="C:\Windows\System32\OpenSSH\ssh.exe" to your Powershell profile the environment variable will always be used.

notepad $profile

```





# katago

[colab](https://colab.research.google.com/drive/1w69zA4bxRwzph5vG2dr4UeE4Xw2I0hE9) [1](https://zhuanlan.zhihu.com/p/594795175)



# disco diffusion

[最近disco diffusion大火，这个模型是如何训练的？如何训练自己的diffusion模型？](https://www.zhihu.com/question/566475839/answer/2950417560)



# Midjourney V5

 [Midjourney V5](https://www.36kr.com/p/2179360611185160)



# chatllama

[chatllama](https://github.com/nebuly-ai/nebullvm/tree/main/apps/accelerate/chatllama)



# UGUI

- https://www.raywenderlich.com/6570-introduction-to-unity-ui-part-1

- https://blog.csdn.net/Wrinkle2017/article/details/117257104  息屏开屏后，屏幕自动旋转刷新

  > ```c#
  >  private void OnApplicationPause(bool pauseStatus)
  >     {
  >         if (pauseStatus)
  >         {
  >             SaveDataToLocal.Instance.SaveAccountData(UserData.Instance.ifFirstJoin, UserData.Instance.CurrentBigClassLeve, MainUIModel.Instance.ifOpenAudio, UserData.Instance.ifFinishGuide1, UserData.Instance.ifFinishGuide2, UserData.Instance.isFirstInNewLevel);
  >             //Screen.orientation = ScreenOrientation.PortraitUpsideDown;
  >             //息屏开屏后，屏幕自动旋转刷新
  >             if (Input.deviceOrientation == DeviceOrientation.LandscapeLeft)
  >                 Screen.orientation = ScreenOrientation.LandscapeRight;
  >             else 
  >                 Screen.orientation = ScreenOrientation.LandscapeLeft;
  >         }
  >         else
  >         {
  >             Screen.orientation = ScreenOrientation.AutoRotation;
  >         }
  >     }
  > 
  > ```



# CXX原生GPU编程

- https://github.com/stotko/stdgpu  gpu可用的字典数据结构



# 多进程计算

```

# main.js
	var Comcluster = new computecluster({
        module: './calc.js',
        max_processes: 3
    })
    let SegmentRun = 3
    for (var i = 0; i < SegmentRun; i++) {
        console.log(`新进程开始 ${i}======================`)
        Comcluster.enqueue({
            "th_proccess":i
        }, function (err, r) {
            r = JSON.parse(r)
            if (err) {
                throw err
            }
            console.log(`进程结束 ${r.th_proccess}======================`)
            if (--SegmentRun === 0) {
                Comcluster.exit()
                console.log(`all task done.`)
            }
        })
    }
    
# calc.js
process.on('message', function (data) {

    return process.send(JSON.stringify({msg:"计算成功", "th_proccess":data.th_proccess}))

})


  
```





# 多线程计算

```
// main.js
    const { Worker,workerData, parentPort } = require('worker_threads')
    let re = await new Promise(function (resolve, reject) {
        const wk1 = new Worker(path.resolve(__dirname, './calc.js'))
        wk1.ref()
        wk1.postMessage({"th_thread":1})
        wk1.on('message', async (re)=>{
            resolve('ok')
        })
    })
    
// calc.js
const { parentPort } = require('worker_threads')
parentPort.onmessage = function (event) {
    const startTime = new Date().getTime()
    let th_thread = event.data.th_thread
    parentPort.postMessage([true, th_thread])
}

    
```





# cudf

  [用法教程](https://docs.rapids.ai/api/cudf/stable/user_guide/10min.html)

- https://blog.csdn.net/ltochange/article/details/121339718  在docker容器中使用显卡

- https://github.com/rapidsai/node/issues/451

  

  [cudf](https://github.com/rapidsai/cudf)

  - https://blog.csdn.net/qq_35916006/article/details/125718801

  [proxychains-ng](https://github.com/rofl0r/proxychains-ng)

  [ssr-command-clien](https://github.com/TyrantLucifer/ssr-command-client)

  [How to setup CUDA 10.2, 11.0, and 11.5 in order to use eddy_cuda10.2](https://www.nemotos.net/?p=5067)

  ```
  
  conda install cudatoolkit=11.2 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/ -c conda-forge
  
  !pip install cudf-cu11 --extra-index-url=https://pypi.nvidia.com/
  	# colab 这样装
  
  pip install cudf-cu11 --extra-index-url=https://pypi.nvidia.com/
  	# autodl 这样装
  
  # downloads a CSV, then uses the GPU to parse it into rows and columns and run calculations
  
  import cudf, requests
  from io import StringIO
  
  url = "https://github.com/plotly/datasets/raw/master/tips.csv"
  content = requests.get(url).content.decode('utf-8')
  
  tips_df = cudf.read_csv(StringIO(content))
  tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
  
  # display average tip by dining party size
  print(tips_df.groupby('size').tip_percentage.mean())
  	# 成功运行！
  
  
  git clone https://github.com/rofl0r/proxychains-ng.git && \
  cd proxychains-ng && \
  ./configure --prefix=/usr --sysconfdir=/etc && \
  make && \
  make install && \
  make install-config
  
  vi /etc/proxychains.conf
  	socks5  127.0.0.1 1080
  	# 改成这样
  
  
  yum install epel-release -y && \
  yum update && \
  yum install libsodium -y && \
  pip install shadowsocksr-cli
  	# yum 是依赖 python2.7 的，不要替换系统的默认python
  
  apt-get update -y && \
  apt-get install -y libsodium-dev && \
  pip install shadowsocksr-cli 
  
  
  shadowsocksr-cli --add-url https://www.ftwnet.net/sub/xxxxx?sub=1
  	# ftwc.cc 找 ssr订阅地址
  
  shadowsocksr-cli -u
  	# 更新订阅
  
  shadowsocksr-cli -l
  	# 列出所有可用代理地址
  	
  shadowsocksr-cli -s 1
  	# 开启代理， 1 是前面打印出来的 编号
  	
  shadowsocksr-cli -S 1
  	# 停止代理
  
  shadowsocksr-cli --test-speed 15
  	# 测速
  	# ldconfig -p | grep libcrypto
  		# 出错的话，看一下这个
  
  shadowsocksr-cli --list-address
  	# 打印监听地址
  	# 默认监听端口是 1080
  	
  vi /etc/resolv.conf  # 临时修改 DNS，配置会实时生效，重启后失效
  nameserver 1.1.1.1
  nameserver 8.8.8.8
  	# 改成这样
  	vi /etc/sysconfig/network-scripts/ifcfg-eth0
  		# 这个是永久的
  	
  	nameserver 172.16.7.1
  	nameserver 114.114.114.114
  		# 原来的值
  		
  
  proxychains4 curl https://www.youtube.com
  	# 成功
  
  
  /root/miniconda3/bin/conda init && \
  ln -s /root/miniconda3/bin/conda /usr/local/bin && \
  ln -s /root/miniconda3/bin/activate /usr/local/bin && \
  ln -s /root/miniconda3/bin/deactivate /usr/local/bin
  
  conda create -n nodecudf pip python=3.8 -y && \
  source activate nodecudf && \
  
  
  conda install -c https://conda.anaconda.org/rapidsai -c numba -c https://conda.anaconda.org/nvidia -c conda-forge cudf=23.02
  
  
  conda install -c nvidia cudatoolkit=11.2 && \
  conda install -c rapidsai-nightly cudf=23.04
  
  
  conda deactivate
  conda info -e
  conda env remove -n nodecudf
  
  
  
  
  
  # P40 titan XP 最高支持到 11.5
  
  #Uninstall the current CUDA version 
  apt-get --purge remove cuda nvidia* libnvidia-* && \
  dpkg -l | grep cuda- | awk '{print $2}' | xargs -n1 dpkg --purge && \
  apt-get remove cuda-* && \
  apt autoremove && \
  apt-get update
  
  apt-get --purge -y remove 'cuda*' && \
  apt-get --purge -y remove 'nvidia*' && \
  apt autoremove -y && \
  apt-get clean && \
  apt update -qq;
  
  sudo apt-get install software-properties-common -y && \
  sudo apt-get update
  
  wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin && \
  sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600 && \
  sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub && \
  sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /" && \
  sudo apt-get update && \
  sudo apt-get -y install cuda
  
  
  
  conda install -c rapidsai -c conda-forge -c nvidia \
      cudf=23.04 python=3.8 cudatoolkit=11.2
  
  
  curl -O 'https://nodejs.org/download/release/v14.21.1/node-v14.21.1-linux-x64.tar.gz'  && \
      tar zxvf node-v14.21.1-linux-x64.tar.gz -C /usr/local && \
      ln -s /usr/local/node-v14.21.1-linux-x64/bin/node /usr/local/bin/node && \
      ln -s /usr/local/node-v14.21.1-linux-x64/bin/npm /usr/local/bin/npm && \
      ln -s /usr/local/node-v14.21.1-linux-x64/bin/npx /usr/local/bin/npx && \
      npm install cnpm@7.1.0  pm2@4.5.1 -g --registry=https://registry.npm.taobao.org && \
      ln -s /usr/local/node-v14.21.1-linux-x64/bin/cnpm /usr/local/bin/cnpm && \
      ln -s /usr/local/node-v14.21.1-linux-x64/bin/pm2 /usr/local/bin/pm2
  
  RAPIDSAI_CUDA_VERSION=11 && \
  npm install @rapidsai/cudf
  
  
  ```

  

- https://github.com/rapidsai/node/tree/main/modules/cudf

  > - https://blog.csdn.net/sinat_26917383/article/details/104504600
  >
  > 用于处理数据，包括加载、连接、聚合和过滤数据。向GPU的转移允许大规模的加速，因为GPU比CPU拥有更多的内核。**一个比较好的使用场景是，代替并行**，在pandas处理比较慢的时候，**切换到cuDF，就不用写繁琐的并行了**。
  >
  > ```
  > docker pull ghcr.io/rapidsai/node:22.8.2-runtime-node16.15.1-cuda11-ubuntu20.04-cudf
  > ```
  >
  > 

- https://github.com/rapidsai/node/tree/main/modules/demo/client-server

  > 地图移动GPU 加速示例

- https://github.com/rapidsai/node

  > nodejs python cuda 加速



### 修改DNS

**方法一 静态ip永久修改dns**

服务器如果是静态ip地址的，那么修改很简单

vi /etc/resolv.conf

```javascript
nameserver 1.1.1.1
nameserver 8.8.8.8
```

复制

这样修改即可，重启仍然有效

**方法二 DHCP永久修改dns**

如果服务器是dhcp的，则需要修改另一个文件

vi /etc/sysconfig/network-scripts/ifcfg-eth0

```javascript
DNS1=8.8.8.8
DNS2=8.8.4.4
```

这样修改了此文件，重启之后/etc/resolv.conf也会生效



## docker 

- https://www.simplilearn.com/tutorials/docker-tutorial/how-to-install-docker-on-ubuntu
- https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04



# jax

```
# pip install jax==0.4.4
	# windows这样装
# github/segment/jax_pytrees.py
# https://jax.readthedocs.io/en/latest/notebooks/xmap_tutorial.html  需要仔细看的文档
# https://github.com/google/jax/issues/196  打印 ShapedArray
import jax
import jax.numpy as np
import jax.numpy as jnp
from typing import Any, Callable
from typing import Dict
from jax.experimental.maps import xmap
from jax import vmap, vjp, jvp
from jax.tree_util import Partial as partial
from jax.experimental.host_callback import call

"""
a={{1},{2}};a//MatrixForm
b= { {1, 2} }; b // MatrixForm
a.b // MatrixForm
c = { {1,3},{2,4} }; c//MatrixForm
c\[Transpose] // MatrixForm
c.c\[Transpose]//MatrixForm
"""

@jax.jit
def selu(x, alpha=1.67, lmbda=1.05):
  call(lambda x: print(f"x: {x}"), x)
  jax.debug.print("{x}", x=x)
  return lmbda * jnp.where(x > 0, x, alpha * jnp.exp(x) - alpha)

key = jax.random.PRNGKey(0)
x = jax.random.normal(key, (1000000,))
selu(x)



apt-get update && \
apt-get install software-properties-common -y && \
apt-get update

wget https://developer.download.nvidia.com/compute/cuda/11.4.4/local_installers/cuda_11.4.4_470.82.01_linux.run

https://developer.nvidia.com/downloads/c118-cudnn-local-repo-ubuntu1804-88012110-1amd64deb

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/ /"
sudo apt-get update
sudo apt-get -y install cuda

```





# gpu.js

- https://gist.github.com/jonathanlurie/04fa6343e64f750d03072ac92584b5df

  > gpu 没有高级数据结构，比如 nodejs 的 json，只有数组

```
    // npm i gup.js --save
    const { GPU } = require('gpu.js');
    const gpu = new GPU({ mode: 'gpu' });

    let arr = [ [1, 2, 3], [4, 5, 6] ]
    const kernel = gpu.createKernel(function ( arr ) {
        return arr[this.thread.y][this.thread.x]  // 获取当前线程的参数 // y 是行索引  x 是列索行
    }, { output: [3, 2] })  // 三列  两行
    const data = kernel(arr)  // 传参
```



```
// 并行生成一万个随机数
const { GPU } = require('gpu.js');
const gpu = new GPU({ mode: 'gpu' });
const nobs=10000;

const kernel = gpu.createKernel(function() {
const y=Math.random();
return y;
}, { output: [nobs] });
const data = kernel();
```







# node-sdl

- https://github.com/kmamal/node-sdl

- https://github.com/fosterseth/sdl2_video_player  **视频播放**

  - [必看](https://gist.github.com/thales17/fb2e4cff60890a51d9dddd4c6e832ad2) [2](https://hustlei.github.io/2018/11/msys2-for-win.html) [3](https://www.v2ex.com/t/823471)

  - [vcpkg 可能是更好的选择](https://github.com/microsoft/vcpkg/issues/23873) [2](https://stackoverflow.com/questions/64079180/vs-auto-linking-against-sdl2-libraries-installed-with-vcpkg-on-windows)

  - [nuget 优先用这个]()

    ```
    打开 C:\msys64\msys2.exe
    	# 从开始菜单进去 MSYS2 MINGW64
    		才找得到 gcc !!!
    	C:\msys64\home\Administrator
    		# 代码放这里
    
    pacman -Rs mingw-w64-x86_64-ffmpeg
    pacman -Rs mingw-w64-x86_64-SDL2
    	# 删除
    	
    pacman -Syu
    	# update all
    
    pacman -S git mingw-w64-x86_64-toolchain mingw64/mingw-w64-x86_64-SDL2 mingw64/mingw-w64-x86_64-SDL2_mixer mingw64/mingw-w64-x86_64-SDL2_image mingw64/mingw-w64-x86_64-SDL2_ttf mingw64/mingw-w64-x86_64-SDL2_net mingw64/mingw-w64-x86_64-cmake make
    
    
    
    sdl2-config --cflags --libs
    --> -IC:/msys64/mingw64/include/SDL2 -Dmain=SDL_main
    -LC:/msys64/mingw64/lib -lmingw32 -mwindows -lSDL2main -lSDL2
    
    // sd.c
    #include <SDL.h>
    int main(int argc, char *argv[]) {
    	return 0;
    }
    
    gcc -IC:/msys64/mingw64/include/SDL2 -Dmain=SDL_main -LC:/msys64/mingw64/lib -lmingw32 -mwindows -lSDL2main -lSDL2 sd.c
    	# 成功编译
    
    ```

    

- https://github.com/raullalves/player-cpp-ffmpeg-sdl 比较新

- https://github.com/kingslay/KSPlayer swiftui

  

msys2 packages:

- mingw-w64-x86_64-ffmpeg 3.3-1
- mingw-w64-x86_64-SDL2 2.0.5-1

```
https://www.msys2.org/
	# install and open it

pacman -S mingw-w64-x86_64-ffmpeg
	# C:\msys64\mingw64\include\libavutil
pacman -S mingw-w64-x86_64-SDL2
	# C:\msys64\mingw64\include\SDL2

gcc -IC:/msys64/mingw64/include/SDL2 -Dmain=SDL_main
-LC:/msys64/mingw64/lib -lmingw32 -mwindows -lSDL2main -lSDL2 sd.c


#include <SDL.h>
int main(int argc, char *argv[]) {
	return 0;
}

git clone https://github.com/fosterseth/sdl2_video_player.git


#include <libavcodec/avcodec.h>
	# 需要加一句

https://blog.csdn.net/jacke121/article/details/79312064
	# codec参数在58版本及之后就不会支持了，需要由codecpar参数所替代
	
	
        /* find decoder for the stream */
        //dec_ctx = st->codec;
        //dec = avcodec_find_decoder(dec_ctx->codec_id);
        //if (!dec) {
        //    fprintf(stderr, "Failed to find %s codec\n",
        //            av_get_media_type_string(type));
        //    return AVERROR(EINVAL);
        //}
			# 注释上面，添加下面

        //找到视频解码器，比如H264
        AVCodec* dec = avcodec_find_decoder(st->codecpar->codec_id);
        //独立的解码上下文
        AVCodecContext* dec_ctx = avcodec_alloc_context3(dec);
        avcodec_parameters_to_context(dec_ctx, st->codecpar);	
	

打开ps命令行
gcc -o ccc -IC:\msys64\mingw64\include -LC:\msys64\mingw64\bin -LE:\t\sdl_vide\sdl2_video_player\bin -lSDL2 -lavcodec-57 vidserv.c 

gcc -o ccc -IC:\msys64\mingw64\include -Dmain=SDL_main sd.c

gcc -o ccc -IC:\msys64\mingw64\include  -municode sd.c

x86_64-w64-mingw32-g++


-IC:/msys64/mingw64/include/SDL2 -Dmain=SDL_main


int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE, PWSTR pCmdLine, int nCmdShow)

```



1. Install MSYS2 from [https://www.msys2.org 2](https://www.msys2.org/)
2. Open “MSYS2 MinGW 64-bit” terminal then install needed software and libraries:
   `pacman -Syu` to update repositories and upgrade outdated packages
   `pacman -S --needed mingw-w64-x86_64-toolchain mingw-w64-x86_64-SDL2 mingw-w64-x86_64-SDL2_image mingw-w64-x86_64-SDL2_mixer mingw-w64-x86_64-SDL2_ttf mingw-w64-x86_64-cmake`
   You can install other needed packages, if you need.
3. Add “MSYS2 MinGW 64-bit” terminal to your VSCode by editing `settings.json`:
   Open command palette by `CTRL + SHIFT + P`
   Choose “Open user settings (JSON)”
   Add a new subobject to `terminal.integrated.profiles.windows` object:

```swift
"MSYS2 MinGW 64-bit": {
	"path": "C:\\msys64\\msys2_shell.cmd",
	"args": [
		"-defterm",
		"-here",
		"-no-start",
		"-mingw64"
	]
}
```

Adjust paths if needed.
Your config will look like this:

```swift
{
	// many other options
	"terminal.integrated.profiles.windows": {
		"MSYS2 MinGW 64-bit": {
			"path": "C:\\msys64\\msys2_shell.cmd",
			"args": [
				"-defterm",
				"-here",
				"-no-start",
				"-mingw64"
			]
		},
		// many other terminals
	}
}
```

1. Install and Microsoft C++ extension via extension marketplace, and you may need to install “CMake” and “CMake Tools” extensions, if you want to use CMake.
   Optional: You can also use clangd as code model, you need to install clangd extension and package ( `mingw-w64-clang-x86_64-clang-tools-extra`) then provide path to clangd executable in VSCode:
   `C:\msys64\mingw64\bin\clangd.exe`
2. In VSCode settings find “Cmake: Cmake Path” setting and enter path to your MinGW CMake:
   `C:\msys64\mingw64\bin\cmake.exe`
3. Create/open your CMake project and start exploring it by yourself.

Maybe I missed something, so feel free to ask about it.

You also can just use Makefiles but it’s not simple for beginner, and you will face some code model issues in VSCode.



# vxe-table

- https://github.com/x-extends/vxe-table



# CSS

- https://blog.csdn.net/zgh0711/article/details/78270555  flex布局保持内容不超出

- https://blog.csdn.net/zgh0711/article/details/86541139  多行显示，溢出时显示省略号

- https://blog.csdn.net/zgh0711/article/details/81536355 display 的 block，inline，inline-block

- https://blog.csdn.net/zgh0711/article/details/80167224  class 动态绑定

- https://blog.csdn.net/zgh0711/article/details/80172174   路由缓存 keep-alive

  > 保存某个组件的状态或避免重新渲染
  >
  >  App.vue
  >
  > ```javascript
  >     <keep-alive>
  >          <router-view v-if="$route.meta.keepAlive"></router-view>
  >         </keep-alive>
  >         <router-view v-if="!$route.meta.keepAlive"></router-view>
  >    ```
  >    
  > 
  >
  > 每个路由都可以给它定义 meta 属性，我们可以给想要缓存功能的路由定义一个 meta 对象，在里面定义一个 keepAlive 属性，值为 true，这个 meta 对象里面还可以定义其他的属性，比如 title。
  >
  > ```javascript
  >     {
  >          path: '/guideList',
  >             name: 'GuideList',
  >             meta: {keepAlive: true, title: 'title'},
  >             component: GuideList
  >         },
  >    ```
  >    
  > 
  >
  
- https://blog.csdn.net/zgh0711/article/details/80171138  给 v-html 渲染出的内容添加样式

  >```javascript
  ><div class="content" v-html="agreement.content"></div>
  >
  >.content >>> span{
  >        width: 100%;
  >        ...
  >    }
  >```
  >
  >通过在需要设置样式的元素前面加三个箭头就可以实现

- https://blog.csdn.net/zgh0711/article/details/80607158   ECharts 画 K 线图

- https://blog.csdn.net/zgh0711/article/details/89562566  自定义指令解决IOS12键盘收起后底部留白

  > ```javascript
  > import Vue from 'vue'
  > /**
  >  * 自定义指令 v-reset-page，以解决 iOS 12 中键盘收起后页面底部有留白的问题
  >  */
  > 
  > Vue.directive('resetPage', {
  >   inserted: function (el) {
  >     // 该方法有时候会出现点击了键盘右上角完成按钮，键盘收起又弹出的情况
  >     // el.addEventListener('blur', function () {
  >     //   if (/(iPhone|iPad|iPod|iOS)/i.test(navigator.userAgent)) {
  >     //     let currentPosition, timer
  >     //     let speed = 1//页面滚动距离
  >     //     timer = setInterval(function () {
  >     //       currentPosition = document.documentElement.scrollTop || document.body.scrollTop
  >     //       currentPosition -= speed
  >     //       window.scrollTo(0, currentPosition)//页面向上滚动
  >     //       currentPosition += speed //speed变量
  >     //       window.scrollTo(0, currentPosition)//页面向下滚动
  >     //       clearInterval(timer)
  >     //     }, 100)
  >     //   }
  >     // })
  >     
  >     // 监听键盘收起事件
  >     document.body.addEventListener('focusout', () => {
  >       if (/(iPhone|iPad|iPod|iOS)/i.test(navigator.userAgent)) {
  >         //软键盘收起的事件处理
  >         setTimeout(() => {
  >           const scrollHeight = document.documentElement.scrollTop || document.body.scrollTop || 0
  >           window.scrollTo(0, Math.max(scrollHeight - 1, 0))
  >         }, 100)
  >       }
  >     })
  >   }
  > })
  > 
  > 
  > ```
  >
  > ```javascript
  > // main.js 中引入
  > import './utils/directive'
  > ```
  >
  > ```javascript
  > // 在 input 中使用
  > <input v-reset-page v-model="searchKey" type="number" placeholder="搜索作品编号">
  > ```

- https://blog.csdn.net/zgh0711/article/details/100013303 背景音乐

  > ```
  > <audio ref="audio" src="https://img.youpenglai.com/penglai/1.mp3" loop preload="auto"></audio>
  > 
  > ```
  >
  > a
  >
  > ```javascript
  > <template>
  >   <div class="page-promotion flex-col">
  >     <div class="con-play flex" @click="audioPlayOrPause()">
  >       <img v-show="playFlag" class="audio-on" src="../assets/img/promotion/ic_sound_on.svg" alt="">
  >       <img v-show="!playFlag" class="audio-off" src="../assets/img/promotion/ic_sound_off.svg" alt="">
  >     </div>
  >     
  >     <audio ref="audio" src="https://img.youpenglai.com/penglai/1.mp3" autoplay loop preload="auto"></audio>
  >   </div>
  > </template>
  > 
  > <script>
  >   export default {
  >     name: 'Promotion',
  >     data () {
  >       return {
  >         playFlag: true,
  >         clickMusicBtn: false,
  >       }
  >     },
  >     
  >     async mounted () {
  >       this.audioAutoPlay()
  >       document.addEventListener("visibilitychange", (e) => { // 兼容ios微信手Q
  >         if (this.clickMusicBtn) { // 点击了关闭音乐按钮
  >           if (this.playFlag) {
  >             this.audioAutoPlay();
  >             this.playFlag = true;
  >           } else {
  >             this.audioPause();
  >             this.playFlag = false;
  >           }
  >       
  >           text.innerHTML = e.hidden;
  >           if (e.hidden) {  // 网页被挂起
  >             this.audioAutoPlay();
  >             this.playFlag = true;
  >           } else { // 网页被呼起
  >             this.audioPause();
  >             this.playFlag = false;
  >           }
  >         } else { // 未点击关闭音乐按钮
  >           if (this.playFlag) {
  >             this.audioPause();
  >             this.playFlag = false;
  >           } else {
  >             this.audioAutoPlay();
  >             this.playFlag = true;
  >           }
  >       
  >           text.innerHTML = e.hidden;
  >           if (e.hidden) {  // 网页被挂起
  >             this.audioPause();
  >             this.playFlag = false;
  >           } else { // 网页被呼起
  >             this.audioAutoPlay();
  >             this.playFlag = true;
  >           }
  >         }
  >       });
  >     },
  >     
  >     methods: {
  >       audioPlayOrPause() {
  >         this.clickMusicBtn = !this.clickMusicBtn;
  >         if (this.playFlag) {
  >           this.audioPause();
  >           this.playFlag = false;
  >         } else {
  >           this.audioAutoPlay();
  >           this.playFlag = true;
  >         }
  >       },
  >       audioPause() {
  >         let audio = this.$refs.audio
  >         audio.pause();
  >         document.addEventListener("WeixinJSBridgeReady", function () {
  >           audio.pause();
  >         }, false);
  >       },
  >       audioAutoPlay() {
  >         let audio = this.$refs.audio
  >         audio.play();
  >         document.addEventListener("WeixinJSBridgeReady", function () {
  >           audio.play();
  >         }, false);
  >       },
  >     },
  >   }
  > </script>
  > 
  > ```
  >
  > vue-cli3 项目，如果通过相对路径引用资源则会经过 webpack 打包，相反，如果通过绝对路径引用则不会经过 webpack 处理，注意这里资源的绝对路径不是 /public/xxx 而是直接填 public 里的路径，官方文档没有例子说这件事。



# React Native

- https://github.com/alantoa/react-native-awesome-slider/tree/main/example

- https://www.v2ex.com/t/843175

  > u2 player

- https://www.cnblogs.com/skychx/p/react-native-tweet.html  2 年 React Native 开发经验
- https://www.cnblogs.com/skychx/p/react-native-flatlist.html FlatList 原理解析与性能优化
- https://www.cnblogs.com/penghuwan/p/11633547.html  从React-Native坑中爬出
- https://www.cnblogs.com/penghuwan/p/11775900.html React-Native 转小程序
- https://github.com/alitajs/alita  umi.js ?



# push stream

- https://github.com/phoboslab/jsmpeg

- https://blog.csdn.net/a843334549/article/details/120697574  海康推流 [github](https://github.com/vCloudSail/jsmpeg-player)

- https://blog.csdn.net/qq_41619796/article/details/121161232

- https://gitee.com/zhairuihao/jsmpeg-ws-web [github](https://github.com/zhairuihao/jsmpeg-ws-web)

  > new account: 173xxxx5535
  >
  > cegbdfa
  >
  > cegfdb link to github
  >
  > link to 123xxxx5&qx.com

- https://www.cnblogs.com/zzsdream/p/13410224.html  **很详细**

  - https://github.com/ivan-94/video-push/blob/master/jsmpeg/server.js
  - https://github.com/phoboslab/jsmpeg/issues/338  websockect + jsmpeg
    - https://github.com/phoboslab/jsmpeg/issues/391

  

# nodegui qt

- https://github.com/nodegui/nodegui

  > NodeGUI is powered by **Qt5** 



# uView UI

```
关于uView UIuView UI 是一个用于uni-app 多端开发的优质UI 组件库， ... 代码，可发布到iOS、Android、Web（响应式）、以及各种小程序（微信/支付宝/ 
```

- https://blog.csdn.net/mrs_chens/article/details/108417919

  > uniapp 项目引入 uView 并简单使用

- https://github.com/panghujiajia/v2ex

  > uniapp 写的 V2EX 小程序

> 以上对比下来
> Flutter == ReactNative >>>>>>> **UniApp(做 App 用这个你就是坑自己**)



## vue和nvue

```
因为uni-app是逻辑和渲染分离的。渲染层，在app端提供了两套排版引擎：小程序方式的webview渲染，和weex方式的原生渲染。
两种渲染引擎可以自己根据需要选。vue文件走的webview渲染，nvue走的原生渲染。组件和js写法是一样的，css不一样，原生排版的能用的css必须是flex布局，这是web的css的子集。当然什么界面都可以用flex布出来。

区别和适用场景官方文档里写的很清楚：https://uniapp.dcloud.io/use-weex

```



# DotNet+Node

- https://github.com/Elringus/DotNetJS



# QT+Vue

- https://blog.csdn.net/yyt593891927/article/details/108546503
- https://zhuanlan.zhihu.com/p/88620573



# Vue+ios

- https://github.com/nativescript-vue/nativescript-vue
- https://docs.nativescript.org/environment-setup.html#macos-ios



# RustDesk

- https://www.v2ex.com/t/853682





# tesseract-ocr

- https://github.com/peirick/Tesseract-OCR_for_Windows

  > ```
  > git clone --recursive https://github.com/peirick/Tesseract-OCR_for_Windows.git
  > 
  > vs2019 编译，编码报错的文件改 gb2312 编码
  > 
  > ```



```javascript
/*

step 1: 安装 tesseract-ocr

先安装c++17
yum install centos-release-scl
yu install devtoolset-7-gcc-c++ --enablerepo='centos-sclo-rh'
scl enable devtoolset-7 'bash' # 切换编译器
which gcc

# https://github.com/tesseract-ocr/tessdata/blob/main/chi_sim.traineddata 先下载语言文件
# 自动安装的语言模型很小，不准确

// https://thelinuxcluster.com/2020/02/04/compiling-tesseract-5-0-on-centos-7/
> yum install autoconf automake libtool pkgconfig.x86_64 libpng12-devel.x86_64 libjpeg-devel libtiff-devel.x86_64 zlib-devel.x86_64
# wget http://www.leptonica.org/source/leptonica-1.79.0.tar.gz .
# tar -zxvf leptonica-1.79.0.tar.gz
# cd leptonica-1.79.0
# ./configure --prefix=/usr/local/leptonica-1.79.0
# make
# make install

> export PKG_CONFIG_PATH=/usr/local/leptonica-1.79.0/lib/pkgconfig
$ git clone https://github.com/tesseract-ocr/tesseract.git
$ cd tesseract
$ ./autogen.sh
$ ./configure --prefix=/usr/local/tesseract-5.0 
$ make
$ make install
$ ln -s /usr/local/tesseract-5.0/bin/tesseract /usr/local/bin/
$ tesseract  --version #  成功


复制语言数据 chi_sim.traineddata  eng.traineddata  到目录  /usr/local/tesseract-5.0/share/tessdata

step 2:  npm install tesseractocr string-algorithms fast-levenshtein


*/


let tesseract = require('tesseractocr')

let recognize = tesseract.withOptions({
    psm: 4,
    language: [ 'chi_sim', 'eng' ],
    config: ['tessedit_do_invert=0', 'oem=1']
})


        let buffer = Buffer.from(imgData, 'base64')

        //const text = await recognize('7001.jpg')
        let tesstext = await recognize(buffer)
```





# NFS



```
nfs 成功
	umount -f -l  /home/data/users/xxx/mnt     # 取消挂载

	https://qizhanming.com/blog/2018/08/08/how-to-install-nfs-on-centos-7

	vi /etc/exports      # .124
		/home/data/users/xxx/data_backup/    192.168.2.0/24(rw,sync,no_root_squash,no_all_squash)
	
	客户端
		yum -y install nfs-utils

		mkdir /yingedu/shared
		chmod 755 /xxx/shared

		showmount -e 192.168.1.xxx     # 显示 .124 的共享文件

		mount -t nfs 192.168.1.xxx:/home/data/users/xxx/data_backup  /yingedu/shared    # 挂载远程目录
```





# v2ray

- https://shadowzenhk.medium.com/%E5%A6%82%E4%BD%95%E6%AD%A3%E7%A1%AE%E4%BD%BF%E7%94%A8cloudflare-cdn%E9%AB%98%E9%80%9Fip%E5%8A%A0%E9%80%9Fv2ray%E8%AE%BF%E9%97%AE-f1abcc76369c



# 3ds

[u](https://www.bilibili.com/video/BV1L5411g7fs/?vd_source=1f4569489a622719e5c3b00101194ac3)

[oldmanemu](https://www.oldmanemu.net/)

[e](https://e-hentai.org/)

```
刚刚亲自测试了一下，在cirta android上玩的方法如下：
1、下载https://github.com/evandixon/DotNet3dsToolkit ，将dump出来的CXI文件extract
2、将luma补丁里的romfs文件夹下内容覆盖extract出来的RomFS文件夹，code.bin覆盖到ExeFS下
3、在DotNet3dsToolkit里rebuild成0-key encrypted 3ds文件
4、在cirta Android上安装3ds文件即为中文版

/storage/emulated/0/citra-emu/sdmc/ 默认位置应该是这里吧  sdmc就是储存卡的意思
没错的话 长按游戏可以设置

有些朋友反映直接安装cia会出现错误，但是用FBI远程安装cia就可以安装
有同样问题的可以试试


```





# djvu

```
DjVuToy的一个德国用户向我介绍过一个校对DjVu中隐藏文本的方法：对同一个DjVu文件，用MODI和ABBYY各OCR一遍，导出纯文本，然后用文本比较工具进行比较，能够较快地发现OCR的错误。按他的说法，至少对于德语来说，MODI和ABBYY各有千秋，所以他用这个方法屡试不爽。有兴趣的不妨也试试。
```



# Tampermonkey  + chrome script



## gpt4-mobile

[infiniteGPT4](https://github.com/linkedlist771/infiniteGPT4)



## ChatGPT-AutoChat

[注入JavaScript](https://m.tongfu.net/home/35/blog/513275.html)

[等待元素出现](https://github.com/jackfrued/Python-100-Days/blob/master/Day61-65/64.%E4%BD%BF%E7%94%A8Selenium%E6%8A%93%E5%8F%96%E7%BD%91%E9%A1%B5%E5%8A%A8%E6%80%81%E5%86%85%E5%AE%B9.md)

[js断点调试](https://juejin.cn/s/selenium%20js%E6%96%AD%E7%82%B9%E8%B0%83%E8%AF%95)

[Chrome ReRes js替换插件](https://bbs.kanxue.com/thread-272800.htm)

see echodict\pandora\chat_with_chatgpt.py

see .77 E:\usr\PandoraNext\pandoraNext_chatgpt_nlpp.mjs

```
xxx.77:7999/c/33f40974-eee5-4fa2-bfbf-09b468edd862
	# 从前端网页 js 代码找 post 参数
	# vscode 折叠所有 Ctrl + K，Ctrl + 0
	
window.webpackChunk_N_E
	# 能取到
 
Y.publicApiCompletionStream = function(Y, et, en) {
	# 可以断下来
	# 它应该是在这个变量里面 86646

Y.post = function(Y, et) {  统一在这里拦截？
	# 聊天接口不过这里


```



```

# https://github.com/dlxj/ChatGPT-AutoChat
# https://github.com/st1vms/gptauto  这个更详细
"""
pip install selenium
    # https://googlechromelabs.github.io/chrome-for-testing/#stable 到这里下载对应 chrome 版本的驱动
    # http://chromedriver.storage.googleapis.com/index.html （旧版在这）

    (Get-Command chromedriver).Source
      # powershell show file local

   .77 windows 位置:
      E:/usr/Python311/ 代码在这
      E 盘就是 linux 挂载的 512G disk, 在 /mnt 上

"""

import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
from selenium.webdriver.support import expected_conditions as EC
# from extract_examples import Extract_Examples

# ext = Extract_Examples()
# lst = [a for a in range(310,400)]
# x,sentences = ext.prompt_examples(2,lst)
prompt =  "hello"
# prompt = prompt+str(sentences)+" [OUTPUT: "
# print(prompt)

op = webdriver.ChromeOptions()
op.add_argument(f"user-agent={UserAgent.random}")
op.add_argument("user-data-dir=./")
op.add_experimental_option("detach", True)
op.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = uc.Chrome(chrome_options=op, driver_executable_path="D:/usr/Python311/chromedriver.exe")

MAIL = ""
PASSWORD = ""
 

driver.get('https://chat.openai.com/auth/login')

sleep(3)

inputElements = driver.find_elements(By.TAG_NAME, "button")
inputElements[0].click()

sleep(3)

mail = driver.find_elements(By.TAG_NAME,"input")[1]
mail.send_keys(MAIL)

btn=driver.find_elements(By.TAG_NAME,"button")[0]
btn.click()

password= driver.find_elements(By.TAG_NAME,"input")[2]
password.send_keys(PASSWORD)

sleep(3)

wait = WebDriverWait(driver, 10)
btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "_button-login-password")))
btn.click()
sleep(10)

inputElements = driver.find_elements(By.TAG_NAME, "textarea")

i = 0
# while i<10:
inputElements[0].send_keys(prompt)
sleep(2)
inputElements[0].send_keys(Keys.ENTER)
sleep(10)
inputElements = driver.find_elements(By.TAG_NAME, "p")
sleep(5)
results = []
for element in inputElements:
   results.append(element.text)
print(results)
i+=1
sleep(5)
```



## gptauto

[gptauto](https://github.com/st1vms/gptauto)

```
git clone https://github.com/st1vms/gptauto.git
 
pip install selenium undetected-chromedriver screeninfo

https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-win64.zip



 
```





## chatgpt delete answer

[[GPT-4] 后端程序员的第一个纯前端 chrome 插件](https://www.v2ex.com/t/935426) 

- [u](https://github.com/qcrao/bulk-delete-chatGPT)



## Always GPT-4



```
脚本可以自动模拟点击那个菜单，保证每次都是 GPT4 ，需要搭配 Tampermonkey 使用。

请新建一个脚本，把下面的代码贴进去启用即可。

// ==UserScript==
// @name Always GPT-4
// @namespace http://tampermonkey.net/
// @version 0.1
// @description try to take over the world!
// @author You
// @match https://chat.openai.com/*
// @icon data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant none
// ==/UserScript==

(function() {
'use strict';
function clickElementWhenAvailable() {
var element = document.querySelector('[class^="relative flex w-full cursor-default"]');
if (element) {
element.click();
observer.disconnect(); // Stop observing once the element is clicked
}
setTimeout(function() {
var ul = document.querySelector('ul');
var secondItem = ul.getElementsByTagName('li')[1];
secondItem.click();
}, 100);
}

var observer = new MutationObserver(clickElementWhenAvailable);

observer.observe(document.body, {
childList: true,
subtree: true,
});

clickElementWhenAvailable(); // Check if the element is available when the script runs
})();
```



## 捕获 ChatGPT 发送前的内容

[Tampermonkey 捕获 ChatGPT 发送前的内容](https://v2ex.com/t/970390#reply4)

```
网页端 ChatGPT 在发送消息时候，回车或者点击发送按钮后，对话框会被清空发送，如果遇到网络状况不佳，消息发送失败，则这条编辑的消息也消失了。

所以想使用 Tampermonkey 来捕获这个发送行为:

// ==UserScript==
// @name         ChatGPT 回车捕获
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://chat.openai.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=openai.com
// @run-at       document-idle
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    function run() {
        const inputElement = document.querySelector('#prompt-textarea');
        if (inputElement) {
            console.log("[ChatGPT 回车捕获]: Hacked!");
            inputElement.addEventListener('keydown', function(event) {
                if (event.keyCode === 13) {
                    console.log("[ChatGPT 回车捕获]: 即将发送的内容=> ", inputElement.value);
                }
            });
        } else {
            console.log("[ChatGPT 回车捕获]: No inputElement found!")
        }
    }
    setTimeout(() => {
        run();
    }, 3000);
    let oldPushState = history.pushState;
    history.pushState = function pushState() {
        let ret = oldPushState.apply(this, arguments);
        window.dispatchEvent(new Event('pushstate'));
        window.dispatchEvent(new Event('locationchange'));
        return ret;
    };
    let oldReplaceState = history.replaceState;
    history.replaceState = function replaceState() {
        let ret = oldReplaceState.apply(this, arguments);
        window.dispatchEvent(new Event('replacestate'));
        window.dispatchEvent(new Event('locationchange'));
        return ret;
    };
    window.addEventListener('popstate', () => {
        window.dispatchEvent(new Event('locationchange'));
    });
    window.addEventListener('locationchange', function () {
        setTimeout(() => {
            run();
        }, 3000);
    });
})();

上面代码虽然能完成这项工作:

监听 #prompt-textarea 这个输入框
当按下回车键时候将输入框内的消息输出到控制台
为了确保页面加载完成再捕获，延迟 3 秒执行
为了解决切换不同的对话导致输入框改变，监听路由改变并重新 hack
但这样的实现也有一些其他问题，比如页面在第 3 秒后才完全加载出来。并且只是监听了回车按键，发送按钮也是一样的逻辑（重复代码，没有写）。

所以这样做有点丑，大佬们有什么其他方法来优化一下？

比如 hack 一些内部方法:

let msg = null;
const OldTextDecoder = TextDecoder;
TextDecoder = class {
    constructor() {
        this.old = new OldTextDecoder(...arguments);
    }
    decode() {
        const res = this.old.decode(...arguments);
        try {
            msg = JSON.parse(res).message.content.parts[0];
        } catch (e) {
        }
        if (msg != null && res == "[DONE]") {
            if (window.ongpt) {
                window.ongpt(msg);
            }
            msg = null;
        }
        return res;
    }
};
但这只是 hack 了 TextDecoder ，输入框发送前的消息应该如何 hack ？


```



## video download

[写了一个无限制视频下载脚本](https://www.v2ex.com/t/856510)

[无差别视频提取工具](https://github.com/Momo707577045/media-source-extract)

- ```
  在给变量命名时使用 $ 符号通常表示该变量是一个引用到 DOM 元素的对象或者是一个用于操作 DOM 的函数。这种约定经常出现在像 jQuery 这样的库中，它使用 $ 作为选择器和操作函数的前缀。
  ```

[通过 Tampermonkey 快速查找 JavaScript 加密入口](https://cloud.tencent.com/developer/article/1563548)

```
很多视频网站的video标签的src指向了 Blob: http(s)://xxx.xxx.xxx/xxx,直接进这个链接的话会显示链接已禁用。 想法：既然能播放视频，就证明视频到最后一定是被 video 拿到了的.

谷歌一圈后发现了: 1.window.URL.createObjectURL(object)方法会返回该链接

A File, Blob, or MediaSource object to create an object URL for.（ https://developer.mozilla.org/en-US/docs/Web/API/URL/createObjectURL ）

2.window.URL.revokeObjectURL(objectURL),禁用上面返回的链接

A string representing a object URL that was previously created by calling createObjectURL().( https://developer.mozilla.org/en-US/docs/Web/API/URL/revokeObjectURL)

尝试：
1.hook 了window.URL.revokeObjectURL(objectURL)来忽略禁用请求，结果没用，依旧被禁用。

2.换个方法，直接 hook 二进制流，你缓存多少，我给你复制多少。查了下MediaSource, 他结合上面的createObjectURL(object)可以分片的方式加载视频，大概就是看多少，就加多少。 其中的音频和视频分别放在两个 sourceBuffer 中，直接 hook 住SourceBuffer.appendBuffer()就能实现视频流的截取了。再将每个分片以数组的方式保存下来，最后等视频缓存完后 new Blob(video/audio bufferArray)这样就实现了视频和音频的保存。

3.由于播放的时候，视频和音频分在两个 SourceBuffer 中，所以最后会得到两个文件。又是一番谷歌，有如下命令：

ffmpeg -i video.mp4 -i audio.mp4 -c:v copy -c:a aac -strict experimental output.mp4
可以将其合并为一个视频。

4.想过用 ffmpeg 的 wasm 库来在线合并，最后输出的，发现 ffmpeg-core 初始化时所需要的文件在国内下载不下来导致报错，从而导致适用的用户可能有点少，所以就没加，可能是我使用方法不对，以后有时间可以改改。

5.发现有些网站的视频是在iframe标签下的，并且加了sandbox属性，而有该属性的话就会导致最后的下载被拦截，于是，我使用了如下代码来将页面中的所有frame替换成无sandbox属性的：

 (function (that) {
          let removeSandboxInterval = setInterval(() => {
             if (that.document.querySelectorAll('iframe')[0] !== undefined) {
                that.document.querySelectorAll('iframe').forEach((v, i, a) => {
                   let ifr = v;
                   ifr.removeAttribute('sandbox');
                   const parentElem = that.document.querySelectorAll('iframe')[i].parentElement;
                   a[i].remove();
                   parentElem.appendChild(ifr);
                });
                clearInterval(removeSandboxInterval);
             }
          }, 1000);
       })(window);
于是有了如下油猴脚本：

英文名：Unlimited_downloader

https://greasyfork.org/en/scripts/445751-unlimited-downloader

Ps: 都是谷歌翻译成英文的，因为英文是个通用语言，所以不同地方的人看起来可能要方便点。

简短说明：
原理：直接 hook 媒体二进制流，换句话说就是你能看到，你就能下载，你能缓存多快，你就能下载多快。

使用方法：安装后，打开任意有视频或音频的网站，等视频缓存条加载完后会自动下载下来。

也可以自己手动开 16 倍速加速缓存，控制台输入：document.querySelector('video').playbackRate = x

最后，免责声明：请在合法范围内使用脚本，请勿用作任何非法用途，后果与作者无关。
第 1 条附言  ·  278 天前
感谢分享功能类似插件，大家可以自己挑个来用，互为补充：

@linglin0924 最近有一些不能下载的视频，我都是用这个插件，看他的运行方式，应该也是读流合并的 https://chrome.google.com/webstore/detail/video-downloader-cococut/gddbgllpilhpnjpkdbopahnpealaklle

@hbtech 很有意思，功能跟这个扩展也有点像： https://chrome.google.com/webstore/detail/stream-recorder-download/iogidnfllpdhagebkblkgbfijkbkjdmm


@tammy 我都是调用 you-get 下载的（Firefox 添加“鼠标中键点击下载按钮条用 you-get.exe 下载视频” 的功能 - Ryan 快快跑），对于支持的网站不用说，一流，默认最高画质，在配合你这个搞不支持的网站，那就更舒服了
```



## CF 流式输出

[cf-openai-with-sub-account-proxy](https://github.com/yinm0591/cf-openai-with-sub-account-proxy)



# 范畴论

[范畴论完全装逼手册](https://blog.oyanglul.us/grokking-monad/part1)

[Haskell中的范畴之函子和自然变换](https://zhuanlan.zhihu.com/p/25565309)

[函数式编程中的functor和monad](http://notes.jimliang.com/2019/%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BC%96%E7%A8%8B%E4%B8%AD%E7%9A%84functor%E5%92%8Cmonad/)

[FPC1：F#函数式编程与范畴论](https://zhuanlan.zhihu.com/p/50122691)  相当的直观

[DeepLX 免费翻译](https://github.com/OwO-Network/DeepLX)

```
const a = Promise.resolve(2)
	# Promise 可以看成是一个范畴，then 返回一个新的值
const b = a.then((i)=> i + 3)

函数式编程里面的运算，都是通过函子完成，它的运算不直接针对值，而是针对这个值的盒子。我们甚至可以通过多种运算，衍生出多种函子，通过这些函子来解决实际问题。


class Container {
  constructor(x) {
    this._value = x
  }
  map(f) {  // 态射接口，具体实现要你传一个变换函数
    return Container.of(f(this._value))
  }
  static of(x) { // 装箱
    return new Container(x)
  }
}

let v = Container.of(2).map(two => two + 2)
console.log(v[`_value`])

```



dependent type



态射（Morphism）是两个对象间的箭头，集合的箭头是函数，群论是群同态，拓朴是连续函数，泛代数是同态。

范畴里面有对象和态射

范畴的范畴（它里面的对象是范畴，它里面的箭头称为**函子**）

函子（Functor）是范畴间的态射，也叫为自然变换。

> 若我们将范畴看成是更高层的范畴的对象，则两个范畴之间的态射就是函子



范畴论是数学的一个分支，它抽象地研究数学结构和这些结构之间的关系。在范畴论中，最基本的概念是对象（Object）和态射（Morphism）。

- **对象（Object）**：范畴中的基本单位，可以理解为某种数学结构。例如，在集合范畴中，每个对象是一个集合。

- **态射（Morphism）**：连接两个对象的箭头，表示这两个对象之间的一种结构性关系或函数。态射可以理解为从一个对象到另一个对象的映射，它描述了这两个对象是如何相关的。

当我们说“态射是两个对象间的箭头”，我们是在说态射代表了一种从一个对象到另一个对象的转换或关系。这个“箭头”的概念是非常抽象的，它可以被实例化为不同数学领域中的具体关系。例如，在集合范畴中，一个对象是一个集合，态射就是集合之间的函数。

- **集合的箭头是函数**：这句话的意思是，在讨论集合作为对象的范畴（通常称为“集合范畴”）时，连接这些集合的态射（即“箭头”）具体而言就是函数。函数定义了一个集合中的元素如何映射到另一个集合中的元素。因此，当我们在集合范畴中谈论态射时，我们实际上是在讨论集合之间的函数。

总的来说，范畴论通过对象和态射的概念，提供了一个统一的框架来研究和表达不同数学结构之间的关系。在这个框架中，“态射是两个对象间的箭头，集合的箭头是函数”这句话揭示了范畴论如何将集合论中的函数概念抽象化为更广泛的数学结构间的关系。



## Python Monads 

[Expression](https://github.com/cognitedata/Expression)

[dejavu audio match](https://github.com/worldveil/dejavu)

- ```
  proxychains4 docker-compose build
  
  ```

- [cpp dejavu](https://github.com/salsowelim/dejavu_cpp_port)

[audiomatch 立等可用](https://github.com/unmade/audiomatch)

- ```
  pip3.10 install audiomatch
  ```

[pyacoustid 自带指纹相似度](https://github.com/beetbox/pyacoustid) [C# audio video](https://github.com/AddictedCS/soundfingerprinting)

- [How to install RPM fusion on AlmaLinux 8](https://linux.how2shout.com/how-to-install-rpm-fusion-on-almalinux-8-rocky-linux-8/)

```
# almalinx9
dnf install epel-release -y && \
dnf config-manager --set-enabled crb && \
dnf install --nogpgcheck https://mirrors.rpmfusion.org/free/el/rpmfusion-free-release-$(rpm -E %rhel).noarch.rpm -y && \
dnf install --nogpgcheck https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-$(rpm -E %rhel).noarch.rpm -y

dnf install ffmpeg ffmpeg-devel && \
rpm -qi ffmpeg

You will need a C++ compiler and CMake to build the library. FFmpeg is required to build the fpcalc tool.

git clone https://github.com/acoustid/chromaprint.git && \
cd chromaprint && \
cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_TOOLS=ON . && \
make && \
make install

pip3.10 install pyacoustid


```





```
from expression import pipe

v = 1
fn = lambda x: x + 1
gn = lambda x: x * 2

assert pipe(v, fn, gn) == gn(fn(v))
```

```
from expression import Some

v = Some(1)
fn = lambda x: x.map(lambda y: y + 1)
	# 范畴里有对象 value ，有态射的接口 map ，态射的具体实现需要你自已传一个函数
gn = lambda x: x.map(lambda y: y * 2)

assert v.pipe(fn, gn) == gn(fn(v))
```





## Nodejs Monads

[monads](https://github.com/sniptt-official/monads)

### Luckysheet 在线文档

[Luckysheet](https://github.com/dream-num/Luckysheet) [vercel.app](https://luckysheet.vercel.app/)



## Julia Monads

[Monads.jl](https://github.com/ulysses4ever/Monads.jl)

- ```
  using Pkg;Pkg.add("Monads")
  	# using Pkg;Pkg.update();Pkg.add("Monads");
  ```

  ```
  wget https://julialang-s3.julialang.org/bin/linux/x64/1.9/julia-1.9.1-linux-x86_64.tar.gz && \
  tar zxvf julia-1.9.1-linux-x86_64.tar.gz && \
  mv /root/julia-1.9.1 /usr/local && \
  ln -s /usr/local/julia-1.9.1/bin/julia /usr/local/bin/julia
  
  ```

  ```
  using Monads
  @mdo MList begin
           a <- MList(1:3)
           b <- MList(1:3)
           guard(a!=b)
           return (a,b)
         end
  ```

  

[如果写出高性能的Julia代码](https://zhuanlan.zhihu.com/p/66289979)

[用于双目重建中的GPU编程：julia-cuda](https://zhuanlan.zhihu.com/p/609702329)

```
function bench_match_smem(cfg, phaL, phaR, w, h, winSize, pha_dif)
    texarr2D = CuTextureArray(phaR)
    tex2D = CuTexture(texarr2D; interpolation = CUDA.LinearInterpolation())
    cp, minv, maxv = cfg.cpdiff, cfg.minv, cfg.maxv
    colstart, colend = cfg.colstart, cfg.colend
    rowstart, rowend = cfg.rowstart, cfg.rowend
    mindis, maxdis = cfg.mindis, cfg.maxdis
    col_ = cld((colend - colstart), 32) * 32
    row_ = cld(rowend - rowstart, 32) * 32 
    stride = Int(cld((maxv - minv + 1), 512))
    threadsPerBlock = round(Int32, cld((maxv - minv + 1) / stride, 32) * 32)
    blocksPerGrid = row_
    println("blocks = $blocksPerGrid threads = $threadsPerBlock left  $(col_) right $(maxv - minv) h=$(row_)")
    @cuda  blocks = blocksPerGrid threads = threadsPerBlock shmem =
        (threadsPerBlock * sizeof(Float32))  phaseMatch_smem!(cp, mindis, maxdis, minv, maxv, colstart, colend, rowstart, rowend, phaL, tex2D, threadsPerBlock,blocksPerGrid,stride, w, h, winSize, pha_dif)
    CUDA.synchronize()
    return
end
 
#进行立体相位匹配
function phaseMatch_smem!(cp, mindis, maxdis, minv, maxv, colstart, colend, rowstart, rowend, phaL, phaR, threadsPerBlock, blocksPerGrid, stride, w, h, winSize, pha_dif)
    #---------------------------------------------------
    # cp: diparity map
    # mindis, maxdis 最近最远视差
    #minv, maxv 仿射变换计算得到的R图中有效横向范围
    # colstart, colend, rowstart, rowend仿射变换计算得到的左图中有效横向、竖向范围
    #phaL, phaR 左右图像
    #w, h图像大小
    #winSize, pha_dif 3*3的框； 阈值：约等于20个像素的平均相位距离和
    # Set up shared memory cache for this current block.
    #--------------------------------------------------- 
    wh = fld(winSize, 2)
    cache = @cuDynamicSharedMem(Float32, threadsPerBlock)
    left_stride = 64 
    minv = max(1,minv)#必须是有效值，且是julia下的下标计数方式
    colstart= max(1,wh*stride)
    # 数据读入共享内存
    j = blockIdx().x + rowstart  # 共用的行序号
    i = threadIdx().x + colstart# 左图的列序号

    while(j <= min(rowend,h - wh)) 
        #数据拷贝到共享内存中去，并将由threadsPerBlock共享
        ri = (threadIdx().x - 1) * stride + minv
        tid = threadIdx().x
        while(tid <= threadsPerBlock && ri <= maxv)
            cache[tid] = phaR[j, ri] 
            tid+=threadsPerBlock
            ri+=threadsPerBlock
        end
        # synchronise threads
        sync_threads()
        maxv = min(fld(maxv - minv,stride) * stride + minv,maxv)
        # 计算最小匹配项 
        while(i <= min(colend,w - (wh*stride))) 
            min_v = 10000
            XR = -1
            VV = phaL[j, i]
            if(VV > 0.001f0)
                kStart = max(minv, i - maxdis) + 1
                kEnd = min(maxv, i - mindis) - 1
                for k = kStart:kEnd  #遍历一整行
                    RK = cache[cld(k - minv + 1,stride)]#从0开始计数
                    if RK <= 0.001f0
                        continue
                    end
                    dif = abs(VV - RK)
                    if dif < pha_dif
                        sum = 0.0f0
                        sn = 1 
                        for ki in 0:(winSize - 1) 
                            R_local = cache[cld(k - minv + 1 - wh + ki,stride)]
                            (R_local < 1e-5) && continue
                            #phaL[j + kj - wh, i + ki - wh*stride]
                            VR = VV - R_local
                            sum = sum + abs(VR)# * VR
                            sn += 1
                        end 
                        v = sum / sn
                        if v < min_v
                            min_v = v
                            XR = k
                        end
                    end
                end 
                #需要作插值
                #https://discourse.julialang.org/t/base-function-in-cuda-kernels/21866
                if XR > 0
                    XR_new = bisection(VV, phaR, Float32(j), Float32(XR - 3), Float32(XR + 3))
                    # 注意，这里直接做了视差处理了
                    state = (i - XR_new) > 0
                    @inbounds cp[j, i] = state ? (i - XR_new) : 0.0f0
                end
            end 
            i+=threadsPerBlock
        end
        j+=blocksPerGrid
    end
    sync_threads()
    return
end
```



## Go Monads

```
dnf install -y golang
```



[Go Monads](https://github.com/samber/mo)

[lo](https://github.com/samber/lo) Lodash-style Go library

[fake api](https://github.com/acheong08/ChatGPT-to-API/tree/master) chat gpt api BY Go

[Github_Hunter安全扫描](https://github.com/Hell0W0rld0/Github_Hunter_By_Golang)

[gocv ](https://github.com/hybridgroup/gocv) 支持 **go + opencv + cuda**

- [Stream for thread-safe concurrency](https://github.com/hybridgroup/gocv/pull/878)

  ```
  cimg, mimg, dimg := NewGpuMat(), NewGpuMat(), NewGpuMat()
  	defer cimg.Close()
  	defer mimg.Close()
  	defer dimg.Close()
  
  	stream := NewStream()
  	defer stream.Close()
  
  	canny := NewCannyEdgeDetector(50, 100)
  	defer canny.Close()
  
  	detector := NewHoughSegmentDetector(1, math.Pi/180, 150, 50)
  	defer detector.Close()
  
  	dest := gocv.NewMat()
  	defer dest.Close()
  
  	cimg.UploadWithStream(src, stream)
  	canny.DetectWithStream(cimg, &mimg, stream)
  	detector.DetectWithStream(mimg, &dimg, stream)
  	dimg.DownloadWithStream(&dest, stream)
  
  	stream.WaitForCompletion()
  ```

  

- ```
  // main.go
  package main
  
  import (
          "fmt"
          "gocv.io/x/gocv"
  )
  
  func main() {
          fmt.Printf("connecting...\n")
  
          webcam, err := gocv.OpenVideoCapture("rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4")
          if err != nil {
                  fmt.Printf("connect fail: %s\n", err)
          }
  
          fmt.Printf("connected successfully!\n")
  }
  ```

  

### go-chatgpt + tview UI 必看

[gpt反代](https://www.v2ex.com/t/947707)

- [纯js实现](https://github.com/PawanOsman/ChatGPT)

[go-chatgpt](https://github.com/linweiyuan/go-chatgpt) [fork 可用，原版已弃坑 必看](https://github.com/xqdoo00o/ChatGPT-to-API)

[tview](https://github.com/rivo/tview)



- [HAR文件池](https://github.com/xqdoo00o/ChatGPT-to-API/blob/master/README_ZH.md#har文件池) 必须

当前登录账号，使用GPT-4模型以及大部分GPT-3.5模型，均需要配置HAR文件（.har后缀名的文件）以完成captcha验证。

1. 使用基于chromium的浏览器（Chrome，Edge）打开浏览器开发者工具（F12），并切换到网络标签页，**勾选保留日志选项**。
2. 登录`https://chat.openai.com/`，新建聊天并选择GPT-4模型，随意输入下文字，切换到GPT-3.5模型，随意输入下文字。
3. 点击网络标签页下的导出HAR按钮，导出文件`chat.openai.com.har`，放置到本程序同级的`harPool`文件夹里。



- cookies.json 必须

  ```
  {
      "echoxxxgg@gmail.com": [
          {
              "Name": "__Secure-next-auth.session-token",
              "Value": "这里填 token",
              "Path": "/",
              "Domain": "",
              "Expires": "0001-01-01T00:00:00Z",
              "MaxAge": 0,
              "Secure": true,
              "HttpOnly": true,
              "SameSite": 2,
              "Unparsed": null
          }
      ]
  }
  ```

  



```
git clone https://github.com/xqdoo00o/ChatGPT-to-API && \
cd ChatGPT-to-API && \
go build && \
./freechatgpt

export SERVER_HOST="0.0.0.0"
	# 改监听地址

{"echodictcom@gmail.com":{"token":"xxx","puid":"user-xxx"}}
	# har + cookies.json 整好
	# 正常启动后会生成 access_tokens.json
	# 其它账号给 pandoraNext 用，因为它用 4 个账号工作量不饱和

curl 127.0.0.1:7070/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer NONEED" \
  -d '{
     "model": "gpt-4",
     "messages": [{"role": "user", "content": "你会说中文吗"}],
     "temperature": 0.7
   }'
	# 成功请求


https://chat.openai.com/backend-api/conversation
	# 官方网页版聊天接口
	# ChatGPT-to-API 不支持, ninja 和 pandoraNext 都支持
	# 但是，ChatGPT-to-API 可以拿到 ArkoseToken ? 这样，可以拿它调那两个的接口


main.go
import 加这一行
	arkose "github.com/xqdoo00o/funcaptcha"


main 函数加
	router.GET("/getArkoseToken", func(c *gin.Context) {
		_, puid := getSecret()
		ArkoseToken, err := arkose.GetOpenAIToken(4, puid, "")
		c.JSON(200, gin.H{
			"err":         err,
			"ArkoseToken": ArkoseToken,
		})
	})


curl --location 'http://xxx.77:7070/getArkoseToken?=null'
	# 自已加的接口，成功获取 ArkoseToken ，然后给 ninja 用，因为它没有次数限制



{"id":"chatcmpl-QXlha2FBbmROaXhpZUFyZUF3ZXNvbWUK","object":"chat.completion","created":0,"model":"gpt-3.5-turbo-0301","usage":{"prompt_tokens":0,"completion_tokens":0,"total_tokens":0},"choices":[{"index":0,"message":{"role":"assistant","content":"会的，我可以用中文回答问题。请随时告诉我您的问题或需求。"},"finish_reason":null}]}

curl 127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: text/event-stream" \
  -H "Connection: keep-alive" \
  -H "Authorization: Bearer NONEED" \
  -d '{
     "model": "gpt-4",
     "messages": [{"role": "user", "content": "你会说中文吗"}],
     "temperature": 0.7,
     "stream": true
   }'
   	# 流式输出好像不太行


```





```
// see D:/GitHub/echodict/README.md
curl --location 'http://127.0.0.1:8080/chatgpt/login' \
--header 'Authorization: Bearer NO_Need_API_KEY_HERE' \
--header 'Content-Type: application/json' \
--data '{
  "username": "",
  "password": ""
}'



```





## F\# Monads

[category-theory-for-dotnet-programmers](https://github.com/cboudereau/category-theory-for-dotnet-programmers)



### Winform

[ff-utils-improved 抽帧](https://github.com/miifanboy/ff-utils-improved) [1](https://blog.csdn.net/Daniel_yka/article/details/109840350)

[Flyleaf](https://github.com/SuRGeoNix/Flyleaf)

[FlyleafDemo](https://github.com/maoleigepu/FlyleafDemo)

[自适应高DPI](https://github.com/densen2014/WinformHighDPICompatibleProgram)

[仿QQ](https://github.com/yashuangyi/Simulation-QQ)

[lossless-cut  js视频剪切](https://github.com/mifi/lossless-cut)

[avidemux2  视频编辑](https://github.com/mean00/avidemux2 )

[downkyicore bili下载 avalonia](https://github.com/yaobiao131/downkyicore/releases)

[ScreenToGif](https://github.com/NickeManarin/ScreenToGif)



### UWP

[3D 穿梭效果](https://www.cnblogs.com/dino623/p/uwp_galaxy_shuttle.html)

[使用离散式关键帧播放动画 ](https://www.cnblogs.com/dino623/p/using_DiscreteDoubleKeyFrame_to_play_animation.html)



### WPF

[ffmediaelement 成品播放器 ?](https://github.com/unosquare/ffmediaelement)

[高仿QQ登录](https://github.com/944095635/DMSkin-QQSignIN)

[高仿LOL](https://github.com/jamesnet214/leagueoflegends)

- ```
  
  https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full-shared.7z
  	# 下载
  
  Unosquare.FFME.Windows.Sample
  	# 设为启动项, 改成 x64 编译
  
  
  ffmediaelement\Unosquare.FFME.Windows.Sample\App.xaml.cs
  	Library.FFmpegDirectory = @"D:/usr/ffmpeg-6.1.1-full_build-shared/bin";
  
  ffmediaelement\Unosquare.FFME\FFmpeg\FFLibrary.cs
  	# 改版本也解决不了
  
  
  https://github.com/unosquare/ffmediaelement/issues/642
  	# 修复方法
  	
  	
  I've updated it to 6.0.0.0
  	package: https://www.nuget.org/packages/zgabi.FFME.Windows
  	source: https://github.com/zgabi/ffmediaelement
  	compatible ffmpeg for example: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full-shared.7z
  	# 成功运行
  	
  
  ffmediaelement\Unosquare.FFME.Windows.Sample\Controls\PlaylistPanelControl.xaml
  <TextBox x:Name="OpenFileTextBox" Text="{Binding Playlist.OpenMediaSource}" Grid.Column="0" Background="Transparent" BorderThickness="0" 
                                   Foreground="#484848" FontSize="16" Padding="2"  FontWeight="Bold" Grid.ColumnSpan="2" />
  
  
  ffmediaelement\Unosquare.FFME.Windows.Sample\Controls\PlaylistPanelControl.xaml.cs
              OpenFileTextBox.KeyDown += async (s, e) =>
              {
                  if (e.Key != Key.Enter) return;
                  await App.ViewModel.Commands.OpenCommand.ExecuteAsync(OpenFileTextBox.Text);
                  e.Handled = true;
              };
  	# 回车就播放
  
  
  
              // Bind the Enter key to the command
              OpenFileTextBox.KeyDown += async (s, e) =>
              {
                  if (e.Key != Key.Enter) return;
  
                  // await App.ViewModel.Commands.OpenCommand.ExecuteAsync(OpenFileTextBox.Text);
                  var m = App.ViewModel.MediaElement;
                  var target = new Uri(@"E:\videos\netflix\anime\japanese\Touch\Episode 1\Touch_S01E01_Episode 1.mp4");
                  await m.Open(target);
  
                  // await App.ViewModel.Commands.OpenCommand.ExecuteAsync(OpenFileTextBox.Text);
                  e.Handled = true;
              };
              
              # 成功播放
  
  
          public string WindowTitle
          {
              get => m_WindowTitle;
              private set => SetProperty(ref m_WindowTitle, value);
          }
          	# 属性的赋值 
  
  在 app 上定义根视图模型
  ffmediaelement\Unosquare.FFME.Windows.Sample\App.xaml
  xmlns:vm="clr-namespace:Unosquare.FFME.Windows.Sample.ViewModels">
              <ResourceDictionary.MergedDictionaries>
                  <ResourceDictionary>
                      <vm:RootViewModel x:Key="ViewModel" />
                  </ResourceDictionary>
  			
  ffmediaelement\Unosquare.FFME.Windows.Sample\App.xaml.cs
  public static RootViewModel ViewModel => Current.Resources[nameof(ViewModel)] as RootViewModel;
  	# 定义它的静态引用
  
  
  
  ```

[WPFDevelopers 各种控件](https://github.com/WPFDevelopersOrg/WPFDevelopers)

[VPet 虚拟桌宠 必看](https://github.com/LorisYounger/VPet)

[WPF 实现裁剪图像](https://v2ex.com/t/950084#)

[WPF UI](https://github.com/lepoco/wpfui)

[HandyControl](https://github.com/HandyOrg/HandyControl)

[Flyleaf wpf player 必看](https://github.com/SuRGeoNix/Flyleaf)

[netch 代理 18.0版不内退](https://github.com/netchx/netch)



```
`[STAThread]` 是 .NET 中的一个属性，它被设计用来表示.NET程序的主线程应该使用单线程单元 (STA) 模型。在 Windows Presentation Foundation (WPF) 应用程序中，通常会在 `Main()` 方法上看到这个属性。

STA模型是 COM（组件对象模型）线程模型的一种。在这种模型中，每个线程看似独立运行，但实际上是由统一的消息队列管理和协调的。这意味着在任何给定时间，只有一个线程访问该线程的内存。

在 WPF 中，某些对象，例如 `Clipboard` 和 `Drag-and-Drop` 只能在 STA 中使用。如果没有 `[STAThread]` 属性，你可能会遇到异常。

以下是如何在代码中使用 `[STAThread]` 属性的示例：

​```csharp
[STAThread]
static void Main()
{
    Application.EnableVisualStyles();
    Application.SetCompatibleTextRenderingDefault(false);
    Application.Run(new Form1());
}
​```
```



```
xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" 定义了默认的名称空间，表示所有不带前缀的元素都属于这个名称空间。这包括了所有的 UI 元素，如 <Window>、<Button> 等等。
xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" 定义了名为 x 的名称空间，主要是包含一些非 UI 类型的功能（像 x:Class、x:Name 等）。
```







### winUI3

**search videoStreamPlayer in outline**

[Bili.Copilot 必看](https://github.com/Richasy/Bili.Copilot) [1](https://zhuanlan.zhihu.com/p/602954895) [2](https://github.com/SuRGeoNix/Flyleaf) [3](https://www.cnblogs.com/chifan/p/16516018.html) [appList](https://github.com/DesignLipsx/WinUI-3-Apps-List) [book](https://github.com/PacktPublishing/Learn-WinUI-3-Second-Edition)

- ```
  vs2022 install  
  	.net 5.0 6.0 7.0 8.0
  	Windows 10 SDK (10.0.19041.0)
  	.NET Multi-platform App UI开发  
  	.NET桌面开发
  	使用C++的桌面开发
  	通用Windows平台开发
  
  ```

  

[biliuwp-lite 上面不活跃了](https://github.com/ywmoyue/biliuwp-lite) 

- ```
  vscode 搜 17763 改成
  10.0.19041.0
  把之前的证书全删掉
  双击 Package.appxmanifest -> 打包 ->创建证书
  
  BiliLite.Packages 设为启动项可以成功运行
  
  ```




[CleanReader.Desktop 阅读器](https://github.com/Clean-Reader/CleanReader.Desktop)



[bili api 大本营](https://github.com/SocialSisterYi/bilibili-API-collect/issues/665)

[Rise-Media-Player](https://github.com/Rise-Software/Rise-Media-Player)

[Screenbox](https://github.com/huynhsontung/Screenbox)  ui good, down to win10

- ```
  C:\Users\Administrator\.nuget\packages
  	# 出错先删除
  
  换 x64 编译成功
  
  ```

- [webrtc-stream](https://github.com/mpromonet/webrtc-streamer)

[Luo-Painter-UWP](https://github.com/ysdy44/Luo-Painter-UWP)  painting



```
vs2022 -> 扩展 -> 管理扩展 -> 搜 utf8 -> 装 utf8 no bom 插件 -> 重启 vs
	# 这样以后源文件都以 utf8 保存

1.ctrl + k +f：非强制的，自己写的代码中自己调整的空格不能格式化. 2.ctrl + K +d：强制的

先添加包源
https://pkgs.dev.azure.com/dotnet/CommunityToolkit/_packaging/CommunityToolkit-Labs/nuget/v3/index.json

namespace App;
	# .net 7.0 可以这样写

装 WinUIEx 2.3.1
   Microsoft.WindowsAppSDK 1.4.231008000
   Microsoft.Windows.SDK.BuildTools 10.0.22621.756
   Microsoft.AppCenter.Analytics 5.0.3
   Microsoft.AppCenter.Crashes 5.0.3
   Vortice.WinUI 3.3.3-beta

	<PackageReference Include="CommunityToolkit.Labs.WinUI.SegmentedControl" Version="0.1.230830" />
	<PackageReference Include="CommunityToolkit.Labs.WinUI.SettingsControls" Version="0.0.18" />
	<PackageReference Include="CommunityToolkit.Labs.WinUI.Shimmer" Version="0.1.230830" />
	<PackageReference Include="CommunityToolkit.WinUI.UI.Animations" Version="7.1.2" />
	<PackageReference Include="CommunityToolkit.WinUI.UI.Controls.Primitives" Version="7.1.2" />
	
	# 这几个包搜不到，要手动贴
	

加入 iBL\App\Forms\WindowBase.cs
using Microsoft.UI;
using WinUIEx;
namespace App.Forms;
public class WindowBase : WindowEx
{
    public WindowBase()
    {
        AppWindow.TitleBar.ExtendsContentIntoTitleBar = true;
        AppWindow.TitleBar.ButtonBackgroundColor = Colors.Transparent;
        AppWindow.TitleBar.ButtonInactiveBackgroundColor = Colors.Transparent;
        AppWindow.TitleBar.IconShowOptions = Microsoft.UI.Windowing.IconShowOptions.HideIconAndSystemMenu;
        SystemBackdrop = new Microsoft.UI.Xaml.Media.MicaBackdrop();
        Title = "iBL";
    }
}

iBL\App\Forms\MainWindow.xaml.cs
namespace App.Forms;
public sealed partial class MainWindow : WindowBase
    public MainWindow()
        InitializeComponent();

iBL\App\Forms\MainWindow.xaml
<local:WindowBase
    x:Class="App.Forms.MainWindow"
    xmlns:local="using:App.Forms"
    
    <Grid x:Name="RootGrid">
        <Frame
            x:Name="MainFrame"
            Grid.Row="1"
            Grid.Column="1"
            Padding="0,12,0,0"
            Background="{ThemeResource LayerFillColorDefaultBrush}"
            BorderBrush="{ThemeResource NavigationViewContentGridBorderBrush}"
            BorderThickness="0,0,0,1" />
    </Grid>
</local:WindowBase>

iBL\App\App.xaml.cs
private WindowBase _window;
protected override void OnLaunched(Microsoft.UI.Xaml.LaunchActivatedEventArgs args)
	_window = new MainWindow();
    _window.Activate();


安装 Microsoft.Windows.CsWin32 0.3.49-beta  # Nuget 里选包含预览版
新建 NativeMethods.txt 和 App.xaml.cs 放在同一目录，内容如下
GetDpiForWindow
SetForegroundWindow
SetWindowsHookEx
UnhookWindowsHookEx
CallNextHookEx
GetModuleHandle

var scaleFactor = Windows.Win32.PInvoke.GetDpiForWindow(new Windows.Win32.Foundation.HWND(windowHandle)) / 96d;
	# 然后这个就可以用了
	

iBL\App\App.xaml.cs
        protected override void OnLaunched(Microsoft.UI.Xaml.LaunchActivatedEventArgs args)
        {
            _window = new MainWindow();
            _window.Activate();
            MoveAndResize();
        }

        private static RectInt32 GetRenderRect(DisplayArea displayArea, IntPtr windowHandle)
        {
            var workArea = displayArea.WorkArea;
            var scaleFactor = Windows.Win32.PInvoke.GetDpiForWindow(new Windows.Win32.Foundation.HWND(windowHandle)) / 96d;
            var previousWidth = 500d; // SettingsToolkit.ReadLocalSetting(SettingNames.WindowWidth, 500d);
            var previousHeight = 800d; // SettingsToolkit.ReadLocalSetting(SettingNames.WindowHeight, 800d);
            var width = Convert.ToInt32(previousWidth * scaleFactor);
            var height = Convert.ToInt32(previousHeight * scaleFactor);

            // Ensure the window is not larger than the work area.
            if (height > workArea.Height - 20)
            {
                height = workArea.Height - 20;
            }

            var lastPoint = new PointInt32(0, 0);  // GetSavedWindowPosition();
            var isZeroPoint = lastPoint.X == 0 && lastPoint.Y == 0;
            var isValidPosition = lastPoint.X >= workArea.X && lastPoint.Y >= workArea.Y;
            var left = isZeroPoint || !isValidPosition
                ? (workArea.Width - width) / 2d
                : lastPoint.X - workArea.X;
            var top = isZeroPoint || !isValidPosition
                ? (workArea.Height - height) / 2d
                : lastPoint.Y - workArea.Y;
            return new RectInt32(Convert.ToInt32(left), Convert.ToInt32(top), width, height);
        }

        private void MoveAndResize()
        {
            var hwnd = WindowNative.GetWindowHandle(_window);
            var windowId = Win32Interop.GetWindowIdFromWindow(hwnd);
            var lastPoint = new PointInt32(0, 0); // GetSavedWindowPosition();
            var displayArea = lastPoint.X == 0 && lastPoint.Y == 0
                ? DisplayArea.GetFromWindowId(windowId, DisplayAreaFallback.Nearest)
                : DisplayArea.GetFromPoint(lastPoint, DisplayAreaFallback.Nearest);
            if (displayArea != null)
            {
                var rect = GetRenderRect(displayArea, hwnd);
                var scaleFactor = Windows.Win32.PInvoke.GetDpiForWindow(new Windows.Win32.Foundation.HWND(hwnd)) / 96d;
                _window.MinWidth = 500;
                _window.MinHeight = 400;

                var maxHeight = (displayArea.WorkArea.Height / scaleFactor) + 16;
                _window.MaxHeight = maxHeight < 400 ? 400 : maxHeight;
                _window.AppWindow.MoveAndResize(rect);
            }
        }

	# 这样就可以调整窗口大小了



Bili.Copilot\src\App\App.xaml.cs
LaunchWindow(IActivatedEventArgs args = default)
        _window = new MainWindow(args);
        _window.Closed += OnMainWindowClosedAsync;
	# 接管关闭事件

private void OnMainWindowClosedAsync(object sender, WindowEventArgs args)
            _window?.Close();
            Environment.Exit(0);
            	# 直接退出
            
            args.Handled = true; // 关闭事件已处理, 不要再往下传了
            _window.Hide();
            	# 隐藏窗口


public class WindowBase : WindowEx
	this.SetIcon("Assets/logo.ico");
	# 设置任务栏上显示的图标 
	

安装包 H.NotifyIcon.WinUI  2.0.118
	# 托盘图标
	

iBL\App\Styles\TrayResources.xaml
<ResourceDictionary
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:tb="using:H.NotifyIcon">
    <tb:TaskbarIcon
        x:Key="TrayIcon"
        ContextMenuMode="PopupMenu"
        IconSource="\Assets\logo.ico"
        NoLeftClickDelay="True"
        ToolTipText="what's this"
        Visibility="Visible">
    </tb:TaskbarIcon>
</ResourceDictionary>


iBL\App\App.xaml
    <Application.Resources>
        <ResourceDictionary>
            <ResourceDictionary.MergedDictionaries>
                <ResourceDictionary Source="ms-appx:///Styles/TrayResources.xaml" />
            </ResourceDictionary.MergedDictionaries>
        </ResourceDictionary>
    </Application.Resources>


iBL\App\App.xaml.cs
private TaskbarIcon TrayIcon { get; set; }
protected override void OnLaunched(Microsoft.UI.Xaml.LaunchActivatedEventArgs args)
	        TrayIcon = (TaskbarIcon)Resources["TrayIcon"];
            TrayIcon.ForceCreate();
	# 成功显示托盘图标



处理托盘的右键退出
iBL\App\Styles\TrayResources.xaml
    xmlns:tb="using:H.NotifyIcon">
    <XamlUICommand x:Key="QuitCommand" Label="exit" />
    <tb:TaskbarIcon
        x:Key="TrayIcon"
        ContextMenuMode="PopupMenu"
        IconSource="\Assets\logo.ico"
        NoLeftClickDelay="True"
        ToolTipText="what's this"
        Visibility="Visible">

        <tb:TaskbarIcon.ContextFlyout>
            <MenuFlyout>
                <MenuFlyoutItem Command="{StaticResource QuitCommand}" />
            </MenuFlyout>
        </tb:TaskbarIcon.ContextFlyout>
    </tb:TaskbarIcon>


iBL\App\App.xaml.cs
        private void OnQuitCommandExecuteRequested(XamlUICommand sender, ExecuteRequestedEventArgs args)
        {
            _window?.Close();
            Environment.Exit(0);
        }

        protected override void OnLaunched(Microsoft.UI.Xaml.LaunchActivatedEventArgs 
            var exitApplicationCommand = (XamlUICommand)Resources["QuitCommand"];
            exitApplicationCommand.ExecuteRequested += OnQuitCommandExecuteRequested;
				# 成功右键退出
	


处理托盘的左键恢复窗口
iBL\App\Styles\TrayResources.xaml
    <XamlUICommand x:Key="ShowHideWindowCommand">
        <XamlUICommand.IconSource>
            <SymbolIconSource Symbol="OpenPane" />
        </XamlUICommand.IconSource>
        <XamlUICommand.KeyboardAccelerators>
            <KeyboardAccelerator Key="S" Modifiers="Control" />
        </XamlUICommand.KeyboardAccelerators>
    </XamlUICommand>
    <tb:TaskbarIcon
        x:Key="TrayIcon"
        ContextMenuMode="PopupMenu"
        IconSource="\Assets\logo.ico"
        LeftClickCommand="{StaticResource ShowHideWindowCommand}"
        NoLeftClickDelay="True"
	
iBL\App\App.xaml.cs
        private void OnShowHideWindowCommandExecuteRequested(XamlUICommand sender, ExecuteRequestedEventArgs args)
        {
            _window.Activate();
            Windows.Win32.PInvoke.SetForegroundWindow(new Windows.Win32.Foundation.HWND(WindowNative.GetWindowHandle(_window)));
        }

OnLaunched(Microsoft.UI.Xaml.LaunchActivatedEventArgs args)
            var showHideWindowCommand = (XamlUICommand)Resources["ShowHideWindowCommand"];
            showHideWindowCommand.ExecuteRequested += OnShowHideWindowCommandExecuteRequested;
	# 成功左键恢复窗口


登录页的 QR 码
Bili.Copilot\src\App\Pages\SignInPage.xaml
                <Grid Width="240" CornerRadius="{StaticResource ControlCornerRadius}">
                    <Image
                        x:Name="QRCodeImage"
                        HorizontalAlignment="Stretch"
                        VerticalAlignment="Stretch"
                        Stretch="Uniform" />
                </Grid>


安装包 QRCoder 1.4.3
安装包 Google.Protobuf 3.24.4
	  Grpc.Net.Client 2.57.0
	  Grpc.Tools      2.58.0


Debug -> Any CPU
	# 生成解决方案 -> 部署解决方案
	# 成功运行

Bili.Copilot\src\ViewModels\Components\FFmpegPlayerViewModel\FFmpegPlayerViewModel.cs
	# 看这里
see Bili.Copilot\src\ViewModels\IPlayerViewModel.cs


webrtc-stream 组件，https://github.com/mpromonet/webrtc-streamer 直接 RTSP 拉流,这个是直接 RTP 流到 webrtc 转换的，所以低延迟，消耗最少；如果你借助 ffmpeg 将 rtsp 转到 flv 或者 hls 流畅度上来说 HLS 要好点，但是 flv 会出现限制，也就是缓冲加载，所以建议 webrtc ；不想用 webrtc-stream ，那就剩下的 GB28181 推流到 ZLM 或者 SRS ，然后 webrtc 再从服务端拉流，目的还是低延迟但是中间还是 监控将流通过 RTP 的方式推流到 ZLM 或者 SRS 了，你提到的 GB+wvp 就是这个原理，通过 GB 协商 监控推流到 RTP 服务器，而 RTP 服务器就是 ZLM ； zlm 和 SRS 内部再将原始流转成 WebRTC 、RTMP 、RTSP 、HLS 、Flv 等格式
```



#### 全局常量

```
Bili.Copilot\src\Models\Models.App\Constants\AppConstants.cs
namespace Bili.Copilot.Models.App.Constants;
public static class AppConstants
{
#pragma warning disable SA1600
    public const string ThemeDefault = "System";
    
Bili.Copilot\src\Models\Models.App\GlobalUsing.cs
global using System.Text.Json.Serialization;
global using Bili.Copilot.Models.Constants.App;
	# 全局引用，再也不用写 using xxx

Bili.Copilot\src\App\Resources\zh-Hans\Resources.resw
  <data name="AppName" xml:space="preserve">
    <value>哔哩助理</value>
  </data>
	# 字符常量
	
Bili.Copilot\src\Models\Models.Constants\Models.Constants.csproj
    <ItemGroup>
        <AdditionalFiles Include="$(SolutionDir)\src\App\Resources\zh-Hans\Resources.resw" />
    </ItemGroup>
    	# 引入资源文件

Bili.Copilot\src\App\Package.appxmanifest
	# 默认语言填 zh-CN

Bili.Copilot\src\Libs\Libs.ResourceGenerator\ResourceGenerator.cs
	context.AddSource("StringNames.g.cs", SourceText.From(sb.ToString(), Encoding.UTF8));
	# 编译期间获取资源文件并生成对应的枚举类型 StringNames
	# 它是 .net 2.0 的独立 project ，奇奇怪怪
	    StyleCop.Analyzers  Version="1.1.118"
	    Microsoft.CodeAnalysis.CSharp.CodeStyle
	    Version="4.4.0"
	    	# Nuget 包
	
	
Bili.Copilot\src\App\Extensions\LocaleExtension.cs
namespace Bili.Copilot.App.Extensions;
[MarkupExtensionReturnType(ReturnType = typeof(string))]
public sealed class LocaleExtension : MarkupExtension
{
    public StringNames Name { get; set; }
    protected override object ProvideValue()
        => ResourceToolkit.GetLocalizedString(Name);
}
	# 多语言扩展

Bili.Copilot\src\App\Forms\MainWindow.xaml
	xmlns:ext="using:Bili.Copilot.App.Extensions"
        <controls:AppTitleBar
            x:Name="CustomTitleBar"
            Title="{ext:Locale Name=AppName}"
        	# 引用常量

```



#### 导航

```
Bili.Copilot\src\ViewModels\Components\AppViewModel\AppViewModel.cs
Navigate(PageType.SignIn);
	# 跳登录页

Bili.Copilot\src\App\Forms\MainWindow.xaml.cs
MainFrame.Navigate(pageType, e.Parameter);
	# 实际干活的是这个



MainFrame 变量是在 xaml 定义，然后自动生成的
        <Frame
            x:Name="MainFrame"
            Grid.Row="1"
            Grid.Column="1"
            Padding="0,12,0,0"
            Background="{ThemeResource LayerFillColorDefaultBrush}"
            BorderBrush="{ThemeResource NavigationViewContentGridBorderBrush}"
            BorderThickness="0,0,0,1" />
        [global::System.CodeDom.Compiler.GeneratedCodeAttribute("Microsoft.UI.Xaml.Markup.Compiler", " 3.0.0.2310")]
private global::Microsoft.UI.Xaml.Controls.Frame MainFrame;
MainFrame = global::WinRT.CastExtensions.As<global::Microsoft.UI.Xaml.Controls.Frame>(obj);
	# 把 page 存在 MainFrame ?

```





Visual Studio 2022





## Rust Monads

[Rust语言圣经](https://course.rs/about-book.html)

[candle 对标 jax ?](https://github.com/huggingface/candle)

[Rust解leecode技术小总结](http://notes.jimliang.com/2020/Rust%E8%A7%A3leecode%E6%8A%80%E6%9C%AF%E5%B0%8F%E6%80%BB%E7%BB%93/)

[Rust bindings for Godot 4](https://github.com/godot-rust/gdext)

[iced GUI对标elm](https://github.com/iced-rs/iced)

[Rust bindings for the Python interpreter](https://github.com/PyO3/pyo3)

[rust-script](https://github.com/fornwall/rust-script)



### ninja pandora开源替代 必看

[ninja](https://github.com/gngpp/ninja)

- [api 文档](https://github.com/gngpp/ninja/blob/main/doc/rest.http)

  ```
  f12 ->网络标签 ->下面一行点"保留日志" ->登录 -> 选中这个接口
  https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147
  
  -> 点上面的 "导出HAR" 按钮 -> 得到 chat.openai.com.har
  
  .77
  ./ninja.exe run --arkose-gpt4-har-dir C:/Users/Administrator/Desktop/ChatGPT-to-API/harPool --bind 0.0.0.0:80
  
  ./ninja.exe run --arkose-gpt4-har-dir E:/huggingface/ChatGPT-to-API/harPool --bind 0.0.0.0:80
  
  
  
  使用这个参数启动 ninja
  ninja run --arkose-chat4-har-file 
  /mnt/huggingface/ninja/HAR/chat.openai.com.har
  	# vscode 单步调试 main.rs 见后面的 vscode launch.json
  
  http://xxx.77:7999/har/upload
  	# 上传 HAR 接口
  
  xxx.xxx.xxx.77:7999
  	# 直接打开前端使用
  	
  http://chat.openai.com/api/auth/session
      # 这里拿 access_token	
  
  
  see postman -> rust_ninja_chatgpt 
  curl --location --request POST 'http://209.141.34.77:7999/backend-api/conversation' \
  --header 'Content-Type: application/json' \
  --header 'Accept: text/event-stream' \
  --header 'Authorization: Bearer 这里填access_token' \
  --data-raw '{
    "action": "next",
    "messages": [
      {
        "id": "02cb22be-4839-455a-9a39-f23968219cef",
        "author": {
          "role": "user"
        },
        "content": {
          "content_type": "text",
          "parts": [
            "new conversation"
          ]
        },
        "metadata": {}
      }
    ],
    "model": "gpt-4",
    "parent_message_id": "02cb22be-4839-455a-9a39-f23968219cef",
    "timezone_offset_min": -480,
    "history_and_training_disabled": false
  }'
  
  	# 流式请求有回应，但是有问题。请研究它自带的网页版，它是能正常回答的，还需要构造额外的参数
  
  vi /etc/nginx/conf.d/gp4_browser_8080.conf
  	# 做了 nginx 反代，8880 -> 7999
  	
  http://echoxxxx.com:8880
  	# 套了 cf ，免魔法访问 
  	
  
  huggingface\ninja\openai\src\serve\mod.rs
  	# 入口点可能在这里 
  	
  
  换 IP 。把不能用的 token 放到 https://chat1.zhile.io/ 试试，看看能否正常使用。
  高危 IP+高危帐号 =》禁止
  高危 IP+低危帐号 =》允许
  低危 IP+高危帐号 =》允许	
  	
  	
  	
  
  
  ```
  
  

```
vscode 安装：rust-analyzer + CodeLLDB

curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
	# 安装 rust 环境
cargo --version

cd /mnt/huggingface

git clone https://huggingface.co/datasets/dlxjj/ninja
	# pandora 的开源替代品

http://127.0.0.1:7999/backend-api/
	# 后端接口地址，后接 openai 的标准接口地址


chat.openai.com 正常聊天后 -> F12 
https://tcr9i.chat.openai.com/fc/gt2/public_key/35536E1E-65B4-4D96-9D97-6ADB7EFF8147
右键这个接口，选保存 HAR

cp chat.openai.com.har /root/.chat4.openai.com.har


# GPT4 接口
  curl 127.0.0.1:7999/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer " \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "你会说中文吗"}]
  }'

examples/chatgpt.rs

```



```
vscode launch.json
ninja/src/main.rs 成功单步调式
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug executable 'ninja'",
            "cargo": {
                "args": [
                    "build",
                    "--bin=ninja",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "ninja",
                    "kind": "bin"
                }
            },
            "args": [
                "run",
                "--arkose-chat4-har-file",
                "/mnt/huggingface/ninja/HAR/chat.openai.com.har"
            ],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in executable 'ninja'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--bin=ninja",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "ninja",
                    "kind": "bin"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug example 'chatgpt'",
            "cargo": {
                "args": [
                    "build",
                    "--example=chatgpt",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "chatgpt",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in example 'chatgpt'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--example=chatgpt",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "chatgpt",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug example 'auth'",
            "cargo": {
                "args": [
                    "build",
                    "--example=auth",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "auth",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in example 'auth'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--example=auth",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "auth",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug example 'crypto'",
            "cargo": {
                "args": [
                    "build",
                    "--example=crypto",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "crypto",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in example 'crypto'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--example=crypto",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "crypto",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug example 'funcaptcha'",
            "cargo": {
                "args": [
                    "build",
                    "--example=funcaptcha",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "funcaptcha",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in example 'funcaptcha'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--example=funcaptcha",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "funcaptcha",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug example 'har'",
            "cargo": {
                "args": [
                    "build",
                    "--example=har",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "har",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in example 'har'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--example=har",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "har",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug example 'pow'",
            "cargo": {
                "args": [
                    "build",
                    "--example=pow",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "pow",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in example 'pow'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--example=pow",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "pow",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug example 'print_image'",
            "cargo": {
                "args": [
                    "build",
                    "--example=print_image",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "print_image",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in example 'print_image'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--example=print_image",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "print_image",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug example 'upgrade'",
            "cargo": {
                "args": [
                    "build",
                    "--example=upgrade",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "upgrade",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        },
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug unit tests in example 'upgrade'",
            "cargo": {
                "args": [
                    "test",
                    "--no-run",
                    "--example=upgrade",
                    "--package=ninja"
                ],
                "filter": {
                    "name": "upgrade",
                    "kind": "example"
                }
            },
            "args": [],
            "cwd": "${workspaceFolder}"
        }
    ]
}
```

har跟账号没有任何关系，只是一个浏览器的特征



#### for windows

[Windows下Clang的简单使用](https://zhuanlan.zhihu.com/p/380290758)

[如何优雅的在 Windows 上使用 LLVM Pass 插件进行代码混淆](https://bbs.kanxue.com/thread-272346.htm) clang.dll

[Building-Zig-on-Windows](https://github.com/ziglang/zig/wiki/Building-Zig-on-Windows)  它有 clang.dll ?

```
https://github.com/llvm/llvm-project/releases
	# LLVM-17.0.4-win64.exe
	# 它没有 clang.dll

visual studio installer -> 修改 -> 单个组件 -> 搜索 clang 
	-> 两个都装上
	
C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\Llvm\x64\bin\libclang.dll
	# 在这里，装完以后 ninja 在 win10 正常跑起来了



```





## C Monads

[C Monads](https://gist.github.com/lukechampine/c460fb2754ef0a7f7652874d9f9ed678)

```c
#include <stdio.h>
#include <stdbool.h>

// Maybe

typedef struct MaybeInt {
    int  just;
    bool nothing;
} MaybeInt;

const MaybeInt Nothing = (MaybeInt) { .nothing = true };

MaybeInt returnMaybe(int x) { return (MaybeInt) { .just = x, .nothing = false }; }

MaybeInt bindMaybe(MaybeInt (*fn)(int), MaybeInt m) {
    return m.nothing ? Nothing : fn(m.just);
}

void printMaybe(MaybeInt m) {
    if (m.nothing) printf("Nothing\n");
    else           printf("%d\n", m.just);
}

MaybeInt maybeFoo(int x) { return (x < 1)  ? Nothing : returnMaybe(x - 3); }
MaybeInt maybeBar(int x) { return (x > 0)  ? Nothing : returnMaybe(x + 3); }
MaybeInt maybeBaz(int x) { return (x != 2) ? Nothing : returnMaybe(x); }


// Either

typedef struct EitherInt {
    int   i;
    char* error;
} EitherInt;

EitherInt returnInt(int i)     { return (EitherInt) { .i = i, .error = NULL }; }
EitherInt returnError(char* e) { return (EitherInt) { .i = 0, .error = e };    }

EitherInt bindEither(EitherInt (*fn)(int), EitherInt m) {
    return (m.error != NULL) ? m : fn(m.i);
}

void printEither(EitherInt m) {
    if (m.error != NULL) printf("%s\n", m.error);
    else                 printf("%d\n", m.i);
}

EitherInt eitherFoo(int x) { return (x < 2)  ? returnError("too small")    : returnInt(x - 3); }
EitherInt eitherBar(int x) { return (x > 0)  ? returnError("not negative") : returnInt(x + 3); }
EitherInt eitherBaz(int x) { return (x != 2) ? returnError("must be 2")    : returnInt(x);     }

int main() {
    MaybeInt m = bindMaybe(maybeBaz, bindMaybe(maybeBar, maybeFoo(7)));
    printMaybe(m); // "Nothing"

    m = bindMaybe(maybeBaz, bindMaybe(maybeBar, maybeFoo(2)));
    printMaybe(m); // "2"


    EitherInt e = bindEither(eitherBaz, bindEither(eitherBar, eitherFoo(7)));
    printEither(e); // "not negative"

    e = bindEither(eitherBaz, bindEither(eitherBar, eitherFoo(2)));
    printEither(e); // "2"
    return 0;
}


typedef struct EitherInt {
    union {
        int   i;
        char* error;
    };
    bool is_error;
} EitherInt;

```



## C++ Monads

[FunctionalPlus](https://github.com/Dobiasd/FunctionalPlus)

- [install](https://github.com/Dobiasd/FunctionalPlus/blob/master/INSTALL.md)

- [vcpkg 包管理](https://github.com/microsoft/vcpkg/blob/master/README_zh_CN.md#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B-windows)

### [utfcpp std::u8string](https://github.com/nemtrif/utfcpp)

  > ```
  > // http://www.unicode.org/cgi-bin/GetUnihanData.pl?codepoint=中
  > 
  > /*
  > 中
  > Decimal	UTF-8	    UTF-16	UTF-32
  > 20013	    E4 B8 AD 	4E2D	00004E2D
  > 文
  > Decimal	UTF-8	    UTF-16	UTF-32
  > 25991	    E6 96 87 	6587	00006587
  > */
  > // 成功逐字符输出中文
  > // see nodejs sumarry.md -> C++ Monads
  > #include <fplus/fplus.hpp>
  > #include <iostream>
  > #include "src/utf8.h"
  > #include <string.h>
  > #include <iostream>
  > #include <string>
  > #include <fstream>
  > #include <vector>
  > using namespace std;
  > 
  > std::string str("中文");
  > for (auto it = str.begin(), it2 = str.begin(); it2 != str.end(); ) {
  > utf8::next(it2, str.end());
  > while (it < it2) {
  >    cout << *it;
  >    ++it;
  > }
  > cout << endl;
  > }
  > 
  > // 先转成 std::u32string 再用正则
  > std::string str2("中文");
  > std::vector<unsigned long> utf32result;
  > 	utf8::utf8to32(str2.begin(), str2.end(), std::back_inserter(utf32result));
  > 	size_t size1 = utf32result.size();
  > std::u32string strr(utf32result.begin(), utf32result.end());
  > cout << "all task done." << endl;
  > 
  > ```
  > ```
  > inline std::wstring from_utf8(const std::string& utf8) {
  >     std::vector<unsigned long> utf32result;
  > 	utf8::utf8to32(utf8.begin(), utf8.end(), std::back_inserter(utf32result));
  > 	size_t size1 = utf32result.size();
  >     std::wstring wstr(utf32result.begin(), utf32result.end());
  >     return wstr;
  > }
  > 
  > inline std::string to_utf8(const std::wstring& ws) {
  >     std::string utf8;
  > 	utf8::utf16to8(ws.begin(), ws.end(), std::back_inserter(utf8));
  > 	return utf8;
  > }
  > 
  > int main()
  > {
  >     std::string test = "john.doe@神谕.com"; // utf8
  >     std::string expr = "[\\u0080-\\uDB7F]+"; // utf8
  > 
  >     std::wstring wtest = from_utf8(test);
  >     std::wstring wexpr = from_utf8(expr);
  > 
  >     std::wregex we(wexpr);
  >     std::wsmatch wm;
  >     if(std::regex_search(wtest, wm, we))
  >     {
  >         std::cout << to_utf8(wm.str(0)) << '\n';
  >     }
  > }
  > ```
  >
  > 

  




```powershell
New-Item -ItemType Directory -Path C:\src -Force
cd C:\src
git clone https://github.com/microsoft/vcpkg
.\vcpkg\bootstrap-vcpkg.bat
.\vcpkg\vcpkg.exe integrate install
.\vcpkg\vcpkg install fplus:x64-windows

--> C:/src/vcpkg/packages/fplus_x64-windows/share/fplus/copyright
fplus provides CMake targets:

    # this is heuristically generated, and may not be correct
    find_package(FunctionalPlus CONFIG REQUIRED)
    target_link_libraries(main PRIVATE FunctionalPlus::fplus)

```



```
# 源码安装
# win -> MINGW64 -> 右键 -> 管理员身份运行
git clone https://github.com/Dobiasd/FunctionalPlus
cmake -S FunctionalPlus -B FunctionalPlus/build && \
cmake --build FunctionalPlus/build && \
cmake --install FunctionalPlus/build
	# CPP Monads
	--> -- Installing: C:/Program Files (x86)/FunctionalPlus/include/fplus
	

```





```c++
#include <fplus/fplus.hpp>
#include <iostream>
using namespace std;

bool is_odd_int(int x) { return x % 2 != 0; }

int main(){
    typedef vector<int> Ints;
    Ints values = { 24, 11, 65, 44, 80, 18, 73, 90, 69, 18 };
    auto odds = fplus::keep_if(is_odd_int, values);
    std::cout << "done." << std::endl;
}
```



#### regex

[ICU support](https://github.com/microsoft/vcpkg/issues/3537) [1](https://www.boost.org/doc/libs/1_33_1/libs/regex/doc/install.html#unicode)

```
cd C:\src\vcpkg
./vcpkg.exe install boost-regex[icu]:x64-windows
	# C:/src/vcpkg/packages/boost-regex_x64-windows
	# C:\src\vcpkg\packages\icu_x64-windows\include
	# C:\src\vcpkg\installed\x64-windows\bin
		# dll 在这，复制到 exe 同目录下成功运行
	# 成功安装
	#include "boost/regex.hpp"
	#include "boost/regex/icu.hpp"
	# 以下不需要了 用 icu_x64-windows\include
	https://github.com/unicode-org/icu/releases 下载
		icu-cldr\icu4c\source\allinone
			# 有 vc 工程
			icu-cldr-2023-09-13\icu4c\source\common\unicode
				# unicode/utypes.h 在这里

visual studio 配置 utf8:
main.cpp 另存为 utf8 编码格式，然后： 
工程属性 -> C++ -> 命令行 其他选项: /utf-8 

u32string u32restr = U"(abc|def)[ghi]";
	# 可以这样定义
	
# build.bat
@echo off
if exist "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" (
    call "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" x64
) else (
    if exist "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat" (
        call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
    ) else (
        call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Enterprise\VC\Auxiliary\Build\vcvarsall.bat" x64
    )
)
set compilerflags=/Od /Zi /EHsc /std:c++latest /I include /I C:\src\vcpkg\packages\fplus_x64-windows\include /I D:\GitHub\echodict\friso_vs2019 /I C:\src\vcpkg\packages\boost-regex_x64-windows\include
set linkerflags=/OUT:bin\main.exe
cl.exe %compilerflags% mmseg_jp.cpp /link %linkerflags%
rem cl.exe %compilerflags% src\*.cpp /link %linkerflags%
del bin\*.ilk *.obj *.pdb



// // Include the Boost regex header 
// #include <boost/regex.hpp> // Include other headers as needed 
// #include <iostream> 
// #include <string>

// int main() {

//     boost::regex reg("[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]+"); 

//     //boost::regex reg("(A.*)");

//     // Create a string that contains some Japanese characters 
//     std::string s = "This is a string with 日本語 characters."; 
//     // Create a regex object with the syntax option for ICU regex 
//     // boost::regex reg("/[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]+/", boost::regex::icu); 
//     // // Use regex_search to check if the string contains any Japanese characters 
//     // if (boost::regex_search(s, re)) {
//     //     std::cout << "The string contains Japanese characters.\n"; 
//     //     // Use regex_iterator to iterate over all the matches of the regex in the string 
//     //     boost::sregex_iterator it(s.begin(), s.end(), re); 
//     //     boost::sregex_iterator end; 
//     //     while (it != end) { 
//     //         // Print each match and its position in the string 
//     //         std::cout << "Match: " << it->str() << "\n"; 
//     //         std::cout << "Position: " << it->position() << "\n"; ++it; } 
//     //     } 
//     // else {
//     //     std::cout << "The string does not contain Japanese characters.\n"; 
//     // } 
//     return 0; 
// }
```





### cuCollections map代表字典

[cuCollections](https://github.com/NVIDIA/cuCollections)

[在 GPU 上使用大规模并行哈希图实现性能最大化](https://developer.nvidia.com/zh-cn/blog/maximizing-performance-with-massively-parallel-hash-maps-on-gpus/)

```
能够做到动态扩容的只有cuCollections的实现。我们在cuCollections的GPU HashTable基础上实现了特殊接口（find_or_insert），对大规模读写性能进行了优化
```



```
mkdir cumap && \
cd cumap && \
mkdir -p cmake && \
wget -O cmake/CPM.cmake https://github.com/cpm-cmake/CPM.cmake/releases/latest/download/get_cpm.cmake

vi CMakeLists.txt
cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

# create project
project(MyProject)

# add executable
add_executable(main main.cpp)

# add dependencies
include(cmake/CPM.cmake)

CPMAddPackage("gh:fmtlib/fmt#7.1.3")
CPMAddPackage("gh:nlohmann/json@3.10.5")
CPMAddPackage("gh:catchorg/Catch2@3.2.1")

# link dependencies
target_link_libraries(main fmt::fmt nlohmann_json::nlohmann_json Catch2::Catch2WithMain)


cmake .
	#  Failed to find nvcc.


```





####  main.cpp

```
#include <cuco/static_map.cuh>

#include <thrust/device_vector.h>
#include <thrust/equal.h>
#include <thrust/iterator/zip_iterator.h>
#include <thrust/sequence.h>
#include <thrust/transform.h>

#include <cmath>
#include <cstddef>
#include <iostream>
#include <limits>

/**
 * @file host_bulk_example.cu
 * @brief Demonstrates usage of the static_map "bulk" host APIs.
 *
 * The bulk APIs are only invocable from the host and are used for doing operations like insert or
 * find on a set of keys.
 *
 */

int main(void)
{
  using Key   = int;
  using Value = int;

  // Empty slots are represented by reserved "sentinel" values. These values should be selected such
  // that they never occur in your input data.
  Key constexpr empty_key_sentinel     = -1;
  Value constexpr empty_value_sentinel = -1;

  // Number of key/value pairs to be inserted
  std::size_t constexpr num_keys = 50'000;

  // Compute capacity based on a 50% load factor
  auto constexpr load_factor = 0.5;
  std::size_t const capacity = std::ceil(num_keys / load_factor);

  // Constructs a map with "capacity" slots using -1 and -1 as the empty key/value sentinels.
  cuco::static_map<Key, Value> map{
    capacity, cuco::empty_key{empty_key_sentinel}, cuco::empty_value{empty_value_sentinel}};

  // Create a sequence of keys and values {{0,0}, {1,1}, ... {i,i}}
  thrust::device_vector<Key> insert_keys(num_keys);
  thrust::sequence(insert_keys.begin(), insert_keys.end(), 0);
  thrust::device_vector<Value> insert_values(num_keys);
  thrust::sequence(insert_values.begin(), insert_values.end(), 0);
  auto zipped =
    thrust::make_zip_iterator(thrust::make_tuple(insert_keys.begin(), insert_values.begin()));

  // Inserts all pairs into the map
  map.insert(zipped, zipped + insert_keys.size());

  // Storage for found values
  thrust::device_vector<Value> found_values(num_keys);

  // Finds all keys {0, 1, 2, ...} and stores associated values into `found_values`
  // If a key `keys_to_find[i]` doesn't exist, `found_values[i] == empty_value_sentinel`
  map.find(insert_keys.begin(), insert_keys.end(), found_values.begin());

  // Verify that all the found values match the inserted values
  bool const all_values_match =
    thrust::equal(found_values.begin(), found_values.end(), insert_values.begin());

  if (all_values_match) { std::cout << "Success! Found all values.\n"; }

  return 0;
}
```







### stdgpu

[stdgpu](https://github.com/stotko/stdgpu)

[nvidia thrust](https://github.com/NVIDIA/thrust)



### ImPlay

[ImPlay IMGUI+MPV](https://github.com/tsl0922/ImPlay/issues/57)

- [mpv lazy](https://github.com/hooke007/MPV_lazy/discussions/120)

```

# windows
打开 MSYS2 MINGW64:
pacman -S base-devel git p7zip mingw-w64-x86_64-gcc mingw-w64-x86_64-cmake mingw-w64-x86_64-freetype


git clone https://github.com/tsl0922/ImPlay.git && \
cd ImPlay && \
mkdir build && cd build && \
cmake -DCMAKE_BUILD_TYPE=RELEASE -DUSE_PATCHED_GLFW=ON -DUSE_OPENGL_ES3=ON -DCREATE_PACKAGE=ON .. && \
cmake --build . --target package


# ubuntu22.04
sudo apt-get install -y build-essential cmake git pkg-config \
    libgtk-3-dev libglfw3-dev libfreetype6-dev libmpv-dev
    
git clone https://github.com/tsl0922/ImPlay.git && \
cd ImPlay && mkdir build && cd build && \
cmake -DCMAKE_BUILD_TYPE=RELEASE ..  && \
cmake --build .  && \
cmake --install .
	# 成功运行

```



[Packaging Requirements](https://github.com/keepassxreboot/keepassxc/wiki/Set-up-Build-Environment-on-Windows)

```
To turn on Microsoft .NET Framework 3.5.1 on Windows 7:
Select Start > Control Panel > Programs > Programs and Features.
Select Turn Windows features on or off.
If not already installed, select Microsoft .NET Framework 3.5.1 and click OK.
Restart the machine when prompted.
```



```
# win10
# 打包需要先安装 https://github.com/wixtoolset/wix3/releases/download/wix3112rtm/wix311.exe
	# 它需要打开 .NET Framework 3.5.1 这个可选项(看上面一节) 

export PATH="${PATH}:/C/Program Files (x86)/WiX Toolset v3.11/bin"
	# wix311 安装在这里

pacman -S base-devel git p7zip mingw-w64-x86_64-gcc mingw-w64-x86_64-cmake mingw-w64-x86_64-freetype

git clone https://github.com/tsl0922/ImPlay.git && \
cd ImPlay && mkdir build && cd build && \
cmake -DCMAKE_BUILD_TYPE=RELEASE -DUSE_PATCHED_GLFW=ON -DUSE_OPENGL_ES3=ON -DCREATE_PACKAGE=ON .. && \
cmake --build . --target package
	# C:/msys64/home/Administrator/ImPlay/build/ImPlay-1.4.0-win64.msi generated.
	# 成功生成安装包 
	

编译好以后直接把 C:\msys64\mingw64\bin 这里面的所有 dll 复制到 C:\msys64\home\Administrator\ImPlay\build 双击 ImPlay.exe 就可以正常运行


```





#### uosc lua ui

[uosc lua UI for mpv](https://github.com/tomasklaen/uosc)

- [mpv 配置文件在哪](https://mpv.io/manual/master/#files)

  ```
  C:\users\USERNAME\AppData\Roaming\mpv\mpv.conf
  ```

  



#### Memento

[mpv for studying Japanese](https://github.com/ripose-jp/Memento)



```
安装 msys2 -> win键 -> 打开 MSYS2 MINGW64

pacman -S base-devel git p7zip mingw-w64-x86_64-gcc mingw-w64-x86_64-cmake mingw-w64-x86_64-freetype
git clone https://github.com/tsl0922/ImPlay.git && \
cd ImPlay && \
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=RELEASE -DUSE_PATCHED_GLFW=ON -DUSE_OPENGL_ES3=ON -DCREATE_PACKAGE=ON ..
cmake --build . --target package
  # This will build a MSI installer and a portable ZIP.
  
```



#### mpv

[问问题](https://github.com/mpv-player/mpv/issues/12158)

[build on ubuntu](https://github.com/mpv-player/mpv-build/issues/131)

```
# 打开 minw64 命令行
echo $MINGW_PACKAGE_PREFIX
	--> mingw-w64-x86_64
	# 它是已经预定义的

pacman -Syu && \
pacman -Su

pacman -S git $MINGW_PACKAGE_PREFIX-{python,pkgconf,gcc,meson} && \
pacman -S $MINGW_PACKAGE_PREFIX-{ffmpeg,libjpeg-turbo,luajit}


git clone https://github.com/mpv-player/mpv.git && \
cd mpv && \ 
meson setup build -Dlibmpv=true --prefix=$MSYSTEM_PREFIX && \
meson compile -C build && \
meson install -C build


Installing player/mpv.com to C:/msys64/mingw64/bin
Installing libmpv-2.dll to C:/msys64/mingw64/bin
Installing libmpv.dll.a to C:/msys64/mingw64/lib
Installing mpv.exe to C:/msys64/mingw64/bin
Installing C:/msys64/home/i/mpv/libmpv/client.h to C:/msys64/mingw64/include/mpv/
Installing C:/msys64/home/i/mpv/libmpv/render.h to C:/msys64/mingw64/include/mpv/
Installing C:/msys64/home/i/mpv/libmpv/render_gl.h to C:/msys64/mingw64/include/mpv/
Installing C:/msys64/home/i/mpv/libmpv/stream_cb.h to C:/msys64/mingw64/include/mpv/
Installing C:/msys64/home/i/mpv/build/meson-private/mpv.pc to C:/msys64/mingw64/lib/pkgconfig
Installing C:/msys64/home/i/mpv/etc/mpv.conf to C:/msys64/mingw64/share/doc/mpv
Installing C:/msys64/home/i/mpv/etc/input.conf to C:/msys64/mingw64/share/doc/mpv
Installing C:/msys64/home/i/mpv/etc/mplayer-input.conf to C:/msys64/mingw64/share/doc/mpv
Installing C:/msys64/home/i/mpv/etc/restore-old-bindings.conf to C:/msys64/mingw64/share/doc/mpv
Installing C:/msys64/home/i/mpv/etc/mpv.bash-completion to C:/msys64/mingw64/share/bash-completion/c
ompletions
Installing C:/msys64/home/i/mpv/etc/_mpv.zsh to C:/msys64/mingw64/share/zsh/site-functions
Installing C:/msys64/home/i/mpv/etc/mpv.desktop to C:/msys64/mingw64/share/applications
Installing C:/msys64/home/i/mpv/etc/mpv.metainfo.xml to C:/msys64/mingw64/share/metainfo
Installing C:/msys64/home/i/mpv/etc/encoding-profiles.conf to C:/msys64/mingw64/etc/mpv
Installing C:/msys64/home/i/mpv/etc/mpv-icon-8bit-16x16.png to C:/msys64/mingw64/share/icons/hicolor
/16x16/apps
Installing C:/msys64/home/i/mpv/etc/mpv-icon-8bit-32x32.png to C:/msys64/mingw64/share/icons/hicolor
/32x32/apps
Installing C:/msys64/home/i/mpv/etc/mpv-icon-8bit-64x64.png to C:/msys64/mingw64/share/icons/hicolor
/64x64/apps
Installing C:/msys64/home/i/mpv/etc/mpv-icon-8bit-128x128.png to C:/msys64/mingw64/share/icons/hicol
or/128x128/apps
Installing C:/msys64/home/i/mpv/etc/mpv-gradient.svg to C:/msys64/mingw64/share/icons/hicolor/scalab
le/apps
Installing C:/msys64/home/i/mpv/etc/mpv-symbolic.svg to C:/msys64/mingw64/share/icons/hicolor/symbol
ic/apps


```



##### vscode task.json 编译

[VScode tasks.json和launch.json的设置](https://zhuanlan.zhihu.com/p/92175757)



##### mpv-winbuild-cmake

[mpv-winbuild-cmake](https://github.com/shinchiro/mpv-winbuild-cmake)

```
win键点一下 -> MSYS2 MSYS
	# MSYS2 MSYS 只能是这个，不要什么 32 64
  
pacman -S base-devel cmake gcc yasm nasm git mercurial subversion gyp tar gmp-devel mpc-devel mpfr-devel python zlib-devel unzip zip p7zip meson libunistring5
	
```



### Dummy-Robot 机械臂

https://github.com/peng-zhihui/Dummy-Robot



### windows内核

[Windows-Kernel-Explorer](https://github.com/AxtMueller/Windows-Kernel-Explorer)

[WKTools](https://github.com/AngleHony/WKTools)





## MMSEG 分词算法

[mmseg](http://technology.chtsai.org/mmseg/)

[python3实现](https://gist.github.com/hailiang-wang/d14c48740d18e701cf470311d75c7ba0)

[dict.txt](https://github.com/hailiang-wang/jieba/blob/master/jieba/dict.txt)

[量子计算](https://quantumctek-cloud.com/)

[Mmseg算法](https://www.jianshu.com/p/e4ae8d194487) 讲得好  



```
abcdefg
从 a 开始，找出三个连续字串（至少前面保证不空，后面可以空）
这样会找出很多个三串，取其中最长的那个，这个串的串头就是第一个有效词
然后去掉这个有效词后，从剩余的字符串再重复上面的过程，直到结束。

一、所有串长度加起来总长度越大越好
南_京_市 3
南京_市  3
南京市   3

长度一样，需要应用下一条规则

二、每串的平均长度越大越好
南京市_长江大桥 —— 平均词长度为7/2=3.5 （既每串的平均长度是3.5）
南京市_长江_大桥 —— 平均词长度为7/3=2.3
总字符数 / 串数量 = 平均词长

三、最小词长方差（每串的长度都更接近平均串长）

这个规则基于“单词长度更倾向于均匀分布”的假设。选取词长变化最小的chunk的第一个词。词长变化一般用词长的方差来衡量。

[方差的计算](https://zh.wikihow.com/%E8%AE%A1%E7%AE%97%E6%A0%87%E5%87%86%E5%B7%AE)

1. 求平均数
2. 求方差 （方差是数据偏离平均数的程度）
   > 每一项都减去平均数，然后全部求平方，再然后全部加起来，最后除以总个数（或者总个数 - 1）
3. 求标准差
   > 方差开平方既可


一般我们在组织语句时，为了朗朗上口，往往使用的词汇组成长度比较一致。
比方，“幸福_快乐”，“人之初_性本善”，“君子一言，驷马难追”。 类似，词语“研究生命科学”


在概率论和统计学中，一个随机变量的方差（Variance）描述的是它的离散程度，也就是该变量离其期望值的距离。因此该规则的前提假设是：Word lengths are usually evenly distributed（句子中的词语长度经常是均匀分布的）。直观来说，对于如下两个“三词语块”：

1.研究 生命 起源
2.研究生 命 起源

其长度为6，平均词长为2，规则一和规则二无能无力，利用规则三：
　语块1的方差 = ((2-2)^2+(2-2)^2+(2-2)^2)/3 = 0
　语块2的方差 = ((3-2)^2+(1-2)^2+(2-2)^2)/3 = 2/3
则语块1为最佳候选，因此该语块的第一个词“研究”为最佳的分词形式。




四、最大单字词语语素自由度之和（Largest sum of degree of morphemic freedom of one-character words）：
　　如下所示，例子中的两个“三词语块”拥有同样的长度、平均词长及方差，因此上述三个规则都无法解决其歧义消解问题：
1. _C1_ _C2_ _C3C4_
2. _C1_ _C2C3_ _C4_

　　这两个语块都包括了两个单字（one-character）词语和一个两字（two-character）词语，规则四主要关注其中的单字词语。直观来看，有些汉字很少作为词语出现，而另一些汉字则常常作为词语出现，从统计角度来看，在语料库中出现频率高的汉字就很可能是一个单字词语，反之可能性就小。计算单词词语语素自由度之和的公式是对“三词语块”中的单字词语频率取对数并求和（The formula used to calculate the sum of degree of morphemic freedom is to sum log(frequency) of all one-character word(s) in a chunk.）规则四则选取其中和最大的语块，并将该语块的第一词语作为最佳的词语切分形式。

```



```
通过一个例句--“研究生命起源“来简述一下复杂最大匹配的分词过程，本例匹配以3个词为一组匹配举例。MMSeg分词算法会得到7个chunk，分别为：

编号	chunk	长度
0	研_究_生	3
1	研_究_生命	4
2	研究_生_命	4
3	研究_生命_起	5
4	研究_生命_起源	6
5	研究生_命_起	5
6	研究生_命_起源	6
使用规则1过滤后得到2个chunk，如下：

编号	chunk	长度
4	研究_生命_起源	6
6	研究生_命_起源	6
计算平均长度后为：

编号	chunk	长度	平均长度
4	研究_生命_起源	6	2
6	研究生_命_起源	6	2
使用规则2过滤后得到2个chunk，如下：

编号	chunk	长度	平均长度
4	研究_生命_起源	6	2
6	研究生_命_起源	6	2
计算标准差的平方后为：

编号	chunk	长度	平均长度	标准差的平方
4	研究_生命_起源	6	2	0
6	研究生_命_起源	6	2	2/3
使用规则3过滤后得到1个chunk，如下：

编号	chunk	长度	平均长度	标准差的平方
4	研究_生命_起源	6	2	0
匹配过程终止。最终取“研究”成词，以相同的方法继续处理“生命起源”。

分词效果:

研究_生命_起源

```







```

echodict\friso_vs2019\mmseg_example.py
	# 看这里

# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright 2017 Hai Liang Wang <hailiang.hl.wang@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# File: wordseg-algorithm/mmseg_example.py
# Author: Hai Liang Wang
# Date: 2017-07-19:22:25:38
#
#===============================================================================

"""
    MMSEG: 
    A Word Identification System for Mandarin Chinese Text Based on Two
    Variants of the Maximum Matching Algorithm
    http://technology.chtsai.org/mmseg/

    Other references:
    http://blog.csdn.net/nciaebupt/article/details/8114460
    http://www.codes51.com/itwd/1802849.html

    Dict:
    https://github.com/Samurais/jieba/blob/master/jieba/dict.txt

    Deps:
    Python3
"""

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-07-19:22:25:38"


import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

import math
import string
from functools import reduce 

class Word():
    '''
    A single word
    '''
    def __init__(self, text="", freq=0):
        self.text = text
        self.freq = freq
        self.length = len(text)

class Chunk():
    '''
    Word Group that split with Forward Maximum Match(FMM)
    '''

    def __init__(self, w1, w2 = None, w3 = None):
        self.words = []
        self.words.append(w1)
        if w2: self.words.append(w2)
        if w3: self.words.append(w3)

    @property
    def total_word_length(self):
        return reduce(lambda x, y: x + y.length, self.words, 0)

    @property
    def average_word_length(self):
        return float(self.total_word_length) / float(len(self.words))

    @property
    def standard_deviation(self):
        return math.sqrt(reduce(lambda x,y: x + \
                        (y.length - self.average_word_length)**2, \
                        self.words, 0.0) / self.total_word_length)
    @property
    def word_frequency(self):
        return reduce(lambda x, y: x + y.freq, self.words, 0)


class Vocabulary():
    '''
    Vocabulary with whole words
    '''

    def __init__(self, dict_path):
        self.dict = {}
        self.dict_path = dict_path
        self.max_word_length = 0
        self.__load()

    def __load(self):
        with open(self.dict_path, encoding='UTF-8') as f:
            for x in f.readlines():
                # text, freq, tag = x.split()
                # self.dict[text] = (len(text), int(freq), tag)
                text, freq, tag = (x.split()[0], 0, '0')
                self.dict[text] = (len(text), int(freq), tag)
                self.max_word_length = max([self.max_word_length, len(text)])

    def get_word(self, text):
        if text in self.dict: 
            return Word(text=text, freq=self.dict[text][1])


class Tokenizer():
    '''
    MMSEG Tokenizer for Python
    '''
    def __init__(self, dict_path):
        self.V = Vocabulary(dict_path=dict_path)

    def cut(self, sentence):
        sentence_length = len(sentence)
        cursor = 0
        arr = []
        while cursor < sentence_length:
            if self.is_chinese_char(sentence[cursor]):
                chunks = self.__get_chunks(sentence, cursor) # Matching Algorithm
                try:
                    words, length = self.__ambiguity_resolution(chunks) # Ambiguity Resolution Rules
                except Exception as e:
                    cursor += 1
                    continue
                cursor += length
                for term in list(filter(None, words)): #yield term
                    arr.append( term )
            else: # 处理非中文单词(英文单词, etc.)
                word, cursor = self.__match_none_chinese_words(sentence, cursor)
                arr.append( word )
                #yield word
        return arr

    def __ambiguity_resolution(self, chunks):
        '''
        根据当前游标位置进行切词
        '''
        # print("# Rule 1: 根据 total_word_length 进行消岐")
        # for x in chunks: [print(y.text) for y in x.words]; print('-'*20)
        if len(chunks) > 1: # Rule 1: 根据 total_word_length 进行消岐
            score = max([x.total_word_length for x in chunks])
            chunks = list(filter(None, \
                            [ x if x.total_word_length == score \
                                else None for x in chunks]))

        # print("# Rule 2: 根据 average_word_length 进行消岐") 
        # for x in chunks: [print(y.text) for y in x.words]; print('-'*20)
        if len(chunks) > 1: # Rule 2: 根据 average_word_length 进行消岐
            score = max([x.average_word_length for x in chunks])
            chunks = list(filter(None, \
                            [ x if x.average_word_length == score \
                                else None for x in chunks]))

        if len(chunks) > 1: # Rule 3: 根据 standard_deviation 进行消岐
            score = max([x.standard_deviation for x in chunks])
            chunks = list(filter(None, \
                            [ x if x.standard_deviation == score \
                                else None for x in chunks]))

        if len(chunks) > 1: # Rule 4: 根据 word_frequency 进行消岐
            score = max([x.word_frequency for x in chunks])
            chunks = list(filter(None, \
                            [ x if x.word_frequency == score \
                                else None for x in chunks]))

        if len(chunks) != 1: 
            '''
            分词失败
            '''
            return ''

        words = chunks[0].words
        return [w.text for w in words], reduce(lambda x,y: x + y.length, words ,0)

    def __get_chunks(self, sentence, cursor):
        '''
        根据游标位置取词组
        '''
        chunks = []
        chunk_begin = self.__match_chinese_words(sentence, cursor)
        for b in chunk_begin: 
            chunk_middle = self.__match_chinese_words(sentence, cursor + b.length)
            if chunk_middle:
                for m in chunk_middle:
                    chunk_end = self.__match_chinese_words(sentence, cursor + b.length + m.length)
                    if chunk_end:
                        for e in chunk_end: 
                            chunks.append(Chunk(b, m, e))
                    else:
                        chunks.append(Chunk(b, m))
            else:
                chunks.append(Chunk(b))

        return chunks

    @staticmethod
    def __match_none_chinese_words(sentence, begin_pos):
        '''
        切割出非中文词
        '''
        # Skip pre-word whitespaces and punctuations
        #跳过中英文标点和空格
        cursor = begin_pos
        while cursor < len(sentence):
            ch = sentence[cursor]
            if Tokenizer.is_ascii_char(ch) or Tokenizer.is_chinese_char(ch):
                break
            cursor += 1
        #得到英文单词的起始位置    
        start = cursor
        
        #找出英文单词的结束位置
        while cursor < len(sentence):
            ch = sentence[cursor]
            if not Tokenizer.is_ascii_char(ch):
                break
            cursor += 1
        end = cursor
        
        #Skip chinese word whitespaces and punctuations
        #跳过中英文标点和空格
        while cursor < len(sentence):
            ch = sentence[cursor]
            if Tokenizer.is_ascii_char(ch) or Tokenizer.is_chinese_char(ch):
                break
            cursor += 1
            
        #返回英文单词和游标地址
        return sentence[start:end], cursor

    def __match_chinese_words(self, sentence, begin_pos):
        '''
        根据游标位置取词
        '''
        sentence_length = len(sentence)
        words = []
        cursor = begin_pos
        index = 0

        while cursor < sentence_length:
            if index >= self.V.max_word_length: break
            if not self.is_chinese_char(sentence[cursor]): break

            cursor += 1
            index += 1
            text = sentence[begin_pos:cursor]
            word = self.V.get_word(text)
            if word: words.append(word)

        if not words: 
            word = Word()
            word.length = 0
            words.append(word)

        return words

    @staticmethod
    def is_ascii_char(charater):
        if charater in string.whitespace:
            return False
        if charater in string.punctuation:
            return False
        return charater in string.printable

    @staticmethod 
    def is_chinese_char(charater):
        '''
        判断该字符是否是中文字符（不包括中文标点）
        '''  
        return 0x4e00 <= ord(charater) < 0x9fa6

def test_chunk_n_word():
    w1 = Word("中文", 1)
    w2 = Word("分词技术", 1)
    c1= Chunk(w1, w2)
    assert c1.total_word_length==6, "total_word_length"
    assert c1.average_word_length==c1.average_word_length , "average_word_length"
    assert c1.standard_deviation==0.5773502691896257 , "standard_deviation"
    assert c1.word_frequency==2, "word_frequency"
    print("passed.")

def test_vocab():
    v = Vocabulary(dict_path=os.path.join(curdir, 'dict.txt'))
    print(len(v.dict))
    print(v.get_word("中文").text)
    print(v.get_word("中文").freq)
    print(v.get_word("中文").length)

def test_token():
    t = Tokenizer(dict_path=os.path.join(curdir, 'dict.txt'))
    # for x in t.cut("CNN报道美国即将开始新一轮的单边制裁朝鲜计划"): print(x)
    print(' '.join(t.cut("CNN报道Washington D.C.即将开始新一轮的单边制裁朝鲜计划")))
    print(' '.join(t.cut("研究生命来源")))
    print(' '.join(t.cut("南京市长江大桥欢迎您")))
    print(' '.join(t.cut("请把手抬高一点儿")))
    print(' '.join(t.cut("长春市长春节致词。")))
    print(' '.join(t.cut("长春市长春药店。")))
    print(' '.join(t.cut("我的和服务必在明天做好。")))
    print(' '.join(t.cut("我发现有很多人喜欢他。")))
    print(' '.join(t.cut("我喜欢看电视剧大长今。")))
    print(' '.join(t.cut("半夜给拎起来陪看欧洲杯糊着两眼半晌没搞明白谁和谁踢。")))
    print(' '.join(t.cut("李智伟高高兴兴以及王晓薇出去玩，后来智伟和晓薇又单独去玩了。")))
    print(' '.join(t.cut("一次性交出去很多钱。 ")))
    print(' '.join(t.cut("这是一个伸手不见五指的黑夜。我叫孙悟空，我爱北京，我爱Python和C++。")))
    print(' '.join(t.cut("我不喜欢日本和服。")))
    print(' '.join(t.cut("雷猴回归人间。")))
    print(' '.join(t.cut("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作")))
    print(' '.join(t.cut("我需要廉租房")))
    print(' '.join(t.cut("永和服装饰品有限公司")))
    print(' '.join(t.cut("我爱北京天安门")))
    print(' '.join(t.cut("abc")))
    print(' '.join(t.cut("隐马尔可夫")))
    print(' '.join(t.cut("雷猴是个好网站")))
    print(' '.join(t.cut("“Microsoft”一词由“MICROcomputer（微型计算机）”和“SOFTware（软件）”两部分组成")))
    print(' '.join(t.cut("草泥马和欺实马是今年的流行词汇")))
    print(' '.join(t.cut("伊藤洋华堂总府店")))
    print(' '.join(t.cut("中国科学院计算技术研究所")))
    print(' '.join(t.cut("罗密欧与朱丽叶")))
    print(' '.join(t.cut("我购买了道具和服装")))
    print(' '.join(t.cut("PS: 我觉得开源有一个好处，就是能够敦促自己不断改进，避免敞帚自珍")))
    print(' '.join(t.cut("湖北省石首市")))
    print(' '.join(t.cut("总经理完成了这件事情")))
    print(' '.join(t.cut("电脑修好了")))
    print(' '.join(t.cut("做好了这件事情就一了百了了")))
    print(' '.join(t.cut("人们审美的观点是不同的")))
    print(' '.join(t.cut("我们买了一个美的空调")))
    print(' '.join(t.cut("线程初始化时我们要注意")))
    print(' '.join(t.cut("一个分子是由好多原子组织成的")))
    print(' '.join(t.cut("祝你马到功成")))
    print(' '.join(t.cut("他掉进了无底洞里")))
    print(' '.join(t.cut("中国的首都是北京")))
    print(' '.join(t.cut("孙君意")))
    print(' '.join(t.cut("外交部发言人马朝旭")))
    print(' '.join(t.cut("领导人会议和第四届东亚峰会")))
    print(' '.join(t.cut("在过去的这五年")))
    print(' '.join(t.cut("还需要很长的路要走")))
    print(' '.join(t.cut("60周年首都阅兵")))
    print(' '.join(t.cut("你好人们审美的观点是不同的")))
    print(' '.join(t.cut("买水果然后来世博园")))
    print(' '.join(t.cut("买水果然后去世博园")))
    print(' '.join(t.cut("但是后来我才知道你是对的")))
    print(' '.join(t.cut("存在即合理")))
    print(' '.join(t.cut("的的的的的在的的的的就以和和和")))
    print(' '.join(t.cut("I love你，不以为耻，反以为rong")))
    print(' '.join(t.cut(" ")))
    print(' '.join(t.cut("")))
    print(' '.join(t.cut("hello你好人们审美的观点是不同的")))
    print(' '.join(t.cut("很好但主要是基于网页形式")))
    print(' '.join(t.cut("hello你好人们审美的观点是不同的")))
    print(' '.join(t.cut("为什么我不能拥有想要的生活")))
    print(' '.join(t.cut("后来我才")))
    print(' '.join(t.cut("此次来中国是为了")))
    print(' '.join(t.cut("使用了它就可以解决一些问题")))
    print(' '.join(t.cut(",使用了它就可以解决一些问题")))
    print(' '.join(t.cut("其实使用了它就可以解决一些问题")))
    print(' '.join(t.cut("好人使用了它就可以解决一些问题")))
    print(' '.join(t.cut("是因为和国家")))
    print(' '.join(t.cut("老年搜索还支持")))

if __name__ == '__main__':
    test_token()


```



### kuromoji-rs

[kuromoji-rs](https://github.com/fulmicoton/kuromoji-rs/tree/master)

```
git clone https://github.com/fulmicoton/kuromoji-rs.git && \
cd kuromoji-rs && \
cargo build

```





# PDF

[pdf-lib](https://github.com/Hopding/pdf-lib/issues/83) extract images from pdf

[extract-images.zip](https://github.com/Hopding/pdf-lib/files/3125076/extract-images.zip)

```
You just need to unzip the file and run yarn install (or npm install) and then run node index.js existing1.pdf or node index.js existing2.pdf. The script will extract as many embedded images as it can from the PDF into the images/ directory.
```





# Excel



```javascript
    let xlsx = require('node-xlsx')  // npm install node-xlsx --save

    function writeExcel(data, fname) {
        let buffer = xlsx.build([
            {
                name: 'sheet1',
                data
            }
        ])
        require('fs').writeFileSync(`${fname}`, buffer, {'flag':'w'}) // 生成excel
    }

    let titles = ['id', 'name'] // 列名
    let data = [] // 写入excel 的数据行
    let fname = './the_content.xlsx'

    data.push(titles)
    data.push([0, 'first'])
    data.push([1, 'second'])
    writeExcel(data, fname)
```



```
// Parse a buffer
const workSheetsFromBuffer = xlsx.parse(fs.readFileSync(`${__dirname}/myFile.xlsx`));
// Parse a file
const workSheetsFromFile = xlsx.parse(`${__dirname}/myFile.xlsx`);
```



## Data

### ak48

```
echodict\chatgpt_server\lib\ak148_extradata.js
	# 提取 excel ，给 pandora 生成解析
```



### nlpp

````
echodict\xml\extract_nlpp.js # 提取 excel ，给 pandora 生成解析
````





## godot excel

[godot-excel-reader 真正的excel](https://github.com/LaoDie1/godot-excel-reader)

[godot-resources-as-sheets-plugin 编辑资源](https://github.com/don-tnowe/godot-resources-as-sheets-plugin) [asset-library](https://godotengine.org/asset-library/asset/1479)

- [godot-sprite-painter](https://github.com/don-tnowe/godot-sprite-painter)

[Add a Spreadsheet resource for handling tabular data](https://github.com/godotengine/godot-proposals/issues/13)



## excel 正则

- https://github.com/liuyi91/Excel



## C#读写excel

```
# https://blog.csdn.net/weixin_42176639/article/details/101648803
	# NOPI读写Excel，并插入图片
```





# Docx



```javascript

let path = require('path')
var mammoth = require("mammoth");

function getTestByWord(fileName) {
    return new Promise((ok, err) => {
        // var url = path.join(__dirname, 'A1-3-2.docx');
        // var url = path.join(__dirname, "../../../file/" + fileName);
        var url = fileName
        mammoth.extractRawText({
                path: url
            })
            .then(function (result) {
                var text = result.value; // The raw text
                var messages = result.messages;
                ok(text);

            })
            .catch((e) => {
                err(false)
            })
            .done();
    })
}

( async()=>{

    let fileName = path.join(__dirname, 'A3-2&3-1.docx');
    let s = await getTestByWord(fileName)
    let a = 1

}) ()


```





```javascript
// https://www.jianshu.com/p/68a420a68ded
	十行代码教你用node.js读取docx中的文本
let rd = require('rd');
let fs = require('fs');
let path = require("path")

let docx4js = require('docx4js');
const AdmZip = require('adm-zip'); //引入查看zip文件的包
const zip = new AdmZip("alldata/A1-1&1-2.docx"); //filePath为文件路径

// 同步遍历目录下的所有 word 文件
rd.eachFileFilterSync('alldata', /\.docx$/, function (fullpath, stats) {

    let basename = path.basename(fullpath);
    
    if (basename != "A1-1&1-2.docx") {
        return;
    }

    let contentXml = zip.readAsText("word/document.xml");   // 内容文本
    
    let str = "";
    contentXml.match(/<w:t>[\s\S]*?<\/w:t>/ig).forEach((item)=>{

        str = str + item.slice(5,-6) + "\n";  // 不知道为什么读出来文档自带的换行没了
    }) 

    fs.writeFileSync('2.txt', str);

});
```





```javascript

// import docx4js from "docx4js"


const docx4js = require('docx4js');


docx4js.docx.load("alldata/A1-1&1-2.docx").then(docx => {
    var content = docx.officeDocument.content.text()
    console.log("[Docx.jsx] docx:", content); // I am able to get the data here.
}).catch(err => {
    console.error("[Docx.jsx] err:", err);
});

To get header you do it like

docx.getObjectPart("word/header1.xml").text();

And you can do the same thing for the footer

docx.getObjectPart("word/footer1.xml").text();

you can get the content/body as well doing like

docx.getObjectPart("word/document.xml").text();
```



## 铁锈电池

```
如何用生活中容易获得的材料自制铁锈电池： 一组铁锈电池的体积跟一台洗衣机加烘衣机差不多，它的原理是，电池放电时吸氧，让浸泡其中的薄铁板生锈，释放电子；充电时，电流则让铁锈还原，吐出氧气。

在生活中自制铁锈电池可以采用以下步骤：

# 准备材料

- 铁板
- 盐水
- 导线
- LED灯或其他小型电子设备
- 容器（例如空的塑料瓶或罐）

准备工具：

- 剪刀
- 绝缘带

# 制作方法

## 1. 铁板处理

取一块铁板，如果铁板上有油漆或者其它涂层，需要彻底清除。这样才能确保铁板表面与盐水接触。

​```markdown
**注意**: 需要穿戴安全手套来防止割伤。
​```

## 2. 配制盐水

把食用盐充分溶解在清水中，得到盐水。

​```markdown
**提示**: 盐水的浓度越高，产生的电流就越大。但是也不能太高，否则会加速铁板的腐蚀。
​```

## 3. 浸泡铁板

把处理过的铁板完全浸入盐水中，然后将容器封闭。

## 4. 连接导线

接上导线，然后通过导线连接到LE灯或其他小型电子设备。

## 5. 等待反应

铁板在盐水中慢慢生锈，这个过程会释放电子，产生电流。这个电流可以通过导线传输，为小型电子设备供电。

以上就是在生活中自制铁锈电池的步骤。你可能需要试验多次才能达到理想的效果，所以不必急于求成。
```

