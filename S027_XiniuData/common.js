/*
@File               : common.js
@Project            : S027_XiniuData
@CreateTime         : 2023/3/10 16:52
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/10 16:52 
@Version            : 1.0
@Description        : None
*/
const crypto = require('crypto')

var _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
  , _p = "W5D80NFZHAYB8EUI2T649RT2MNRMVE2O";
function e1(e) {
    if (null == e)
        return null;
    for (var t, n, r, o, i, a, c, u = "", s = 0; s < e.length; )
        o = (t = e.charCodeAt(s++)) >> 2,
        i = (3 & t) << 4 | (n = e.charCodeAt(s++)) >> 4,
        a = (15 & n) << 2 | (r = e.charCodeAt(s++)) >> 6,
        c = 63 & r,
        isNaN(n) ? a = c = 64 : isNaN(r) && (c = 64),
        u = u + _keyStr.charAt(o) + _keyStr.charAt(i) + _keyStr.charAt(a) + _keyStr.charAt(c);
    return u
}
function e2(e) {
    if (null == (e = _u_e(e)))
        return null;
    for (var t = "", n = 0; n < e.length; n++) {
        var r = _p.charCodeAt(n % _p.length);
        t += String.fromCharCode(e.charCodeAt(n) ^ r)
    }
    return t
}
function sig(e) {
    const hash = crypto.createHash('md5')
    return hash.update(e + _p).digest('hex').toUpperCase()

    // modify the source code here
    // return md5(e + _p).toUpperCase()
}
function d1(e) {
    var t, n, r, o, i, a, c = "", u = 0;
    for (e = e.replace(/[^A-Za-z0-9\+\/\=]/g, ""); u < e.length; )
        t = _keyStr.indexOf(e.charAt(u++)) << 2 | (o = _keyStr.indexOf(e.charAt(u++))) >> 4,
        n = (15 & o) << 4 | (i = _keyStr.indexOf(e.charAt(u++))) >> 2,
        r = (3 & i) << 6 | (a = _keyStr.indexOf(e.charAt(u++))),
        c += String.fromCharCode(t),
        64 != i && (c += String.fromCharCode(n)),
        64 != a && (c += String.fromCharCode(r));
    return c
}
function _u_e(e) {
    if (null == e)
        return null;
    e = e.replace(/\r\n/g, "\n");
    for (var t = "", n = 0; n < e.length; n++) {
        var r = e.charCodeAt(n);
        r < 128 ? t += String.fromCharCode(r) : r > 127 && r < 2048 ? (t += String.fromCharCode(r >> 6 | 192),
        t += String.fromCharCode(63 & r | 128)) : (t += String.fromCharCode(r >> 12 | 224),
        t += String.fromCharCode(r >> 6 & 63 | 128),
        t += String.fromCharCode(63 & r | 128))
    }
    return t
}
function _u_d(e) {
    for (var t = "", n = 0, r = 0, o = 0, i = 0; n < e.length; )
        (r = e.charCodeAt(n)) < 128 ? (t += String.fromCharCode(r),
        n++) : r > 191 && r < 224 ? (o = e.charCodeAt(n + 1),
        t += String.fromCharCode((31 & r) << 6 | 63 & o),
        n += 2) : (o = e.charCodeAt(n + 1),
        i = e.charCodeAt(n + 2),
        t += String.fromCharCode((15 & r) << 12 | (63 & o) << 6 | 63 & i),
        n += 3);
    return t
}
function d2(e) {
    for (var t = "", n = 0; n < e.length; n++) {
        var r = _p.charCodeAt(n % _p.length);
        t += String.fromCharCode(e.charCodeAt(n) ^ r)
    }
    return t = _u_d(t)
}


// requests, can't figure out why there is transform between s and l
function encrypt_payload(data_dict){
    // standard format {'payload':{'sort': 1, 'start': 80, 'limit': 20}}
    // we add a pack, so that external python code just provide {'sort': 1, 'start': 80, 'limit': 20}
    let data = {}
    data['payload'] = data_dict
    const s = JSON.stringify(data)
        , l = JSON.parse(s);
    let f = e1(e2(JSON.stringify(l.payload)))
    let p = sig(f);
    return {'payload':f,'sig':p}
}

// console.log(encrypt_payload(n))

// response
// l is data part of response, actually there are different branches based v value in source code
// here we ignore it
function decrypt_response(data_str){
    const d = d1(data_str)
        , v = d2(d)
    ;
    return JSON.parse(v)
}

