
module.exports = {
    name: `create`,
    author: ``,
    params: {
      dbname: {
        type: 'string',
        remark: ''
      }
    },
    remark: ``,
    sql: `
    CREATE DATABASE temp2 
        WITH OWNER = postgres 
        ENCODING = 'UTF8' 
        TABLESPACE = pg_default 
        CONNECTION LIMIT = -1 
        TEMPLATE template0;
    `,
  };

  