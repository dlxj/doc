module.exports = {
    name: `search`,
    author: ``,
    params: {
        tablename: {
            type: 'string',
            remark: ''
        },
        keywd: {
            type: 'string',
            remark: ''
        },
        search_field: {
            type: 'enum',
            range:["v_jp","v_zh"],
            remark: '',
            default:'v_jp'
        },
    },
    remark: ``,
    sql: `
        SELECT id, jp_ruby as jp, zh, p.begintime as time, type, name, seasion FROM $$(tablename) p  WHERE p.$$(search_field) @@ to_tsquery($(keywd))  ORDER BY RANDOM()  LIMIT 3;
    `,
  }

  /*
  
  "SELECT id, jp_ruby as jp, zh, p.begintime as time, name, seasion FROM pokemon p  WHERE p.v_jp @@ to_tsquery('{keywd}')  ORDER BY RANDOM()  LIMIT 3;"

  "SELECT id, jp_ruby as jp, zh, p.begintime as time, name, seasion FROM pokemon p  WHERE p.v_zh @@ to_tsquery('{keywd}')  ORDER BY RANDOM() LIMIT 3;"
  
  */