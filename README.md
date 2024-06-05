

1.下载selenium使用的浏览器驱动chromedriver.exe
查找chrome版本：Chrome://version

下载对应版本chromedriver



2.安装selenium库，不建议使用最新版本，会闪退，可以使用4.5.0版本：

```
pip install selenium==4.5.0
```

3.修改下面的四个修改项

```
# *******************************修改项***************************************
 
# chromedriver.exe路径
driver_path='C:\\Users\\34512\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'
 
# 视频初始url（即随便点开一个视频的url，如果url中有action_id，将其删掉即可，类似下面这个url）
chushi_url="https://course.zhaopin.com/#/courseLearning?classId=1463&taskId=4492&isChapter=true&b_idx=0&s_idx=0"
 
# 每章的小节个数，例如下方为一共四个章节，第一章12个小节。。。等等
lists=[16,7,12,14,13,7,5,4,5]
 
# 开始播放大章
beginchart=4
#开始播放小节
beginchartsmall=13
 
# *******************************修改项***************************************
```
4.第一次使用需要自己进行登陆获取cookie，在弹出的浏览器上自主登陆，成功后点击弹框中的“确认”即可自动获取cookie
