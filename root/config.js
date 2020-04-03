class Config {
    constructor() {
        if(!Config.instance) {
            this._csvHeader = []
            this._csvData = []
            this._csvFormatedHeader = []
            this._imgUrl = []
            this._imgFormatedUrl = []
            this._mediaList = []
            Config.instance = this
        }
        
        return Config.instance
    }
    get csvHeader(){
        return this._csvHeader
    }

    get csvData(){
        return this._csvData
    }

    get csvFormatedHeader(){
        return this._csvFormatedHeader
    }

    get imgUrl(){
        return this._imgUrl
    }

    get imgFormatedUrl(){
        return this._imgFormatedUrl
    }

    get mediaList(){
        return this._mediaList
    }

    set csvHeader(new_csvHeader) {
        this._csvHeader = new_csvHeader
    }

    set csvData(new_csvData) {
        this._csvData = new_csvData
    }

    set csvFormatedHeader(new_csvFormatedHeader) {
        this._csvFormatedHeader = new_csvFormatedHeader
    }

    set imgUrl(new_imgUrl) {
        this._imgUrl = new_imgUrl
    }

    set imgFormatedUrl(new_imgFormatedUrl) {
        this._imgFormatedUrl = new_imgFormatedUrl
    }

    set mediList(new_mediaList) {
        this._mediaList = new_mediaList
    }
}