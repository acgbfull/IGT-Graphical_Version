# IGT(graphical version)

## Description

**IGT**是一款具有收集IP地理位置、同IP网站、端口信息、IP地址、WHOIS、子域名信息的工具。
（IGT is a tool for collecting IP Location, reverse IP info, port info, IP address, WHOIS, subdomains info.）


## Operating environment

> python 3+
>
> window 7
>
> nmap （nmap添加到环境变量中）
>
> python 第三方库 sqlalchemy
>
> python 第三方库 PyQt5


## Configuration Guide
配置文件：config/config.py <br>
可设置http请求超时时间和nmap扫描时的默认参数. <br>
生成的results.html、保有数据的数据库文件和log文件默认保存于程序根目录下的project目录. <br>


## Installation guide

>git clone https://github.com/acgbfull/IGT-Graphical_Version.git


## Usage

> python igt.py


## Demo

python igt.py

![UI截图](https://github.com/acgbfull/IGT-Graphical_Version/raw/master/images/UI.png "UI截图")

**程序运行中**

![run截图](https://github.com/acgbfull/IGT-Graphical_Version/raw/master/images/run.png "UI截图")

**程序运行生成的results.html**

![result截图](https://github.com/acgbfull/IGT-Graphical_Version/raw/master/images/result.png "UI截图")


## CHANGE LOG

>2018/6/17  version:1.0.0

