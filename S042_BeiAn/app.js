/*
@File               : app.js
@Project            : S042_BeiAn
@CreateTime         : 2023/4/6 11:56
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/6 11:56 
@Version            : 1.0
@Description        : None
*/
// 夜幕OB 一键还原：https://ob.nightteam.cn/

const jsdom = require("jsdom");
const {JSDOM} = jsdom;
const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
window = dom.window;
document = window.document;
location = window.location;

function hash(_0x2434e0) {
  function _0x3187c8(_0x2a72b2, _0x43832a) {
    return _0x2a72b2 << _0x43832a | _0x2a72b2 >>> 32 - _0x43832a;
  }

  function _0x42e159(_0x9b0115, _0x3201cb) {
    var _0x451709 = "4|2|5|1|0|3|7|6"["split"]('|');

    var _0x2d44d3 = 0;

    var _0x3679c5;

    var _0x243a55;

    var _0x2d75fc;

    var _0x3a612b;

    var _0x138e59;

    _0x2d75fc = _0x9b0115 & 2147483648;
    _0x3a612b = _0x3201cb & 2147483648;
    _0x3679c5 = _0x9b0115 & 1073741824;
    _0x243a55 = _0x3201cb & 1073741824;
    _0x138e59 = (_0x9b0115 & 1073741823) + (_0x3201cb & 1073741823);
    if (_0x3679c5 & _0x243a55) return _0x138e59 ^ 2147483648 ^ _0x2d75fc ^ _0x3a612b;

    if (_0x3679c5 | _0x243a55) {
      if (_0x138e59 & 1073741824) return _0x138e59 ^ 3221225472 ^ _0x2d75fc ^ _0x3a612b;else return _0x138e59 ^ 1073741824 ^ _0x2d75fc ^ _0x3a612b;
    } else return _0x138e59 ^ _0x2d75fc ^ _0x3a612b;
  }

  function _0x55f2c0(_0x123f45, _0x373905, _0x1f23ee) {
    return _0x123f45 & _0x373905 | ~_0x123f45 & _0x1f23ee;
  }

  function _0x272eb2(_0x258b6f, _0x162b35, _0x586eba) {
    return _0x258b6f & _0x586eba | _0x162b35 & ~_0x586eba;
  }

  function _0x1bd60a(_0x2c49f3, _0x6d3305, _0x133140) {
    return _0x2c49f3 ^ _0x6d3305 ^ _0x133140;
  }

  function _0x3ff2a5(_0xb6a2d5, _0x220046, _0xdff9d4) {
    return _0x220046 ^ (_0xb6a2d5 | ~_0xdff9d4);
  }

  function _0x1c7786(_0x4f5d7c, _0x2594bd, _0x5f5151, _0x428be9, _0x8ff2a2, _0x39b7cd, _0xfac110) {
    _0x4f5d7c = _0x42e159(_0x4f5d7c, _0x42e159(_0x42e159(_0x55f2c0(_0x2594bd, _0x5f5151, _0x428be9), _0x8ff2a2), _0xfac110));
    return _0x42e159(_0x3187c8(_0x4f5d7c, _0x39b7cd), _0x2594bd);
  }

  function _0x4c54df(_0x1f6a11, _0x140638, _0x1760ab, _0x4bdd3c, _0x2567a5, _0x20a66c, _0x572217) {
    _0x1f6a11 = _0x42e159(_0x1f6a11, _0x42e159(_0x42e159(_0x272eb2(_0x140638, _0x1760ab, _0x4bdd3c), _0x2567a5), _0x572217));
    return _0x42e159(_0x3187c8(_0x1f6a11, _0x20a66c), _0x140638);
  }

  function _0x471cff(_0x43214e, _0x50a4b3, _0x5a13b2, _0x2ca729, _0x3adfa7, _0x1460be, _0x25d068) {
    _0x43214e = _0x42e159(_0x43214e, _0x42e159(_0x42e159(_0x1bd60a(_0x50a4b3, _0x5a13b2, _0x2ca729), _0x3adfa7), _0x25d068));
    return _0x42e159(_0x3187c8(_0x43214e, _0x1460be), _0x50a4b3);
  }

  function _0x4a70ff(_0x1c4d7f, _0x5606e3, _0x2a1973, _0x12a60f, _0x306e4d, _0x285ada, _0xb8bcac) {
    _0x1c4d7f = _0x42e159(_0x1c4d7f, _0x42e159(_0x42e159(_0x3ff2a5(_0x5606e3, _0x2a1973, _0x12a60f), _0x306e4d), _0xb8bcac));
    return _0x42e159(_0x3187c8(_0x1c4d7f, _0x285ada), _0x5606e3);
  }

  function _0x5da4b4(_0x39d7cd) {
    var _0x2c1cd1 = "9|1|0|11|13|2|3|6|7|10|14|4|12|8|5"["split"]('|');

    var _0x5d435f = 0;

    var _0x1ff6c9;

    var _0x292d5d = _0x39d7cd["length"];

    var _0x4ce8ae = _0x292d5d + 8;

    var _0x1a962c = (_0x4ce8ae - _0x4ce8ae % 64) / 64;

    var _0x50f13e = (_0x1a962c + 1) * 16;

    var _0x43168d = Array(_0x50f13e - 1);

    var _0x4b22ba = 0;
    var _0xe7de51 = 0;

    while (_0xe7de51 < _0x292d5d) {
      _0x1ff6c9 = (_0xe7de51 - _0xe7de51 % 4) / 4;
      _0x4b22ba = _0xe7de51 % 4 * 8;
      _0x43168d[_0x1ff6c9] = _0x43168d[_0x1ff6c9] | _0x39d7cd["charCodeAt"](_0xe7de51) << _0x4b22ba;
      _0xe7de51++;
    }

    _0x1ff6c9 = (_0xe7de51 - _0xe7de51 % 4) / 4;
    _0x4b22ba = _0xe7de51 % 4 * 8;
    _0x43168d[_0x1ff6c9] = _0x43168d[_0x1ff6c9] | 128 << _0x4b22ba;
    _0x43168d[_0x50f13e - 2] = _0x292d5d << 3;
    _0x43168d[_0x50f13e - 1] = _0x292d5d >>> 29;
    return _0x43168d;
  }

  function _0x282525(_0x5d1863) {
    var _0x3e506e = '';
    var _0x72fb56 = '';

    var _0x458e92;

    var _0x58a1f5;

    for (_0x58a1f5 = 0; _0x58a1f5 <= 3; _0x58a1f5++) {
      _0x458e92 = _0x5d1863 >>> _0x58a1f5 * 8 & 255;
      _0x72fb56 = '0' + _0x458e92["toString"](16);
      _0x3e506e = _0x3e506e + _0x72fb56["substr"](_0x72fb56["length"] - 2, 2);
    }

    return _0x3e506e;
  }

  var _0x337c43 = Array();

  var _0x1dbd8f;

  var _0x2bafd8;

  var _0x2f28a5;

  var _0x509fcd;

  var _0x5898f9;

  var _0x1fe3d2;

  var _0x5dd116;

  var _0x36be8e;

  var _0x4811aa;

  var _0x253032 = 7;
  var _0x42545c = 12;
  var _0x2e2e65 = 17;
  var _0x315e8b = 22;
  var _0x21f4d4 = 5;
  var _0x2e9921 = 9;
  var _0x5ea5cc = 14;
  var _0x234ec4 = 20;
  var _0x29a1e2 = 4;
  var _0x1858ec = 11;
  var _0x5828c4 = 16;
  var _0x58942b = 23;
  var _0x2e18e0 = 6;
  var _0x35d25d = 10;
  var _0x52af7d = 15;
  var _0x481e56 = 21;
  _0x337c43 = _0x5da4b4(_0x2434e0);
  _0x1fe3d2 = 1732584193;
  _0x5dd116 = 4023233417;
  _0x36be8e = 2562383102;
  _0x4811aa = 271733878;

  for (_0x1dbd8f = 0; _0x1dbd8f < _0x337c43["length"]; _0x1dbd8f += 16) {
    var _0x5d167d = "35|62|41|49|50|20|36|7|51|32|57|27|19|64|44|68|58|61|21|1|23|9|26|37|65|48|28|45|56|53|22|5|67|17|59|34|71|24|66|10|55|11|46|12|31|40|13|33|69|60|6|3|8|25|18|38|2|63|70|4|43|30|16|14|39|29|54|52|0|15|47|42"["split"]('|');

    var _0x146dd3 = 0;
    _0x2bafd8 = _0x1fe3d2;
    _0x2f28a5 = _0x5dd116;
    _0x509fcd = _0x36be8e;
    _0x5898f9 = _0x4811aa;
    _0x1fe3d2 = _0x1c7786(_0x1fe3d2, _0x5dd116, _0x36be8e, _0x4811aa, _0x337c43[_0x1dbd8f + 0], _0x253032, 3614090360);
    _0x4811aa = _0x1c7786(_0x4811aa, _0x1fe3d2, _0x5dd116, _0x36be8e, _0x337c43[_0x1dbd8f + 1], _0x42545c, 3905402710);
    _0x36be8e = _0x1c7786(_0x36be8e, _0x4811aa, _0x1fe3d2, _0x5dd116, _0x337c43[_0x1dbd8f + 2], _0x2e2e65, 606105819);
    _0x5dd116 = _0x1c7786(_0x5dd116, _0x36be8e, _0x4811aa, _0x1fe3d2, _0x337c43[_0x1dbd8f + 3], _0x315e8b, 3250441966);
    _0x1fe3d2 = _0x1c7786(_0x1fe3d2, _0x5dd116, _0x36be8e, _0x4811aa, _0x337c43[_0x1dbd8f + 4], _0x253032, 4118548399);
    _0x4811aa = _0x1c7786(_0x4811aa, _0x1fe3d2, _0x5dd116, _0x36be8e, _0x337c43[_0x1dbd8f + 5], _0x42545c, 1200080426);
    _0x36be8e = _0x1c7786(_0x36be8e, _0x4811aa, _0x1fe3d2, _0x5dd116, _0x337c43[_0x1dbd8f + 6], _0x2e2e65, 2821735955);
    _0x5dd116 = _0x1c7786(_0x5dd116, _0x36be8e, _0x4811aa, _0x1fe3d2, _0x337c43[_0x1dbd8f + 7], _0x315e8b, 4249261313);
    _0x1fe3d2 = _0x1c7786(_0x1fe3d2, _0x5dd116, _0x36be8e, _0x4811aa, _0x337c43[_0x1dbd8f + 8], _0x253032, 1770035416);
    _0x4811aa = _0x1c7786(_0x4811aa, _0x1fe3d2, _0x5dd116, _0x36be8e, _0x337c43[_0x1dbd8f + 9], _0x42545c, 2336552879);
    _0x36be8e = _0x1c7786(_0x36be8e, _0x4811aa, _0x1fe3d2, _0x5dd116, _0x337c43[_0x1dbd8f + 10], _0x2e2e65, 4294925233);
    _0x5dd116 = _0x1c7786(_0x5dd116, _0x36be8e, _0x4811aa, _0x1fe3d2, _0x337c43[_0x1dbd8f + 11], _0x315e8b, 2304563134);
    _0x1fe3d2 = _0x1c7786(_0x1fe3d2, _0x5dd116, _0x36be8e, _0x4811aa, _0x337c43[_0x1dbd8f + 12], _0x253032, 1804603682);
    _0x4811aa = _0x1c7786(_0x4811aa, _0x1fe3d2, _0x5dd116, _0x36be8e, _0x337c43[_0x1dbd8f + 13], _0x42545c, 4254626195);
    _0x36be8e = _0x1c7786(_0x36be8e, _0x4811aa, _0x1fe3d2, _0x5dd116, _0x337c43[_0x1dbd8f + 14], _0x2e2e65, 2792965006);
    _0x5dd116 = _0x1c7786(_0x5dd116, _0x36be8e, _0x4811aa, _0x1fe3d2, _0x337c43[_0x1dbd8f + 15], _0x315e8b, 1236535329);
    _0x1fe3d2 = _0x4c54df(_0x1fe3d2, _0x5dd116, _0x36be8e, _0x4811aa, _0x337c43[_0x1dbd8f + 1], _0x21f4d4, 4129170786);
    _0x4811aa = _0x4c54df(_0x4811aa, _0x1fe3d2, _0x5dd116, _0x36be8e, _0x337c43[_0x1dbd8f + 6], _0x2e9921, 3225465664);
    _0x36be8e = _0x4c54df(_0x36be8e, _0x4811aa, _0x1fe3d2, _0x5dd116, _0x337c43[_0x1dbd8f + 11], _0x5ea5cc, 643717713);
    _0x5dd116 = _0x4c54df(_0x5dd116, _0x36be8e, _0x4811aa, _0x1fe3d2, _0x337c43[_0x1dbd8f + 0], _0x234ec4, 3921069994);
    _0x1fe3d2 = _0x4c54df(_0x1fe3d2, _0x5dd116, _0x36be8e, _0x4811aa, _0x337c43[_0x1dbd8f + 5], _0x21f4d4, 3593408605);
    _0x4811aa = _0x4c54df(_0x4811aa, _0x1fe3d2, _0x5dd116, _0x36be8e, _0x337c43[_0x1dbd8f + 10], _0x2e9921, 38016083);
    _0x36be8e = _0x4c54df(_0x36be8e, _0x4811aa, _0x1fe3d2, _0x5dd116, _0x337c43[_0x1dbd8f + 15], _0x5ea5cc, 3634488961);
    _0x5dd116 = _0x4c54df(_0x5dd116, _0x36be8e, _0x4811aa, _0x1fe3d2, _0x337c43[_0x1dbd8f + 4], _0x234ec4, 3889429448);
    _0x1fe3d2 = _0x4c54df(_0x1fe3d2, _0x5dd116, _0x36be8e, _0x4811aa, _0x337c43[_0x1dbd8f + 9], _0x21f4d4, 568446438);
    _0x4811aa = _0x4c54df(_0x4811aa, _0x1fe3d2, _0x5dd116, _0x36be8e, _0x337c43[_0x1dbd8f + 14], _0x2e9921, 3275163606);
    _0x36be8e = _0x4c54df(_0x36be8e, _0x4811aa, _0x1fe3d2, _0x5dd116, _0x337c43[_0x1dbd8f + 3], _0x5ea5cc, 4107603335);
    _0x5dd116 = _0x4c54df(_0x5dd116, _0x36be8e, _0x4811aa, _0x1fe3d2, _0x337c43[_0x1dbd8f + 8], _0x234ec4, 1163531501);
    _0x1fe3d2 = _0x4c54df(_0x1fe3d2, _0x5dd116, _0x36be8e, _0x4811aa, _0x337c43[_0x1dbd8f + 13], _0x21f4d4, 2850285829);
    _0x4811aa = _0x4c54df(_0x4811aa, _0x1fe3d2, _0x5dd116, _0x36be8e, _0x337c43[_0x1dbd8f + 2], _0x2e9921, 4243563512);
    _0x36be8e = _0x4c54df(_0x36be8e, _0x4811aa, _0x1fe3d2, _0x5dd116, _0x337c43[_0x1dbd8f + 7], _0x5ea5cc, 1735328473);
    _0x5dd116 = _0x4c54df(_0x5dd116, _0x36be8e, _0x4811aa, _0x1fe3d2, _0x337c43[_0x1dbd8f + 12], _0x234ec4, 2368359562);
    _0x1fe3d2 = _0x471cff(_0x1fe3d2, _0x5dd116, _0x36be8e, _0x4811aa, _0x337c43[_0x1dbd8f + 5], _0x29a1e2, 4294588738);
    _0x4811aa = _0x471cff(_0x4811aa, _0x1fe3d2, _0x5dd116, _0x36be8e, _0x337c43[_0x1dbd8f + 8], _0x1858ec, 2272392833);
    _0x36be8e = _0x471cff(_0x36be8e, _0x4811aa, _0x1fe3d2, _0x5dd116, _0x337c43[_0x1dbd8f + 11], _0x5828c4, 1839030562);
    _0x5dd116 = _0x471cff(_0x5dd116, _0x36be8e, _0x4811aa, _0x1fe3d2, _0x337c43[_0x1dbd8f + 14], _0x58942b, 4259657740);
    _0x1fe3d2 = _0x471cff(_0x1fe3d2, _0x5dd116, _0x36be8e, _0x4811aa, _0x337c43[_0x1dbd8f + 1], _0x29a1e2, 2763975236);
    _0x4811aa = _0x471cff(_0x4811aa, _0x1fe3d2, _0x5dd116, _0x36be8e, _0x337c43[_0x1dbd8f + 4], _0x1858ec, 1272893353);
    _0x36be8e = _0x471cff(_0x36be8e, _0x4811aa, _0x1fe3d2, _0x5dd116, _0x337c43[_0x1dbd8f + 7], _0x5828c4, 4139469664);
    _0x5dd116 = _0x471cff(_0x5dd116, _0x36be8e, _0x4811aa, _0x1fe3d2, _0x337c43[_0x1dbd8f + 10], _0x58942b, 3200236656);
    _0x1fe3d2 = _0x471cff(_0x1fe3d2, _0x5dd116, _0x36be8e, _0x4811aa, _0x337c43[_0x1dbd8f + 13], _0x29a1e2, 681279174);
    _0x4811aa = _0x471cff(_0x4811aa, _0x1fe3d2, _0x5dd116, _0x36be8e, _0x337c43[_0x1dbd8f + 0], _0x1858ec, 3936430074);
    _0x36be8e = _0x471cff(_0x36be8e, _0x4811aa, _0x1fe3d2, _0x5dd116, _0x337c43[_0x1dbd8f + 3], _0x5828c4, 3572445317);
    _0x5dd116 = _0x471cff(_0x5dd116, _0x36be8e, _0x4811aa, _0x1fe3d2, _0x337c43[_0x1dbd8f + 6], _0x58942b, 76029189);
    _0x1fe3d2 = _0x471cff(_0x1fe3d2, _0x5dd116, _0x36be8e, _0x4811aa, _0x337c43[_0x1dbd8f + 9], _0x29a1e2, 3654602809);
    _0x4811aa = _0x471cff(_0x4811aa, _0x1fe3d2, _0x5dd116, _0x36be8e, _0x337c43[_0x1dbd8f + 12], _0x1858ec, 3873151461);
    _0x36be8e = _0x471cff(_0x36be8e, _0x4811aa, _0x1fe3d2, _0x5dd116, _0x337c43[_0x1dbd8f + 15], _0x5828c4, 530742520);
    _0x5dd116 = _0x471cff(_0x5dd116, _0x36be8e, _0x4811aa, _0x1fe3d2, _0x337c43[_0x1dbd8f + 2], _0x58942b, 3299628645);
    _0x1fe3d2 = _0x4a70ff(_0x1fe3d2, _0x5dd116, _0x36be8e, _0x4811aa, _0x337c43[_0x1dbd8f + 0], _0x2e18e0, 4096336452);
    _0x4811aa = _0x4a70ff(_0x4811aa, _0x1fe3d2, _0x5dd116, _0x36be8e, _0x337c43[_0x1dbd8f + 7], _0x35d25d, 1126891415);
    _0x36be8e = _0x4a70ff(_0x36be8e, _0x4811aa, _0x1fe3d2, _0x5dd116, _0x337c43[_0x1dbd8f + 14], _0x52af7d, 2878612391);
    _0x5dd116 = _0x4a70ff(_0x5dd116, _0x36be8e, _0x4811aa, _0x1fe3d2, _0x337c43[_0x1dbd8f + 5], _0x481e56, 4237533241);
    _0x1fe3d2 = _0x4a70ff(_0x1fe3d2, _0x5dd116, _0x36be8e, _0x4811aa, _0x337c43[_0x1dbd8f + 12], _0x2e18e0, 1700485571);
    _0x4811aa = _0x4a70ff(_0x4811aa, _0x1fe3d2, _0x5dd116, _0x36be8e, _0x337c43[_0x1dbd8f + 3], _0x35d25d, 2399980690);
    _0x36be8e = _0x4a70ff(_0x36be8e, _0x4811aa, _0x1fe3d2, _0x5dd116, _0x337c43[_0x1dbd8f + 10], _0x52af7d, 4293915773);
    _0x5dd116 = _0x4a70ff(_0x5dd116, _0x36be8e, _0x4811aa, _0x1fe3d2, _0x337c43[_0x1dbd8f + 1], _0x481e56, 2240044497);
    _0x1fe3d2 = _0x4a70ff(_0x1fe3d2, _0x5dd116, _0x36be8e, _0x4811aa, _0x337c43[_0x1dbd8f + 8], _0x2e18e0, 1873313359);
    _0x4811aa = _0x4a70ff(_0x4811aa, _0x1fe3d2, _0x5dd116, _0x36be8e, _0x337c43[_0x1dbd8f + 15], _0x35d25d, 4264355552);
    _0x36be8e = _0x4a70ff(_0x36be8e, _0x4811aa, _0x1fe3d2, _0x5dd116, _0x337c43[_0x1dbd8f + 6], _0x52af7d, 2734768916);
    _0x5dd116 = _0x4a70ff(_0x5dd116, _0x36be8e, _0x4811aa, _0x1fe3d2, _0x337c43[_0x1dbd8f + 13], _0x481e56, 1309151649);
    _0x1fe3d2 = _0x4a70ff(_0x1fe3d2, _0x5dd116, _0x36be8e, _0x4811aa, _0x337c43[_0x1dbd8f + 4], _0x2e18e0, 4149444226);
    _0x4811aa = _0x4a70ff(_0x4811aa, _0x1fe3d2, _0x5dd116, _0x36be8e, _0x337c43[_0x1dbd8f + 11], _0x35d25d, 3174756917);
    _0x36be8e = _0x4a70ff(_0x36be8e, _0x4811aa, _0x1fe3d2, _0x5dd116, _0x337c43[_0x1dbd8f + 2], _0x52af7d, 718787259);
    _0x5dd116 = _0x4a70ff(_0x5dd116, _0x36be8e, _0x4811aa, _0x1fe3d2, _0x337c43[_0x1dbd8f + 9], _0x481e56, 3951481745);
    _0x1fe3d2 = _0x42e159(_0x1fe3d2, _0x2bafd8);
    _0x5dd116 = _0x42e159(_0x5dd116, _0x2f28a5);
    _0x36be8e = _0x42e159(_0x36be8e, _0x509fcd);
    _0x4811aa = _0x42e159(_0x4811aa, _0x5898f9);
  }

  var _0x1ec3a9 = _0x282525(_0x1fe3d2) + _0x282525(_0x5dd116) + _0x282525(_0x36be8e) + _0x282525(_0x4811aa);

  return _0x1ec3a9["toLowerCase"]();
}

