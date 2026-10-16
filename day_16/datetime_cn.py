"""
date和datetime区别是什么:
date      = 只管“哪一天”
datetime  = 管“哪一天 + 几点几分几秒”
"""
#1
from datetime import datetime, date
now = datetime.now()
day = now.day#是属性，不需要括号
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(year, month, day, hour, minute, timestamp)

#2 cuowu strftime: datetime → string
format_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(format_date)

#3  strptime: string → datetime
today_str = '2019年12月5日' 
today = datetime.strptime(today_str, "%Y年%m月%d日")
print("today =", today)   #格式要对应2019年12月5日

#4 错误 now是datetime new_year是date，不能直接减
# new_year = date(year=2027, month=1,day=1)
new_year= datetime(year=2027,month=1,day=1)
time_left_for_newyear = new_year - now
print('距离新年的距离： ', time_left_for_newyear)

#5 改成datetime
date_1970=datetime(year=1970, month=1, day=1)
time_left_for_1970 = now-date_1970
print('距离1970年的距离: ', time_left_for_1970)

#6思考，你可以将datetime模块用于什么？
"""
datetime 可以用于获取当前日期和时间、格式化时间、
把字符串转换成日期对象、
计算两个日期之间的差值，
以及记录程序事件发生的时间。
"""
