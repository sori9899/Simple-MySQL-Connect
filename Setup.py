import pymysql

class DB:

    conn = None
    cur = None

    def MackConn(self, localhost, user, password, DB):
        self.conn = pymysql.connect(host=localhost, user=user, password=password, db=DB, charset='utf8')


    def OpenCur(self):
        try:
            self.cur = self.conn.cursor()
            return "DB connected Success"
        except:
            return "DB Connected Fail"


    def CloseCur(self):
        self.cur.close()

    def CloseConn(self):
        self.conn.close()

    
    def SearchSQL(self,sql):
        try:
            self.cur.execute(sql)
            row = self.cur.fetchall()
            return row
        except:
            return "Wrong SQL. Please check your qurey!"
