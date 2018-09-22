# -*- coding: UTF-8 -*-

from datetime import datetime, timedelta

left = 4

closeDict = {"01.13": 7.31, "01.14": 7.28,
             "01.15": 7.40, "01.16": 7.43, "01.17": 7.41}

closeDict["01.20"] = 7.44

closeDict["01.16"] = 7.50

## 通过数组排序查找

closeKeys = list(closeDict.keys())
closeKeys.sort()

days1 = closeKeys[-left:]
for d in days1:
    print(d, closeDict[d])

## 通过 datetime 循环

today = datetime.strptime("2018.01.21", "%Y.%m.%d")

days2 = [];
while left > 0:
    day = today - timedelta(days=1)
    key = day.strftime("%m.%d")

    if closeDict.get(key):
        days2.append(key)
        left -= 1

    today = day

days2.sort()
for d in days2:
    print(d, closeDict[d])

