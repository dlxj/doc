import tkinter as tk
import requests
import re   
from lxml import etree
import time
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}


def get_download_url(url):
    num = 1
    mp4_list = ['80', '64', '32', '16']
    mp3_list = ['30280', '30232', '30216']
    res = requests.get(url, headers=headers)
    text = res.text
    html = etree.HTML(text)
    title = html.xpath("//span[@class='tit' or @class='tit tr-fix']/text()")
    if not len(title):
        title = '未命名%d' % num
        num += 1
    else:
        title = title[0]
    title = re.sub(r'[\\/:\*\?"<>|]', '', title)
    mp4_list = list(map(lambda x: '{"id":' + x + ',"baseUrl":"(.*?)",', mp4_list))
    mp3_list = list(map(lambda x: '{"id":' + x + ',"baseUrl":"(.*?)",', mp3_list))
    mp3 = match_url(mp3_list, text)
    mp4 = match_url(mp4_list, text)
    return title, mp3, mp4


def get_url(url):
    res = requests.get(url, headers=headers)
    text = res.text
    hrefs = re.findall(r'<div class="info"><a href="(.*?)"', text)
    return hrefs


def match_url(conditions, text):
    for condition in conditions:
        result = re.search(condition, text)
        if result:
            return result.group(1)
    else:
        return -1


def downloader(title, mp3, mp4):
    is_exists = os.path.exists('小破站')
    if not is_exists:
        os.mkdir('小破站')
    start = time.time()
    down(mp3, title, 'mp3')
    down(mp4, title, 'mp4')
    end = time.time()
    print('\n下载完成！用时%.2f秒' % (end - start))


def down(url, title, type):
    download_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
        'Referer': 'https://www.bilibili.com/video/av6499012',
        'Origin': 'https://www.bilibili.com',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
    res = requests.get(url, headers=download_headers, stream=True)
    chunk_size = 1024
    content_size = int(res.headers['content-length'])
    size = 0
    if res.status_code == 200:
        if type == 'mp4':
            print()
        print(title + '.' + type + '文件大小 ：%0.2f MB' % (content_size / chunk_size / 1024))
        with open('小破站/' + title + '.' + type, 'wb') as fp:
            for data in res.iter_content(chunk_size=chunk_size):
                fp.write(data)
                size += len(data)
                print(
                    '\r' + '[下载进度]:%s%.2f%%' % ('>' * int(size * 50 / content_size), float(size / content_size * 100)),
                    end='')


def method_av(av):
    base_url = 'https://www.bilibili.com/video/av'
    url = base_url + av
    title, mp3, mp4 = get_download_url(url)
    if mp3 != -1 and mp4 != -1:
        downloader(title, mp3, mp4)
    else:
        print('此视频可能无法下载，抱歉。')


def method_rank(a, b, c, d):
    area = ['all/', 'origin/']
    time = ['/0/', '/1/']
    duration = ['1', '3', '7', '30']
    zone = ['0', '1', '168', '3', '129', '4', '36', '188', '160', '119', '155', '5', '181']
    base_url = 'https://www.bilibili.com/ranking/'
    full_url = base_url + area[a] + zone[b] + time[c] + duration[d]
    urls = get_url(full_url)
    num = 0
    fail = []
    for url in urls:
        num += 1
        title, mp3, mp4 = get_download_url(url)
        if mp3 != -1 and mp4 != -1:
            downloader(title, mp3, mp4)
        else:
            fail.append(num)
    if len(fail):
        print('全部下载完成！第' + str(fail) + '个下载失败！\n')
    else:
        print('全部下载完成！')


def check_input(num):
    t = eval(input())
    while True:
        if t == -1:
            break
        elif t not in range(num):
            print('输入错误!请重新输入!')
            t = eval(input())
        else:
            break
    return t


