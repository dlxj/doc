
module.exports = {
  name: `drop`,
  author: ``,
  params: {
    dbname: {
      type: 'string',
      remark: ''
    }
  },
  remark: ``,
  sql: `
    DROP DATABASE IF EXISTS $$(dbname);
  `,
};

/*

 $$() 表示字面替换
 $()  替换成 $1 占位符， params 数组里面有相应的实参

*/

