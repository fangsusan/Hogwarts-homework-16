import time

import yaml
from selenium import webdriver


class Test_Weixin:
  # 复用浏览器
    def test_weixin(self):
         opt = webdriver.ChromeOptions()   #设置代理
      # 设置debug地址
         opt.debugger_address = "127.0.0.1:9222"
         driver = webdriver.Chrome(options=opt)
          # driver.get("http://www.baidu.com")
         driver.implicitly_wait(5)
         driver.get("https://work.weixin.qq.com/wework_admin/frame")
         driver.find_element_by_id("menu_contacts").click()
         print(driver.get_cookies())

# 使用cookie登录
    def test_cookie(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '1ZU6kh1msPT_OoUIY3_SI1F8Uu7GLoNAHI7xlteiCGXtuPL7R0CIPg4MxYUFum6MmH0ZFK0rjAB3okI2q9S6AWGuio6d0JnGzgAen-KSghuj078sX8fYVphgvlLMtHk5fsEPZlvoidC76wWcQlMSQX20VQBDc_5HfQIz5jF92JRMC-yDFNc0uiTZ1aMlXKQdheZMHaxG6_9ubE1Dco30-9A0eWEmKMXXHD0p9NmZzUh_lhypQF0dHxL-RuwVsfWnroMpuiPxjNBl5Sn2Q6NlPw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '7gJNsUJeMLu8tx83a4D0LuErbYqWgtnsnKLWAmtC_-CWYZZPdpjnkLWq0XA0tkPS'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a8654368'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850407896350'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850407896350'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325098204094'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '7949046174'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639742829, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1608206821'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': 'work.weixin.qq.com', 'expiry': 1608304769, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '2oio9gj'}, {'domain': '.qq.com', 'expiry': 1608360782, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.148551028.1608206821'}, {'domain': '.qq.com', 'expiry': 1671346382, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2064294516.1605166952'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636702950, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1610866382, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '22822722952365680'}, {'domain': '.qq.com', 'expiry': 1608274442, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '9836817408'}]
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element_by_id("menu_contacts").click()
        time.sleep(5)
        driver.quit()

        # 获取cookie，序列化后存入yaml文件内
    def test_get_cookie(self):
          opt = webdriver.ChromeOptions()
      # 设置debug地址
          opt.debugger_address = "127.0.0.1:9222"
          driver = webdriver.Chrome(options=opt)
          driver.implicitly_wait(5)
          driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
          cookie = driver.get_cookies()
          print(cookie)
          with open("cookie_data.yaml", "w", encoding="UTF-8") as f:
               yaml.dump(cookie,f)

  # 使用序列化cookie的方法进行登录
    def test_login(self):
         driver = webdriver.Chrome()
         driver.implicitly_wait(5)
         driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
         with open("cookie_data.yaml", encoding="UTF-8") as f:
             yaml_data = yaml.safe_load(f)
             for cookie in yaml_data:
                 driver.add_cookie(cookie)
         driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
         time.sleep(10)
