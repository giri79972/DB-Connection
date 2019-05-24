import mysql.connector

class DBConnect:
    con=''
    def openConnection():
        try:
            DBConnect.con=mysql.connector.connect(user='root',password='root',host='127.0.0.1')
            print("connect--------------------------------------------------")
        except Exception as e:
            print("Exception")
        finally:
            if DBConnect.con!='':
                DBConnect.con.close()
                print("connect resturn")
        return

def main():
    DBConnect.openConnection()
    return

DBConnect.main()

