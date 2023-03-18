# Ruijie-Campus-Network
基于JS逆向的通用大学网络认证自动登录，可开机自启

### 锐捷校园网 网页认证通用
![ruije](https://user-images.githubusercontent.com/79371047/226113334-1d706b96-a37a-4dc3-a3a3-927aaffdda9b.png)

### 使用方法

<img width="197" alt="image" src="https://user-images.githubusercontent.com/79371047/226113516-21c8157f-b216-4007-ba23-efcbb61a31a4.png">

输入账号密码，密码加密与否都可以，正确输入后勾选开机自启

### 打包方式

```shell
pyinstaller -F -w -i 网络认证.png --add-data 'mini_racer.dll;.'  main.py
```

### 安全保障

只保存RSA加密的密码，不可迁移，几乎无法逆向，和锐捷一样安全！

# 点个星星！
