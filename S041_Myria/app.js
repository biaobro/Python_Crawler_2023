/*
@File               : app.js
@Project            : S041_Myria
@CreateTime         : 2023/4/5 12:15
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/5 12:15 
@Version            : 1.0
@Description        : None
*/

function c(e) {
    (0, n.A7)(e, 20) || s.throwArgumentError("invalid address", "address", e);
    const t = (e = e.toLowerCase()).substring(2).split("")
        , r = new Uint8Array(40);
    for (let n = 0; n < 40; n++)
        r[n] = t[n].charCodeAt(0);
    const a = (0, n.lE)((0, i.w)(r));
    for (let n = 0; n < 40; n += 2)
        a[n >> 1] >> 4 >= 8 && (t[n] = t[n].toUpperCase()),
        (15 & a[n >> 1]) >= 8 && (t[n + 1] = t[n + 1].toUpperCase());
    return "0x" + t.join("")
}

function l(e) {
    let t = (e = (e = e.toUpperCase()).substring(4) + e.substring(0, 2) + "00").split("").map((e => d[e])).join("");
    for (; t.length >= f;) {
        let e = t.substring(0, f);
        t = parseInt(e, 10) % 97 + t.substring(e.length)
    }
    let r = String(98 - parseInt(t, 10) % 97);
    for (; r.length < 2;)
        r = "0" + r;
    return r
}

// 对 e 做格式化
function h(e) {
    let t = null;
    if ("string" !== typeof e && s.throwArgumentError("invalid address", "address", e), e.match(/^(0x)?[0-9a-fA-F]{40}$/))
        "0x" !== e.substring(0, 2) && (e = "0x" + e),
            t = c(e),
        e.match(/([A-F].*[a-f])|([a-f].*[A-F])/) && t !== e && s.throwArgumentError("bad address checksum", "address", e);
    else if (e.match(/^XE[0-9]{2}[0-9A-Za-z]{30,31}$/)) {
        for (e.substring(2, 4) !== l(e) && s.throwArgumentError("bad icap checksum", "address", e),
                 t = (0, a.g$)(e.substring(4)); t.length < 40;)
            t = "0" + t;
        t = c("0x" + t)
    } else
        s.throwArgumentError("invalid address", "address", e);
    return t
}

var ee = "0x12bc003dbc3a8586fbf51d584dce7bf56e97e22b"
console.log(h(ee))

