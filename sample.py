import os
import sys
import cx_Oracle as cx
from flask import Flask

try:
    empno = sys.argv[1]
except:
    print('Must pass empno as a parameter')
    exit()

db_user = os.environ.get('ADB_USER','oml')
db_password = os.environ.get('ADB_PASSWORD','Welc0me!')
service_port = os.environ.get('PORT','1521')

print('Running on Micrsoft Azure VM..')
db = cx.Connection(db_user +'/' + db_password + '@dbs_high')

print('Connected to database running on Oracle Cloud..')

cursor = cx.Cursor(db)
sql = 'select * from emp where empno='+ empno


#Fetch x number of rows at a time
cursor.arraysize = 1000
cursor.execute(sql)

emprec = cursor.fetchmany()
print('Employee record received: ',emprec)
print('Done')