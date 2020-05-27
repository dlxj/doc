[TOC]



[string](https://github.com/chenshuo/recipes/blob/master/string/StringTrivial.h)



```python
 // In C++11, this is unifying assignment operator
  String& operator=(String rhs) // yes, pass-by-value
  {
    // http://en.wikibooks.org/wiki/More_C++_Idioms/Copy-and-swap
    swap(rhs);
    return *this;
  }

  // C++11 move-ctor
  String(String&& rhs) noexcept
    : data_(rhs.data_)
  {
    rhs.data_ = nullptr;
  }

  /* Not needed if we have pass-by-value operator=() above,
   * and it conflits. http://stackoverflow.com/questions/17961719/
  String& operator=(String&& rhs)
  {
    swap(rhs);
    return *this;
  }
  */
```



sudo add-apt-repository ppa:codeblocks-devs/release

sudo apt update

sudo apt install codeblocks codeblocks-contrib



sudo add-apt-repository --remove ppa:codeblocks-devs/release

sudo apt remove --autoremove codeblocks codeblocks-contrib





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









vector<string> char_vec;

```cpp
    map<string, vector<string> > senten_words;
    senten_words.insert(std::pair<string, vector<string> >( "a b c",  vector<string>({"a", "b", "c"}) ) );
    senten_words.insert(std::pair<string, vector<string> >( "a b c",  vector<string>({"a", "b", "c"}) ) );
    senten_words.insert(std::pair<string, vector<string> >( "a b c",  vector<string>({"a", "b", "c"}) ) );
    
    vector<pair<string, double> > great_sents;
    SentenceRank rank(3, 100, 0.85, 0.0001);
    
    rank.ExtractKeySentence(senten_words, great_sents, 2);
```



