
/*

step 1: 安装 tesseract-ocr

先安装c++17
yum install centos-release-scl
yu install devtoolset-7-gcc-c++ --enablerepo='centos-sclo-rh'
scl enable devtoolset-7 'bash' # 切换编译器
which gcc

# https://github.com/tesseract-ocr/tessdata/blob/main/chi_sim.traineddata 先下载语言文件
# 自动安装的语言模型很小，不准确

// https://thelinuxcluster.com/2020/02/04/compiling-tesseract-5-0-on-centos-7/
> yum install autoconf automake libtool pkgconfig.x86_64 libpng12-devel.x86_64 libjpeg-devel libtiff-devel.x86_64 zlib-devel.x86_64
# wget http://www.leptonica.org/source/leptonica-1.79.0.tar.gz .
# tar -zxvf leptonica-1.79.0.tar.gz
# cd leptonica-1.79.0
# ./configure --prefix=/usr/local/leptonica-1.79.0
# make
# make install

> export PKG_CONFIG_PATH=/usr/local/leptonica-1.79.0/lib/pkgconfig
$ git clone https://github.com/tesseract-ocr/tesseract.git
$ cd tesseract
$ ./autogen.sh
$ ./configure --prefix=/usr/local/tesseract-5.0 
$ make
$ make install
$ ln -s /usr/local/tesseract-5.0/bin/tesseract /usr/local/bin/
$ tesseract  --version #  成功


复制语言数据 chi_sim.traineddata  eng.traineddata  到目录  /usr/local/tesseract-5.0/share/tessdata

step 2:  npm install tesseractocr string-algorithms fast-levenshtein


*/


(async ()=>{
    
    let tesseract = require('tesseractocr')

    let recognize = tesseract.withOptions({
        psm: 7,
        language: [ 'chi_sim' ],
        config: ['oem=0']
    })
    
    
    // let buffer = Buffer.from(imgData, 'base64')
    
    let tesstext = await recognize('ch_sim.jpg')

    require('fs').writeFileSync('result.txt', tesstext, {encoding:'utf8'})
    
    let a = 1
})()






