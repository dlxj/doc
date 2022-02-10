
module.exports = {
    name: `dropAndCreateDb`,
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

/*

let re = await libpg.defaultDB.query('DROP DATABASE IF EXISTS temp2;', [])
re = await libpg.defaultDB.query(`
    CREATE DATABASE temp2 
        WITH OWNER = postgres 
        ENCODING = 'UTF8' 
        TABLESPACE = pg_default 
        CONNECTION LIMIT = -1 
        TEMPLATE template0;
    `, [])

*/
