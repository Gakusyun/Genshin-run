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
        yuan = True
        shen = True
        qi = True
        dong = True
        xie = True
        zai = True
        runRank = 0
        for i in sys.argv[1]:
            if i == "原":
                if yuan == True:
                    runRank += 1
                    yuan = False
            elif i == "神":
                if shen == True:
                    runRank += 1
                    shen = False
            elif i == "启":
                if qi == True:
                    runRank += 10
                    qi = False
            elif i == "动":
                if dong == True:
                    runRank += 10
                    dong = False
            elif i == "卸":
                if xie == True:
                    runRank += 100
                    xie = False
            elif i == "载":
                if zai == True:
                    runRank += 100
                    zai = False
        if runRank == 22:
            run = True
        elif runRank == 202:
            uninstall = True
        else:
            print("未提取到有效信息")
        break
    else:
        print("输入不正确，请重试")

if uninstall == True:
    subprocess.Popen(uninstallPath)

if run == True:
    subprocess.Popen(gamePath)
