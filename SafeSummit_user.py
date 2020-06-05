from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

bs = webdriver.Chrome()
bs.maximize_window()
bs.implicitly_wait(3)
# 进入智慧理工登陆页面
bs.get("http://ids.njust.edu.cn/authserver/login?service=http%3A%2F%2Fehall.njust.edu.cn%2Flogin%3Fservice%3Dhttp%3A%2F%2Fehall.njust.edu.cn%2Fnew%2Findex.html")
bs.implicitly_wait(3)
bs.find_element_by_id("username").send_keys("123456789")# 这里是用户名
bs.implicitly_wait(3)
bs.find_element_by_id("password").send_keys("123456789")# 差点把我自己的密码给push上来了
bs.implicitly_wait(3)
bs.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[3]/div/form/p[5]/button").click()
bs.implicitly_wait(3)
# 以上登陆智慧理工

# 从热门应用中点击报平安
bs.implicitly_wait(20)
ele = bs.find_element_by_xpath('/html/body/article[5]/section/div[2]/div[1]/div[4]/pc-card-html-4786697535230905-01/amp-w-frame/div/div[2]/div/div[1]/widget-app-item[7]/div/div/div[2]/div[1]')
ActionChains(bs).move_to_element(ele).perform()
ActionChains(bs).click().perform()
bs.implicitly_wait(3)

# 点击进入服务
print(bs.current_window_handle)
bs.find_element_by_id('ampDetailEnter').click()
bs.implicitly_wait(3)

print(bs.current_window_handle)
# 获取当前页句柄
n = bs.window_handles
print(n)
# 切换到新的网页窗口
bs.switch_to.window(n[1])

# 填写电话号码 //*[@id="V1_CTRL4"] #V1_CTRL4
time.sleep(5)
bs.find_element_by_xpath("/html/body/div[4]/form/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td[4]/div/input").send_keys("13365339364")# 这里改成你的电话号码，前面是我的，算是偷偷留个联系方式吧🌝🌝
bs.implicitly_wait(3)

# 勾选 本人承诺以上填写内容真实可靠
bs.find_element_by_xpath("/html/body/div[4]/form/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[49]/td/div/font/input").click()
bs.implicitly_wait(3)

# 确认填报，提交（鼠标悬停、点击）
# ele = bs.find_element_by_xpath('//a[@class="command_button_content"]')
ele = bs.find_element_by_xpath('/html/body/div[4]/form/div/div[2]/div[3]/div/div[1]/div[3]/ul/li')
ActionChains(bs).move_to_element(ele).perform()
ActionChains(bs).click().perform()

# bs.find_element_by_xpath('//a[@class="command_button_content"]').send_keys(Keys.ENTER)
bs.implicitly_wait(3)

bs.find_element_by_xpath("/html/body/div[7]/div/div[2]/button[1]").click()
bs.implicitly_wait(3)
# bs.quit()
