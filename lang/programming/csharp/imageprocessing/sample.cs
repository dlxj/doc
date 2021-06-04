
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
            Cv2.Threshold(src, img_binary, 175, 255, ThresholdTypes.Binary); // 二值化
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


    // 删除过小的非连通对象
    public Mat DeleteSmallComponents(Mat im)
    {
        // https://qiita.com/kaiyu_tech/items/a37fc929ac0f3328fea1

        Mat outputLabels = new Mat();
        Mat stats = new Mat();
        Mat img_color = new Mat();
        Mat centroids = new Mat();

        // 计算所有4 个方向的连通块
        int numberofComponents = Cv2.ConnectedComponentsWithStats(im, outputLabels, stats, centroids, PixelConnectivity.Connectivity4, MatType.CV_32SC1);

        var indexes = stats.Col((int)ConnectedComponentsTypes.Area).SortIdx(SortFlags.EveryColumn);
        var indexer = stats.GetGenericIndexer<int>();

        for (int i = 0; i < indexes.Rows - 1; i++)
        {
            var index = indexes.Get<int>(i);

            var area = indexer[index, (int)ConnectedComponentsTypes.Area];


        }


            Vec3b[] colors = new Vec3b[numberofComponents + 1];

        // 背景色
        colors[0] = new Vec3b(0, 0, 0);

        //Random rand = new Random();
        

        //// 每个连通块随机分配一种不同的颜色
        //for (int i = 1; i <= numberofComponents; i++)
        //{
        //    // 随机产生红绿蓝三个通道的颜色
        //    Byte r = (Byte)(rand.Next(0, 32767) % 256);  // R
        //    Byte g = (Byte)(rand.Next(0, 32767) % 256);  // G
        //    Byte b = (Byte)(rand.Next(0, 32767) % 256);  // B

        //    colors[i] = new Vec3b(r, g, b);
        //}

        ////Area threshold:
        //int minArea = 25 * 25; // px


        //// 面积过小的块用粉色标注
        ////for (int i = 1; i <= numberofComponents; i++)
        ////{

        ////    int blobArea = stats.At<int>(i - 1);

        ////    //apply the area filter:
        ////    if (blobArea < minArea)
        ////    {
        ////        //filter blob below minimum area:
        ////        //small regions are painted with (ridiculous) pink color
        ////        colors[i - 1] = new Vec3b(248, 48, 213);  // cv::Vec3b(0, 0, 0);

        ////    }
        ////}

        //for (int i = 0; i < indexes.Rows; i++)
        //{
        //    var index = indexes.Get<int>(i);

        //    var blobArea = indexer[index, (int)ConnectedComponentsTypes.Area];

        //    if (blobArea < minArea)
        //    {
        //        colors[i + 1] = new Vec3b(248, 48, 213);  // cv::Vec3b(0, 0, 0);
        //    }
        //}



        //// 新建一张彩图
        //Mat color_img = Mat.Zeros(im.Size(), MatType.CV_8UC3);

        //Mat cleaned = im.Clone();

        //for (int x = 0; x < im.Rows; x++)
        //{
        //    for (int y = 0; y < im.Cols; y++)
        //    {
        //        int label = outputLabels.At<int>(x, y);
        //        color_img.At<Vec3b>(x, y) = colors[label];

        //        //if (colors[label] == new Vec3b(248, 48, 213))
        //        //{
        //        //    cleaned.At<Byte>(x, y) = 0;
        //        //}

        //    }
        //}


        //Cv2.ImShow("color", color_img);
        ////Cv2.ImShow("clean", cleaned);
        //Cv2.ImShow("origin", im);
        //Cv2.WaitKey();

        return im;


    }

}
