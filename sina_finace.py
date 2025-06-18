import requests
from bs4 import BeautifulSoup
import pandas as pd
import pprint

# A股银行字典
BANKS_IN_STOCK_A = [
    {"code": "601398", "name": "工商银行"},
    {"code": "600036", "name": "招商银行"},
    {"code": "601288", "name": "农业银行"},
    {"code": "601988", "name": "中国银行"},
    {"code": "000001", "name": "平安银行"},
    {"code": "601939", "name": "建设银行"},
    {"code": "601166", "name": "兴业银行"},
    {"code": "601328", "name": "交通银行"},
    {"code": "600016", "name": "民生银行"},
    {"code": "601658", "name": "邮储银行"},
    {"code": "600919", "name": "江苏银行"},
    {"code": "601169", "name": "北京银行"},
    {"code": "601916", "name": "浙商银行"},
    {"code": "600000", "name": "浦发银行"},
    {"code": "603323", "name": "苏农银行"},
    {"code": "601009", "name": "南京银行"},
    {"code": "601998", "name": "中信银行"},
    {"code": "002142", "name": "宁波银行"},
    {"code": "601818", "name": "光大银行"},
    {"code": "600015", "name": "华夏银行"},
    {"code": "600926", "name": "杭州银行"},
    {"code": "601997", "name": "贵阳银行"},
    {"code": "601229", "name": "上海银行"},
    {"code": "600928", "name": "西安银行"},
    {"code": "601860", "name": "紫金银行"},
    {"code": "002936", "name": "郑州银行"},
    {"code": "601838", "name": "成都银行"},
    {"code": "601128", "name": "常熟银行"},
    {"code": "601528", "name": "瑞丰银行"},
    {"code": "001227", "name": "兰州银行"},
    {"code": "002807", "name": "江阴银行"},
    {"code": "002966", "name": "苏州银行"},
    {"code": "601963", "name": "重庆银行"},
    {"code": "601187", "name": "厦门银行"},
    {"code": "600908", "name": "无锡银行"},
    {"code": "002948", "name": "青岛银行"},
    {"code": "601665", "name": "齐鲁银行"},
    {"code": "601577", "name": "长沙银行"},
]

# 港股银行字典
BANKS_IN_STOCK_H = [
    {"code": "00939", "name": "建设银行"},
    {"code": "01398", "name": "工商银行"},
    {"code": "03968", "name": "招商银行"},
    {"code": "03988", "name": "中国银行"},
    {"code": "01288", "name": "农业银行"},
    {"code": "01658", "name": "邮储银行"},
    {"code": "01988", "name": "民生银行"},
    {"code": "00998", "name": "中信银行"},
    {"code": "03328", "name": "交通银行"},
    {"code": "02016", "name": "浙商银行"},
    {"code": "00011", "name": "恒生银行"},
    {"code": "06818", "name": "中国光大银行"},
    {"code": "03618", "name": "重庆农村商业银行"},
    {"code": "06199", "name": "贵州银行"},
    {"code": "03866", "name": "青岛银行"},
    {"code": "06196", "name": "郑州银行"},
    {"code": "00023", "name": "东亚银行"},
    {"code": "01963", "name": "重庆银行"},
    {"code": "03698", "name": "徽商银行"},
    {"code": "06138", "name": "哈尔滨银行"},
    {"code": "09889", "name": "东莞农商银行"},
    {"code": "01578", "name": "天津银行"},
    {"code": "09668", "name": "渤海银行"},
    {"code": "01916", "name": "江西银行"},
    {"code": "01551", "name": "广州农商银行"},
    {"code": "01216", "name": "中原银行"},
    {"code": "02066", "name": "盛京银行"},
    {"code": "02139", "name": "甘肃银行"},
    {"code": "02356", "name": "大新银行集团"},
    {"code": "hsmbi", "name": "恒生中国内地银行业指数"},
    {"code": "06122", "name": "九台农商银行"},
    {"code": "80011", "name": "恒生银行-R"},
    {"code": "06190", "name": "九江银行"},
    {"code": "01983", "name": "泸州银行"},
    {"code": "02596", "name": "宜宾银行"},
    {"code": "02558", "name": "晋商银行"},
    {"code": "09677", "name": "威海银行"},
]


def get_banks_dividend():
    """新浪财经分红数据抓取函数"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Referer": "https://finance.sina.com.cn/",
    }

    for bank in BANKS_IN_STOCK_A:
        # A股获取链接
        url = f"https://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_ShareBonus/stockid/{bank['code']}.phtml"
        # H股获取链接
        # url = "https://stock.finance.sina.com.cn/hkstock/dividends/00939.html"

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            # 设置网页编码检测，防止中文乱码
            if response.encoding == "ISO-8859-1":
                response.encoding = "gb2312"

            # 创建bs4解析对象
            soup = BeautifulSoup(response.text, "lxml")
            # 查找分红表格
            table = soup.find("table", id="sharebonus_1")

            if not table:
                print("未找到分红表格，建议手动检查页面结构。")
                print(f"你可以在终端运行：$BROWSER {url}")
                return pd.DataFrame()

            # 解释列
            columns = [th.get_text(strip=True) for th in table.select("tr th")]
            # 只取前5列
            columns = columns[1:7]
            # 调整表头
            lis = ["送股(股)", "转赠(股)", "派息(税前)(元)"]
            columns[1:2] = lis
            # print("解析到的表头：", columns)

            data = []
            # 解释行
            for row in table.select("tbody tr"):
                cells = [td.get_text(strip=True) for td in row.select("td")]
                cells = cells[:-1]  # 去掉最后一个单元格（查看详细链接）
                # print(cells)
                # 如果行数据长度与列数匹配，则解析该行
                if len(cells) == len(columns):
                    row_dict = dict(zip(columns, cells))
                    try:
                        record = {
                            "股票类型": "A股",
                            "股票代码": bank["code"],
                            "股票名称": bank["name"],
                            "公告日期": row_dict.get("公告日期"),
                            "除净日": row_dict.get("除权除息日"),
                            "派息(税前)(元)": row_dict.get("派息(税前)(元)"),
                            "派息日": row_dict.get("除权除息日"),
                        }
                        data.append(record)
                    except Exception as e:
                        print("解析某行数据失败：", row_dict, e)

                # 将数据保存到DRF中

            # 打印已经获得的数据
            print("解析到的数据行数：", len(data))

        except Exception as e:
            print(f"数据获取失败，错误类型：{type(e).__name__}, 详情：{str(e)}")
            return pd.DataFrame()


if __name__ == "__main__":
    df = get_banks_dividend()
