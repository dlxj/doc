flask run --host 0.0.0.0 --port 8085
cmd.exe

rem kill -9 $(lsof -i:8085 | tail -n +2  |  awk '{print $2}' | tr '\n' ' ')