function go(_0x59d9b8) {
  function _0x2d06fb() {
    var _0x1b30b1 = window["navigator"]["userAgent"];
    var _0x4d3f20 = ["Phantom"];

    for (var _0x4937e2 = 0; _0x4937e2 < _0x4d3f20["length"]; _0x4937e2++) {
      if (_0x1b30b1["indexOf"](_0x4d3f20[_0x4937e2]) != -1) {
        return true;
      }
    }

    if (window["callPhantom"] || window["_phantom"] || window["Headless"] || window["navigator"]["webdriver"] || window["navigator"]["__driver_evaluate"] || window["navigator"]["__webdriver_evaluate"]) {
      return true;
    }
  }

  if (_0x2d06fb()) {
    return;
  }

  var _0x5b5a50 = new Date();

  function _0xb06fd4(_0x58fefe, _0x316070) {
    var _0x5364b0 = _0x59d9b8["chars"]["length"];

    for (var _0x504c47 = 0; _0x504c47 < _0x5364b0; _0x504c47++) {
      for (var _0x313f8e = 0; _0x313f8e < _0x5364b0; _0x313f8e++) {
        var _0x1ee179 = _0x316070[0] + _0x59d9b8["chars"]["substr"](_0x504c47, 1) + _0x59d9b8["chars"]["substr"](_0x313f8e, 1) + _0x316070[1];

        if (hash(_0x1ee179) == _0x58fefe) {
          return [_0x1ee179, new Date() - _0x5b5a50];
        }
      }
    }
  }

  var _0xae701d = _0xb06fd4(_0x59d9b8['ct'], _0x59d9b8["bts"]);
  console.log(_0xae701d);

  if (_0xae701d) {
    var _0x4b12e4;

    if (_0x59d9b8['wt']) {
      _0x4b12e4 = parseInt(_0x59d9b8['wt']) > _0xae701d[1] ? parseInt(_0x59d9b8['wt']) - _0xae701d[1] : 500;
    } else {
      _0x4b12e4 = 1500;
    }

    setTimeout(function () {
      document["cookie"] = _0x59d9b8['tn'] + '=' + _0xae701d[0] + ";Max-age=" + _0x59d9b8['vt'] + "; path = /";
      // location["href"] = location["pathname"] + location["search"];
    }, _0x4b12e4);
  } else {
    alert("è¯·æ±éªè¯å¤±è´¥");
  }
}

go({
  "bts": ["1680752333.703|0|Y6t", "sRQ5uvxYxOy4jzI2aoGzMs%3D"],
  "chars": "iUprIWP1gmNgwirbpRBtWq",
  "ct": "0d251b96a5d8b9db464aec5a2f2e053a",
  "ha": "md5",
  "tn": "__jsl_clearance_s",
  "vt": "3600",
  "wt": "1500"
});

