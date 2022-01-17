
# https://jishuin.proginn.com/p/763bfbd5a01a
# https://www.cnblogs.com/wqzn/p/14568794.html

# pip install selenium

"""
centos7 + selenium
pip3.8 install selenium

curl https://intoli.com/install-google-chrome.sh | bash
/opt/google/chrome/chrome  # Running as root without --no-sandbox is not supported.

google-chrome-stable --no-sandbox --headless --disable-gpu --screenshot https://www.baidu.com/  # 成功后后生成一个文件 screenshot.png

google-chrome --version
    # 97.0.4692.71
    # http://chromedriver.storage.googleapis.com/index.html  到这里下载这个版本的驱动


whereis python3.8
cp chromedriver /usr/local/bin

crontab -e # edit
crontab -l # list all task

00    07    *    *    *    python3.8 -u /root/sign.py > /root/log_sign.txt

"""

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
        # opt.binary_location = '/usr/local/bin/chromedriver'
        # opt.add_argument('no-sandbox')   # root account need this
        # opt.add_argument('disable-dev-shm-usage')
        # opt.add_argument("--remote-debugging-port=9223")
        # opt.add_experimental_option('useAutomationExtension', False)
        # opt.add_experimental_option('excludeSwitches', ['enable-automation'])
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
