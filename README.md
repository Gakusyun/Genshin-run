# Genshin-run

由门酱[哔站](https://space.bilibili.com/245015918) [抖音](https://v.douyin.com/iJCQ7kkw/)驱动的控制台原神启动器.

## 使用方法

使用本项目需要：安装 [go](https://golang.google.cn/) 、安装 [python](https://python.org/) 、安装 [jieba](https://github.com/fxsjy/jieba).

>注意！安装 Python 时，请务必勾选添加到 PATH！！！

### 自动构建

安装完 go、python 后，以管理员运行文件夹内 run.bat 可一键安装 jieba.

### 您也可以选择手动构建

右击鼠标，在终端中打开文件夹(以下操作都是在终端中进行)

- 安装 jieba 库

```
pip install jieba
```

或者使用华为源

```
pip install -i https://repo.huaweicloud.com/repository/pypi/simple jieba
```

- 构建主程序 exe 文件

```
go build
```

### 使用

本程序提供了多种原神启动方法.

但是在启动之前，需要先将 config.ini 中的 path 修改为自己游戏文件的 path.

- 终端中启动

在终端中打开当前文件夹(需要管理员权限，可右击 Windows 徽标，选择`终端（管理员)`,然后利用 `cd` 命令到程序所在文件夹),在终端中输入.

```
Genshin-run 原神启动
```

即可启动原神.这里，`原神启动`可以换成任何含原神及启动的句子

还可以使用

```
 python start.py 原神启动
```

来启动原神.同样，这里的`原神启动`可以换成任何含原神及启动的句子.

- 直接启动 exe 文件

这里建议右击文件，以管理员身份运行.进入程序后，输入`原神启动`等即可启动原神.
