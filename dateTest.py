from main_db import *
from datetime import date, timedelta

# print(date.today()+timedelta(days=2))

def addInDbTest(key,value,date,level=1):
        con = sqlite3.connect("list.db")
        cur = con.cursor()
        with con:
                cur.execute('''INSERT INTO list(KEY,VALUE,LEVEL,AddDate) VALUES(?,?,?,?)''',(key,value,level,date))


def addDaysFromToday(val):
    Retday = date.today()+timedelta(days=val)
    return Retday    


def substractDaysFromToday(val):
    Retday = date.today()-timedelta(days=val)
    return Retday  


# updateLevel(1,1)


# addInDbTest('day','рух',addDaysFromToday(1),1)
# addInDbTest('day','рух',addDaysFromToday(5),1)
# addInDbTest('week','рух',addDaysFromToday(9),2)
# addInDbTest('month','рух',addDaysFromToday(40),3)
# addInDbTest('lot','рух',addDaysFromToday(180),4)
# addInDbTest('lot','рух',addDaysFromToday(175),4)
# addInDbTest('week','рух',addDaysFromToday(7),2)
# addInDbTest('year','рух',addDaysFromToday(400),5)

addInDbTest('day1','рух1',substractDaysFromToday(1),1)
addInDbTest('day2','рух2',substractDaysFromToday(0),2)

addInDbTest('week1','тиждень1',substractDaysFromToday(7),3)
addInDbTest('week2','тиждень2',substractDaysFromToday(8),3)
addInDbTest('week3','тиждень3',substractDaysFromToday(6),3)


addInDbTest('month1','місяць1',substractDaysFromToday(30),4)
addInDbTest('month2','місяць2',substractDaysFromToday(30),4)
addInDbTest('month3','місяць3',substractDaysFromToday(29),4)



addInDbTest('year1','півРоку1',substractDaysFromToday(180),5)
addInDbTest('year2','півРоку2',substractDaysFromToday(176),5)
addInDbTest('year4','півРоку4',substractDaysFromToday(174),5)
addInDbTest('yea3','півРоку3',substractDaysFromToday(175),5)
addInDbTest('yea5','півРоку5',substractDaysFromToday(150),5)


# addInDbTest('year1','рух',substractDaysFromToday(400),5)

# for i in range(24):
#     updateLevel(1,i)