# -*- coding: utf-8 -*-

#priceSequence为某一股票交易日内开市后的日内成交价格序列

#求开盘价
def OpenPrice(priceSequence):
    Open = priceSequence[0]
    return(Open)

#求收盘价
def ClosePrice(priceSequence):
    Close = priceSequence[-1]
    return(Close)

#求最高价
def HighPrice(priceSequence):
    High = max(priceSequence)
    return(High)

#求最低价
def LowPrice(priceSequence):
    Low = min(priceSequence)
    return(Low)

