import requests


def send_message(msg):
    # robot webhook
    url = r"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ce1718e9-7db8-40d8-8d16-c9eb4028b62f"

    # 构造数据包头
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    # 发起post请求
    try:
        res = requests.post(url=url, json=msg, headers=headers, verify=False)
        res.encoding = "utf-8"
        return True
    except requests.HTTPError as e:
        print(e.errno)