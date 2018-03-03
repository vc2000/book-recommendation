import csv
from math import sqrt

def open_file(file_name):
    data= csv.reader(open(file_name + ".csv",'r',encoding='utf-8', errors='ignore'))

    return data


count=0
raw_user_book_rate=[]
for line in open_file("BX-Book-Ratings"):
    for item in line:
        lis=[]
        if 1< count < 69:
            lis.extend(item.split(";"))
            raw_user_book_rate.append(lis)
    count +=1


###############   ubr  #################
"""ubr={}
for i in raw_user_book_rate:
    userID = i[0]
    dicts={}
    rate = float(i[2].replace('"', ''))
    if i[1] in dicts:
        dicts[i[1]]= dicts[i[1]] + rate
    else:
        dicts[i[1]]= rate

    ubr[userID] = dicts"""

###############   isbn - book  #################
raw_user_book_rate=[]
for i in open_file("BX-Books"):
    for item in line:
        lis=[]
        if 1< count < 69:
            lis.extend(item.split(";"))
            raw_user_book_rate.append(lis)
    count +=1

isbn_book={}
