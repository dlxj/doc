
(async () => {

    let formurlencoded = require('form-urlencoded')

    const bent = require('./browser.js')

    let json = {
        passwd: 'rn'
    }

    let formurlencoded_json = formurlencoded(json)

    let url = 'http://127.0.0.1:80'
    let post = bent(url, 'POST', 'json', 200)
    let response = await post('/anime/insert', formurlencoded_json, { 'Content-Type': 'application/x-www-form-urlencoded' })

    let a = 1

})()

