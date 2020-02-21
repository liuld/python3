#!/usr/local/bin/python3
# _*_ coding _*_
# time模块

# 表示时间的方式
#   1.时间戳(timestamp)：通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。
#   2.格式化的时间字符串(Format String)
#   3.结构化的时间(struct_time)：struct_time元组共有9个元素共九个元素:(年，月，日，时，分，秒，一年中第几周，一年中第几天，夏令时)

# 转换方法:
#   1.时间戳 --> 结构化的时间 time.localtime(time.time())  time.gmtime(time.time())
#   2.结构化的时间 --> 时间戳 time.mktime(time.localtime())
#   3.结构化的时间 --> 格式化的时间字符串  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) 
#   4.格式化的时间字符串 --> 结构化的时间  time.strptime('2019-04-03 15:39:53','%Y-%m-%d %H:%M:%S')
#   5.时间戳 --> 'Wed Apr  3 15:59:42 2019'  time.ctime(time.time())
#   6.结构化的时间 --> 'Wed Apr  3 15:59:42 2019'  time.asctime(time.localtime())
import time
import datetime
# https://www.cnblogs.com/chenhuabin/p/10099766.html
# datetime
now_datetime = datetime.datetime.now()
# datetime --> timetuple
now_timetuple = now_datetime.timetuple()
# timetuple -- > 时间戳
now_tc = time.mktime(now_timetuple)
# 时间戳 --> datetime
now_datetime = datetime.datetime.fromtimestamp(now_tc)
# datetime --> str
now_str = now_datetime.strftime("%Y-%m-%d %H:%M:%S")
# str --> datetime
now_datetime = datetime.datetime.strptime(now_str, "%Y-%m-%d %H:%M:%S")
