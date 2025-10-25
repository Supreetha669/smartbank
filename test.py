import pymysql
conn = pymysql.connect(host='localhost', user='bankuser', password='password123', database='bankdb')
print("Connected successfully")
conn.close()