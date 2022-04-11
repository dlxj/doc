
module.exports = {

    debug: true,
    insertPasswd:'RightNow',
    http:{
        port:8880,
        port_debug:8880,
        headers: {
            "Server": `pmserver`,
            "Access-Control-Allow-Origin": `*`,
            "Content-Type": `text/json`,
            'Access-Control-Allow-Headers': `content-type`,
            'Access-Control-Request-Method': `GET,POST`
        }
    },
    dbs:{
        host_debug:'127.0.0.1',
        defaultDB: {
            host: 'xxx',
            user: 'postgres',
            password: 'xxx',
            port: '5432',
            database: 'postgres',
            ssl: false
        },
        anime: {
            host: 'xxx',
            user: 'postgres',
            password: 'xxx',
            port: '5432',
            database: 'anime',
            ssl: false
        }
    },
    rootDir: {
        "win32": `E:\\`,
        "linux": `/mnt/`,
        "darwin": `/Users/olnymyself/Downloads/`
    },
    root_subtitles:{
        "win32": `D:\\GitHub\\doc\\lang\\Japanese\\anime\\sutitles`,
        "linux": `/mnt/`,
        "darwin": `/Users/olnymyself/Downloads/`
    },
    root_vd:{
        "win32": `E:\\videos\\anime`,
        "linux": `/mnt/`,
        "darwin": `/Users/olnymyself/Downloads/`
    },
    subtitleSteams: {
        "danganronpa": [ 0 ],  // nth stream is srt 4 ffpmeg
        //"pokemon": [ 0, 2 ], 
        "pokemon_c2club": [ 0, 2 ], 
        "pokemon_amazon": [ 0 ], 
        "hibike_euphonium": [ 2 ],  // 2 jp_chs
    }
}

