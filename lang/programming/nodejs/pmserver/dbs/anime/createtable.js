
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
        id BIGSERIAL PRIMARY KEY,
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

id integer primary key generated always as identity, 

// 后期再加索引吧，windows 装不了这个插件
create extension rum;
CREATE INDEX rum_anime_v_jp ON anime USING rum (v_jp rum_tsvector_ops);
CREATE INDEX rum_anime_v_zh ON anime USING rum (v_zh rum_tsvector_ops);


CREATE INDEX fts_rum_$$(tablename) ON $$(tablename) USING rum (v_jp rum_tsvector_ops);

cur.execute("CREATE INDEX fts_rum_$$(tablename) ON $$(tablename) USING rum (v_jp rum_tsvector_ops);")


CREATE INDEX fts_rum_studio ON studio USING rum (v_zh rum_tsvector_ops);

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

/*

    CREATE TABLE $$(tablename)_srt_jp (
        id integer primary key generated always as identity, 
        name text, 
        jp text, 
        type text, 
        begintime text,
        endtime text,
        v_jp  tsvector, 
        seasion text DEFAULT '',
        seasionname text DEFAULT '',
        episode text DEFAULT '',
        videoname text 
      );
*/
