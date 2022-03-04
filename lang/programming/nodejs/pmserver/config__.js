
module.exports = {

    debug: true,
    insertPasswd:'rn',
    http:{
        port:1001,
        port_debug:80,
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
            host: 'xxx.77',
            user: 'postgres',
            password: 'xxxx',
            port: '5432',
            database: 'postgres',
            ssl: false
        },
        anime: {
            host: 'xxx.77',
            user: 'postgres',
            password: 'xxxx',
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
    subtitleSteams: {
        "danganronpa": [ 0 ],  // nth stream is srt 4 ffpmeg
        "pokemon": [ 0, 2 ], 
        "hibike_euphonium": [ 2 ],  // 2 jp_chs
    }
}

