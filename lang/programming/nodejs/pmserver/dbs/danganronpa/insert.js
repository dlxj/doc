
module.exports = {
  name: `insert`,
  author: ``,
  params: {
  },
  remark: ``,
  sql: `
  INSERT INTO danganronpa (name, seasion, jp, zh, begintime, jp_ruby, v_jp, v_zh, videoname, episode, seasionName, endtime, audio, video)
  VALUES
  ( $(name), $(seasion), $(jp), $(zh), $(begintime), $(jp_ruby), to_tsvector($(v_jp)), to_tsvector($(v_zh)), $(videoname), $(episode), $(seasionName), $(endtime), $(audio), $(video) );
  `
}





















/*


                // re = await tempDB.query(`
                // INSERT INTO pokemon (name, seasion, jp, zh, begintime, jp_ruby, v_jp, v_zh, videoname, episode, seasionName, endtime, audio, video)
                // VALUES
                //  ( $1, $2, $3, $4, $5, $6, to_tsvector($7), to_tsvector($8), $9, $10, $11, $12, $13, $14 );
                //  `, [name, seasion, jp, zh, begintime, ruby, jp_ng, zh_ng, videoname, episode, seasionName, endtime, audio, video])
            
            

*/


