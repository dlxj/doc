
using OpenCvSharp;
using System;

class Sample
{
    //// 边缘检测
    //public static void canny()
    //{
    //    // https://blog.csdn.net/zanllp/article/details/79829813
    //    Mat src = new Mat("1.jpg", ImreadModes.Grayscale);
    //    Mat dst = new Mat();

    //    Cv2.Canny(src, dst, 50, 200);
    //    Cv2.ImWrite("2.jpg", dst);

    //    Cv2.ImShow("src image", src);
    //    Cv2.ImShow("dst image", dst);
    //    Cv2.WaitKey();
    //}

    //// 最小外接矩形
    //public static void minAreaRect()
    //{
    //    // https://www.cnblogs.com/little-monkey/p/7429579.html
    //    Mat src = new Mat("minAreaRect.jpg", ImreadModes.Grayscale);
    //    Mat dst = src.Clone();
    //    Cv2.Threshold(src, src, 100, 255, ThresholdTypes.Binary);
    //    Cv2.ImShow("src binary", src);
    //    Cv2.WaitKey();
    //}

   
    //// 透视变换
    //public static void perspectiveTransformation()
    //{
    //    // https://www.cnblogs.com/wj-1314/p/11975977.html
    //    // https://github.com/LeBron-Jian/ComputerVisionPractice



    //}

    // 灰度化
    public Mat Grayize(string path_src)
    {
        using (Mat src = Cv2.ImRead(path_src, ImreadModes.Color))
        using (Mat img_gray = new Mat())
        {
            Cv2.CvtColor(src, img_gray, ColorConversionCodes.BGR2GRAY); // 灰度化
            return img_gray.Clone();
        }
    }

    // 二值化
    public  Mat Binarize(Mat src)
    {
        // https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-1-simple-thresholding/
        using (Mat img_binary = new Mat())
        {
            Cv2.Threshold(src, img_binary, 185, 255, ThresholdTypes.Binary); // 二值化
            return img_binary.Clone();
        }
    }



    // 删除边缘的对象
    public Mat DeleteBorderComponents(Mat src)
    {
        // https://stackoverflow.com/questions/65534370/remove-the-element-attached-to-the-image-border
        using (Mat neg = new Mat())
        using (Mat pad = new Mat())
        {
            Cv2.BitwiseNot(src, neg);  // 反色
            Cv2.CopyMakeBorder(neg, pad, 1, 1, 1, 1, BorderTypes.Constant, 255);  // 上下左右各加一像素
            Size size = pad.Size();
            Mat mask = Mat.Zeros(size.Height + 2, size.Width + 2, MatType.CV_8UC1);  // Mask 图像宽高都比pad 多两像素

            Rect rect_floodfill = new Rect();
            Cv2.FloodFill(pad, mask, new Point(0, 0), 0, out rect_floodfill, 5, 0, FloodFillFlags.Link8);  // 填充

            Mat tmp = pad.Clone(new Rect(2, 2, size.Width - 2, size.Height - 2));  // 宽高前面各加了共两像素，这里减去
            Cv2.BitwiseNot(tmp, tmp);
            return tmp;
        }
    }


    // 去污
    public Mat Clean(Mat im)
    {
        // https://stackoverflow.com/questions/33881175/remove-background-noise-from-image-to-make-text-more-clear-for-ocr?rq=1
        // https://github.com/VahidN/OpenCVSharp-Samples/blob/master/OpenCVSharpSample19/Program.cs  

        // apply Otsu threshold
        Mat bw = new Mat();
        Cv2.Threshold(im, bw, 0, 255, ThresholdTypes.BinaryInv | ThresholdTypes.Otsu);

        // take the distance transform
        Mat dist = new Mat();
        Cv2.DistanceTransform(bw, dist, DistanceTypes.L2, DistanceTransformMasks.Precise);

        // threshold the distance transformed image
        Mat dibw = new Mat();
        double SWTHRESH = 2;    // stroke width threshold
        Cv2.Threshold(dist, dibw, SWTHRESH / 2, 255, ThresholdTypes.Binary);

        //// perform opening, in case digits are still connected
        //Mat kernel = Cv2.GetStructuringElement(MorphShapes.Rect, new Size(3, 3));
        //Mat morph = new Mat();
        //Cv2.MorphologyEx(dibw, morph, MorphTypes.Open, kernel);
        dibw.ConvertTo(dibw, MatType.CV_8UC1);


        //Mat binary = new Mat();
        //Cv2.CvtColor(dibw, binary, ColorConversionCodes.GRAY2BGR);

        //Point[][] contours;
        //HierarchyIndex[] hierarchy;

        //// find contours and filter
        //double HTHRESH = im.Rows / 8;    // height threshold
        //double WTHRESH = HTHRESH;
        //Mat cont = new Mat();
        //morph.ConvertTo(cont, MatType.CV_8UC1);

        //Cv2.FindContours(cont, out contours, out hierarchy, RetrievalModes.CComp, ContourApproximationModes.ApproxSimple, new Point(0, 0));

        //if (contours.Length == 0) throw new Exception("Couldn't find any object in the image.");

        //var contourIndex = 0;
        //while ((contourIndex >= 0))
        //{
        //    var contour = contours[contourIndex];
        //    Rect rect = Cv2.BoundingRect(contour); //Find bounding rect for each contour

        //    // 可能是中文字符
        //    if (rect.Height > HTHRESH && rect.Width > WTHRESH)
        //    {
        //        Cv2.Rectangle(binary, new Point(rect.X, rect.Y), new Point(rect.X + rect.Width - 1, rect.Y + rect.Height - 1), new Scalar(0, 0, 255), 1);
        //    }

        //    contourIndex = hierarchy[contourIndex].Next;
        //}

        Cv2.BitwiseNot(dibw, dibw);

        return dibw;
    }


