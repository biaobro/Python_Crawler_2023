# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : utils.py
@Project            : S035_HangHangCha
@CreateTime         : 2023/3/15 16:44
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/15 16:44 
@Version            : 1.0
@Description        : None
"""


def flat_key(layer):
    """ Example: flat_key(["1","2",3,4]) -> "1[2][3][4]" """
    if len(layer) == 1:
        return layer[0]
    else:
        _list = ["[{}]".format(k) for k in layer[1:]]
        return layer[0] + "".join(_list)


def flat_dict(_dict):
    if not isinstance(_dict, dict):
        raise TypeError("argument must be a dict, not {}".format(type(_dict)))

    def __flat_dict(pre_layer, value):
        result = {}
        for k, v in value.items():
            layer = pre_layer[:]
            layer.append(k)
            if isinstance(v, dict):
                result.update(__flat_dict(layer, v))
            else:
                result[flat_key(layer)] = v
        return result

    return __flat_dict([], _dict)
