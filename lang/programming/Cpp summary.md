[TOC]



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





pair 是有first, second两个成员变量的结构体  



std::pair<std::string, double>("This is a StringTest0.", 9.7);

std::make_pair("This is a StringTest.", 9.9);  













