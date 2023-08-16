import csv
import pandas
import pandas as pd
import pymysql
# with open('公司.csv',mode='w') as csv_file:
#     fieldnames = ['姓名','公司名','电话']
#     writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'姓名':'王胜','公司名':'模拟','电话':'132929818'})
#     writer.writerow({'姓名':'周子为','公司名':'型日葵','电话':'1733763500'})
#     writer.writerow({'姓名':'环中','公司名':'火烈鸟','电话':'1234581'})
# web = pandas.read_csv('公司.csv',encoding='GBK')
#
# print(web)
# b = ['小帅b', '小帅c', '小帅d']
# c = ['18岁', '19岁', '20岁']
# d = ['18cm', '17cm', '16cm']
#
# df = pd.DataFrame({'你是谁' : b, '你几岁' : c, '你多高' : d})
# df.to_csv("xsb.csv", index=False, sep=',')
# 使用 connect 方法，传入数据库地址，账号密码，数据库名就可以得到你的数据库对象
db = pymysql.connect(host='localhost',port=3306,user='root',password= "root1234",database= 'avIdol')
# 接着我们获取 cursor 来操作我们的 avIdol 这个数据库
cursor = db.cursor()

# 比如我们来创建一张数据表
# sql = """create table beautyGirls(
# name char(20) not null,
# age int
# )"""
# cursor.execute(sql)
# # 最后我们关闭这个数据库的连接
#插入数据
sql = "insert into beautyGirls(name,age)values('王胜',23)"
try:
    cursor.execute(sql)
    db.commit()   #pymysql 对数据进行更新需要调用commit()
except:
    # 回滚db.rollback() 数据添加可能出现异常
    db.rollback()
db.close()