    // 定位中文字符
    public Mat FindChinesecharacter(Mat i)
    {
        Mat im = i.Clone();
        Cv2.BitwiseNot(im, im);

        // perform opening, in case digits are still connected
        Mat kernel = Cv2.GetStructuringElement(MorphShapes.Rect, new Size(3, 3));
        Mat morph = new Mat();
        Cv2.MorphologyEx(im, morph, MorphTypes.Open, kernel);

        Mat binary = new Mat();
        Cv2.CvtColor(im, binary, ColorConversionCodes.GRAY2BGR);

        Point[][] contours;
        HierarchyIndex[] hierarchy;

        // find contours and filter
        double HTHRESH = im.Rows / 8;    // height threshold
        double WTHRESH = HTHRESH;
        Mat cont = new Mat();
        morph.ConvertTo(cont, MatType.CV_8UC1);

        Cv2.FindContours(cont, out contours, out hierarchy, RetrievalModes.CComp, ContourApproximationModes.ApproxSimple, new Point(0, 0));

        if (contours.Length == 0) throw new Exception("Couldn't find any object in the image.");

        var contourIndex = 0;
        while ((contourIndex >= 0))
        {
            var contour = contours[contourIndex];
            Rect rect = Cv2.BoundingRect(contour); //Find bounding rect for each contour

            // 可能是中文字符
            if (rect.Height > HTHRESH && rect.Width > WTHRESH)
            {
                // 绘制矩形
                Cv2.Rectangle(binary, new Point(rect.X, rect.Y), new Point(rect.X + rect.Width - 1, rect.Y + rect.Height - 1), new Scalar(0, 0, 255), 1);
            }

            contourIndex = hierarchy[contourIndex].Next;
        }

        return binary;
    }


    // 删除过小的对象
    public Mat DeleteSmallComponents(Mat im)
    {

        // https://qiita.com/kaiyu_tech/items/a37fc929ac0f3328fea1

        Cv2.BitwiseNot(im, im);  // 反色

        var labels = new Mat();
        var stats = new Mat();
        var centroids = new Mat();
        var count = Cv2.ConnectedComponentsWithStats(im, labels, stats, centroids, PixelConnectivity.Connectivity8, MatType.CV_32SC1);

        var indexes = stats.Col((int)ConnectedComponentsTypes.Area).SortIdx(SortFlags.EveryColumn);


        var indexer = stats.GetGenericIndexer<int>();

        var output = im.CvtColor(ColorConversionCodes.GRAY2BGR);


        // 遍历每一个像素
        for (int x = 0; x < im.Rows; x++)
        {
            for (int y = 0; y < im.Cols; y++)
            {

                int label = labels.At<int>(x, y);

                if (label == 0)
                {
                    // 是背景对象，跳过
                    continue;
                }

                var area = indexer[label, (int)ConnectedComponentsTypes.Area];

                var rect = new Rect
                {
                    X = indexer[label, (int)ConnectedComponentsTypes.Left],
                    Y = indexer[label, (int)ConnectedComponentsTypes.Top],
                    Width = indexer[label, (int)ConnectedComponentsTypes.Width],
                    Height = indexer[label, (int)ConnectedComponentsTypes.Height]
                };

                // 所处的连通块面积过小则删除（变成背景色）
                if (area < 20)
                {
                    im.At<Byte>(x, y) = 0;
                }
            }
        }

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

            // 绘制矩形
            if (area < 20)
            {
                output.Rectangle(rect, Scalar.Blue);
            }
            //else
            //{
            //    output.Rectangle(rect, Scalar.Red);
            //}
        }


        Cv2.BitwiseNot(im, im);

        return im;

    }


    // 去除黑边后的矩形区域

    public Rect DeBoardRect(Mat t)
    {

        Sample sample = new Sample();

        Mat im = sample.Binarize(t);  // 二值化
        im = sample.DeleteBorderComponents(im);  // 删除边缘对象

        im = sample.DeleteSmallComponents(im);  // 删除面积过小的像素点

        //im = sample.Binarize(im);

        // 遍历每一个像素
        for (int x = 0; x < im.Rows; x++)
        {
            for (int y = 0; y < im.Cols; y++)
            {
                // Point p(x, y); 第几行第几列
                // At(y, x) 第几行第几列
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

            if (count > 0)
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
            Height = im.Rows - (Y + (im.Rows - Y2))
        };

        return rect;
    }


    //  // rect 矩形区域以外全部变白
    public Mat Whited(Mat t, Rect rect)
    {
        for (int x = 0; x < t.Cols; x++)  // x 第几列
        { 
            for (int y = 0; y < t.Rows; y++)  // y 第几行
            {
                bool whiteQ = true;

                if (x >= rect.X && x <= rect.X + rect.Width)
                {
                    if ( y >= rect.Y && y<= rect.Y + rect.Height )
                    {
                        whiteQ = false;  // 矩形区域以内的像素保留
                    }
                }

                if (whiteQ)
                {
                    t.At<Byte>(y, x) = 255;   // 矩形区域以外的像素变白
                }

            }
        }

        return t;
    }
}
