# -*- coding:utf-8 -*-
import requests
import urllib.parse
from lxml import etree

url = "http://m.life.httpcn.com/m/xingming/"

params = {}
params['act'] = 'submit'  # 默认值
params['data_type'] = '0' # 日期类型，0 表示公历，1 表示农历
params['RenYue'] = '0'    # 默认为 0
params['year'] = '1988'   # 输入出生年份
params['month'] = '12'     # 输入出生月份
params['day'] = '21'       # 输入出生日
params['hour'] = '9'     # 输入出生时
params['minute'] = '30'    # 输入出生分
params['zty'] = '0'       # 真太阳时，默认不使用为 0
params['wxxy'] = '0'      # 喜用五行，0 表示自动分析，1 表示自定喜用神
params['xing'] = '周'     # 输入姓，也可复姓
params['ming'] = '宁'   # 输入名，也可单字名
params['sex'] = '1'       # 性别，0 表示女孩，1 表示男孩
params['isbz'] = '1'      # 默认值为 1

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'content-type': "application/x-www-form-urlencoded",
    'host': "m.life.httpcn.com",
    'origin': "http://m.life.httpcn.com",
    'referer': "http://m.life.httpcn.com/xingming/",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
}

response = requests.request("POST", url, data=params, headers=headers)
response.encoding = 'UTF-8'

selector = etree.HTML(response.text)
# 解析得到“五格数理”分数
wuge_score = selector.xpath('//div[@class="mui-collapse-content hc-cha-content"]/div[1]/div/text()')
# 解析得到“八字五行”分数
bazi_score = selector.xpath('//div[@class="mui-collapse-content hc-cha-content"]/div[4]/div/text()')

print("姓名：周宁" + '\t' + "五格数理分数：" + str(wuge_score)  + '\t' + "八字五行分数：" + str(bazi_score))
