module.exports = {
    name: `search`,
    author: ``,
    params: {
        keywd: {
            type: 'string',
            remark: ''
        }
    },
    remark: ``,
    sql: `
        SELECT id, jp_ruby as jp, zh, p.begintime as time, name, seasion FROM pokemon p  WHERE p.v_jp @@ to_tsquery($(keywd))  ORDER BY RANDOM()  LIMIT 3;
    `,
  }

  /*
  
  "SELECT id, jp_ruby as jp, zh, p.begintime as time, name, seasion FROM pokemon p  WHERE p.v_jp @@ to_tsquery('{keywd}')  ORDER BY RANDOM()  LIMIT 3;"

  "SELECT id, jp_ruby as jp, zh, p.begintime as time, name, seasion FROM pokemon p  WHERE p.v_zh @@ to_tsquery('{keywd}')  ORDER BY RANDOM() LIMIT 3;"
  
  */