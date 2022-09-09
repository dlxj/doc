
import numpy as np
import cv2


def DeleteBorderComponents():

    # img = cv2.imread("t.png")
    img = cv2.imdecode(np.fromfile('./5.jpg', dtype=np.uint8), -1)
    img_copy = img.copy()
    cv2.bitwise_not(img_copy, img_copy)

    cv2.imshow("box", img_copy)
    cv2.waitKey(0)

    h, w = img_copy.shape[:2]

    # convert to gray
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

    

    # add 1 pixel white border all around
    pad = cv2.copyMakeBorder(gray, 1,1,1,1, cv2.BORDER_CONSTANT, value=255)
    h, w = pad.shape

    # create zeros mask 2 pixels larger in each dimension
    mask = np.zeros([h + 2, w + 2], np.uint8)

    # floodfill outer white border with black
    img_floodfill = cv2.floodFill(pad, mask, (0,0), 0, (5), (0), flags=8)[1]

    # remove border
    img_floodfill = img_floodfill[1:h-1, 1:w-1]    

    # save cropped image
    # cv2.imwrite('lungs_floodfilled.png',img_floodfill)

    # show the images
    cv2.imshow("img_floodfill", img_floodfill)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # if len(img_copy.shape) > 2:
    #     img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

    # cv2.bitwise_not(img, img_copy)

    # pad = cv2.copyMakeBorder(img_copy, 1,1,1,1, cv2.BORDER_CONSTANT, None, 255) # 上下左右各加一像素

    # height, width = pad.shape[:2]

    # mask = np.zeros((height + 2, width + 2), np.uint8)

    # # cv2.FLOODFILL_MASK_ONLY

    #             # Cv2.FloodFill(pad, mask, new Point(0, 0), 0, out rect_floodfill, 5, 0, FloodFillFlags.Link8);  // 填充


    # cv2.floodFill(pad, mask, (0, 0), 255)



    # cv2.imshow("box", pad)
    # cv2.waitKey(0)

def DeleteBorderComponentsv2():
    img = cv2.imdecode(np.fromfile('./5.jpg', dtype=np.uint8), -1)
    img_copy = img.copy()
    cv2.bitwise_not(img_copy, img_copy)

    cv2.imshow("box", img_copy)
    cv2.waitKey(0)

# DeleteBorderComponents()

"""
// C++

void DeleteBorderComponents(Mat& im) {

    Mat neg;
    cv::bitwise_not(im, neg);  // 反色

    Mat pad;

    cv::copyMakeBorder(neg, pad, 1,1,1,1, cv::BorderTypes::BORDER_CONSTANT, 255); // 上下左右各加一像素

    Size size = pad.size();
    Mat mask = Mat::zeros(size.height + 2, size.width + 2, CV_8UC1);  // Mask 图像宽高都比pad 多两像素


    cv::floodFill(pad, mask, Point(0, 0), cv::Scalar(0), 0, cv::Scalar(), cv::Scalar(), 8); // 填充

   
    cv::Rect r(2, 2, size.width - 2, size.height - 2);
    Mat tmp = pad(r).clone();

    cv::bitwise_not(tmp, tmp);
    
    imshow("cleaned", tmp);
    cv::waitKey();
}
"""
