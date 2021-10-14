using System;

using Medallion.Shell;
using Npgsql;
using NpgsqlTypes;
using MeCab;
using System.Text.RegularExpressions;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using OpenCCNET;
using Kawazu;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;

/*
 
 dotnet publish -c Release -r linux-x64 # 在dangan 根目录运行

 cd /mnt/dangan/Server/bin/Release/net5.0/linux-x64

 ./dangan.Server --urls http://0.0.0.0:5000
	# 外网正常访问
 
 */

namespace dangan
{
    public class anime
    {

        public static bool initQ = false;

        public static NpgsqlConnection g_conn = null;

        public static string unhana_remove(string s)
        {
            return Regex.Replace(s, @"[^\u3040-\u309F^\u30A0-\u30FF]", "");
        }

        public static string unchinese_remove(string s)
        {
            return Regex.Replace(s, @"[^\u4e00-\u9fa5]", "");
        }

        public static string chinese_remove(string s)
        {
            return Regex.Replace(s, @"[\u4e00-\u9fa5]", "");
        }

        public static bool hasHanaQ(string s)
        {
            return unhana_remove(s).Length > 0;
        }

        public static bool jpQ(string s)
        {
            return unhana_remove(s).Length > 0;
        }

        public static bool chQ(string s)
        {
            return !jpQ(s) && chinese_remove(s).Length == 0;
        }

        public static Tuple<string, string> parseSrtTime(string time)
        {
            // time = "00:01:12,960 --> 00:01:14,640"
            string begin = time.Split(new string[] { "-->" }, StringSplitOptions.None)[0].Trim();
            string end = time.Split(new string[] { "-->" }, StringSplitOptions.None)[1].Trim();

            begin = begin.Replace(',', '.');
            end = end.Replace(',', '.');

            return new Tuple<string, string>(begin, end);
        }

        public static string extractSRT(string ffmpegExe, string videopath, string frtname, string ecxutePath)
        {
            //string fname = @"F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv";
            //string frtname = $"{ecxutePath}/out.srt";
            //var ffmpegExe = @"E:\Program Files\ffmpeg-4.3.2-2021-02-02-full_build\bin\ffmpeg.exe";
            var ffmpegArgs = new List<string>() { "-y", "-loglevel", "error", "-i", videopath, "-map", "0:s:0", frtname };

            var outlog = $"{ecxutePath}/outlog.txt";

            var command = Command.Run(ffmpegExe, ffmpegArgs); // 执行命令

            using (StreamWriter sw = File.AppendText(outlog)) // 写入日志
            {
                sw.WriteLine($"Exit code: {command.Result.ExitCode}");
                sw.WriteLine($"Stdout: {command.Result.StandardOutput}");
                sw.WriteLine($"Stderr: {command.Result.StandardError}");
            }

            string strs = "\n" + File.ReadAllText(frtname, new System.Text.UTF8Encoding(false)) + "\n";   // utf8 无BOM

            return strs;
        }
        public static Byte[] extractAudio(string ffmpegExe, string videopath, string begintime, string endtime)
        {
            //# Audio: mp3 (libmp3lame), 44100 Hz, stereo, fltp, 192 kb/s (default)
            //# -vn  no video
            //# out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-i", videopath, "-vn", "-ss", begintime, "-to", endtime, "-acodec", "mp3", \
            //#   "-ar", "44100", "-ac", "2", "-b:a", "192k", \
            //#   "tmp.mp3"])

            var ffmpegArgs = new List<string>() {
                "-y", "-hide_banner", "-loglevel", "error", "-i", videopath, "-vn", "-ss", begintime, "-to", endtime, "-acodec", "mp3",
                "-ar", "44100", "-ac", "2", "-b:a", "192k",
                "tmp.mp3"
            };

            string ecxutePath = Environment.CurrentDirectory;

            var outlog = $"{ecxutePath}/outlog.txt";

            var command = Command.Run(ffmpegExe, ffmpegArgs);

            using (StreamWriter sw = File.AppendText(outlog))
            {
                sw.WriteLine($"Exit code: {command.Result.ExitCode}");
                sw.WriteLine($"Stdout: {command.Result.StandardOutput}");
                sw.WriteLine($"Stderr: {command.Result.StandardError}");
            }

            byte[] bts = null;

            using (FileStream stream = new FileStream("tmp.mp3", FileMode.Open, FileAccess.Read))
            using (BinaryReader reader = new BinaryReader(new BufferedStream(stream)))
            {
                bts = reader.ReadBytes(Convert.ToInt32(stream.Length));
            }

            return bts;
        }

