/*
@File               : index.js
@Project            : S028_ChinaIndex
@CreateTime         : 2023/3/11 13:52
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/11 13:52 
@Version            : 1.0
@Description        : None
*/
// index.28827ebe.js

function dataFilter(e, t) {
    const n = e
        , r = n.data;
    if (n.isEncrypt === 1) {
        const i = Vm_parse(n.lastFetchTime + "000")
            , a = Vm_parse(n.lastFetchTime + "000")
            , s = zie_decrypt(r.toString(), i, {iv: a})
            , c = s.toString(Vm);
        return n.data = JSON.parse(c),
            n
    } else
        return n.isEncrypt === 0 && typeof r == "string" ? (n.data = JSON.parse(r),
            n) : e
}

function Vm_parse(p) {
    return E_parse(unescape(encodeURIComponent(p)))
}

function E_parse(p) {
    for (var m = p.length, I = [], C = 0; C < m; C++)
        I[C >>> 2] |= (p.charCodeAt(C) & 255) << 24 - C % 4 * 8;
    return new init(I,m)
}

function init(p, m) {
    p = this.words = p || [],
    // m != i ? this.sigBytes = m : this.sigBytes = p.length * 4
    m = this.sigBytes = p.length * 4
}

console.log(Vm_parse(1678516035095))

// F 是个字符串
// K 是个字典
const F = "DAn5LrFpw5fg6tLMaSPrPw=="
const Y = {
    "words": [
        825636664,
        892417332,
        892940595,
        942682160
    ],
    "sigBytes": 16
}
const K = {
    "iv": {
        "words": [
            825636664,
            892417332,
            892940595,
            942682160
        ],
        "sigBytes": 16
    }
}

// 如果没有经验，分析到这里就卡住了，从这里往下是无穷尽的调用
// 但根据视频给的思路，这里其实就是AES 解密
// 所以对 AES 加解密，DES 加解密的形式要了解
// 具体的实现见 ctx.js，
// function zie_decrypt(F, Y, K) {
//     return D(Y).decrypt(P, F, Y, K)
// }

