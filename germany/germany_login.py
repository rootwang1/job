import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Cookie": "",
}
bro = webdriver.Chrome()

# 发送请求
bro.get('https://visa.vfsglobal.com/chn/zh/deu/login',)
time.sleep(15)

# 模拟登录
username = WebDriverWait(bro, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='username']")))
username.send_keys('1733763500@qq.com')
password = WebDriverWait(bro, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='password']")))
password.send_keys('Wangsheng12!')
time.sleep(3)
dian = bro.find_element(By.ID, 'widgetId')
ActionChains(bro).move_to_element(dian).click().perform()
time.sleep(10)

bro.quit()  # 关闭浏览器
