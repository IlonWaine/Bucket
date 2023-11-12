import sqlite3

DbName = ''

def getConect(listName):
        # connect to database
        con = sqlite3.connect(listName)
        cur = con.cursor()
        global DbName 
        DbName = listName
        # create table if not exists
        cur.execute(''' CREATE TABLE if not exists list (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        KEY TEXT,
        VALUE TEXT,
        LEVEL INTEGER,
        AddDate DATE
        ); ''')
        
 
# input value into DB word / translation / level 
def addInDb(key,value,level=1):
        con = sqlite3.connect(DbName)
        cur = con.cursor()
        with con:
                cur.execute('''INSERT INTO list(KEY,VALUE,LEVEL,AddDate) VALUES(?,?,?,DATE('now'))''',(key,value,level))
    
    
# select word / translation / id from table list and return list of elements    
# def takeFromDb(level):
#         con = sqlite3.connect(DbName)
#         cur = con.cursor()
#         cur.execute('SELECT KEY, VALUE, ID FROM list WHERE LEVEL = ?',(level,))
#         levelList = cur.fetchall()
#         return levelList


# select N numebr rows of word / translation / id from table list and return list of elements    
def takeFromDbLim(level,lim):
        con = sqlite3.connect(DbName)
        cur = con.cursor()
        if level ==1 :
                days = 0 
        elif level ==2 :
                days = 1
        elif level ==3 :
                days = 7
        elif level ==4 :
                days = 30
        elif level ==5 :
                days = 176
        elif level ==6 :
                days = 365
        cur.execute('''SELECT KEY, VALUE, ID, AddDate 
                    FROM list 
                    WHERE LEVEL = ? AND abs(JULIANDAY(AddDate)-JULIANDAY(DATE('now'))) >= ? 
                    LIMIT ?''',(level,days,lim))
        
        levelList = cur.fetchall()
        return levelList    

# update level by id 
def updateLevel(level,id):
        con = sqlite3.connect(DbName)
        cur = con.cursor()
        with con:
                cur.execute('''UPDATE list SET LEVEL = ? , AddDate = DATE('now') WHERE ID = ?''',(level,id)) 
                # cur.execute('''UPDATE list SET LEVEL = ? WHERE ID = ?''',(level,id)) 


# def selectCountTime(level):
#         con = sqlite3.connect(DbName)
#         cur = con.cursor()
#         cur.execute('''SELECT level, COUNT(*) FROM list WHERE LEVEL = ? AND JULIANDAY(AddDate)-JULIANDAY(DATE('now')) >= ? AND JULIANDAY(AddDate)-JULIANDAY(DATE('now')) <= ? GROUP BY LEVEL''',(getDays(level)))
#         countDict = dict(cur.fetchall())
#         return countDict


def selectCount():
        con = sqlite3.connect(DbName)
        cur = con.cursor()
        cur.execute('SELECT level, COUNT(*)  FROM list GROUP BY LEVEL')
        countDict = dict(cur.fetchall())
        return countDict


def selectCountReady():
    con = sqlite3.connect(DbName)
    cur = con.cursor()

    cur.execute('''
        SELECT LEVEL,
               COUNT(*) AS Count
        FROM list
        WHERE abs(JULIANDAY(AddDate) - JULIANDAY(DATE('now'))) >= 
            CASE
                WHEN LEVEL = 1 THEN 0
                WHEN LEVEL = 2 THEN 1
                WHEN LEVEL = 3 THEN 7
                WHEN LEVEL = 4 THEN 30
                WHEN LEVEL = 5 THEN 176
                WHEN LEVEL = 6 THEN 365
                ELSE 0
            END
        GROUP BY LEVEL
    ''')
    
    countDict = dict(cur.fetchall())
    con.close()  # Close the connection
    return countDict




#print(selectCount())



def takeFromDb(level):
        con = sqlite3.connect(DbName)
        cur = con.cursor()
        if level ==1 :
                days = 0 
        elif level ==2 :
                days = 1
        elif level ==3 :
                days = 7
        elif level ==4 :
                days = 30
        elif level ==5 :
                days = 176
        elif level ==6 :
                days = 365
        cur.execute('''SELECT KEY, VALUE, ID, AddDate FROM list WHERE LEVEL = ? AND abs(JULIANDAY(AddDate)-JULIANDAY(DATE('now'))) >= ? ''',(level,days))
        # cur.execute('''SELECT abs(JULIANDAY(AddDate)-JULIANDAY(DATE('now'))), AddDate FROM list WHERE LEVEL = ?  ''',(level,))

        levelList = cur.fetchall()
        return levelList





def takeFromDbList(level):
        con = sqlite3.connect(DbName)
        cur = con.cursor()
        cur.execute('''SELECT KEY, VALUE, CAST (abs(JULIANDAY(AddDate)-JULIANDAY(DATE('now'))) AS INT ) FROM list WHERE LEVEL = ?  ''',(level,))
        # cur.execute('''SELECT abs(JULIANDAY(AddDate)-JULIANDAY(DATE('now'))), AddDate FROM list WHERE LEVEL = ?  ''',(level,))
        levelList = cur.fetchall()
        return levelList



def deleteByIndex(id):
        con = sqlite3.connect(DbName)
        cur = con.cursor()
        with con:
                cur.execute('''DELETE FROM list WHERE ID = ?''',(id,)) 
                
# deleteBuIndex(12)
# deleteBuIndex(13)
# deleteBuIndex(14)
# deleteBuIndex(15)
# deleteBuIndex(16)
# deleteBuIndex()
# print(takeFromDb1(1))
# print(selectCountTime(1))
# addInDb('man','чоловік')
# result_dict = selectCountReady()
# print(result_dict)



# def selectCountReady(level):
#         con = sqlite3.connect("list.db")
#         cur = con.cursor()
#         match(level):
#                 case 1: 
#                         days = 0                     
#                 case 2:
#                         days = 1
#                 case 3: 
#                         days = 7
#                 case 4:
#                         days = 30
#                 case 5:
#                         days = 175
#                 case 6:
#                         days = 365
#         # cur.execute('SELECT level, COUNT(*)  FROM list GROUP BY LEVEL HAVING ')
#         cur.execute('''SELECT level, COUNT(*) FROM list WHERE LEVEL = ? AND abs(JULIANDAY(AddDate)-JULIANDAY(DATE('now'))) >= ? ''',(level,days))
        
#         countDict = dict(cur.fetchall())
#         return countDict

# list = list()
# for i in range(1,7):
#         list.append(selectCountReady(i))
        
# print(list)
