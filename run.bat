@ECHO OFF
echo 是否使用华为源安装 jieba & pywin32 (默认为 y)[y/n]
set choice=
set /p choice=请输入 y 或 n 并回车：
if /i "%choice%"=="n" goto jiebains
echo 正在安装 jieba & pywin32...
pip install -i https://repo.huaweicloud.com/repository/pypi/simple jieba
pip install -i https://repo.huaweicloud.com/repository/pypi/simple pywin32
goto build
:jiebains
echo 正在安装 jieba & pywin32...
pip install jieba
pip install pywin32
:build
echo 是否构建 main.go (默认为 y)[y/n]
set choice=
set /p choice=请输入 y 或 n 并回车：
if /i "%choice%"=="n" goto over
go build
:over