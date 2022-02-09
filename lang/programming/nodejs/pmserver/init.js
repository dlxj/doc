
let path = require('path')
let fs = require('fs')
let rd = require('rd')
let libfiles = require('./lib/files')

let startDir = path.resolve(__dirname, '.')  // startup dir
let apiDir = path.join(startDir, `/http/api/`)
let serviceDir = path.join(startDir, '/service/api/')
let libDir = path.join(startDir, '/lib/')

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

let services = {}  // 所有的service 存在这里，service 只能由api 调用
Object.defineProperty(global, 'services', {
    get() {
        return services
    }
})

module.exports = function () {

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



    let a = 1

}
