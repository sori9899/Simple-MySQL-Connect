import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='sorikim1590!@', db='baesisi', charset='utf8')

cur = conn.cursor()

sql_query ="select * from user"

cur.execute(sql_query)

result = cur.fetchall()

print(result)

for row in result:
    print(row)
    print(row[1])


cur.close()
conn.close()

#https://dbaant.tistory.com/102