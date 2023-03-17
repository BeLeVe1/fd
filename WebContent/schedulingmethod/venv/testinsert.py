import pymysql
import time


# 打开数据库连接
# db = pymysql.connect(host="localhost", user="root", password="123456", database="testdb")
# 在默认情况下cursor方法返回的是BaseCursor类型对象，BaseCursor类型对象在执行查询后每条记录的结果以列表(list)表示。
# 如果要返回字典(dict)表示的记录，就要设置cursorclass参数为MySQLdb.cursors.DictCursor类。
db = pymysql.connect(host="localhost", user="root", password="123456", database="dss",
                     cursorclass=pymysql.cursors.DictCursor)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# SQL 插入语句
t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
sql = "INSERT INTO planindex(PSTime, PEtime, PDockNum, PCarName, PChange, PWindow, PGNum) \
       VALUES (%s, %s,  %s,  %s, %s, %s, %s)" % \
       (123, 789, 3, '小车3', t , 1, 1)
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()