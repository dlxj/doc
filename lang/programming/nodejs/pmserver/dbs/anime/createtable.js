
module.exports = {
  name: `createtable`,
  author: ``,
  params: {
    tablename: {
      type: 'string',
      remark: ''
    }
  },
  remark: ``,
  sql: `
    CREATE TABLE $$(tablename) (
        id integer primary key generated always as identity, 
        name text, 
        jp text, 
        zh text DEFAULT '', 
        en text DEFAULT '', 
        type text, 
        begintime text,
        endtime text,
        jp_ruby text,
        jp_mecab text, 
        v_jp  tsvector, 
        v_zh  tsvector, 
        v_en  tsvector, 
        seasion text DEFAULT '',
        seasionname text DEFAULT '',
        episode text DEFAULT '',
        audio bytea, 
        video bytea,
        videoname text 
      );

      CREATE INDEX $$(tablename)_name_index ON $$(tablename) (name);

  `
}

/*

  sql: `
    CREATE TABLE $$(tablename) (
        id integer primary key generated always as identity, 
        name text, 
        jp text, 
        zh text DEFAULT '', 
        en text DEFAULT '', 
        type text, 
        begintime text,
        endtime text,
        jp_ruby text,
        jp_mecab text, 
        v_jp  tsvector, 
        v_zh  tsvector, 
        v_en  tsvector, 
        seasion text DEFAULT '',
        seasionname text DEFAULT '',
        episode text DEFAULT '',
        audio bytea, 
        video bytea,
        videoname text 
      );
    create extension pgroonga;
    create extension pg_jieba;
    CREATE INDEX pgroonga_jp_index ON $$(tablename) USING pgroonga (jp);
    CREATE INDEX animename_index ON $$(tablename) (name);
    CREATE INDEX episode_index ON $$(tablename) (episode);
  `

`
    CREATE TABLE danganronpa (
        id integer primary key generated always as identity, 
        name text, 
        jp text, 
        zh text DEFAULT '', 
        en text DEFAULT '', 
        type text, 
        begintime text,
        endtime text,
        jp_ruby text,
        jp_mecab text, 
        v_jp  tsvector, 
        v_zh  tsvector, 
        v_en  tsvector, 
        seasion text DEFAULT '',
        seasionname text DEFAULT '',
        episode text DEFAULT '',
        audio bytea, 
        video bytea,
        videoname text 
      );
    create extension pgroonga;
    create extension pg_jieba;
    CREATE INDEX pgroonga_jp_index ON danganronpa USING pgroonga (jp);
    CREATE INDEX animename_index ON danganronpa (name);
    CREATE INDEX episode_index ON danganronpa (episode);
  `

*/


