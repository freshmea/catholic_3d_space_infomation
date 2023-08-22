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
        sql = ''
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for data in res:
            print(data)

    def __del__(self):
        self.conn.close()
        print('DB 연결 끊김')

def main():
    con = Connection()
    con.insert()

if __name__ == '__main__':
    main()
