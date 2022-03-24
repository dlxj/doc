

let path = require('path')
let fs = require('fs')
let rd = require('rd')
let libfiles = require('./lib/files')
let pg = require('./application/db/pgsql.js')

let startDir = path.resolve(__dirname, '.')  // startup dir
let apiDir = path.join(startDir, `/http/api/`)
let serviceDir = path.join(startDir, '/service/api/')
let dbsDir = path.join(startDir, '/dbs/')
let libDir = path.join(startDir, '/lib/')

let config = require('./config.js')

Object.defineProperty(global, 'config', {
    get() {
        return config
    }
})

Object.defineProperty(global, 'pg', {
    get() {
        return pg
    }
})

Object.defineProperty(global, 'startDir', {  // global 是保留关键字，系统全局对象
    get() {
        return startDir
    }
})

// 缓存api 对象，不用每次都读磁盘
let apiCache = {}  // api 是入口
Object.defineProperty(global, 'apiCache', {
    get() {
        return apiCache
    }
})

let serviceCache = {}  // service 供api 调用，是库
Object.defineProperty(global, 'serviceCache', {
    get() {
        return serviceCache
    }
})

let libCache = {}  // lib 供api, service, lib 调用
Object.defineProperty(global, 'libCache', {
    get() {
        return libCache
    }
})

let services = {}  // 所有的service 存在这里，service 只能由api 调用
Object.defineProperty(global, 'services', {
    get() {
        return services
    }
})

let dbs = {}  // 所有的service 存在这里，service 只能由api 调用
Object.defineProperty(global, 'dbs', {
    get() {
        return dbs
    }
})

let libs = {}  // 所有lib 都存在这里
Object.defineProperty(global, 'libs', {
    get() {
        return libs
    }
})

let animes = {}  // 所有mkv 信息都存在这里
Object.defineProperty(global, 'animes', {
    get() {
        return animes
    }
})