        public static void createAnimeDB(string host, string port)
        {
            using (var conn = new NpgsqlConnection($"Server={host};Port={port};Database=postgres;User Id=postgres;Password=echodict.com;"))
            {
                conn.Open();

                using (var cmd = new NpgsqlCommand("DROP DATABASE IF EXISTS anime;", conn))
                {
                    cmd.ExecuteNonQuery();
                }

                using (var cmd = new NpgsqlCommand(@"CREATE DATABASE anime 
                        WITH OWNER = postgres 
                        ENCODING = 'UTF8' 
                        TABLESPACE = pg_default 
                        CONNECTION LIMIT = -1 
                        TEMPLATE template0; ", conn))
                {
                    cmd.ExecuteNonQuery();
                }



                conn.Close();

            }

            using (var conn = new NpgsqlConnection($"Server={host};Port={port};Database=anime;User Id=postgres;Password=echodict.com;"))
            {
                conn.Open();



                using (var cmd = new NpgsqlCommand("DROP TABLE IF EXISTS anime;", conn))
                {
                    cmd.ExecuteNonQuery();
                }

                using (var cmd = new NpgsqlCommand(@"create table anime( 
                        id integer primary key generated always as identity, 
                        name text, 
                        jp text, 
                        zh text DEFAULT '', 
                        en text DEFAULT '', 
                        type text, 
                        time text, 
                        jp_mecab text, 
                        v_jp  tsvector, 
                        v_zh  tsvector, 
                        v_en  tsvector, 
                        videoname text, 
                        seasion text DEFAULT '', 
                        audio bytea, 
                        video bytea 
                    ); ", conn))
                {
                    cmd.ExecuteNonQuery();
                }


                using (var cmd = new NpgsqlCommand(@"CREATE extension pgroonga;
                        CREATE INDEX pgroonga_jp_index ON anime USING pgroonga(jp);
                        CREATE INDEX pgroonga_jpmecab_index ON anime USING pgroonga (jp_mecab);
                        CREATE extension pg_jieba;
                        CREATE INDEX animename_index ON anime (name);
                        CREATE INDEX videoname_index ON anime (videoname);
                    ", conn))
                {
                    cmd.ExecuteNonQuery();
                }

                // @禁止转义符内部用两个双引"" 表示单个双引，否则出现语法错误 
                using (var cmd = new NpgsqlCommand(@"
CREATE OR REPLACE FUNCTION JPQ (TEXT) RETURNS INT AS
$func$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
	s TEXT;
BEGIN
  FOREACH s IN ARRAY string_to_array($1, '|')
  LOOP
    
		FOREACH js IN ARRAY pgroonga_tokenize(s, 'tokenizer', 'TokenMecab(""use_base_form"", true, ""include_reading"", true)')

        LOOP

            reading = (js-> 'metadata'->> 'reading');
                    IF reading IS NULL THEN
                            RETURN 0;
                    END IF;

                    END LOOP;
                    END LOOP;

                    RETURN 1;

                    END;
$func$ LANGUAGE plpgsql IMMUTABLE;
                    ", conn))
                {
                    cmd.ExecuteNonQuery();
                }

                conn.Close();
            }
        }

        public static string mecab(string sentence)
        {
            string result = "";

            var parameter = new MeCabParam();
            var tagger = MeCabTagger.Create(parameter);

            foreach (var node in tagger.ParseToNodes(sentence))
            {
                if (node.CharType > 0)
                {
                    var features = node.Feature.Split(',');
                    var displayFeatures = string.Join(", ", features);

                    result += $"{node.Surface}\t{displayFeatures}\n";
                }
            }

            return result;
        }


        public static void allfiles(string targetDirectory, List<string> fnames)
        {
            // Process the list of files found in the directory.
            string[] fileEntries = Directory.GetFiles(targetDirectory);
            foreach (string fileName in fileEntries)
                fnames.Add(fileName);

            // Recurse into subdirectories of this directory.
            string[] subdirectoryEntries = Directory.GetDirectories(targetDirectory);
            foreach (string subdirectory in subdirectoryEntries)
                allfiles(subdirectory, fnames);
        }



        public static void importAnime(string ffmpegExe, string animename, string seasion, string frtname, string videoname, string videopath)
        {
            List<string> chinese = new List<string>();
            List<Tuple<string, string>> japanese = new List<Tuple<string, string>>();

            Dictionary<string, string> dic_chs = new Dictionary<string, string>();

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

                var time = arr[0];
                content = arr[1];

                Regex r = new Regex("size=.+>(.+?)</font>");

                string subtitle = "";
                if (r.Match(content).Groups.Count > 0)
                {
                    subtitle = r.Match(content).Groups[1].Value;  // 0 永远是整个串，并不是捕获组。1 才是第一个组
                }
                else
                {
                    content = Regex.Replace(content, "face=\".+?\"", "");
                    content = Regex.Replace(content, "size=\"\\d+\"", "");
                    content = Regex.Replace(content, "color=\".+?\"", "");
                    content = Regex.Replace(content, "<font.+?>", "");
                    content = Regex.Replace(content, "{\\\\an7}", "");

                    subtitle = content;
                }

                subtitle = subtitle.Replace("<b>", "").Replace("</b>", "");

                if (hasHanaQ(subtitle)) // 有jia ming 的是jp
                {
                    japanese.Add(new Tuple<string, string>(subtitle, time));
                }
                else
                {
                    if (unchinese_remove(subtitle).Length > 0)
                    {
                        if (dic_chs.ContainsKey(time))
                        {
                            continue;
                        }

                        dic_chs[time] = subtitle;

                        string beginTime = time.Split(new string[] { "-->" }, StringSplitOptions.None)[0].Trim();
                        string endTime = time.Split(new string[] { "-->" }, StringSplitOptions.None)[1].Trim();
                    }
                }
            }

            japanese = japanese.OrderBy(tu => tu.Item2).ToList<Tuple<string, string>>(); // sort by time asc

            var conn = new NpgsqlConnection("Server=209.141.34.77;Port=5432;Database=anime;User Id=postgres;Password=echodict.com;");
            conn.Open();

            int total = 0;

            foreach (var tu in japanese)
            {
                string j = tu.Item1;
                string zh = "";

                string t = tu.Item2;
                var (begintime, endtime) = parseSrtTime(t);

                if (dic_chs.ContainsKey(t))
                {
                    zh = dic_chs[t];
                }

                var bts = extractAudio(ffmpegExe, videopath, begintime, endtime);


                //string animename = "a";
                //string seasion = "b";
                string tags = mecab(j);
                //string videoname = Path.GetFileName(fname);

                string sql = $"insert into anime(name, seasion, jp, time, jp_mecab, zh, v_zh, videoname, audio, video) values('{animename}', '{seasion}','{j}', '{t}', '{tags}', '{zh}', to_tsvector('jiebacfg', '{zh}'), '{videoname}', @audio, @video);";

                using (var cmd = new NpgsqlCommand(sql, conn))
                {
                    NpgsqlParameter paramAudio = cmd.CreateParameter();
                    paramAudio.ParameterName = "@audio";
                    paramAudio.NpgsqlDbType = NpgsqlTypes.NpgsqlDbType.Bytea;
                    paramAudio.Value = bts;
                    cmd.Parameters.Add(paramAudio);

                    NpgsqlParameter paramVideo = cmd.CreateParameter();
                    paramVideo.ParameterName = "@video";
                    paramVideo.NpgsqlDbType = NpgsqlTypes.NpgsqlDbType.Bytea;
                    paramVideo.Value = bts;
                    cmd.Parameters.Add(paramVideo);


                    cmd.ExecuteNonQuery();
                }

                total += 1;
                Console.WriteLine($"###### {total} / {japanese.Count}");

                //break;
            }

            conn.Close();
        }


        public static Action import = () =>
        {
            /*

             python3.8

                out_bytes = subprocess.check_output([r"ffmpeg", "-y", "-loglevel", "error", "-i", fname, "-map", "0:s:0", frtname])
                out_text = out_bytes.decode('utf-8')

             windows cmd
                ffmpeg -y -i "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" -map 0:s:0 out.srt

             MedallionShell

             */

            // CommandTimeout=0;
            //NpgsqlConnection conn_pool = 


            string ecxutePath = Environment.CurrentDirectory; // 可执行文件运行目录
            string path = new DirectoryInfo("../").FullName;  // 上级目录

            string OS = "";

            if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
            {
                OS = "Windows";
            }
            else if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX))
            {
                OS = "OSX";
            }
            else if (RuntimeInformation.IsOSPlatform(OSPlatform.Linux))
            {
                OS = "Linux";
            }
            else
            {
                Console.WriteLine("##### ERROR:Unkonw OS Type!");
                return;
            }

            Console.WriteLine($"OS: {OS}");


            string host = "209.141.34.77";
            string port = "5432";

            createAnimeDB(host, port);


            var ffmpegExe = @"E:\Program Files\ffmpeg-4.3.2-2021-02-02-full_build\bin\ffmpeg.exe";
            string realroot = @"F:\videos\anime";

            if (OS == "Linux")
            {
                realroot = @"/mnt/videos/anime";
                ffmpegExe = "/usr/bin/ffmpeg";
            }
            if (OS == "OSX")
            {
                realroot = @"/Users/olnymyself/Downloads/videos/anime";
            }

            List<string> fnames = new List<string>();


            allfiles(realroot, fnames);

            fnames = fnames.OrderBy(s => s).ToList();


            string dir = Directory.GetParent(fnames[0]).FullName;
            string dir2 = Directory.GetParent(dir).FullName;
            string dir3 = Directory.GetParent(dir2).FullName;
            string rootorigin = dir;  //# root origin
            string seasion = Path.GetFileName(dir2);
            string animename = Path.GetFileName(dir3);



            int cur = 0;

            foreach (var fname in fnames)
            {
                string videoname = Path.GetFileName(fname);
                string frtname = $"{ecxutePath}/out.srt";


                string srts = extractSRT(ffmpegExe, fname, frtname, ecxutePath);

                importAnime(ffmpegExe, animename, seasion, frtname, videoname, fname);

                cur = cur + 1;

                Console.WriteLine($"one task done.  {cur} / {fnames.Count}");

                //break;
            }

        };

        public async static Task<List<Dictionary<string, string>>> search(string keywd)
        {

           if (!initQ)
            {
                g_conn = new NpgsqlConnection("Server=209.141.34.77;Port=5432;Database=anime;User Id=postgres;Password=echodict.com;MinPoolSize=2;Maximum Pool Size=3;Connection Idle Lifetime=200;Tcp Keepalive = true;Keepalive = 30;");
                initQ = true;
            }

            bool isEn = false;
            bool isCh = false;
            bool isJp = false;

            //keyword = ZhConverter.HansToHant(keyword);  // chs to cht  

            if (chQ(keywd))
            {
                Console.WriteLine("### ch.");
                //keywd = ZhConverter.HansToHant(keywd);  // chs to cht // https://github.com/CosineG/OpenCC.NET
                isCh = true;
            }
            else if (jpQ(keywd))
            {
                Console.WriteLine("### jp.");
                isJp = true;
            }
            else
            {
                Console.WriteLine("### en.");
                isEn = true;
            }

            //var jaconv = new KawazuConverter();

            //JArray ret = new JArray();

            List<Dictionary<string, string>> ret = new List<Dictionary<string, string>>();

            string sql = "";

            if (isJp)
            {
                if (unhana_remove(keywd).Length == keywd.Length)
                {
                    //var converter = new KawazuConverter(); // https://github.com/Cutano/Kawazu
                    //keywd = await converter.Convert(keywd, To.Katakana, Mode.Normal, RomajiSystem.Hepburn, "(", ")");
                }

                sql = $"SELECT id, jp, zh, time FROM anime WHERE jp_mecab &@ '{keywd}' ORDER BY RANDOM() limit 3;";

            }
            else if (isCh)
            {
                sql = $"SELECT id, jp, zh, time FROM anime WHERE v_zh @@  to_tsquery('jiebacfg', '{keywd}') ORDER BY RANDOM() limit 3;";
            }


            if (sql != "")
            {

                g_conn.Open();

                using (var cmd = new NpgsqlCommand(sql, g_conn))
                {
                    NpgsqlDataReader reader = await cmd.ExecuteReaderAsync();
                    if (reader.HasRows)
                    {
                        while (reader.Read())
                        {
                            string id = reader["id"].ToString();
                            string jp = reader["jp"].ToString();
                            string zh = reader["zh"].ToString();
                            string time = reader["time"].ToString();

                            var d = new Dictionary<string, string> { { "id", id }, { "jp", jp }, { "zh", zh }, { "time", time } };

                            ret.Add(d);

                            //JObject jo = new JObject { { "id", id }, { "jp", jp }, { "zh", zh }, { "time", time } };
                        }
                    }
                }

                g_conn.Close();
            }

            return ret;
        }

    }
}
