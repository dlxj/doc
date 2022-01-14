
# https://jishuin.proginn.com/p/763bfbd5a01a

# pip install seleniu


from selenium import webdriver

if __name__  ==  "__main__": 

    # python目录下必须有chromedriver.exe （http://chromedriver.storage.googleapis.com/index.html 这里下载和当前使用版本一致的）
    wd=webdriver.Chrome()
    wd.implicitly_wait(1)

    # open
    url = 'https://www.pdawiki.com/forum/'
    wd.get(url)

    input_usernanme = wd.find_element_by_xpath('//*[@id="ls_username"]')
    input_usernanme.send_keys('howdyhappy')

    input_passwd = wd.find_element_by_xpath('//*[@id="ls_password"]')
    input_passwd.send_keys('v14')

    input_login = wd.find_element_by_xpath('//*[@id="lsform"]/div/div[1]/table/tbody/tr[2]/td[3]/button')
    input_login.click()

    """
    <input type="text" name="username" id="ls_username" autocomplete="off" class="px vm" tabindex="901">
    //*[@id="lsform"]/div/div[1]/table/tbody/tr[2]/td[3]/button
    //*[@id="ls_password"]  # 找到元素，复制 xpath
    """

    a = 1


# from selenium import webdriver#导入库
# browser = webdriver.Chrome()#声明浏览器

# # username = "xxxxxx"
# # password = "xxxxxx"
# # 模拟浏览器打开网站
# def AutoSign(username, password):
#     chrome_options = Options()
#     # 使用无界面浏览器
#     chrome_options.add_argument('--headless')
#     browser = webdriver.Chrome(options=chrome_options)
#     browser.get(url)
#     locator = (By.XPATH, '//*[@id="login_box"]/ul/li[1]/div/input')

#     # 延时2秒，以便网页加载所有元素，避免之后找不到对应的元素
#     # time.sleep(2)
#     WebDriverWait(browser, 3, 0.3).until(EC.presence_of_element_located(locator))

#     # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
#     browser.find_element_by_xpath('//*[@id="login_box"]/ul/li[1]/div/input').send_keys(username)
#     browser.find_element_by_xpath('//*[@id="login_box"]/ul/li[2]/div/input').send_keys(password)
#     # 在输入用户名和密码之后,点击登陆按钮
#     browser.find_element_by_xpath('//*[@id="login_box"]/div[2]/button[1]').click()
#     WebDriverWait(browser, 3, 0.3).until(EC.visibility_of_element_located((By.ID, 'name-a')))
#     time.sleep(0.5)
#     browser.execute_script("window.scrollTo(0,1000);")
#     # 点击登陆后的页面中的签到,跳转到签到页面
#     browser.find_element_by_xpath('//*[@id="member"]/div[6]/div/div[2]/div[1]/div/div/h3').click()
#     # time.sleep(1)
#     # browser.execute_script("window.scrollTo(0,1000);")
#     # time.sleep(1)
#     browser.find_element_by_xpath('//*[@id="member"]/div[6]/div/div[2]/div[2]/div/div/a[1]/div').click()
#     # time.sleep(2)
#     WebDriverWait(browser, 2, 0.3).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="sign"]/div[3]/div')))
#     # 点击签到,实现功能
#     browser.find_element_by_xpath('//*[@id="sign"]/div[3]/div').click()
#     time.sleep(0.5)

#     # 这个print其实没什么用,如果真的要测试脚本是否运行成功，可以用try来抛出异常
#     print("签到成功")

#     # 脚本运行成功,退出浏览器
#     browser.quit()
