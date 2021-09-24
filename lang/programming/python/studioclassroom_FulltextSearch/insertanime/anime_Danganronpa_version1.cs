            using Medallion.Shell;

            string ecxutePath = Environment.CurrentDirectory; // 可执行文件运行目录
            string path = new DirectoryInfo("../").FullName;  // 上级目录

            string fname = @"F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv";
            string frtname = $"{ecxutePath}/out.srt";
            var ffmpegExe = @"E:\Program Files\ffmpeg-4.3.2-2021-02-02-full_build\bin\ffmpeg.exe";
            var ffmpegArgs = new List<string>() { "-y", "-loglevel", "error", "-i", fname, "-map", "0:s:0", frtname };

            var outlog = $"{ecxutePath}/outlog.txt";

            var command = Command.Run(ffmpegExe, ffmpegArgs); // 执行命令

            using (StreamWriter sw = File.AppendText(outlog)) // 写入日志
            {
                sw.WriteLine($"Exit code: {command.Result.ExitCode}");
                sw.WriteLine($"Stdout: {command.Result.StandardOutput}");
                sw.WriteLine($"Stderr: {command.Result.StandardError}");
            }

            string strs = "\n" + File.ReadAllText(frtname, new System.Text.UTF8Encoding(false)) + "\n";   // utf8 无BOM

            MatchCollection matches = Regex.Matches(strs, @"\n\d+\n");

            int count = matches.Count;

            for (int i = 0; i < count; i++)
            {
                var item = matches[i];

                int start = item.Index;
                int end = start + item.Length;
                int len = item.Length;

                string text = strs.Substring(start, len);  // 和item.Value 应该是一样的

                string content = "";

                if ( i == count - 1 )
                {
                    content = strs.Substring(end);    
                } else
                {
                    int l = matches[i + 1].Index - end ;
                    content = strs.Substring(end, l);
                }

                var arr = content.Trim().Split('\n');
                if (arr.Length < 2)
                {
                    continue;
                }

                var time = content.Trim().Split('\n')[0];
                content = content.Trim().Split('\n')[1];



                string v = item.Value;
                Console.WriteLine(start);
            }






void test2()
        {
            /*
              
             python3.8

                out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-loglevel", "error", "-i", fname, "-map", "0:s:0", frtname])
                out_text = out_bytes.decode('utf-8')
             
             windows cmd
                ffmpeg -y -i "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" -map 0:s:0 out.srt
             
             MedallionShell
                

             */





            string ecxutePath = Environment.CurrentDirectory; // 可执行文件运行目录
            string path = new DirectoryInfo("../").FullName;  // 上级目录

            string fname = @"F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv";
            string frtname = $"{ecxutePath}/out.srt";
            var ffmpegExe = @"E:\Program Files\ffmpeg-4.3.2-2021-02-02-full_build\bin\ffmpeg.exe";
            var ffmpegArgs = new List<string>() { "-y", "-loglevel", "error", "-i", fname, "-map", "0:s:0", frtname };

            var outlog = $"{ecxutePath}/outlog.txt";

            var command = Command.Run(ffmpegExe, ffmpegArgs); // 执行命令

            using (StreamWriter sw = File.AppendText(outlog)) // 写入日志
            {
                sw.WriteLine($"Exit code: {command.Result.ExitCode}");
                sw.WriteLine($"Stdout: {command.Result.StandardOutput}");
                sw.WriteLine($"Stderr: {command.Result.StandardError}");
            }

            string strs = "\n" + File.ReadAllText(frtname, new System.Text.UTF8Encoding(false)) + "\n";   // utf8 无BOM

            MatchCollection matches = Regex.Matches(strs, @"\n\d+\n");

            int count = matches.Count;

            for (int i = 0; i < count; i++)
            {
                var item = matches[i];

                int start = item.Index;
                int end = start + item.Length;
                int len = item.Length;

                string text = strs.Substring(start, len);  // 和item.Value 应该是一样的

                string content = "";

                if (i == count - 1)
                {
                    content = strs.Substring(end);
                }
                else
                {
                    int l = matches[i + 1].Index - end;
                    content = strs.Substring(end, l);
                }

                var arr = content.Trim().Split('\n');
                if (arr.Length < 2)
                {
                    continue;
                }

                var time = content.Trim().Split('\n')[0];
                content = content.Trim().Split('\n')[1];

                Regex r = new Regex("size=.+>(.+?)</font>");

                string subtitle = "";
                if (r.Match(content).Groups.Count > 0)
                {
                    subtitle = r.Match(content).Groups[1].Value;  // 0 永远是整个串，并不是捕获组。1 才是第一个组
                } else
                {
                    content = Regex.Replace(content, "face=\".+?\"", "");
                    content = Regex.Replace(content, "size=\"\\d+\"", "");
                    content = Regex.Replace(content, "color=\".+?\"", "");
                    content = Regex.Replace(content, "<font.+?>", "");
                    content = Regex.Replace(content, "{\\an7}", "");

                    subtitle = content;
                }

                subtitle = subtitle.Replace("<b>", "").Replace("</b>", "");

                //MatchCollection matches2 = Regex.Matches(content, @"size=.+>(.+?)\<\/font\>");

                //if (matches2.Count > 0)
                //{
                //    string subtitle = matches2.G.Value;
                //} else
                //{

                //}



                //string v = item.Value;
                //Console.WriteLine(start);
            }
