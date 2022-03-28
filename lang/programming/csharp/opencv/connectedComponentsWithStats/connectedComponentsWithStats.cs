using System;
using System.Collections.Generic;
using OpenCvSharp;

namespace connectedComponentsWithStats
{
    class connectedComponentsWithStats
    {
        static void Main(string[] args)
        {
            Mat img = Cv2.ImRead(@"D:\workcode\csharp\opencv\connectedComponentsWithStats\small3.jpg", ImreadModes.Color);
            Cv2.CvtColor(img, img, ColorConversionCodes.BGR2GRAY);

            var labels = new Mat();
            var stats = new Mat();
            var centroids = new Mat();
            int num = Cv2.ConnectedComponentsWithStats(img, labels, stats, centroids);

            List<Vec3b> color = new List<Vec3b>(num +1);
            color.Add(new Vec3b(0, 0, 0));  //背景色
            Random rd = new Random();
            for (int m = 1; m <= num; m++)
            {
                var c = new Vec3b((byte)(rd.Next(0, 32767) % 256), (byte)(rd.Next(0, 32767) % 256), (byte)(rd.Next(0, 32767) % 256));  // rd.next(0,32767)(生成0~32767之间的随机数，不包括32767)
                color.Add(c); 
                //if (stats.at<int>(m - 1, CC_STAT_AREA) < 30)
                //color[m] = Vec3b(0, 0, 0);
            }

            Mat src_color = Mat.Zeros(img.Size(), MatType.CV_8UC3);

            for (int x = 0; x < img.Rows; x++)
                for (int y = 0; y < img.Cols; y++)
                {
                    int label = labels.At<int>(x, y); //注意labels是int型，不是uchar.
                                                      // 图像总共有 num 个连通块, labels 会告诉你每一个坐标属于哪一个连通块
                    src_color.At<Vec3b>(x, y) = color[label];
                    // color 总共分配了 num + 1 种随机颜色, 每一个连通块都能分到一个随机色 
                }

            Cv2.ImShow("labelMap", src_color);
            Cv2.WaitKey();

            //Console.WriteLine("Hello World!");
        }
    }
}

