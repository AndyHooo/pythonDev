#coding: utf-8
##连接mysql数据库比较常用的两个driver:1.MySQLdb(c语言实现) 2.mysql-connector(纯python实现)
import MySQLdb  
# import mysql.connector
conn = MySQLdb.connect (host = "127.0.0.1", user = "root", passwd = "mysql", db = "master")  
cursor = conn.cursor ()  
cursor.execute ("SELECT VERSION()")  
row = cursor.fetchone ()  
print "MySQL server version:", row[0]  
cursor.close ()  
conn.close ()

# cnx = mysql.connector.connect(user='root',password='mysql',host='127.0.0.1',database='master')
# cur=cnx.cursor()
# cur.execute('SELECT VERSION()')
# print cur.fetcone()[0]
# cur.close()
# cnx.close()