import datetime
import time
from urllib.error import HTTPError
from selenium import webdriver
from selenium.webdriver.common.by import By
import Ocr
from robot import send_message


def Login(username, password):
    try:
        url = "http://210.76.75.168/gdjkjc/aLogIn.m"

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--ignore-ssl-errors")

        driver = webdriver.Chrome(
            executable_path=r"D:\OneDrive - 华南师范大学\陈沛华文件\workspaces\gdjkjc_auto_login_win\chromedriver.exe",
            options=chrome_options,
        )

        # 打开登录页面，url为要打开的地址
        driver.get(url)

        # 最大化浏览器
        # driver.maximize_window()

        # 元素定位到用户名输入框，输入用户名
        driver.find_element(By.ID, "username").send_keys(username)

        # 元素定位到密码输入框，并输入密码
        driver.find_element(By.ID, "password").send_keys(password)

        # 元素定位到验证码
        randImage = driver.find_element(By.ID, "randImage")
        # 获取验证码
        data = randImage.screenshot_as_png
        # OCR识别验证码
        res = Ocr.GetCodeFromByte(data)

        # 元素定位到验证码，并输入验证码
        driver.find_element(By.ID, "rand").send_keys(res)

        # 元素定位到登录按钮，并点击登录
        driver.find_element(By.ID, "submitForm").click()
        time.sleep(10)

        # 登录成功后开始操作
        # 打开网页左边收起来的菜单栏

        driver.find_element(By.XPATH, '//*[@id="menuContent"]/li[1]/span/span').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="menuContent"]/li[2]/span/span').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="menuContent"]/li[4]/span/span').click()
        time.sleep(5)
        # 网页切换到iframe
        driver.switch_to.frame("rightFrame")
        time.sleep(5)
        driver.find_element(By.ID, "lsbxz").click()
        time.sleep(15)
        driver.find_element(By.ID, "lsbxz1").click()
        time.sleep(5)
        driver.find_element(By.ID, "ok").click()
        return True

    except HTTPError:
        return False


if __name__ == "__main__":
    now_time = datetime.datetime.now()

    users_list = [
        {"name": "陈沛华", "username": "13652520301", "password": "ABCabc135"},
        {"name": "邢彦年", "username": "18566122558", "password": "ABCabc123"},
        {"name": "郭美娟", "username": "13078497884", "password": "283786Gmj"},
        {"name": "温沃滢", "username": "13702637986", "password": "Wen5747642"},
        {"name": "蔡其恩", "username": "17858990065", "password": "21WLJS2b"},
        {"name": "钟启文", "username": "18826842322", "password": "ABCabc123"},
        {"name": "张美霞", "username": "15112791145", "password": "Zmx123456"},
    ]

    for user in users_list:
        msg = {
            "msgtype": "markdown",
            "markdown": {"content": "**%s 零上报成功！**    `儿童青少年健康监测`" % user["name"]},
        }

        if Login(user["username"], user["password"]):
            send_message(msg)
