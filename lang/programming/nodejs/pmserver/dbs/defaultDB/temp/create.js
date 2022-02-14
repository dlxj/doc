
module.exports = {
    name: `create`,
    author: ``,
    params: {
    },
    remark: ``,
    sql: `
    CREATE DATABASE temp 
        WITH OWNER = postgres 
        ENCODING = 'UTF8' 
        TABLESPACE = pg_default 
        CONNECTION LIMIT = -1 
        TEMPLATE template0;
    `,
  }

  /*
      dbname: {
        type: 'string',
        remark: ''
      }
  */

  