import sys
import jieba
import subprocess
run = False
try:
    list=jieba.cut(sys.argv[1],cut_all=False)
except:
    list=jieba.cut(input("输入启动密码"),cut_all=False)

for i in list:
    if i in ["原神","原始人"]:
        game_path = r'C:\Program Files\Genshin Impact\Genshin Impact Game\YuanShen.exe'
    if i in ["启动","起洞"]:
        run = True

if run == True:
    subprocess.Popen(game_path)

            