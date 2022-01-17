
# https://jishuin.proginn.com/p/763bfbd5a01a

# pip install seleniu


from pymysql import NULL
from selenium import webdriver

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys

import time


# show = True  # UI OR not
show = False

if __name__  ==  "__main__": 

    # python目录下必须有chromedriver.exe （http://chromedriver.storage.googleapis.com/index.html 这里下载和当前使用版本一致的）
    
    
    opt = webdriver.ChromeOptions()
    opt.headless = show

    if show:
        wd=webdriver.Chrome()
    else:
        wd=webdriver.Chrome(options=opt) # NO UI setting
    wd.implicitly_wait(5)
    #wd.set_page_load_timeout(10)

    # open
    url = 'https://www.pdawiki.com/forum/'
    wd.get(url)

    input_usernanme = wd.find_element_by_xpath('//*[@id="ls_username"]')
    input_usernanme.send_keys('howdyhappy')

    input_passwd = wd.find_element_by_xpath('//*[@id="ls_password"]')
    input_passwd.send_keys('v14')

    input_login = wd.find_element_by_xpath('//*[@id="lsform"]/div/div[1]/table/tbody/tr[2]/td[3]/button')
    input_login.click()

    time.sleep(3)

    try:
        input_sing = wd.find_element_by_xpath('//*[@id="mn_N462e"]/a')   # click sign label
        input_sing.send_keys(Keys.ENTER)
        time.sleep(1)
    except:
        print('##### err.....')
    finally:
        print('continue.....')

    input_dont = wd.find_element_by_xpath('//*[@id="qiandao"]/table[2]/tbody/tr[1]/td/label[3]/input')  # I don't gonna write text
    input_dont.click()

    time.sleep(1)

    input_raku_img = wd.find_element_by_xpath('//*[@id="kx"]/center/img')
    input_raku_img.click()

    time.sleep(1)
    
    input_sign_img = wd.find_element_by_xpath('//*[@id="qiandao"]/table[1]/tbody/tr/td/div/a/img')
    input_sign_img.click()
    
    time.sleep(1)

    print('success sign!')

    wd.quit()
