
module.exports = {

    debug: true,
    http:{
        port:1001,
        port_debug:80
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
    subtitleSteams: {
        "danganronpa": [ 0 ],  // nth stream is srt 4 ffpmeg
        "pokemon": [ 0, 2 ],   
    }
}

