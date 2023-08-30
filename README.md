# Ruijie-Campus-Network
基于JS逆向的通用校园网络认证自动登录，可开机自启，无感登录

### 锐捷校园网 网页认证通用
![ruije](https://user-images.githubusercontent.com/79371047/226113334-1d706b96-a37a-4dc3-a3a3-927aaffdda9b.png)

### 使用方法
<a href="https://github.com/Epxir/Ruijie-Campus-Network/releases/latest">下载最新版</a>到任意位置打开

<img width="197" alt="image" src="https://user-images.githubusercontent.com/79371047/226113516-21c8157f-b216-4007-ba23-efcbb61a31a4.png">

输入账号密码，密码加密与否都可以，正确输入后勾选开机自启

全流程实现，无需获取任何cookie和抓包

注册到window服务，高优先级自启

### 打包方式

```shell
pyinstaller -F -w -i 网络认证.png --add-data 'mini_racer.dll;.'  main.py
```

### 安全保障

只保存RSA加密的密码，不可迁移，和锐捷一样安全！

# 点个星星！
