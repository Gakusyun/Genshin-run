import sys
import jieba
import subprocess
import configparser
import os
import win32com.client


# 获取游戏路径
shortcut = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\原神\原神.lnk'
shell = win32com.client.Dispatch("WScript.Shell")
launcher = shell.CreateShortCut(shortcut)
laundir = launcher.TargetPath.replace('launcher.exe', '')
genshinPath = os.path.join(laundir, 'Genshin Impact Game', 'YuanShen.exe')
genUninsPath = os.path.join(laundir, 'uninstall.exe')
if os.path.exists(genshinPath):
    print('已获取游戏路径')
else:
    config = configparser.ConfigParser()
    config.read("config.ini", encoding="utf-8")
    genshinPath = config.get("Paths", "gamePath")
    if os.path.exists(genshinPath):
        print('已获取游戏路径')
    else:
        genshinPath = laundir
        print("文件路径异常，请编辑文件夹内 config.ini")

#初始化变量
run = False
uninstall = False



print("选择模式")
print("1.关键词模式")
print("2.关键字模式，只要出现")
while True:
    if input() == "1":
        try:
            list=jieba.cut(sys.argv[1],cut_all=False)
        except:
            list=jieba.cut(input("输入启动密码:"),cut_all=False)
        for i in list:
            if i in ["原神","原始人"]:
                gamePath = genshinPath
                uninstallPath = genUninsPath
            if i in ["启动","起洞"]:
                run = True
            elif i in ["卸载","删除"]:
                uninstall = True
        break
    elif input() == "2":
        key={}
        for i in sys.argv[1]:
            try:
                key[i] +=1
            except:
                key[i] = 0
        if key["原"] > 0 and key["神"] > 0 :
            gamePath = genshinPath
            uninstallPath = genUninsPath
        if key["起"] > 0 and key["动"] > 0:
            run = True
            if key["卸"] > 0 and key["载"] > 0:
                if key["起"]+key["动"]<key["卸"]+key["载"]:
                    uninstall = True
        if key["卸"] > 0 and key["载"] > 0:
            uninstall = True
        if key["起"] > 0 and key["动"] > 0:
            if key["起"]+key["动"]>key["卸"]+key["载"]:
                run = True
if uninstall == True:
    subprocess.Popen(uninstallPath)
if run == True:
    subprocess.Popen(gamePath)