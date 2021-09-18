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
            string[] files = Directory.GetFiles(@"F:\数字化_21ZJ75_2021年中级职称资格考试应试指导 药学中级_20210430\扫描\正文\灰阶", "*.bmp", SearchOption.AllDirectories);
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



            Vec3b[] colors = new Vec3b[count + 1];

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

        // 透视变换
        static void demo2()
        {
            // https://github.com/shimat/opencvsharp/blob/c925abadf53cc82396c4be2bbfe839c773235113/test/OpenCvSharp.Tests/calib3d/Calib3dTest.cs
            // https://www.youtube.com/watch?v=ZZ5M7Q5ZWX4
            // https://www.gitmemory.com/issue/shimat/opencvsharp/1093/739471217


            string impath = @"D:\workcode\csharp\imageprocessing\dot_Bobbin_img.png";

            var src = new Mat(impath, ImreadModes.Grayscale);

            var patternSize = new Size(18, 13);

            var centers = new Mat();
            var found = Cv2.FindCirclesGrid(src, patternSize, centers, FindCirclesGridFlags.SymmetricGrid);

            var points_img = new Mat();
            Cv2.CvtColor(src.Clone(), points_img, ColorConversionCodes.GRAY2BGR);

            Cv2.DrawChessboardCorners(points_img, patternSize, centers, true);


            int left_margin = 26;
            int top_margin = 18;
            int interval = 44;

            var object_points = new Mat<Point3f>(patternSize.Height * patternSize.Width, 1);
            Point3f[] arr = new Point3f[patternSize.Height * patternSize.Width];


            for (int j = 0; j < patternSize.Height; j++)
            {
                for (int i = 0; i < patternSize.Width; i++)
                {

                    Point3f p = new Point3f(left_margin + i * interval, top_margin + j * interval, 0);

                    arr.SetValue(p, j * patternSize.Width + i);

                }
            }

            object_points.SetArray(arr);

            var imageSize = src.Size();

            var cameraMatrix = new Mat<double>(3, 3);
            var distCoeffs = new Mat<double>(5, 1);

            Cv2.CalibrateCamera(new[] { object_points }, new[] { centers }, imageSize, cameraMatrix, distCoeffs, out Mat[] rvecs, out Mat[] tvecs);

            var newImageSize = new Size();
            var newCameraMatrix = Cv2.GetOptimalNewCameraMatrix(cameraMatrix, distCoeffs, imageSize, 1, newImageSize, out Rect validPixROI);

            var data = new Mat(impath, ImreadModes.Grayscale);

            var temp_img = new Mat();
            Cv2.Undistort(data, temp_img, cameraMatrix, distCoeffs, newCameraMatrix);

            var rotation = new Mat();
            Cv2.Rodrigues(rvecs[0], rotation);

            var transRot = new Mat<double>(3, 3);
            rotation.Col(0).CopyTo(transRot.Col(0));
            rotation.Col(1).CopyTo(transRot.Col(1));

            var transData = new double[3, 3] { { 0, 0, tvecs[0].At<double>(0) }, { 0, 0, tvecs[0].At<double>(1) }, { 0, 0, tvecs[0].At<double>(2) } };
            var translate = InputArray.Create(transData).GetMat();
            translate.Col(2).CopyTo(transRot.Col(2));

            var dst_img = new Mat();
            var m = newCameraMatrix * transRot;
            Cv2.WarpPerspective(temp_img, dst_img, m, newImageSize, InterpolationFlags.WarpInverseMap);


            Cv2.ImShow("src", src);

            Cv2.ImShow("points", points_img);

            Cv2.ImShow("temp", temp_img);

            Cv2.ImShow("dst", dst_img);
            Cv2.WaitKey();
        }


        // 去黑边后确定主体内容的边界
        static void demo3()
        {
            //largeborder_clean.jpg

            Sample sample = new Sample();
            Mat t = sample.Grayize(@"D:\workcode\csharp\大边框原图.jpg");  // 以灰度图加载

            Rect ret = sample.DeBoardRect(t);

            Mat noboard = sample.Whited(t, ret);

            Cv2.ImShow("after_noboard", noboard);
            Cv2.WaitKey();

            //Mat noboard = t.Clone(rect);
            Cv2.ImWrite(@"D:\workcode\csharp\noboard.jpg", noboard);



            Mat im = sample.Binarize(t);  // 二值化
            im = sample.DeleteBorderComponents(im);  // 删除边缘对象

            im = sample.DeleteSmallComponents(im);  // 删除面积过小的像素点

            im = sample.Binarize(im);

            var output = im.CvtColor(ColorConversionCodes.GRAY2BGR);

            Cv2.ImShow("after_clean", im);
            Cv2.WaitKey();

            // 遍历每一个像素
            for (int x = 0; x < im.Rows; x++)
            {
                for (int y = 0; y < im.Cols; y++)
                {
                    // Point p(x, y); 第几行第几列
                    // At(y, x) 第几列第几行
                    // Rect(X=y, Y=x) 第几列第几行
                    // 注意这两个传参的顺序是不一样的
                    int pixel = im.At<Byte>(y, x);

                    if (pixel == 255)  // 未反色前255 是白色
                    {
                        //im.At<Byte>(y, x) = 135;  // 纯白全部变成一个特定的灰色

                    } 
                }
            }

            int X = 0;
            // 从左向右移动，条件是这一整列的像素几乎都是0
            for (int x = 0; x < im.Cols; x++)  // x 代表的是第几列
            {
                double count = 0;

                for (int y = 0; y < im.Rows; y++)  // y 代表的是第几行
                {
                    int pixel = im.At<Byte>(y, x);
                    if (pixel != 255)
                    {
                        count++;  // 计算这一列有多少个非纯白像素点
                    }
                }

                double percent = count / im.Cols;

                if(count > 0)
                {
                    X = x;
                    break;
                }

            }


            int X2 = im.Cols;
            // 从右向左移动，条件是这一整列的像素几乎都是0
            for (int x = im.Cols - 1; x >= 0; x--)  // x 代表的是第几列
            {
                double count = 0;

                for (int y = 0; y < im.Rows; y++)  // y 代表的是第几行
                {
                    int pixel = im.At<Byte>(y, x);
                    if (pixel != 255)
                    {
                        count++;  // 计算这一列有多少个非0 像素点
                    }
                }

                if (count > 0.01)
                {
                    X2 = x;
                    break;
                }

            }


            int Y = 0;
            // 从上向下移动，条件是这一整行的像素几乎都是0
            for (int y = 0; y < im.Rows; y++)  // y 代表的是第几行
            {
                double count = 0;

                if (y == 268)
                {

                }

                for (int x = 0; x < im.Cols; x++) // x 代表的是第几列
                {
                    int pixel = im.At<Byte>(y, x);
                    if (pixel != 255)
                    {
                        count++;  // 计算这一列有多少个非纯白像素点
                    }
                }

                if (count > 0)
                {
                    Y = y;
                    break;
                }
            }


            int Y2 = im.Rows;
            // 从下向上移动，条件是这一整行的像素几乎都是0
            for (int y = im.Rows - 1; y >= 0; y--)  // y 代表的是第几行
            {
                double count = 0;

                for (int x = 0; x < im.Cols; x++) // x 代表的是第几列
                {
                    int pixel = im.At<Byte>(y, x);
                    if (pixel != 255)
                    {
                        count++;  // 计算这一行有多少个非0 像素点
                    }
                }

                if (count > 0)
                {
                    Y2 = y;
                    break;
                }
            }


            // 宽度 = 有多少列 im.Cols
            // 高度 = 有多少行 im.Rows
            // x in im.Cols 是 第几列
            // y in im.Rows 是 第几行

            var rect = new Rect
            {
                X = X,
                Y = Y,
                Width = im.Cols - (X + (im.Cols - X2)),
                Height = im.Rows - (Y + ( im.Rows - Y2 ))
            };


            // 绘制矩形
            output.Rectangle(rect, Scalar.Red);

            Cv2.ImShow("after_rected", output);
            Cv2.WaitKey();

            Cv2.ImWrite(@"D:\workcode\csharp\after_rected.jpg", output);


        }

        static void Main(string[] args)
        {
            demo3();

            Sample sample = new Sample();
            //Mat t = sample.Grayize(@"D:\workcode\csharp\imageprocessing\largeborder.bmp");  // 以灰度图加载

            Mat t = sample.Grayize(@"D:\workcode\csharp\6015.bmp");

            t = sample.Binarize(t);  // 二值化
            t = sample.DeleteBorderComponents(t);  // 删除边缘对象

            //t = sample.DeleteSmallComponents(t);  // 删除面积过小的像素点

            Cv2.ImShow("cleaned", t);


            Cv2.ImWrite(@"D:\workcode\csharp\largeborder_clean.jpg", t);


            //demo();
            //demo2();




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


            //Mat jj = sample.Grayize(@"D:\workcode\csharp\imageprocessing\small.jpg");
            //Mat j = jj.Clone();
            //j = sample.DeleteSmallComponents(j); // 删除边缘对象


            // 预处理图片并保存
            var paths = bmp_paths();
            foreach (var path in paths)
            {
                var src = path.Item1;
                var dst = path.Item2;


                Mat tmp = sample.Grayize(src);  // 以灰度图加载
                tmp = sample.Binarize(tmp);  // 二值化
                tmp = sample.DeleteBorderComponents(tmp);  // 删除边缘对象

                tmp = sample.DeleteSmallComponents(tmp);  // 删除面积过小的像素点



                Mat im = tmp.Clone();


                Cv2.BitwiseNot(im, im);  // 反色

                var labels = new Mat();
                var stats = new Mat();
                var centroids = new Mat();
                var count = Cv2.ConnectedComponentsWithStats(im, labels, stats, centroids, PixelConnectivity.Connectivity8, MatType.CV_32SC1);

                var indexes = stats.Col((int)ConnectedComponentsTypes.Area).SortIdx(SortFlags.EveryColumn);


                var indexer = stats.GetGenericIndexer<int>();

                Cv2.BitwiseNot(im, im);
                var output = im.CvtColor(ColorConversionCodes.GRAY2BGR);


                bool flag = false;

                //List<Mat> mats = new List<Mat>();

                // 遍历每一个连通块
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

                    if (area <= 50)
                    {
                        continue;
                    }

                    double ratio = (double)rect.Width / rect.Height;
                    if (ratio >= 0.8 && ratio <= 1.2)
                    {
                        // 宽高比接近 1:1 ，可能是中文字符
                        double rt = (double)rect.Width / im.Cols;
                        if (rt >= 1.0 / 100 && rt <= 1.0 / 50)
                        {
                            // 绘制矩形，把中文框出来
                            output.Rectangle(rect, Scalar.Red);
                            flag = true;


                            string zh_path = @"F:\zhs\" + Path.GetFileName(dst) + i.ToString() + ".jpg";
                            Cv2.ImWrite(zh_path, im.Clone(rect));

                            //mats.Add(im.Clone(rect));
                        }

                    }
                }

                if (flag)
                {
                    Cv2.ImWrite(dst, output);
                }


            }

        }


    }
}
