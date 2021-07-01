

## Install

https://dev.to/polkovnikovph/basic-haskell-vscode-windows-environment-in-2021-189j



Global setup:

- Install latest Haskell Platform from [prior versions](https://www.haskell.org/platform/prior.html) page. Newer versions of Haskell Platform are installable only through Chocolatey and elevated command prompt, and in the end it won't work, because GHC 9 is too new and not supported by VSCode plugins.
- Restart VSCode, if it was running. On Windows global environment variables get fixed at program startup, and extensions won't find GHC.
- Install [syntax highlighting extension](https://marketplace.visualstudio.com/items?itemName=justusadam.language-haskell).
- Install [language service client](https://marketplace.visualstudio.com/items?itemName=haskell.haskell) extension. The first time `*.hs` file is opened, it will download required language server binaries.
- Open Msys command prompt (available as *Git Bash* from context menu in any folder, if Git is installed).
- Run `cabal update` to download latest package version version information.
- Run `cabal install ghci-dap haskell-debug-adapter`.
- Install [Haskell debugger](https://marketplace.visualstudio.com/items?itemName=phoityne.phoityne-vscode) extension.

Project setup (mostly from Haskell debugger extension `readme`):

- Create a folder.
- Run `cabal init`, `cabal configure`, and `cabal bulid` in it (this time regular command prompt is enough).
- Switch to `Run and Debug` tab in VSCode and press `Create a launch.json file` link. Select `haskell-debug-adapter` there.
- In toolbar select `haskell(cabal)` configuration.
- Put a breakpoint and press F5 to run.



## Excel

https://github.com/v0d1ch/HExcel







## mr



https://github.com/Enzo-Liu/monao/blob/master/Main.hs



```
fromJust is pretty much equivalent to:

fromJust :: Maybe a -> a
fromJust (Just t) = t
Note that it’s the same pattern match! If you’re sure that your Maybe going to be a Just and not a Nothing, you can use fromJust to get its value without pattern matching
```





## 定义类型别名



```
Type Synonyms
定义类型别名的方法
type B = Int
data A = A BookInfo Int B
type C = (A, B)

这里C 的类型是tupe(A,B)，这些类型别名没有值构造器
```

