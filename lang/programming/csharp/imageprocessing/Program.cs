using System;
using System.Collections.Generic;
using System.IO;

using OpenCvSharp;

namespace horizontalLine
{
    class Program
    {

        static List<Tuple<string, string>> bmp_paths()
        {
            string[] files = Directory.GetFiles(@"F:\xxxxxxxxxxxxxx", "*.bmp", SearchOption.AllDirectories);
            List<Tuple<string, string>> paths = new List<Tuple<string, string>>();

            foreach (string path_src in files)
            {
                string path_dst = Path.Join(@"F:\out", Path.GetFileName(path_src));
                paths.Add(new Tuple<string, string>(path_src, path_dst));
            }
            return paths;
        }


        // 卷积、连通面积、小对象着色
        static void demo()
        {
            var src = new Mat(@"D:\workcode\csharp\imageprocessing\data.png", ImreadModes.Grayscale);

            float[,] filterX = { { 0,  0, 0 },
                     { 0, -1, 1 },
                     { 0,  0, 0 },
};

            float[,] filterY =  { { 0,  0, 0 },
                      { 0, -1, 0 },
                      { 0,  1, 0 },
};

            var filter2D = new Mat();

            Cv2.Filter2D(src, filter2D, MatType.CV_32FC1, InputArray.Create(filterX));
            Cv2.Filter2D(filter2D, filter2D, MatType.CV_32FC1, InputArray.Create(filterY));

            filter2D = Cv2.Abs(filter2D);

            Cv2.Normalize(filter2D, filter2D, 0, 255, NormTypes.MinMax, MatType.CV_8UC1);

            Cv2.Threshold(filter2D, filter2D, 1, 255, ThresholdTypes.Binary);



            byte[,] element1 = { { 0, 0, 1 },
                     { 0, 1, 0 },
                     { 1, 0, 0 },
};

            Cv2.MorphologyEx(filter2D, filter2D, MorphTypes.Close, InputArray.Create(element1));

            byte[,] element2 = { { 1, 0 },
                     { 0, 1 },
};

            Cv2.MorphologyEx(filter2D, filter2D, MorphTypes.Close, InputArray.Create(element2));

            var labels = new Mat();
            var stats = new Mat();
            var centroids = new Mat();
            var count = Cv2.ConnectedComponentsWithStats(filter2D, labels, stats, centroids, PixelConnectivity.Connectivity8, MatType.CV_32SC1);

            var indexes = stats.Col((int)ConnectedComponentsTypes.Area).SortIdx(SortFlags.EveryColumn);
            

            var indexer = stats.GetGenericIndexer<int>();

            var output = filter2D.CvtColor(ColorConversionCodes.GRAY2BGR);

            for (int i = 0; i < indexes.Rows - 1; i++)
            {
                var index = indexes.Get<int>(i);

                var area = indexer[index, (int)ConnectedComponentsTypes.Area];

                var rect = new Rect
                {
                    X = indexer[index, (int)ConnectedComponentsTypes.Left],
                    Y = indexer[index, (int)ConnectedComponentsTypes.Top],
                    Width = indexer[index, (int)ConnectedComponentsTypes.Width],
                    Height = indexer[index, (int)ConnectedComponentsTypes.Height]
                };

                if (area < 8)
                {
                    output.Rectangle(rect, Scalar.Blue);
                }
                else
                {
                    output.Rectangle(rect, Scalar.Red);
                }
            }



            Vec3b[] colors = new Vec3b[ count + 1 ];

            // 背景色，对应的label 是 0，总共有 count 个label
            colors[0] = new Vec3b(0, 0, 0);

            // 每个连通块随机分配一种不同的颜色
            for (int i = 1; i <= count; i++)
            {
                // 随机生成红、绿、蓝 三个通道的颜色
                Random rand = new Random();
                Byte r = (Byte)(rand.Next(0, Int32.MaxValue) % 256);
                Byte g = (Byte)(rand.Next(0, Int32.MaxValue) % 256);
                Byte b = (Byte)(rand.Next(0, Int32.MaxValue) % 256);

                colors[i] = new Vec3b(r, g, b);
            }


            // 新建一张彩图
            Mat color_img = Mat.Zeros(output.Size(), MatType.CV_8UC3);

            for (int x = 0; x < output.Rows; x++)
            {
                for (int y = 0; y < output.Cols; y++)
                {

                    int label = labels.At<int>(x, y);
                    color_img.At<Vec3b>(x, y) = colors[label];

                    if (label != 0)
                    {
                        var area = indexer[label, (int)ConnectedComponentsTypes.Area];

                        // small regions are painted with (ridiculous) pink color
                        if (area < 8)
                        {
                            color_img.At<Vec3b>(x, y) = new Vec3b(248, 48, 213);
                        }
                    }

                }
            }

            Cv2.ImShow("color_img", color_img);
            Cv2.ImShow("filter2D", filter2D);
            Cv2.ImShow("output", output);
            Cv2.WaitKey();

        }


        static void Main(string[] args)
        {
            demo();

            Sample sample = new Sample();

            //Mat ii = sample.Grayize(@"D:\workcode\csharp\imageprocessing\booktitle.jpg");
            //Mat i = ii.Clone();
            //i = sample.DeleteBorderComponents(i); // 删除边缘对象
            //i = sample.Binarize(i);  // 二值化
            //i = sample.Clean(i);     // 去污

            //Mat signed = sample.FindChinesecharacter(i);

            //Cv2.ImShow("origin", ii);  // 原图
            //Cv2.ImShow("cleaned", i);  // 清理后
            //Cv2.ImShow("signed", signed); // 标记中文字符
            //Cv2.WaitKey();


            Mat jj = sample.Grayize(@"D:\workcode\csharp\imageprocessing\small.jpg");
            Mat j = jj.Clone();
            j = sample.DeleteSmallComponents(j); // 删除边缘对象


            // 预处理图片并保存
            var paths = bmp_paths();
            foreach (var path in paths)
            {
                var src = path.Item1;
                var dst = path.Item2;
                
                Mat tmp = sample.Grayize(src);  // 以灰度图加载

                tmp = sample.DeleteBorderComponents(tmp);  // 删除边缘对象

                tmp = sample.Binarize(tmp);  // 二值化

                Cv2.ImWrite(dst, tmp);

            }

        }


    }
}
