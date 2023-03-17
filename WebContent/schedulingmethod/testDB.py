#!/usr/bin/python3
import numpy
import pymysql
import copy
import random
import run_this
import time  # 引入time模块


def split_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]


# 打开数据库连接
# db = pymysql.connect(host="localhost", user="root", password="123456", database="testdb")
# 在默认情况下cursor方法返回的是BaseCursor类型对象，BaseCursor类型对象在执行查询后每条记录的结果以列表(list)表示。
# 如果要返回字典(dict)表示的记录，就要设置cursorclass参数为MySQLdb.cursors.DictCursor类。
db = pymysql.connect(host="localhost", user="root", password="123456", database="dss",
                     cursorclass=pymysql.cursors.DictCursor)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# # 使用预处理语句创建表
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
#
# cursor.execute(sql)

# # SQL 插入语句
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#        LAST_NAME, AGE, SEX, INCOME) \
#        VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
#        ('Mac', 'Mohan', 20, 'M', 2000)
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 如果发生错误则回滚
#    db.rollback()

# SQL 查询语句
sql = "SELECT userresindex.*,SVip FROM userresindex LEFT JOIN supplierindex on userresindex.Rsname=supplierindex.SName"
sql1 = "SELECT DNum,Dcartpye  FROM dockindex"
sql2 = "delete from planindex"

try:
    # 执行SQL语句
    cursor.execute(sql2)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    cursor.execute(sql1)
    results1 = cursor.fetchall()
    print(results)
    print(results1)
    i = 0
    A = []  # 提前惩罚
    B = []  # 拖后惩罚
    D = []  # 时间窗
    P = []  # 作业时间
    Lbn = []  # 车辆类型
    Lbm = []  # 可加工车辆类型
    num = 0
    temp = []
    restime = []

    for row1 in results1:
        if row1['Dcartpye'] == '5':
            Lbm.append([5])
        elif row1['Dcartpye'] == '4':
            Lbm.append([4, 5])
        elif row1['Dcartpye'] == '3':
            Lbm.append([3, 4, 5])
        elif row1['Dcartpye'] == '2':
            Lbm.append([2, 3, 4, 5])
        elif row1['Dcartpye'] == '1':
            Lbm.append([1, 2, 3, 4, 5])
        num = num + 1
    for row in results:

        Lbn.append(row['Rcartype'])
        restime.append(row['Rdate'])

        temp.clear()
        for i in range(0, num):
            temp.append(eval(row['Rrestime']))  # eval()去除单引号
        c = copy.deepcopy(temp)  # temp在下个循环变化后 这里的值也会变化，所以只能用copy复制此时的temp值
        P.append(c)

        if row['SVip'] == 1:  # 根据供应商设置提前拖后惩罚

            A.append(1)
            B.append(2)
        else:
            A.append(5)
            B.append(10)
        if row['Rtime'] == '09:00-09:30':
            D.append([0, 30])
        elif row['Rtime'] == '09:30-10:00':
            D.append([30, 60])
        elif row['Rtime'] == '10:00-10:30':
            D.append([60, 90])
        elif row['Rtime'] == '10:30-11:00':
            D.append([90, 120])
        elif row['Rtime'] == '14:00-14:30':
            D.append([120, 150])
        elif row['Rtime'] == '14:30-15:00':
            D.append([150, 180])
        elif row['Rtime'] == '15:00-15:30':
            D.append([180, 210])
        elif row['Rtime'] == '15:30-16:00':
            D.append([210, 240])
        print('shijian:', row['Rtime'])

    print('Lbn=', Lbn)
    print('Lbm=', Lbm)
    print('A=', A)
    print('B=', B)
    print('D=', D)
    print('P=', P)

    # 运行调度算法
    Stime, Etime, pop = run_this.dss(Lbn, Lbm, A, B, D, P)
    print('Stime:', Stime)
    print('Etime:', Etime)
    print('pop', pop)
    # 运行调度算法

    # for row in results:
    #     fname = row[0]
    #     lname = row[1]
    #     age = row[2]
    #     sex = row[3]
    #     income = row[4]
    #     # 打印结果
    #     print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
    #           (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")
# 关闭数据库连接
db.close()

db = pymysql.connect(host="localhost", user="root", password="123456", database="dss",
                     cursorclass=pymysql.cursors.DictCursor)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
sql = "SELECT * FROM userresindex"
rnum = []
rcar = []
rwin = []
t = []
try:
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    # print(results)
    for row in results:
        t.append("'" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "'")
        rnum.append(row['Rnum'])
        rcar.append("'" + row['Rcar'] + "'")
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
        print('shijian:', row['Rtime'])
except:
    print("Error: unable to fetch data")
# 关闭数据库连接
print('rnum:', rnum)
print('rcar:', rcar)
print('rwin:', rwin)
print('stime', Stime)
print('etime', Etime)
print('pop', pop)

# 处理pop 前半是小车序号，后半对应月台号
pop = numpy.array(pop)
pop1, pop2 = split_list(pop)
print('pop1:', pop1)
print('pop2:', pop2)
pop1inds = pop1.argsort()
sorted_pop1 = pop1[pop1inds]
sorted_pop2 = pop2[pop1inds]
print('sorted_pop1:', sorted_pop1)
print('sorted_pop2:', sorted_pop2)

rlen = len(rnum)
for i in range(0, rlen):
    print('rnum:', rnum[i])
    print('rcar:', rcar[i])
    print('rwin:', rwin[i])
    print('stime', Stime[i])
    print('etime', Etime[i])
    print('sorted_pop2', sorted_pop2[i])
    print('t', t[i])
    sql = "INSERT INTO planindex(PSTime, \
        PETime, PCarName, PDockNum, PWindow,Pchange,PResTime) \
        VALUES ('%s', '%s',  %s,  '%s',  %s,%s,'%s')" % \
          (Stime[i], Etime[i], rcar[i], sorted_pop2[i], rwin[i], t[i], restime[i])
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
