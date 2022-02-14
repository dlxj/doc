module.exports = {
    name: 'insert',
    remark: '',
    params: {
    },
    async handler({}) {

        

        let obj = this

        let mkvs = this.libs.files.allmkv(global.animes.root, 'Danganronpa')
        //dbpaths.forEach((dbPath) => {

        let re = await this.dbs.defaultDB.drop.query({'dbname':'danganronpa'})  // drop db
        re = await this.dbs.defaultDB.danganronpa.create.query({})              // create db
        re = await this.dbs.danganronpa.createtable.query({})                   // create table 

        //let re = await this.services.user.getuser( { userid:'0' } )

        // let re = await this.dbs.temp2.search.query({keywd})

        return 'hi from insert'

        // return 'hi from service.'

    }
}