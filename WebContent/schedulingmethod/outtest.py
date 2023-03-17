import pymysql
import random

Stime =[0, 60, 90, 150, 30, 90, 30]
Etime =[30, 90, 120, 151, 50, 95, 33]
s,e =[0, 60, 90, 150, 30, 90, 30],[30, 90, 120, 151, 50, 95, 33]
db = pymysql.connect(host="localhost", user="root", password="123456", database="dss",
                     cursorclass=pymysql.cursors.DictCursor)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
sql = "SELECT * FROM userresindex"
rnum=[]
rcar=[]
rwin=[]
try:
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    #print(results)
    for row in results:
        rnum.append(row['Rnum'])
        rcar.append(row['Rcar'])
        if row['Rtime'] == '09:00-09:30':
            rwin.append('1')
        elif row['Rtime'] == '09:30-10:00':
            rwin.append('2')
        elif row['Rtime'] == '10:00-10:30':
            rwin.append('3')
        elif row['Rtime'] == '10:30-11:00':
            rwin.append('4')
        elif row['Rtime'] == '14:00-14:30':
            rwin.append('5')
        elif row['Rtime'] == '14:30-15:00':
            rwin.append('6')
        elif row['Rtime'] == '15:00-15:30':
            rwin.append('7')
        elif row['Rtime'] == '15:30-16:00':
            rwin.append('8')
        print('shijian:',row['Rtime'])
except:
    print("Error: unable to fetch data")
# 关闭数据库连接
print('rnum:',rnum)
print('rcar:',rcar)
print('rwin:',rwin)
print('stime',Stime)
print('etime',Etime)
rlen=len(rnum)
for i in range(0,rlen):
    print('rnum:', rnum[i])
    print('rcar:', rcar[i])
    print('rwin:', rwin[i])
    print('stime', Stime[i])
    print('etime', Etime[i])
    sql = "INSERT INTO planindex_copy1(PSTime, \
        PETime, PCarName, PDockNum, PWindow) \
        VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
       (Stime[i], Etime[i],rcar[i], random.randint(0, 10), rwin[i])
    print('sql', sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()

db.close()