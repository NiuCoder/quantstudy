# -*- coding: utf-8 -*-
#方法一 利用ascii码来判断
import re
def isChar(char):
    if (((username[0]>'a') and (username[0]<'z')) or 
        ((username[0]>'A') and (username[0]<'A'))):
        return True
    else:
        return False
#方法二 利用正则表达式判断
def isCharter(char):
        value = re.compile(r'[a-zA-Z]')
        result = value.match(char)
        return result

username = input('请输入用户名：')
while True:
    #if(ifChar(username[0])):
    #if(username[0].isalpha()):
    if(isCharter(username[0])):
        print('用户名为'+username) 
        break
    else:
        print('用户名必须以字母开头\n')
        username = input('请输入用户名：')
   
password = input('请输入密码：')
while True:
    if(not isCharter(username[0])):
        print('密码必须以字母开头')
        password = input('请输入密码：')
    if(len(password)<=6):
        print('密码需要大于6位')
        password = input('请输入密码：')
    exp = re.compile(r'\d')
    result = exp.search(password)
    if(not result):
        print('密码必须包含数字')
        password = input('请输入密码：')
    exp2 = re.compile(r'[_\*#]')
    result2 = exp2.search(password)
    if(not result2):
         print('密码必须包含_*#中的一个')
         password = input('请输入密码：')
    print('用户名密码创建成功')
    break
