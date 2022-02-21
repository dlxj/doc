
module.exports = {
  name: `insert`,
  author: ``,
  params: {
    name: {
      type: 'string',
      remark: ''
    },
    seasion: {
      type: 'string',
      remark: ''
    },
    jp: {
      type: 'string',
      remark: ''
    },
    zh: {
      type: 'string',
      remark: ''
    },
    begintime: {
      type: 'string',
      remark: ''
    },
    endtime: {
      type: 'string',
      remark: ''
    },
    jp_ruby: {
      type: 'string',
      remark: ''
    },
    v_jp: {
      type: 'string',
      remark: ''
    },
    v_zh: {
      type: 'string',
      remark: '',
      default:''
    },
    videoname: {
      type: 'string',
      remark: ''
    },
    episode: {
      type: 'string',
      remark: ''
    },
    seasionname: {
      type: 'string',
      remark: '',
      default:''
    },
    audio: {
      type: 'object',
      remark: ''
    },
    video: {
      type: 'object',
      remark: ''
    }
  },
  remark: ``,
  sql: `
  INSERT INTO $$(name) (name, seasion, jp, zh, begintime, endtime, jp_ruby, v_jp, v_zh, videoname, episode, seasionname, audio, video)
  VALUES
  ( $(name), $(seasion), $(jp), $(zh), $(begintime), $(endtime), $(jp_ruby), to_tsvector($(v_jp)), to_tsvector($(v_zh)), $(videoname), $(episode), $(seasionname), $(audio), $(video) );
  `
}





















/*


                // re = await tempDB.query(`
                // INSERT INTO pokemon (name, seasion, jp, zh, begintime, jp_ruby, v_jp, v_zh, videoname, episode, seasionName, endtime, audio, video)
                // VALUES
                //  ( $1, $2, $3, $4, $5, $6, to_tsvector($7), to_tsvector($8), $9, $10, $11, $12, $13, $14 );
                //  `, [name, seasion, jp, zh, begintime, ruby, jp_ng, zh_ng, videoname, episode, seasionName, endtime, audio, video])
            
            

*/


