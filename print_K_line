# -*- coding:utf-8 -*-
#Auther: dshowing

import datetime
import matplotlib.pyplot as plt

from matplotlib.pylab import date2num
from mpl_finance import candlestick_ohlc
import jqdatasdk
"""
注意date2num()参数格式为datetime.datetime类；
candlestick_ohlc可接受列表参数和单个参数；
jqdatasdk返回DataFrema数据，注意格式转换
"""

# jqdatasdk.auth
jqdatasdk.auth('ID', 'secure_id')

# 从joinquant获取历史行情
date1 = '2018-10-01'
date2 = '2019-02-01'
quotes = jqdatasdk.get_price(
    '000001.XSHE',
    start_date=date1,
    end_date=date2,
    frequency='daily',
    fields=None,
    skip_paused=True,
    fq=None
)

# 遍历转换
data_list = []
for dates, row in quotes.iterrows():
    #dates为Datafrema数据，强制转换为str方可使用
    date_time = datetime.datetime.strptime(str(dates), '%Y-%m-%d %H:%M:%S')
    #接收datetime.datetime数据
    t = date2num(date_time)
    open, high, low, close = row[:4]
    datas = (t, open, high, low, close)
    data_list.append(datas)

# 创建一个figure
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

# 设置x轴为日期
ax.xaxis_date()
plt.xticks(rotation=45)
plt.yticks()
plt.title('000001.XSHE: 2016/01/01-2019/02/01')
plt.xlabel("时间")
plt.ylabel("股价（元）")

candlestick_ohlc(ax=ax, quotes=data_list, width=0.6, colorup='b', colordown='r')
plt.grid(True)

plt.show()

