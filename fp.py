
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
import tkinter
from tkinter import messagebox  # 引入弹窗库，防止解释器弹出报错。
 
 
# *******************************注意以及使用***************************************
 
# 1.安装selenium库，不建议使用最新版本，会闪退，可以使用4.5.0版本：pip install selenium==4.5.0
# 2.修改下面的四个修改项，直接运行
 
# *******************************注意以及使用***************************************
 
 
 
# *******************************修改项***************************************
 
# chromedriver.exe路径
driver_path='C:\\Users\\34512\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'
 
# 视频初始url（即随便点开一个视频的url，如果url中有action_id，将其删掉即可，类似下面这个url）
chushi_url="https://course.zhaopin.com/#/courseLearning?classId=1463&taskId=4492&isChapter=true&b_idx=0&s_idx=0"
 
# 每章的小节个数，例如下方为一共四个章节，第一章12个小节。。。等等
lists=[16,7,12,14,13,7,5,4,5]
 
# 开始播放的小节
beginchart=4
beginchartsmall=13
 
# *******************************修改项***************************************
 
 
 
def get_cookie():
    browser = webdriver.Chrome(driver_path)
    browser.get("https://course.zhaopin.com/")
    print("开始获取cookie")
    print("在弹出的浏览器上自主登陆，成功后点击弹框中的“确认”即可自动获取cookie")
    print("弹窗可能被浏览器挡住,登陆成功后可最小化浏览器（不要直接关闭）")
 
    root = tkinter.Tk()
    root.withdraw()
    root.geometry('1800x1200')
    messagebox.showinfo(title="获取cookie", message="在弹出的浏览器上自主登陆，成功后点击弹框中的“确认”即可自动获取cookie，先登录！！再点“确认”！！")
 
    cookies = browser.get_cookies()
    with open("cookie.json", "w") as fp:
        json.dump(cookies, fp)
    print("获取cookie成功，准备开始播放")
    browser.close()
 
 
def main():
    try:
        with open("cookie.json", "r", encoding="utf-8") as cks: #从json文件中获取之前保存的cookie
             cookie=json.load(cks)
    except:
        print("cookie有误，或未登陆，请在弹出浏览器进行手动登陆")
        get_cookie()
        main()
    driver = webdriver.Chrome(driver_path)
    driver.get(chushi_url)
    # 添加Cookie
    driver.delete_all_cookies()
    for cc in cookie:
        driver.add_cookie(cc)
 
    driver.get(chushi_url)
    time.sleep(2)
    title = driver.find_element(By.XPATH, '//title').text
    findvideo=False
    if title=='登录 - 学员端':
        driver.close()
        print("cookie过期，请重新登陆")
        get_cookie()
        main()
    else:
        
        for i in range(len(lists)):
            print(i)
            for j in range(lists[i]):
                if beginchart==i+1 and beginchartsmall==j+1:
                    findvideo=True
                    print("findvideo")
                if findvideo==True:
                    print(f'正在播放第{str(i+1)}章，{str(j+1)}小节')
                    path = f'/html/body/div/div/div/section/div/div[1]/div/div[2]/div/div[1]/section/div/div[{i+1}]/div[{j+ 1}]'
                    a = driver.find_element(By.XPATH, path)
                    a.click()
                    t1 = a.text.split('\n')
                    t2 = t1[1].split(' ')
                    t3 = t2[1]
                    t4 = t3.split(':')
                    t = int(t4[0]) * 60 + int(t4[1]) + 5
                    print(f'此小节时间为{t-5}s')
                    for k in range(t, 0, -1):
                        print("\r正在播放，剩余时间{}秒".format(k), end="", flush=True)
                        time.sleep(1)
                    time.sleep(5)
                    print("\r此小节播放完成")
                    print("************************************")
 
        time.sleep(3)
        print('视频全部播放完毕')
        driver.close()
 
main()
