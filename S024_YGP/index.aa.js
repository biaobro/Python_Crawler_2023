/*
@File               : index.aa.js.js
@Project            : S024_YGP
@CreateTime         : 2023/3/8 14:23
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/8 14:23 
@Version            : 1.0
@Description        : None
*/

const crypto = require('crypto')
const ky = "zxcvbnmlkjhgfdsaqwertyuiop0987654321QWERTYUIOPLKJHGFDSAZXCVBNM"
  , Fq = ky + "-@#$%^&*+!";

function yq(e, t) {
    switch (arguments.length) {
    case 1:
        return parseInt(Math.random() * e + 1, 10);
    case 2:
        return parseInt(Math.random() * (t - e + 1) + e, 10);
    default:
        return 0
    }
}

function lr(e=[]) {
    return e.map(t=>Fq[t]).join("")
}
function Aq(e) {
    return [...Array(e)].map(()=>ky[yq(0, 61)]).join("")
}
function Ig(e={}) {
    const {p: t, t: n, n: u, k: o} = e
      , r = Bq(t);
    const hash = crypto.createHash('sha256')
    console.log(u + o + decodeURIComponent(r) + n)
    return hash.update(u + o + decodeURIComponent(r) + n).digest('hex')
}
function Bq(e) {
    let t = "";
    return typeof e == "object" ? t = Object.keys(e).map(n=>`${n}=${e[n]}`).sort().join("&") : typeof e == "string" && (t = e.split("&").sort().join("&")),
    t
}

// 本地生成cookie， uid 和 sid
function genUUID() {
    var uuid = "", ii;
    for (ii = 0; ii < 32; ii += 1) {
        switch (ii) {
        case 8:
        case 20:
            uuid += "-";
            uuid += ((Math.random() * 16) | 0).toString(16);
            break;
        case 12:
            uuid += "-";
            uuid += "4";
            break;
        case 16:
            uuid += "-";
            uuid += ((Math.random() * 4) | 8).toString(16);
            break;
        default:
            uuid += ((Math.random() * 16) | 0).toString(16)
        }
    }
    return uuid
}

// test data
test_data = {
    "type": "trading-type",
    "publishStartTime": "",
    "publishEndTime": "",
    "siteCode": "44",
    "secondType": "A",
    "projectType": "",
    "thirdType": "",
    "dateType": "",
    "total": 0,
    "pageNo": 1,
    "pageSize": 10,
    "openConvert": false
}

function format(data){
    return JSON.stringify(data).replace(/:/g, '=').
    replace(/,/g, '&').
    replace(/'/g, '').
    replace(/"/g, '').
    replace(/{/g, '').
    replace(/}/g, '')
}

// console.log(format(payload))

// 业务

function hash256(data){
    const a = Date.now()
        , l = Aq(16) // 从Fq 字符串中随机拼接，得到长度为16 的字符串
        , c = lr([8, 28, 20, 42, 21, 53, 65, 6]) // 因为数字固定，所以结果也是固定值："k8tUyS$m"
        , d = Ig({
            p: format(data),
            t: a,
            n: l,
            k: c
        })

    return {
        'App' : lr([11, 11, 0, 21, 62, 25, 24, 19, 20, 15, 7]),
        'Nonce' : l,
        'Signature' : d,
        'Timestamp' : a,
    }
}

// console.log(hash256(payload))


function generate_cookies(){
    return {
        'uid' : genUUID(),
        'sid' : genUUID()
    }
}