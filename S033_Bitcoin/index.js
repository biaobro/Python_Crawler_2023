/*
@File               : index.js
@Project            : S033_Bitcoin
@CreateTime         : 2023/3/14 22:32
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/14 22:32 
@Version            : 1.0
@Description        : None
*/


const API_KEY = "a2c903cc-b31e-4547-9299-b6d07b7631ab"


function encryptApiKey() {
    var t = API_KEY
        , e = t.split("")
        , n = e.splice(0, 8);
    return t = e.concat(n).join("")
}


function encryptTime(t) {
    const a = 1111111111111
    var e = (1 * t + a).toString().split("")
        , n = parseInt(10 * Math.random(), 10)
        , r = parseInt(10 * Math.random(), 10)
        , o = parseInt(10 * Math.random(), 10);
    return e.concat([n, r, o]).join("")
}


function comb(t, e) {
    var n = "".concat(t, "|").concat(e);
    return btoa(n)
}


function getApiKey() {
    var t = (new Date).getTime()
        , e = encryptApiKey();
    return t = encryptTime(t),
        comb(e, t)
}


function getTimestamp(t) {
    var e = atob(t).split("|")[1];
    return e = e.slice(0, -3),
        e -= a
};

// console.log(getApiKey())

function generateUUID() {
    var e = Date.now() + window.performance.now();
    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (t) {
        var n = (e + 16 * Math.random()) % 16 | 0;
        return e = Math.floor(e / 16),
            ("x" === t ? n : 3 & n | 8).toString(16)
    })
}
