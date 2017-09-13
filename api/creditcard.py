import json
import urllib
from urllib.parse import urlencode
from urllib.request import urlopen


# 身份证信息查询
def imformation(cardno, m="GET"):
    appkey = "ee87a73550dc1edc8f51ca73c796b79b"
    url = "http://apis.juhe.cn/idcard/index"
    params = {
        "cardno": cardno,  # 身份证号码
        "dtype": "",  
        "key": appkey,

    }
    params = urlencode(params)
    if m == "GET":
        f = urlopen("%s?%s" % (url, params))
    else:
        f = urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            return res["result"]
        else:
            return "%s:%s" % (res["error_code"], res["reason"])
    else:
        return "request api error"
