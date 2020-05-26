[TOC]

vscode configure

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(gdb) Launch",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/build/textrank",
            "args": ["/home/ubuntu/workcode/gitlab/cpp/textrank-master/data/abc.txt", "1", "2", "./out.txt"],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ]
        }
    ]
}
```



https://launchpad.net/~codeblocks-devs/



## Dictionary



```c++
map<string, vector<string> > sentence_token_map;  // key: sentence  value: words 
sentence_token_map.begin()->first
```





# List



```cpp
    // mapStudent.insert(pair<int, string>(1, "student_one"));
    // vector添加数据的缺省方法是push_back()  

    map<string, vector<string> > senten_words;
    vector<string> words;
    //senten_words.insert(make_pair(sent_vec[i], bigram_vec));
```





![image-20200520123051219](C:\Users\echod\AppData\Roaming\Typora\typora-user-images\image-20200520123051219.png)



[textrank c++](https://github.com/lostfish/textrank)



```cpp
    map<string, vector<string> > senten_words;
    senten_words.insert(std::pair<string, vector<string> >( "a b c",  vector<string>({"a", "b", "c"}) ) );
    senten_words.insert(std::pair<string, vector<string> >( "a b c",  vector<string>({"a", "b", "c"}) ) );
    senten_words.insert(std::pair<string, vector<string> >( "a b c",  vector<string>({"a", "b", "c"}) ) );
    
    vector<pair<string, double> > great_sents;
    SentenceRank rank(3, 100, 0.85, 0.0001);
    
    rank.ExtractKeySentence(senten_words, great_sents, 2);
```



