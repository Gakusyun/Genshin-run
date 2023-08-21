import sys
import jieba
import subprocess
import configparser
import os
import win32com.client

run = False
uninstall = False
try:
    list=jieba.cut(sys.argv[1],cut_all=False)
except:
    list=jieba.cut(input("输入启动密码:"),cut_all=False)
for i in list:
    if i in ["原神","原始人"]:
        shortcut = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\原神\原神.lnk'
        shell = win32com.client.Dispatch("WScript.Shell")
        launcher = shell.CreateShortCut(shortcut)
        launcher = launcher.TargetPath.replace('launcher.exe', '')
        game_path = os.path.join(launcher, 'Genshin Impact Game', 'YuanShen.exe')
        uninstall_path = os.path.join(launcher, 'uninstall.exe')
        if os.path.exists(game_path):
            print('已获取游戏路径')
        else:
            config = configparser.ConfigParser()
            config.read("config.ini", encoding="utf-8")
            game_path = config.get("Paths", "game_path")
            if os.path.exists(game_path):
                print('已获取游戏路径')
            else:
                print("文件路径异常，请编辑文件夹内 config.ini")
    if i in ["启动","起洞"]:
        run = True
    elif i in ["卸载","删除"]:
        uninstall = True

if uninstall == True:
    subprocess.Popen(uninstall_path)

if run == True:
    subprocess.Popen(game_path)
