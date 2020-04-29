[TOC]



# Python



## Terminal Run



View -> Terminal 

> python --version
> python iTextRankTest.py



## Plugin Run

> Ctrl + Shift + X  -> search python  -> install
> Ctrl + Shift + P ->  python select interpreter





## Formatting

> 
>
> pip install yapf
>
> linting





I had the same issue and to fix that I added following line to the settings.json file:

{
    // to fix 'Timeout waiting for debugger connections'
    "python.terminal.activateEnvironment": false
}

```py
"python.terminal.activateEnvironment": false
```







