
// 对所有Components 着色  C++

/*

环境: win10 + vs2019 + opencv3
  
    附加包含目录
        E:\opencv3\opencv\build\include
        E:\opencv3\opencv\build\include\opencv2

    附加库目录
        E:\opencv3\opencv\build\x64\vc15\lib

*/

#include <iostream>
#include <opencv.hpp>
#include <opencv2/imgproc.hpp>

#pragma comment(lib, "opencv_world3414d.lib")  // for debug
//#pragma comment(lib, "opencv_world3414.lib") // for release

using namespace cv;
using namespace std;

int main()
{

    Mat img = cv::imread("small3.jpg", CV_LOAD_IMAGE_COLOR);
    cv::cvtColor(img, img, CV_BGR2GRAY);

    Mat src, src_color, g_src, labels, stats, centroids;
    int num = cv::connectedComponentsWithStats(img, labels, stats, centroids);
    vector<Vec3b> color(num + 1);
    color[0] = Vec3b(0, 0, 0);  //背景色
    for (int m = 1; m <= num; m++) {
        color[m] = Vec3b(rand() % 256, rand() % 256, rand() % 256);
        //if (stats.at<int>(m - 1, CC_STAT_AREA) < 30)
            //color[m] = Vec3b(0, 0, 0);
    }
    src_color = Mat::zeros(img.size(), CV_8UC3);
    for (int x = 0; x < img.rows; x++)
        for (int y = 0; y < img.cols; y++)
        {
            int label = labels.at<int>(x, y);//注意labels是int型，不是uchar.
            src_color.at<Vec3b>(x, y) = color[label];
        }
    imshow("labelMap", src_color);
    cv::waitKey();

    std::cout << "Hello World!\n";
}