module.exports = async function () {

    // 从js 文件加载dbs 对象
    let dbpaths = libfiles.allfiles(dbsDir, 'js')
    dbpaths.forEach((dbPath) => {
        if (!fs.existsSync(dbPath)) {
            throw `file not exists: ${dbPath}`
        }

        let schema = require(dbPath) // 定义了参数, sql 语句的对象

        let basePath = dbPath.replace(dbsDir, '').replace('.js', '')
        let arr = basePath.split(new RegExp(String.raw`[\\/]`))

        let dbName = arr[0]

        if (global.dbs[dbName] == undefined) {
            global.dbs[dbName] = global.pg.getDB(dbName)  // 实例化
        }

        let lastobj = global.dbs
        for (let i = 0; i < arr.length; i++) {

            let name = arr[i]

            if (i == arr.length - 1) {

                let pgdb = global.dbs[dbName]

                let item = {}

                //套一层参数验证
                item.query = async function (param) {
                    const paramData = require('./lib/paramVerify.js')(schema.params, param)
                    return pgdb.query(schema.sql, paramData)  // 执行查询
                }

                lastobj[name] = item

            } else {

                if (!(name in lastobj)) {
                    lastobj[name] = {}
                    lastobj = lastobj[name]
                } else {
                    lastobj = lastobj[name]
                }
            }

        }

    })

    // 从js 文件加载api 对象
    let apipaths = libfiles.allfiles(apiDir, 'js')
    apipaths.forEach((apiPath) => {
        if (!fs.existsSync(apiPath)) {
            throw `file not exists: ${apiPath}`
        }
        let api = require(apiPath)
        //注入msg函数
        Object.defineProperty(api, "msg", {
            get() {
                return (status, data) => {
                    return { status, data }
                }
            }
        })

        global.apiCache[apiPath] = api
    })

    // 从js 文件加载service 对象
    let servicepaths = libfiles.allfiles(serviceDir, 'js')
    servicepaths.forEach((servicePath) => {
        if (!fs.existsSync(servicePath)) {
            throw `file not exists: ${servicePath}`
        }
        let service = require(servicePath)

        global.serviceCache[servicePath] = service
    })

    // 从js 文件加载lib 对象
    let libpaths = libfiles.allfiles(libDir, 'js')
    libpaths.forEach((libPath) => {
        if (!fs.existsSync(libPath)) {
            throw `file not exists: ${libPath}`
        }

        let lib = require(libPath) // 定义了参数, sql 语句的对象

        let basePath = libPath.replace(libDir, '').replace('.js', '')
        let arr = basePath.split(new RegExp(String.raw`[\\/]`))

        let lastobj = global.libs
        for (let i = 0; i < arr.length; i++) {

            let name = arr[i]

            if (i == arr.length - 1) {

                lastobj[name] = lib
                //global.libCache[servicePath] = service
            } else {

                if (!(name in lastobj)) {
                    lastobj[name] = {}
                    lastobj = lastobj[name]
                } else {
                    lastobj = lastobj[name]
                }
            }

        }
    })

    // api 注入 dbs,  用于在api 对象支持这种调用：this.dbs.defaultDB.temp.create.query({ dbname })
    for (let apiPath in global.apiCache) {

        let api = global.apiCache[apiPath]
        if (api['dbs'] === undefined) {
            Object.defineProperty(api, "dbs", {
                get() {
                    return global.dbs
                }
            })
        }

    }

    // service 注入 dbs
    for (let servicePath in global.serviceCache) {

        let service = global.serviceCache[servicePath]

        if (service['dbs'] === undefined) {
            Object.defineProperty(service, "dbs", {
                get() {
                    return global.dbs
                }
            })
        }

    }

    // api 注入 service,  用于在api 对象支持这种调用：this.service.user.getuser()
    for (let apiPath in global.apiCache) {

        let api = global.apiCache[apiPath]

        if (api['services'] === undefined) {
            Object.defineProperty(api, "services", {
                get() {
                    return global.services
                }
            })
        }

        for (let servicePath in global.serviceCache) {

            let service = global.serviceCache[servicePath]
            //套一层参数验证
            service._handler = async function (param) {
                const paramData = require('./lib/paramVerify.js')(service.params, param)
                return service.handler(paramData)
            }

            let basePath = servicePath.replace(serviceDir, '').replace('.js', '')
            let arr = basePath.split(new RegExp(String.raw`[\\/]`))  // 此 service 的 每一个“文件夹”

            let lastobj = api['services']
            for (let i = 0; i < arr.length; i++) {

                let name = arr[i]

                if (i == arr.length - 1) {

                    lastobj[name] = service._handler //service.handler

                } else {

                    if (!(name in lastobj)) {
                        lastobj[name] = {}
                        lastobj = lastobj[name]
                    } else {
                        lastobj = lastobj[name]
                    }
                }

            }

        }

    }

    // service 注入 其他service
    for (let servicePath in global.serviceCache) {

        let service = global.serviceCache[servicePath]

        if (service['services'] === undefined) {
            Object.defineProperty(service, "services", {
                get() {
                    return global.services
                }
            })
        }
    }

    // 解决那个奇怪的问题
    if (global.services['services'] === undefined) {
        Object.defineProperty(global.services, "services", {
            get() {
                return global.services
            }
        })
    }

    let root = ''
    let platform = process.platform
    let platforms = [ 'win32', 'linux', 'darwin' ]
    if ( ! platforms.includes( platform ) ) {
        throw 'unknow os type.'
    }

    // check if config is correct
    let rootdirs = Object.keys( global.config.rootDir )
    if ( ! rootdirs.includes(platform) ) {
        throw `config.js rootDir not includes this platform: ${platform}`
    }

    let rootdir = global.config.rootDir[platform]
    root = require('path').join(rootdir, 'videos', 'anime')
    let root_audio = require('path').join(rootdir, 'audios')

    let root_subtitles = require('path').join(rootdir, 'sutitles')


    global.animes.root = root
    global.animes.root_audio = root_audio
    global.root_subtitles = root_subtitles

    // service 注入 animes
    for (let servicePath in global.serviceCache) {

        let service = global.serviceCache[servicePath]

        if (service['animes'] === undefined) {
            Object.defineProperty(service, "animes", {
                get() {
                    return global.animes
                }
            })
        }
    }


    // api 注入 libs
    for (let apiPath in global.apiCache) {

        let api = global.apiCache[apiPath]
        if (api['libs'] === undefined) {
            Object.defineProperty(api, "libs", {
                get() {
                    return global.libs
                }
            })
        }

    }

    // service 注入 libs
    for (let servicePath in global.serviceCache) {

        let service = global.serviceCache[servicePath]

        if (service['libs'] === undefined) {
            Object.defineProperty(service, "libs", {
                get() {
                    return global.libs
                }
            })
        }
    }
    

    // libs 注入 libs
    // for (let libPath in global.libs) {

    //     let a = 1
    //     if (service['libs'] === undefined) {
    //         Object.defineProperty(service, "libs", {
    //             get() {
    //                 return global.libs
    //             }
    //         })
    //     }

    // }

    // 务必只初始化一次
    await global.libs.mecab.init()
    
}
