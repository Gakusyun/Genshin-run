@ECHO OFF
echo 是否使用七牛云作为go模块代理(默认为y)[y/n]
set choice=
set /p choice=请直接输入对应数字回车：
if /i "%choice%"=="n" goto py
go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.cn,direct
goto py
:py
echo 是否使用清华源作为pipy镜像服务器(默认为y)[y/n]
set choice=
set /p choice=请直接输入对应数字回车：
if /i "%choice%"=="n" goto jiebains
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
:jiebains
echo 正在安装jieba...
pip install jieba
echo 是否构建main.go(默认为y)[y/n]
set choice=
set /p choice=请直接输入对应数字回车：
if /i "%choice%"=="n" goto over
go build
:over