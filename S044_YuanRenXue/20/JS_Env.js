function Hlclient(wsURL) {
    this.wsURL = wsURL;
    this.handlers = {};
    this.socket = {};
    if (!wsURL) {
        throw new Error('wsURL can not be empty!!')
    }
    this.connect()
    this.handlers["_execjs"]=function (resolve,param){
        var res=eval(param)
        if (!res){
            resolve("没有返回值")
        }else{
            resolve(res)
        }

    }
}

Hlclient.prototype.connect = function () {
    console.log('begin of connect to wsURL: ' + this.wsURL);
    var _this = this;
    try {
        this.socket["ySocket"] = new WebSocket(this.wsURL);
        this.socket["ySocket"].onmessage = function (e) {
            try{
                let blob=e.data
                blob.text().then(data =>{
                    _this.handlerRequest(data);
                })
            }catch{
                console.log("not blob")
                _this.handlerRequest(blob)
            }

        }
    } catch (e) {
        console.log("connection failed,reconnect after 10s");
        setTimeout(function () {
            _this.connect()
        }, 10000)
    }
    this.socket["ySocket"].onclose = function () {
        console.log("connection failed,reconnect after 10s");
        setTimeout(function () {
            _this.connect()
        }, 10000)
    }

};
Hlclient.prototype.send = function (msg) {
    this.socket["ySocket"].send(msg)
}

Hlclient.prototype.regAction = function (func_name, func) {
    if (typeof func_name !== 'string') {
        throw new Error("an func_name must be string");
    }
    if (typeof func !== 'function') {
        throw new Error("must be function");
    }
    console.log("register func_name: " + func_name);
    this.handlers[func_name] = func;
    return true

}

//收到消息后这里处理，
Hlclient.prototype.handlerRequest = function (requestJson) {
    var _this = this;
    var result=JSON.parse(requestJson);
    //console.log(result)
    if (!result['action']) {
        this.sendResult('','need request param {action}');
        return
    }
    var action=result["action"]
    var theHandler = this.handlers[action];
    if (!theHandler){
        this.sendResult(action,'action not found');
        return
    }
    try {
        if (!result["param"]){
            theHandler(function (response) {
                _this.sendResult(action, response);
            })
        }else{
            var param=result["param"]
            try {
                param=JSON.parse(param)
            }catch (e){
                console.log("")
            }
            theHandler(function (response) {
                _this.sendResult(action, response);
            },param)
        }

    } catch (e) {
        console.log("error: " + e);
        _this.sendResult(action+e);
    }
}

Hlclient.prototype.sendResult1 = function (action, e) {
    var ss = action + atob("aGxeX14") + e;
    this.send(ss);
}

Hlclient.prototype.sendResult = function (action, response) {
    var responseJson;
    if (typeof response == 'string') {
        try {
            responseJson = JSON.parse(response);
        } catch (e) {
            responseJson = {};
            responseJson['data'] = response;
        }
    } else if (typeof response == 'object') {
        responseJson = response;
    } else {
        responseJson = {};
        responseJson['data'] = response;
    }
    if (Array.isArray(responseJson)) {
        responseJson = {
            data: responseJson,
            code: 0
        }
    }

    if (responseJson['code']) {
        responseJson['code'] = 0;
    } else if (responseJson['status']) {
        responseJson['status'] = 0;
    } else {
        responseJson['status'] = 0;
    }
    var responseText = JSON.stringify(responseJson);
    this.send(action + atob("aGxeX14") + responseText);
}

// 上面是用于建立环境的源码
// 注入环境后连接通信
// var demo = new Hlclient("ws://127.0.0.1:12080/ws?group=zzz&name=hlg");

// 连接通信
var client = new Hlclient("ws://127.0.0.1:12080/ws?group=match20&name=yuanrenxue");

// demo_001
// 注册一个方法 第一个参数hello为方法名，
// 第二个参数为函数，resolve里面的值是想要的值(发送到服务器的)
client.regAction("hello1", function (resolve) {
    //这样每次调用就会返回“好困啊+随机整数”
    var Js_sjz = "好困啊"+parseInt(Math.random()*1000);
    resolve(Js_sjz);
})
// 访问接口，获得js端的返回值
// http://localhost:12080/go?group=zzz&name=hlg&action=hello

// demo_002
//写一个传入字符串，返回base64值的接口(调用内置函数btoa)
client.regAction("hello2", function (resolve,param) {
    //这样添加了一个param参数，http接口带上它，这里就能获得
    var base666 = btoa(param)
    resolve(base666);
})

// demo_003
//假设有一个函数 需要传递两个参数
function hlg(User,Status){
    return User+"说："+Status;
}

client.regAction("hello3", function (resolve,param) {
    //这里还是param参数 param里面的key 是先这里写，但到时候传接口就必须对应的上
    res=hlg(param["user"],param["status"])
    resolve(res);
})
// url = "http://localhost:12080/go"

// 第二个参数为函数，resolve里面的值是想要的值(发送到服务器的)
// param是可传参参数，可以忽略
client.regAction("ShiGuang", function (resolve, param) {
    t = Date.parse(new Date());
    var list = {
        "page": String(param),
        "sign": window.sign(String(param) + '|' + t.toString()),
        "t": t,
    }
    resolve(list)
})