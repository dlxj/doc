using System;
using OpenCvSharp;
using SixLabors.ImageSharp;
using System.IO;
using Newtonsoft.Json.Linq;
using System.Linq;
using System.Text.Json.Serialization;
using System.Text.Json;

namespace paiban
{
    class Program
    {
        //
        // 对阿里云OCR 返回的结果进行重新排版 https://ocrapi-advanced.taobao.com/ocrservice/advanced
        //
        public static string paiban(string strAliyunOCRJson, Tuple<OpenCvSharp.Point, OpenCvSharp.Point> points = null)
        {

            // 图片的左上角坐标，右下角坐标

            OpenCvSharp.Point p1;
            OpenCvSharp.Point p2;


            string strJson = strAliyunOCRJson;

            JObject jObj = JObject.Parse(strJson);

            //JToken statusJtoken = jObj["status"];

            //var status = statusJtoken.ToString();

            //string content = jObj["data"]["content"].ToString();

            //string content = jObj.ToString();

            // 所有识别出的文字内容，中间的空格字符用于表示空白符，但是并不知道它应该是空格还是换行
            //var arr = content.Split(' ');

            //string ori_results = string.Join("\n", arr);

            // 图片宽高
            //int weight = Convert.ToInt32(jObj["data"]["width"].ToString());
            //int height = Convert.ToInt32(jObj["data"]["height"].ToString());

            int weight = Convert.ToInt32(jObj["width"].ToString());
            int height = Convert.ToInt32(jObj["height"].ToString());

            if (points == null)
            {
                p1 = new OpenCvSharp.Point(0, 0);
                p2 = new OpenCvSharp.Point(weight, height);
            }
            else
            {
                p1 = points.Item1;
                p2 = points.Item2;
            }

            string result = "";

            int lastY = 999999;

            int firstX = 0;

            //JArray wordsInfo = JArray.Parse(jObj["data"]["prism_wordsInfo"].ToString());

            JArray wordsInfo = JArray.Parse(jObj["prism_wordsInfo"].ToString());


            int leftest = 999999;
            // 先找出最左边的字符x 坐标
            for (int j = 0; j < wordsInfo.Count(); j++)
            {
                var jo = wordsInfo[j];

                var charInfo = jo["charInfo"];
                for (int i = 0; i < charInfo.Count(); i++)
                {
                    var joc = charInfo[i];
                    var c = joc["word"].ToString();
                    var cx = Convert.ToInt32(joc["x"].ToString());
                    var cy = Convert.ToInt32(joc["y"].ToString());
                    var cw = Convert.ToInt32(joc["w"].ToString());

                    if (cx < leftest)
                    {
                        leftest = cx;
                    }
                }
            }


            for (int j = 0; j < wordsInfo.Count(); j++)
            {
                var jo = wordsInfo[j];

                string word = jo["word"].ToString();

                var pos = jo["pos"]; // 四个角的位置

                var x = Convert.ToInt32(pos[0]["x"].ToString()); // 左上
                var y = Convert.ToInt32(pos[0]["y"].ToString());

                //
                //处理同一行的字符要不要加空格（一个字符一个字符的检查x 坐标，确定它们之间是不是有空格）
                //
                int lastx_mini = 0;  // 下一个字符x 坐标的下界（肯定不小于这个值）
                int prew = 0; // 上一个字符的宽度
                var words = "";
                var charInfo = jo["charInfo"];
                //foreach (JObject joc in charInfo)
                for (int i = 0; i < charInfo.Count(); i++)
                {
                    var joc = charInfo[i];
                    var c = joc["word"].ToString();
                    var cx = Convert.ToInt32(joc["x"].ToString());
                    var cy = Convert.ToInt32(joc["y"].ToString());
                    var cw = Convert.ToInt32(joc["w"].ToString());


                    // 只要指定矩形范围内的字符

                    if (cx < p1.X || cx > p2.X)
                    {
                        continue;
                    }

                    if (cy < p1.Y || cy > p2.Y)
                    {
                        continue;
                    }


                    if (j == 0)
                    {
                        // 记录第一个字符的x 坐标

                        firstX = cx;

                    }

                    if (i == 0)
                    {
                        //首字符缩进

                        if (y - lastY >= 50 || j == 0)  // Y 坐标相差太大的不是同一行
                        {
                            int ns = Convert.ToInt32((cx - leftest) / 50.0);
                            for (int k = 0; k < ns; k++)
                            {
                                words += " ";
                            }
                        }
                    }

                    if (cx - lastx_mini < 40) // 如果这个字符的x 坐标和坐标下界的宽度相差不多，那么中间没有空格
                    {
                        words = words + c;
                    }
                    else
                    {
                        if (i == 0)
                        {
                            words = words + c;
                        }
                        else
                        {
                            words = words + "  " + c;

                        }
                    }

                    prew = cw;
                    lastx_mini = cx + cw;
                }


                //
                // 处理可能不是可一行的文本之间要不要加入换行
                //
                if (y - lastY < 50) // Y 坐标相差不大的是同一行
                {
                    if (result == "")
                    {
                        result += words;
                    }
                    else
                    {
                        result += "  " + words; //+ word;
                    }
                }
                else
                {
                    // 换行
                    result = result + "\n" + words; //+ word;
                }

                lastY = y;


            }


            return result;

        }

        static void Main(string[] args)
        {
            // D:\workcode\nodejs\OCR_修正英文定位框\json\feef2b5d91b07e7e0b2599f22bbf30a8.json

            var path = @"D:\workcode\nodejs\OCR_修正英文定位框\data\json\feef2b5d91b07e7e0b2599f22bbf30a8.json";

            string strjson = null;
            using (StreamReader r = new StreamReader(path, System.Text.Encoding.UTF8))
            {
                strjson = r.ReadToEnd();
            }

            string text = paiban(strjson);

            Console.WriteLine(text);
        }
    }
}
