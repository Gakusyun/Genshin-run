@ECHO OFF
echo �Ƿ�ʹ����ţ����Ϊgoģ�����(Ĭ��Ϊy)[y/n]
set choice=
set /p choice=��ֱ�������Ӧ���ֻس���
if /i "%choice%"=="n" goto py
go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.cn,direct
goto py
:py
echo �Ƿ�ʹ���廪Դ��Ϊpipy���������(Ĭ��Ϊy)[y/n]
set choice=
set /p choice=��ֱ�������Ӧ���ֻس���
if /i "%choice%"=="n" goto jiebains
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
:jiebains
echo ���ڰ�װjieba...
pip install jieba
echo �Ƿ񹹽�main.go(Ĭ��Ϊy)[y/n]
set choice=
set /p choice=��ֱ�������Ӧ���ֻس���
if /i "%choice%"=="n" goto over
go build
:over