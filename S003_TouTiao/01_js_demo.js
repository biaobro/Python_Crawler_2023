const jsdom = require("jsdom");
const {JSDOM} = jsdom;

const resourceLoader = new jsdom.ResourceLoader({
    userAgent:"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
});

const html = `<!DOCTYPE html><p>Hello World</p>`
const dom = new JSDOM(html, {
    url : 'https://www.toutiao.com',
    referrer : 'https://example.com',
    contentType : 'text/html',
    resources : resourceLoader
});

console.log(dom.window.location)
console.log(dom.window.navigator.userAgent)
console.log(dom.window.document.referrer)


window = global //{}
params = {
    navigator : {
        appCodeName : "Mozilla",
        appName : "Netscape",
        appVersion : "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        language : "zh-CN",
        platform : "Win32",
        product : "Gecko",
        userAgent : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        vendor : "Google Inc.",
        webdriver : false
    }
}

Object.assign(window, params)

console.log(window.navigator)
console.log(navigator.appCodeName)