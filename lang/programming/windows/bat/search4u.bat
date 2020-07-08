@echo off

if exist a.txt del a.txt

for /r %CD%\data %%i in (*.txt,*.ass) do echo %%i >>a.txt

rem cmd.exe


