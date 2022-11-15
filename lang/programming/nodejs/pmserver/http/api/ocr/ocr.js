const request = require('request');
const fs = require('fs');
const path = require('path')

let ocr_img_dir = global.config.ocr_img_dir

module.exports =
{
  name: `调用阿里云OCR识别图片`,
  author: `wqb`,
  params: {
    md5: {
      type: 'string',
      remark: '源文件MD5码 注意不是压缩后的文件MD5码'
    },
    imgData: {
      type: `string`,
      remark: `图片base64数据`
    },
    userID: {
      type: 'number',
      remark: '用户ID'
    },
    bookNO: {
      type: `string`,
      remark: `图书编号`,
      default:''
    },
    imgName: {
      type: `string`,
      remark: `图片名（需要存到'扫描'文件夹里）`,
      default:''
    },
    originImgData: {
      type: `string`,
      remark: `原始图片base64数据`,
      default:''
    },
  },
  async handler({ md5, imgData, __ip__, userID, bookNO, imgName, originImgData }) {

    // if (userID == null || userID == undefined || userID == '') {
    //   throw `Error: ocr userID is empty! ${userID} ${__ip__}`
    // }

    // //识别结果JSON存储路径
    // const jsonPath = `${global.config.dataPath}/json/${md5}.json`;
    // //识别图片的存储位置
    // const imgPath = `${global.config.dataPath}/img/${md5}.txt`;

    // let rows = await this.dbs.ocrDB.imgs.get.query({ "md5": md5 });
    // let rows_temp = await this.dbs.ocrDB.imgs.get_temp.query({ "md5": md5 });  // 查临时表（ base64 已被替换成 [xxx.gif] ）


    // if (rows_temp.length > 0 &&  rows_temp[0]['content'] != null && rows_temp[0]['content'] != '' ) {
    //   // 用文件夹里的图片替换 img_context 里的base64
    //   let [rows_new, rows_temp_new, ms_replaceBase64] = this.libs.img.base64img.replaceBase64(rows, rows_temp)
    //   if (rows_new === null || rows_temp_new === undefined ) {
    //     //return this.msg(201, {data:ms_replaceBase64})
    //     console.log(`Warning: 用文件夹里的图片替换 img_context 里的base64 但是图片不存在 ${ms_replaceBase64} MD5:${md5}`)
    //   } else {
    //     rows = rows_new
    //     rows_temp = rows_temp_new
    //   }

    // }

    // //已经有历史识别结果
    // if ( rows.length > 0) {
    //   //const retJson = fs.readFileSync(jsonPath).toString();

    //   let retJson = null

    //   if (fs.existsSync( jsonPath )) {

    //     retJson = fs.readFileSync(jsonPath, {encoding:'utf-8'})

    //     return this.msg(200,
    //     {
    //       //教研已经保存的内容 HTML （有HTML的前端已经用HTML直接还原）
    //       content: rows[0]['content'],
    //       //阿里识别的结果
    //       firstResult: JSON.parse(retJson),
    //       //教研已经保存的内容JSON
    //       saveContent: rows[0]['saveContent'] != '' && rows[0]['saveContent'] != null ? JSON.parse(rows[0]['saveContent']) : '',
    //       submitTime: rows[0]['submitTime'],
    //       createUserID: rows[0]['createUserID'],
    //       updateUserID: rows[0]['updateUserID'],
    //       lastUpdateTime: rows[0]['lastUpdateTime'],
    
    //       content_temp: rows_temp[0]['content'],
    //       saveContent_temp: rows_temp[0]['saveContent'] != '' && rows_temp[0]['saveContent'] != null ? JSON.parse(rows_temp[0]['saveContent']) : ''
    //     });

    //     } else {

    //       console.log(`Warning: 已经有历史识别结果但识别结果JSON不存在! ${jsonPath}`)

    //     }
        
    // }

    // if (imgData == 'hasTest') {
    //   return this.msg(201, '无识别结果');
    // }

    // // 讯飞识别结果
    // // let data2 = await this.services.img.xfOCR( { md5, imgData } )

    // // let data2 = await this.services.img.xfocrGeneral( { md5, imgData } )  // 通用文字识别

    // // https://help.aliyun.com/document_detail/294540.html 阿里云ocr结果字段定义
    //     // prism-wordsInfo 里的 angle 文字块的角度，这个角度只影响width和height，当角度为-90、90、-270、270，width和height的值需要自行互换
        
    // const api = global.config.aliOCR.api;
    // const appCode = global.config.aliOCR.appCode;

    // const data = await new Promise((resolve, reject) => {
    //   request.post({
    //     url: api,
    //     timeout: 1000 * 60 * 2,
    //     headers: {
    //       "Authorization": `APPCODE ${appCode}`,
    //       "Content-Type": "application/json;charset=UTF-8"
    //     },
    //     body: JSON.stringify({
    //       img: imgData,
    //       prob: true,
    //       charInfo: true,
    //       table: true,
    //       sortPage: true,
    //       NeedRotate:true
    //     })
    //   }, (error, response, body) => {
    //     if (error) {
    //       reject(error);
    //     }
    //     else {
    //       let aliResult = null;
    //       try {
    //         aliResult = JSON.parse(body);
    //       } catch (ex) {
    //         console.log(ex.message);
    //         console.log(response.statusCode);
    //         console.log(error);
    //         console.log(body);
    //       }
    //       resolve(aliResult);
    //     }
    //   })
    // });

    // if (data.error_code !== undefined && data.error_code !== null) {
    //   return this.msg(data.error_code, data.error_msg);
    // }

    // //JSON写入
    // fs.writeFileSync(jsonPath, JSON.stringify(data));
    // //图片写入
    // fs.writeFileSync(imgPath, imgData);

    // if (bookNO !== '' && imgName !== '' && originImgData !== '' ) {

    //   let imgBuf = Buffer.from(originImgData, 'base64')

    //   //let ext = path.parse(imgName).ext   // 扩展名
    //   //imgName = path.parse(imgName).name  // 去掉扩展名
    //   //let imgname = `${imgName}_${md5}${ext}`

    //   let path_scan = path.join(ocr_img_dir, bookNO, '扫描')
    //   if ( !fs.existsSync(path_scan) ) {
    //     fs.mkdirSync(path_scan, { recursive: true })
    //   }

    //   let imgpath = path.join(path_scan, imgName)
    //   fs.writeFileSync(imgpath, imgBuf)
    // }

    // await this.dbs.ocrDB.imgs.add.query({ "md5": md5, "api": `aliyun`, ip: __ip__, userID });

    // return this.msg(200, data);
    return this.msg(200, 'ok')
  },
  remark: ``
}