# -*- coding: utf-8 -*-
#习题中的精选

#9.1 创建账户的函数，并对账户名和密码进行校验
def create_name():
    name = input('请输入用户名\n')
    if ord(name[0])<65 or ord(name[0])>122:
        print('用户名必须以字母开头')
        return(create_name())
    else:
        return(name)

def verify_passwd(passwd):
    head = 65<=ord(passwd[0])<=122
    contain_number = any([str(x) in passwd for x in range(10)])
    contain_symbol = any([str(x) in passwd for x in ('_','*','#')])
    return (head and (contain_number or contain_symbol))

def create_passwd():
    passwd = input('请输入密码\n')
    is_legal = verify_passwd(passwd)
    if is_legal:
        return(passwd)
    else:
        return (create_passwd())
    
def create_account():
    create_name()
    create_passwd()
    print('用户创建成功')

create_account()

#9.5创建日期和股价的字典
import datetime as dt
dates = [dt.datetime(2015,1,13)+dt.timedelta(i) for i in range(5)]
closes = [7.31,7.28,7.40,7.43,7.41]
prices = {dates[i]:closes[i] for i in range(5)}
print(prices)
#创建策略，如果当期价格比前一期价格高，买进，第二期卖出。初始10000元，用50%买入，买入股票为整数
#产生一个持有股票份额的字典对象
import math
cash = 10000
share = {dates[0]:0}
for i in range(1,5):
    if prices[dates[i]]>prices[dates[i-1]]:
        buyshare = math.floor(0.5*cash/prices[dates[i]])
        share[dates[i]] = buyshare
        cash = cash-buyshare*prices[dates[i]]+share[dates[i-1]]*prices[dates[i]]
    else:
        share[dates[i]]=0
print(share)