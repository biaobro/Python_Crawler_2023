var t = "/immediately/content-list.html?type=all&roll=gt";
var e = {
    last_update_time: 1682061808
}

function C(t, e) {
    e || (e = {}),
        e.platform = "web";
    var n = {
        type: "all",
        roll: "gt"
    };
    t = "/immediately/content-list.html?type=all&roll=gt&",
        // 对字符串 "last_update_time=1682061808&platform=web&roll=gt&type=all" 做 sha1 加密得到 token
        t += "token=".concat(Object(m["tokenCrypto"])(v(v({}, e), n))),
        // t = "/immediately/content-list.html?type=all&roll=gt&token=6e3fd14d1a3e39585c2da00ebfd14778f4c6e714"
        _({
            data: e,
            type: "get",
            url: t
        })
}

function w(t) {
    var e = t.split("?");
    if (1 == e.length)
        return {};
    e = e[1].split("&");
    var n, r = {}, a = b(e);
    try {
        for (a.s(); !(n = a.n()).done;) {
            var i = n.value;
            r[i.split("=")[0]] = i.split("=")[1]
        }
    } catch (c) {
        a.e(c)
    } finally {
        a.f()
    }
    return r
}

function b(t, e) {
    var n = "undefined" !== typeof Symbol && t[Symbol.iterator] || t["@@iterator"];
    if (!n) {
        if (Array.isArray(t) || (n = k(t)) || e && t && "number" === typeof t.length) {
            n && (t = n);
            var r = 0
                , a = function () {
            };
            return {
                s: a,
                n: function () {
                    return r >= t.length ? {
                        done: !0
                    } : {
                        done: !1,
                        value: t[r++]
                    }
                },
                e: function (t) {
                    throw t
                },
                f: a
            }
        }
        throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
    }
    var i, c = !0, o = !1;
    return {
        s: function () {
            n = n.call(t)
        },
        n: function () {
            var t = n.next();
            return c = t.done,
                t
        },
        e: function (t) {
            o = !0,
                i = t
        },
        f: function () {
            try {
                c || null == n.return || n.return()
            } finally {
                if (o)
                    throw i
            }
        }
    }
}


// t = {"last_update_time": 1682061808,"platform": "web"}
// t = {"last_update_time": 1682061808,"platform": "web","type": "all","roll": "gt"}

function v(t) {
    for (var e = 1; e < arguments.length; e++) {
        var n = null != arguments[e] ? arguments[e] : {};
        e % 2 ? g(Object(n), !0).forEach((function (e) {
                Object(l["a"])(t, e, n[e])
            }
        )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(t, Object.getOwnPropertyDescriptors(n)) : g(Object(n)).forEach((function (e) {
                Object.defineProperty(t, e, Object.getOwnPropertyDescriptor(n, e))
            }
        ))
    }
    return t
}

//
function R(t) {
    function e(t) {
        if (!t)
            return "";
        var e = [];
        return Object.keys(t).sort().map((function (n) {
                void 0 !== t[n] && e.push("".concat(n, "=").concat(t[n]))
            }
        )),
            e.join("&")
    }
    // 上面这个函数 得到 "last_update_time=1682061808&platform=web&roll=gt&type=all"

    return Object(p["a"])(e(t))
}