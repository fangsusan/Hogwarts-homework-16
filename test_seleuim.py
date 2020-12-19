import time

import allure
import yaml
from selenium import webdriver


class Test_Weixin:
    # 使用序列化cookie的方法进行登录
    # 获取cookie，序列化后存入yaml文件内
    # def test_get_cookie(self):
    #     opt = webdriver.ChromeOptions()
    #   # 设置debug地址
    #     opt.debugger_address = "127.0.0.1:9222"
    #       # 开启debug地址
    #     driver = webdriver.Chrome(options=opt)
    #     driver.implicitly_wait(5)
    #       # 先打开目标网站，企业微信的扫码登录的页面
    #     driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    #     # driver.find_element_by_id("menu_contacts").click()
    #     cookie = driver.get_cookies()
    #     print(cookie)
    #     with open("cookie_data.yaml","w",encoding="UTF-8") as f:
    #         yaml.dump(cookie,f)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @allure.title("复用浏览器，跳过登录，新增成员")
    def test_login(self):
        opt = webdriver.ChromeOptions()
    #     # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        # cookie = driver.get_cookies()
        with open("cookie_data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(10)
        driver.find_element_by_id("menu_contacts").click()
        time.sleep(5)

        with open("./add_mem.yaml") as f:
            add_mem = yaml.safe_load(f)
            for add_number_data in add_mem:
                username = add_mem["username"]
                acctid = add_mem["memberAdd_acctid"]
                phone = add_mem["memberAdd_phone"]

        # 跳转到新增成员页面
        with allure.step("跳转至新增成员页面"):
            driver.find_element_by_css_selector("[class=ww_operationBar] a:nth-child(2)").click()
            driver.find_element_by_id("username").send_keys(username)
            driver.find_element_by_id("memberAdd_acctid").send_keys(acctid)
            driver.find_element_by_id("memberAdd_phone").send_keys(phone)
            driver.find_element_by_link_text("保存").click()

        # 断言
        # assert driver.find_element_by_id("party_name")