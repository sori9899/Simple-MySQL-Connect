from Setup import DB


setup = DB()

setup.MackConn(localhost='127.0.0.1', user='root', password='INSERT_YOUR_PASSWORD', DB='INSER_YOUR_DB')


print(setup.OpenCur())

sql = "Select * from Table_Name"

result = setup.SearchSQL(sql)

for row in result:
    print(row)
    print(row[2])