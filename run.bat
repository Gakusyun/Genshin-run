@ECHO OFF
echo 是否使用华为源安装 jieba (默认为 y)[y/n]
set choice=
set /p choice=请输入 y 或 n 并回车：
if /i "%choice%"=="n" goto jiebains
pip install -i https://repo.huaweicloud.com/repository/pypi/simple jieba
goto build
:jiebains
echo 正在安装 jieba...
pip install jieba
:build
echo 是否构建 main.go (默认为 y)[y/n]
set choice=
set /p choice=请输入 y 或 n 并回车：
if /i "%choice%"=="n" goto over
go build
:over