def gui():
    window = tk.Tk()
    window.title('下载B站视频')
    window.geometry('750x350')

    a = tk.IntVar()
    a.set(0)
    b = tk.IntVar()
    b.set(0)
    c = tk.IntVar()
    c.set(0)
    d = tk.IntVar()
    d.set(0)
    tk.Label(window, fg='red', text='下载过程中，此页面会未响应，下载完就好啦！', font=('微软雅黑', 15)).place(x=300, y=275)
    tk.Label(window, text='下载排行榜所有视频', font=('微软雅黑', 15)).place(x=5, y=10)
    frame1 = tk.Frame(bd=1, width=100, height=80, relief=tk.GROOVE).place(x=5, y=50)
    tk.Radiobutton(frame1, text='全站榜', variable=a, value=0, font=('微软雅黑', 15)).place(x=8, y=55)
    tk.Radiobutton(frame1, text='原创榜', variable=a, value=1, font=('微软雅黑', 15)).place(x=8, y=90)
    frame2 = tk.Frame(bd=1, width=120, height=80, relief=tk.GROOVE).place(x=150, y=50)
    tk.Radiobutton(frame2, text='全部投稿', variable=c, value=0, font=('微软雅黑', 15)).place(x=153, y=55)
    tk.Radiobutton(frame2, text='近期投稿', variable=c, value=1, font=('微软雅黑', 15)).place(x=153, y=90)
    frame3 = tk.Frame(bd=1, width=260, height=80, relief=tk.GROOVE).place(x=320, y=50)
    tk.Radiobutton(frame3, text='日排行', variable=d, value=0, font=('微软雅黑', 15)).place(x=323, y=55)
    tk.Radiobutton(frame3, text='三日排行', variable=d, value=1, font=('微软雅黑', 15)).place(x=323, y=90)
    tk.Radiobutton(frame3, text='周排行', variable=d, value=2, font=('微软雅黑', 15)).place(x=460, y=55)
    tk.Radiobutton(frame3, text='月排行', variable=d, value=3, font=('微软雅黑', 15)).place(x=460, y=90)
    frame4 = tk.Frame(bd=1, width=670, height=80, relief=tk.GROOVE).place(x=5, y=140)
    tk.Radiobutton(frame4, text='全站', variable=b, value=0, font=('微软雅黑', 15)).place(x=8, y=145)
    tk.Radiobutton(frame4, text='动画', variable=b, value=1, font=('微软雅黑', 15)).place(x=100, y=145)
    tk.Radiobutton(frame4, text='国创相关', variable=b, value=2, font=('微软雅黑', 15)).place(x=192, y=145)
    tk.Radiobutton(frame4, text='音乐', variable=b, value=3, font=('微软雅黑', 15)).place(x=320, y=145)
    tk.Radiobutton(frame4, text='舞蹈', variable=b, value=4, font=('微软雅黑', 15)).place(x=412, y=145)
    tk.Radiobutton(frame4, text='游戏', variable=b, value=5, font=('微软雅黑', 15)).place(x=504, y=145)
    tk.Radiobutton(frame4, text='科技', variable=b, value=6, font=('微软雅黑', 15)).place(x=8, y=180)
    tk.Radiobutton(frame4, text='数码', variable=b, value=7, font=('微软雅黑', 15)).place(x=100, y=180)
    tk.Radiobutton(frame4, text='生活', variable=b, value=8, font=('微软雅黑', 15)).place(x=192, y=180)
    tk.Radiobutton(frame4, text='鬼畜', variable=b, value=9, font=('微软雅黑', 15)).place(x=320, y=180)
    tk.Radiobutton(frame4, text='时尚', variable=b, value=10, font=('微软雅黑', 15)).place(x=412, y=180)
    tk.Radiobutton(frame4, text='娱乐', variable=b, value=11, font=('微软雅黑', 15)).place(x=504, y=180)
    tk.Radiobutton(frame4, text='影视', variable=b, value=12, font=('微软雅黑', 15)).place(x=596, y=180)

    def av():
        method_rank(a.get(), b.get(), c.get(), d.get())
    tk.Button(window, text='下载！', font=('微软雅黑', 15), command=av).place(x=625, y=65)

    tk.Label(window, text='下载指定av号视频(输入数字即可)', font=('微软雅黑', 15)).place(x=5, y=230)

    def rank():
        av = var.get()
        method_av(av)

    var = tk.StringVar()
    tk.Entry(window, textvariable=var, show=None, font=('微软雅黑', 15), width=12).place(x=5, y=279)
    tk.Button(window, text='下载！', font=('微软雅黑', 15), command=rank).place(x=172, y=270)

    window.mainloop()


def main():
    gui()


if __name__ == '__main__':
    main()