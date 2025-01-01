/*
@File               : app.js.js
@Project            : S035_HangHangCha
@CreateTime         : 2023/3/15 17:05
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/15 17:05 
@Version            : 1.0
@Description        : None
*/


const CryptoJS = require('crypto-js')

var c = "3sd&d2"
    , r = "4h@$udD2s"
    , a = "*";


function decrypt(n, e) {
    // e 传入为 undefined, 可以固定为 "3sd&d24h@$udD2s*"
    e = e || "".concat(c).concat(r).concat(a);
    var t = CryptoJS.enc.Utf8.parse(e)
        // n 是 data， t 是 key
        , i = CryptoJS.AES.decrypt(n, t, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        });
    return JSON.parse(CryptoJS.enc.Utf8.stringify(i).toString())
}

// console.log(decrypt(n))