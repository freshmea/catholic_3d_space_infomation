import pymysql
import time

class Connection:
    def __init__(self):
        self.ip = '127.0.0.1'
        self.user = 'guest'
        self.password = '1q2w3e4r'
        self.database = 'testdb'
        self.conn = pymysql.connect(host=self.ip, user=self.user, password=self.password, database=self.database, charset='utf8')
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
        print('DB 연결 완료')

    def insert(self):
        # sql = 'insert into student (name, address, kor, eng, math, scienct) values (%s, %s, %s, %s, %s, %s);'
        # self.cur.execute(sql, ("'kim'", "'sungnamSi'",'70', '88', '88', '23'))
        sql = "insert into student (name, address, kor, eng, math, scienct) values ('kim', 'sungnamSi', 50, 40, 55, 23);"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for data in res:
            print(data)
        self.conn.commit()
    
    def select(self):
        sql = 'select * from student ;'
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for data in res:
            print(data)
        self.conn.commit()

    def __del__(self):
        self.conn.close()
        print('DB 연결 끊김')

def main():
    con = Connection()
    # con.insert()
    con.select()

if __name__ == '__main__':
    main()
