import io
import json
import requests
from requests.models import HTTPError
import urllib3
from Ocr import GetCodeFromByte

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# 利用企业ID和corps
# ecret构造request请求，获取access_token
def get_code():
    url = r"https://im.dgitc.net/msjsAjaxHandlerRoad/UserAction.msjs?acttype=GetValCode&0.7731219702467694"

    # 构造数据包头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }
    # 发起get请求
    try:
        res = requests.get(url=url, headers=headers, verify=False)
        print(GetCodeFromByte(res.content))

    except requests.HTTPError as e:
        print(e.errno)


# 利用url+access_token,提交学生数据
def info_send(access_token, body_json):
    # url+access_token拼接新的访问请求
    url = (
        r"https://qyapi.weixin.qq.com/cgi-bin/oa/applyevent?access_token="
        + access_token
    )

    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    }

    data = body_json.encode("utf-8")
    try:
        res = requests.post(url=url, data=data, headers=headers, verify=False)
        # 打印返回信息
        if res.status_code == 200:
            resJson = json.loads(res.text)
            if resJson["errcode"] == 0:
                return "发送成功！请返回企业微信中，请在企业微信关注审批状态变化"
            else:
                return f'错误代码：{resJson["errcode"]},错误原因：{resJson["errmsg"]}'
    except requests.HTTPError as e:
        return "网络错误。"


def main():
    # 获取验证码
    code = get_code()


if __name__ == "__main__":
    main()
