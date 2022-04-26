tesseract t3.jpg stdout  --oem 2  --psm 7  -l chi_sim+eng

rem --oem 2  Legacy + LSTM 双引擎  Legacy的文字框得准，LSTM 识别得准
rem --psm 7  整个图片被认为是一行文本
rem -l chi_sim+eng  语言  中英

cmd.exe
