from Setup import DB


setup = DB()

setup.MackConn(localhost='127.0.0.1', user='root', password='sorikim1590!@', DB='baesisi')


print(setup.OpenCur())

sql = "Select * from user"

result = setup.SearchSQL(sql)

for row in result:
    print(row)
    print(row[2])