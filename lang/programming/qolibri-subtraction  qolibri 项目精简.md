



# qolibri-subtraction  qolibri 项目精简



只留搜索框。并图片回调保持正常



## 先自行编译eblib 安装到 /usr/local/lib



## 原始CMake 的修改



加入：

find_library(EB_LIBRARY eb /usr/local/lib/ REQUIRED)



然后在链接的最后加入：

${EB_LIBRARY}



target_link_libraries(qolibri Qt5::Multimedia Qt5::Network Qt5::WebEngine Qt5::WebEngineWidgets Qt5::Widgets z ${EB_LIBRARY}) # eb















