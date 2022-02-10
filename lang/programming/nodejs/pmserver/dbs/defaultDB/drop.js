
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
    DROP DATABASE IF EXISTS $(dbname);
  `,
};

