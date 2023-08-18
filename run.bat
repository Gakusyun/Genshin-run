@ECHO OFF
echo 是否使用清华源作为 pipy 镜像服务器(默认为 y)[y/n]
set choice=
set /p choice=请输入 y 或 n 并回车：
if /i "%choice%"=="n" goto jiebains
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
:jiebains
echo 正在安装 jieba...
pip install jieba
echo 是否构建 main.go (默认为 y)[y/n]
set choice=
set /p choice=请输入 y 或 n 并回车：
if /i "%choice%"=="n" goto over
go build
:over