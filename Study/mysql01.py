import pymysql

conn = pymysql.connect(host = '127.0.0.1', user = 'root', password = '1234', db = 'hanbitDB', charset = 'utf8')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS userTable(id char(4) not null, userName varchar(30), email varchar(50),birthYear int)")
cur.execute("insert into userTable values('Nam', 'GEONI', 'namgeoni0330@gmail.com', 1995)")
conn.commit

conn.close()  #utf 8