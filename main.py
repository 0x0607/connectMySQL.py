'''
    ### 連線到資料庫啦~e04
    By Maizuru5272#0678
'''
import pymysql      # mysql for python
#####################################################################################
class mysql():
    def __init__(self,host:str='127.0.0.1',port:int=3306,user:str='root',password:str='passwd'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
    def try_connect(self,database:str='testdb',charset:str='utf8mb4'):
        try:
            cursorclass=pymysql.cursors.DictCursor
            db = pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.password,database=database,charset=charset,cursorclass=cursorclass)
            # print('DataBase version: {}'.format(db.cursor().execute("SELECT VERSION()")))
            db.close()
            return True
        except:
            print('[WARN] Failed to connect {}:{}'.format(self.host,self.port))
            return False
mysql('127.0.0.1',3306,'root','passwd').try_connect()
#####################################################################################
