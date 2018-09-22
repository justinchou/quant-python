# -*- coding: UTF-8 -*-

closeDict = {"01.13": 7.31, "01.14": 7.28,
             "01.15": 7.40, "01.16": 7.43, "01.17": 7.41}

closeDict["01.20"] = 7.44

days = list(closeDict.keys())
days.sort()
print(days)

share = {}
currentShare = 0
cash = 1000

for i in range(len(days)):
    if (i == 0):
        continue

    # 现卖后买还是先买后卖?

    lastPrice = closeDict[days[i - 1]]
    curPrice = closeDict[days[i]]
    if (curPrice > lastPrice):
        calcShare = (cash / 2.0) // curPrice
        cash -= calcShare * curPrice
        currentShare += calcShare
        share[days[i]] = calcShare
        print("day %s buy %s cash %s" % (days[i], calcShare, cash))

    if (days[i - 1] in share.keys()):
        lastShare = share[days[i - 1]]
        calcCash = lastShare * curPrice
        cash += calcCash
        currentShare -= lastShare
        print("day %s sell %s cash %s" %(days[i], lastShare, cash))

print(share, currentShare, cash)
